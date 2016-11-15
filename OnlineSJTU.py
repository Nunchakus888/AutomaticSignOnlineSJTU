# /usr/bin/python
# -*- coding: utf-8 -*-

import os

import requests
import encodings
import re, json


def parse_page(myPage, tag):
    if tag is None:
        reg_str = r'<tr bgcolor=#F7FAFF>(.*?)</tr>'
    elif tag == 'td':
        reg_str = r'<td .*?>(.*?)</td>'
    elif tag == 'a':
        reg_str = '<a href="?\'?([^"\'>]*)'

    return re.findall(reg_str, myPage, re.S)


def page_save(save_path, filename, content):
    if content:
        reg = "a+"
    else:
        reg = "w+"

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path + "/" + filename + ".html"
    with open(path, reg) as fp:
        for s in content:
            fp.write(s.encode("utf8"))


def login():
    br = "\n"
    gbk = "gbk"
    Userid = '716901010082'
    password = '1023268613'
    usertype = '0'
    login_url = 'http://www.onlinesjtu.com/Index.aspx'
    login_data = {'Userid': Userid, 'password': password, 'userType': usertype}
    global header_data
    header_data = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
        'Host': 'www.onlinesjtu.com',
        'Referer': 'http://www.onlinesjtu.com/'
    }
    '''login'''
    _session.post(login_url, data=login_data, headers=header_data)

    # 考勤列表
    _session.get(
        'http://www.onlinesjtu.com/learningspace/learning/enterbridge.asp?UserID=716901010082&Password=0510ee23dbe8ce9d&UserType=0&IsOpen=1')
    # check work page...
    r = _session.get(kaoqin_url + '/kaoqin_list.asp?studentid=716901010082&omgid=2088&.9807027=.8985102')
    check_work_page = r.content.decode(gbk)
    tr_check_work_page = parse_page(check_work_page, None)
    global href_list
    href_list = []
    for td in tr_check_work_page:
        rows = parse_page(td, 'td')
        for item in rows:
            item += br
            page_save("OnlineSJTU", "checkWork", item)
            # url = parse_page(item, 'a')[0]
            href_list.append(parse_page(item, 'a')[0]) if "href" in item else None
    page_save("OnlineSJTU", "checkWork", href_list)


def query_lesson_details():
    for url in href_list:
        print kaoqin_url + url
        r = _session.get(kaoqin_url + url)
        print r


class OnlineSJTU:
    def __init__(self):
        global _session
        global kaoqin_url
        kaoqin_url = 'http://www.onlinesjtu.com/learningspace/learning/student/'
        _session = requests.session()
        page_save("OnlineSJTU", "checkWork", "")
        login()
        query_lesson_details()


if __name__ == '__main__':
    letUsGo = OnlineSJTU()
