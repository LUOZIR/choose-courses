import requests
import re
from 教务系统网站相关配置 import *
from encrypt import Encryption  


# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


# 全局会话对象
会话 = requests.Session()
def 获取学生学号密码():
    """
    :return: 学号,密码
    """
    return input("请输入你的学号："), input("请输入你的密码：")

def 保存学生信息为JSON(学号,密码):
    """
    :param 学号: 学生学号
    :param 密码: 学生密码
    :return:
    """
    import json
    json_str = json.dumps({"学号":学号,"密码":密码},ensure_ascii=False)
    # 保存在当前目录下配置文件.json中,使用utf-8编码
    with open("./配置文件.json","w",encoding="utf-8") as f:
        f.write(json_str)

def 读取配置文件():
    """
    :return: 学号,密码
    """
    import json
    # 判断配置文件是否存在,不存在创建
    from os import path
    if not path.exists("./配置文件.json"):
        print("配置文件不存在,请输入你的学号和密码")
        学号,密码 = 获取学生学号密码()
        保存学生信息为JSON(学号,密码)
        return 学号,密码
    # 读取配置文件返回学号和密码
    with open("./配置文件.json","r",encoding="utf-8") as f:
        print("配置文件已存在,读取配置文件")
        json_str = f.read()
        json_dict = json.loads(json_str)
        return json_dict["学号"],json_dict["密码"]



def 获取cookie(学号, 密码):
    encry_info = Encryption(密码, 教务系统登录地址, 请求PublicKey的地址, 会话)
    encry_info.encrypt()

    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Connection': 'keep-alive',
        'Referer': 教务系统登录地址 + str(encry_info.time),
        'Upgrade-Insecure-Requests': '1',
    }

    data = {
        'csrftoken': encry_info.token,
        'mm': encry_info.password,
        'yhm': 学号
    }

    try:
        响应 = 会话.post(url=教务系统登录地址, headers=headers, data=data, verify=False)
        cookie = 响应.request.headers.get('cookie')
        if re.findall(r'用户名或密码不正确', 响应.text):
            print('用户名或密码错误,请查验..')
            return None
        else:
            print("登录成功")
            return cookie
    except Exception as e:
        print(str(e))
        return None

def 关闭会话():
    会话.close()
    print("会话已关闭")
    
def 登录教务系统():
    学号,密码 = 读取配置文件()
    cookie = 获取cookie(学号,密码)
    return cookie

if __name__ == "__main__":
    cookie = 登录教务系统()
    print("Cookie:",cookie)
    关闭会话()