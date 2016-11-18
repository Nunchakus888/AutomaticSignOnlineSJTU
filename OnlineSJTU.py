# /usr/bin/python
# -*- coding: utf-8 -*-

import os

import requests
import re
from parseHtml import MyParser


def parse_page(myPage, tag):
    if tag is None:
        reg_str = r'<tr bgcolor=#F7FAFF>(.*?)</tr>'
    elif tag == 'td':
        reg_str = r'<td .*?>(.*?)</td>'
    elif tag == 'a':
        reg_str = '<a href="?\'?([^"\'>]*)'

    return re.findall(reg_str, myPage, re.S)
# <td width=30% height=31 align=center bgcolor=#ffffff>
# bgcolor="#A2B9DD"
def parse_download_lesson_page(myPage):
    reg = '<tr bgcolor=#A2B9DD>(.*?)</tr>'
    re.findall(reg, myPage, re.S)
    return re.findall(reg, myPage, re.S)


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
    Userid = '716901010082'
    password = ''
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


def lesson_url_list0():
    # 考勤列表
    _session.get(
        'http://www.onlinesjtu.com/learningspace/learning/enterbridge.asp?UserID=716901010082&Password=0510ee23dbe8ce9d&UserType=0&IsOpen=1')
    # check work page...
    r = _session.get(kaoqin_url + '/kaoqin_list.asp?studentid=716901010082&omgid=2088&.9807027=.8985102')
    check_work_page = r.content.decode(gbk)
    tr_check_work_page = parse_page(check_work_page, None)
    for td in tr_check_work_page:
        rows = parse_page(td, 'td')
        for item in rows:
            item += br
            page_save("OnlineSJTU", "checkWork", item)
            # url = parse_page(item, 'a')[0]
            href_list.append(parse_page(item, 'a')[0]) if "href" in item else None
    page_save("OnlineSJTU", "checkWork", href_list)


def lesson_url_list0_0():
    for url in href_list:
        print kaoqin_url + url
        r = _session.get(kaoqin_url + url)
        print r

    downloadR = _session.get("http://www.onlinesjtu.com/learningspace/learning/student/downloadlist.asp?term_identify=2016_3&userid=716901010082&courseid=345&username=%D5%C5%BD%C3%BD%C3&.7055475=.533424")

    print parse_download_lesson_page(downloadR.content.decode(gbk))


if __name__ == '__main__':
    br = "\n"
    gbk = "gbk"
    href_list = []
    _session = requests.session()
    kaoqin_url = 'http://www.onlinesjtu.com/learningspace/learning/student/'

    page_save("OnlineSJTU", "checkWork", "")
    # login()
    # myParser = MyParser()
    lesson_url_list0()
    lesson_url_list0_0()
