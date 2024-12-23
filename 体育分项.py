import log_in as log
import asyncio
import API
import aiohttp
import asyncio



async def fetch(session, url, headers, data,timeout=3):
    try:
        async with session.post(url, headers=headers, data=data,timeout=aiohttp.ClientTimeout(total=timeout)) as response:
            return await response.json()
    except asyncio.TimeoutError:
        return await fetch(session, url, headers, data)
async def fetch2(session, url, headers, data,timeout=2):
    try:
        async with session.post(url, headers=headers, data=data,timeout=aiohttp.ClientTimeout(total=timeout)) as response:
            return await response.json()
    except asyncio.TimeoutError:
        return {'result': '请求超时'}

async def display(lis1: list, lis2: list, lis3: list):
    num = 0
    for each in zip(lis1, lis2, lis3):
        print(num)
        print(each)
        num += 1

async def get_info(cookie, user_agent):
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': cookie,
        'Host': 'jwgl.nwu.edu.cn',
        'Origin': 'https://jwgl.nwu.edu.cn',
        'Referer': 'https://jwgl.nwu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=2023117550',
        'sec-ch-ua': r'";Not A Brand";v="99", "Chromium";v="94"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': r'"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user_agent,#如果出现第一个请求无法获取正确数据，请尝试更换这一行
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'njdm_id_list[0]': '2023', #入学年份
        'sksj_list[0]': '5' ,      #星期
        'skjc_list[0]' : '7',      #节数
        "yl_list[0]": "1",         #是否有余量
        'rwlx': '2',               #主修是1，体育，英语通识是2
        'xkly': '0',
        'bklx_id': '0',
        'sfkkjyxdxnxq': '0',
        'xqh_id': '1',
        'jg_id': '18',
        'njdm_id_1': '2023',
        'zyh_id_1': '1811',
        'zyh_id': '1811',
        'zyfx_id': 'wfx',
        'njdm_id': '2023',
        'bh_id': '2023181104',
        'xbm': '1',
        'xslbdm': 'wlb',
        'mzm': '01',
        'xz': '4',
        'ccdm': '3',
        'xsbj': '4294967296',
        'sfkknj': '0',
        'sfkkzy': '0',
        'kzybkxy': '0',
        'sfznkx': '0',
        'zdkxms': '0',
        'sfkxq': '0',
        'sfkcfx': '0',
        'kkbk': '0',
        'kkbkdj': '0',
        'sfkgbcx': '0',
        'sfrxtgkcxd': '0',
        'tykczgxdcs': '0',
        'xkxnm': '2024',#现在的时间年份
        'xkxqm': '12', #现在的时间月份
        'kklxdm': '05',#通识是10，主修是01，体育是05，英语07
        'bbhzxjxb': '0',
        'rlkz': '0',
        'xkzgbj': '0',
        'kspage': '1',
        'jspage': '100',
        'jxbzb': ''
    }
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False,limit=25),trust_env=True) as session:
        response = await fetch(session, API.列表数据, header, data)
        result = response
        # 获取大列表

        name_list = []
        kch_id_list = []
        full_kch_id_list = []
        for each in result['tmpList']:
            if each['kch_id'] not in kch_id_list:
                kch_id_list.append(each['kch_id'])
            name_list.append(each['kcmc'])
            full_kch_id_list.append(each['kch_id'])

        do_jxb_id_list = []
        teachers_list = []
        duration_list = []
        tasks = []
        for each in kch_id_list:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.265.400 QQBrowser/12.7.5769.400",
                "Cookie": cookie
            }
            data = {
                'njdm_id_list[0]': '2023', #入学年份
                'sksj_list[0]': '5' ,      #星期
                'skjc_list[0]' : '7',      #节数
                "yl_list[0]": "1",         #是否有余量
                'rwlx': '2',               #主修是1，体育，英语通识是2
                "xkly": "0",
                "bklx_id": "0",
                "sfkkjyxdxnxq": "0",
                "xqh_id": "1",
                "jg_id": "18",
                "zyh_id": "1811",
                "zyfx_id": "wfx",
                "njdm_id": "2023",
                "bh_id": "2023181104",
                "xbm": "1",
                "xslbdm": "wlb",
                "mzm": "01",
                "xz": "4",
                "ccdm": "3",
                "xsbj": "4294967296",
                "sfkknj": "0",
                "gnjkxdnj": "0",
                "sfkkzy": "0",
                "kzybkxy": "0",
                "sfznkx": "0",
                "zdkxms": "0",
                "sfkxq": "0",
                "sfkcfx": "0",
                "bbhzxjxb": "0",
                "kkbk": "0",
                "kkbkdj": "0",
                "xkxnm": "2024",#现在的时间年份
                "xkxqm": "12",#现在的时间月份
                "xkxskcgskg": "0",
                "rlkz": "0",
                "kklxdm": "05",#通识是10，主修是01，体育是05，英语07
                "kch_id": each,
                "jxbzcxskg": "0",
                "xkkz_id": "273A624F0979A99AE0632901280AAD7F",
                "cxbj": "0",
                "fxbj": "0"
            }
            task = asyncio.create_task(fetch(session, API.具体数据, headers, data))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        for result in results:
            for j in result:
                do_jxb_id_list.append(j['do_jxb_id'])
                teachers_list.append(j['jsxx'])
                duration_list.append(j['sksj'])
        print("-------------------------------------课程列表---------------------------------------")
        await display(name_list, teachers_list, duration_list)
        print("----------------------------------课程列表（结束）---------------------------------------")
        return[do_jxb_id_list,full_kch_id_list]

