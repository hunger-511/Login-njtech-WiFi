import requests
from lxml import etree
import time
def con_Njtech_Home(stuid,psw,cha):
        if cha == '@telecom':
                chashow = '中国电信'      
        elif cha == '@cmcc':
                chashow = '中国移动'
        else :
                print("运营商错误\n")
        con_url = 'https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232'
        con_header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': 'keep-alive',
                'Host': 'u.njtech.edu.cn',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.68'
        }
        ###############################################          实例个连接对象
        b = requests.Session()
        responseA = b.get(con_url,headers = con_header)
        ###################################################             获取LT
        tree = etree.HTML(responseA.text)
        lt = tree.xpath('//*[@id="fm1"]/div/div[1]/div[4]/input[1]')
        lt = lt[0].attrib
        lt = lt['value']
        ##################################################              填写第一次的请求头
        new_con_header = con_header.copy()
        new_con_header['Cache-Control'] = 'max-age=0'
        new_con_header['Content-Length'] = '214'
        new_con_header['Content-Type'] = 'application/x-www-form-urlencoded'
        ###################################################             获取cookie对象，字符串化提取所需
        bb = str(responseA.cookies)
        aa = bb.split(' ')
        insert_cookie = aa[1]
        # JSESSIONID = aa[5]
        # new_con_header['Cookie'] = 'JSESSIONID'+'; '+'insert_cookie'
        new_con_header['Origin'] = 'https://u.njtech.edu.cn'
        new_con_header['Referer'] = con_url
        ##################################################              填写第一次数据表单
        data = {
                'username': stuid,
                'password': psw,
                'channelshow': chashow,
                'channel': cha,
                'lt': lt,
                'execution': 'e1s1',
                '_eventId': 'submit',
                'login': '登录'
        }
        response = b.post(con_url,data = data,headers = new_con_header,cookies = responseA.cookies, allow_redirects=False)
        ##################################################              跳转前更新的cookie与URL
        c = response.cookies
        b.cookies.update(c)
        bb = str(response.headers)
        aa = bb.split("'")
        sec_jump_url = aa[23]
        ##################################################              填写第二次的请求头
        sec_jump_header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': insert_cookie,
                'Host': 'u.njtech.edu.cn',
                'Referer': 'https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'
        }
        response = b.get(sec_jump_url,headers = sec_jump_header,allow_redirects=False)
        c = response.cookies
        b.cookies.update(c)
        bb = str(response.headers)
        aa = bb.split("'")
        thr_jump_url = aa[11]
        thr_jump_header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': 'u.njtech.edu.cn',
                'Referer': 'https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'
        }
        response = b.get(thr_jump_url,headers = thr_jump_header,cookies = b.cookies, allow_redirects=False)
        bb = str(response.headers)
        aa = bb.split("'")
        for_jump_url = aa[11]
        c = response.cookies
        b.cookies.update(c)
        for_jump_header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': 'i.njtech.edu.cn',
                'Referer': 'https://u.njtech.edu.cn/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38'
        }
        response = b.get(for_jump_url,headers = for_jump_header, allow_redirects=False)
        c = response.cookies
        b.cookies.update(c)
        fiv_jump_url = 'https://i.njtech.edu.cn/index.html'
        fiv_jump_header={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': 'i.njtech.edu.cn',
                'Referer': 'https://u.njtech.edu.cn/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38'
        }
        response = b.get(fiv_jump_url,headers = fiv_jump_header,cookies = b.cookies)
        c = response.cookies
        b.cookies.update(c)
        print("连接成功\n")
        response.encoding = 'utf-8'
        # print(response.text)
        return b.cookies

def read_info():
        fo = open("info.txt", "r")
        stuid = fo.readline()
        stuid = stuid.replace("\n", "")
        password = fo.readline()
        password = password.replace("\n", "")
        channel = fo.readline()
        channel = channel.replace("\n", "")
        fo.close()
        info = [stuid,password,channel]
        return info



info = read_info()
con_Njtech_Home(info[0],info[1],info[2])
