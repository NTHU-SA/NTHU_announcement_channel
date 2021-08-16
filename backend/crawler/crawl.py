import urllib.parse

import requests
from bs4 import BeautifulSoup

from backend.models import News


def nthu_crawler(url):
    r = requests.get(url)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "lxml")
    result = []

    for announce in soup.find_all(class_="mtitle"):
        try:
            title = announce.find("a").text.strip()
            post_url = announce.find("a").get("href")
            if title is not None and post_url is not None:
                if "http" not in url:
                    post_url = urllib.parse.urljoin(url, post_url)
                result.append([title, post_url])
        except:
            pass
    for i in result:
        print(i)
    return result


def NTHU_CS(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(school="NTHU", dep="CS", category=office, title=title, url=url)


def NTHU_EE(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(school="NTHU", dep="EE", category=office, title=title, url=url)


def NTHU_IPTH(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(
            school="NTHU", dep="IPTH", category=office, title=title, url=url
        )


def NTHU_OSA(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(
            school="NTHU", dep="OSA", category=office, title=title, url=url
        )


def NTHU_OAA(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(
            school="NTHU", dep="OAA", category=office, title=title, url=url
        )


def NTHU_DSH(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(
            school="NTHU", dep="DSH", category=office, title=title, url=url
        )


def NTHU_PEO(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(
            school="NTHU", dep="PEO", category=office, title=title, url=url
        )


def NTHU_OGA(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(
            school="NTHU", dep="OGA", category=office, title=title, url=url
        )


def NTHU_CCC(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(
            school="NTHU", dep="CCC", category=office, title=title, url=url
        )


def NTHU_LANGUAGE(office, ta_link):
    result = nthu_crawler(ta_link)
    for title, url in result:
        News.objects.add(
            school="NTHU", dep="LANGUAGE", category=office, title=title, url=url
        )


def NTHU_SS(office, ta_link):
    r = requests.get(ta_link)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.find_all(class_="mc")

    for announce in tables:
        try:
            title = announce.find(class_="ptname").a.string
            title = str(title).strip()
            url = announce.find(class_="ptname").a.get("href")
            data = announce.find(class_="date float-right")
            if data is not None:
                data = data.string.split()[1]
            print(title)
            News.objects.add(
                school="NTHU", dep="SS", category=office, title=title, url=url
            )
        except:
            pass


def NCTU_CS(office, ta_link):
    r = requests.get(ta_link)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.find_all(class_="announcement-item")
    for announce in tables:
        try:
            title = str(announce.find_all("a")[0].string).strip()
            title = str(title).strip()
            url = announce.find_all("a")[0]["href"]
            data = announce.find_all("span")
            data = str(data).split("\n")[-2].split()[0]
            print(title)
            News.objects.add(
                school="NCTU", dep="CS", category=office, title=title, url=url
            )
        except:
            pass


def NCTU_EE(office, ta_link):
    r = requests.get(ta_link)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.find_all(class_="i-annc__title")
    datas = soup.find_all(class_="i-annc__postdate-content")
    for i in range(len(tables)):
        announce = tables[i]
        data = datas[i]
        try:
            title = str(announce.string).strip()
            print("NCTU_EE:", title)
            url = "https://www.dece.nctu.edu.tw/"
            url += str(announce.get("href"))
            data = str(data).split()[-1][:-7]
            News.objects.add(
                school="NCTU", dep="EE", category=office, title=title, url=url
            )
        except:
            pass