def get_input():
    while True:
        x=int(input("课程序号(输入-1以结束):"))
        if x == -1:
            break
        choose.append(x)

async def get(do_jxb_id_list,full_kch_id_list):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.265.400 QQBrowser/12.7.5769.400",
            "Cookie": cookie
        }
        session = aiohttp.ClientSession()
        for each in choose:
            data = {
                "jxb_ids": do_jxb_id_list[each],
                "kch_id": full_kch_id_list[each],
                "rwlx": "2",#主修是1，体育，英语通识是2
                "rlkz": "0",
                "rlzlkz": "1",
                "sxbj": "1",
                "xxkbj": "0",
                "qz": "0",
                "cxbj": "0",
                "xkkz_id": "273A624F0979A99AE0632901280AAD7F",
                "njdm_id": "2023",
                "zyh_id": "1811",
                "kklxdm": "01",
                "xklc": "2",
                "xkxnm": "2024",#现在的时间年份
                "xkxqm": "12",#现在的时间月份
                "jcxx_id": ""
            }
            response = await fetch2(session, API.数据提交, header, data)
            print(response)
        await session.close()
async def run (): 
    task_list=[asyncio.create_task(get_info(cookie,user_agent)) for _ in range(10)]
    done,_=await asyncio.wait(task_list,return_when=asyncio.FIRST_COMPLETED)
    for task in task_list:
        task.cancel()
    result=[]
    for task in done:
        result.append(task.result())
    result=result[0]

    do_jxb_id_list=result[0]
    full_kch_id_list=result[1]
    get_input()
    task_list=[asyncio.create_task(get(do_jxb_id_list,full_kch_id_list)) for _ in range(20)]
    done,_ = await asyncio.wait(task_list,return_when=asyncio.ALL_COMPLETED) 
    result=[]
    for task in done:
        result.append(task.result())


if __name__ == '__main__':
    choose = []
    cookie = log.登录教务系统()  #如须加速，将这一行改为自己的cookie，注意学校cookie每日更新
    print(cookie)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    print("-----------------------------------------------------------------")
    asyncio.run(run())
    print("-----------------------------------------------------------------")
    print("finish")