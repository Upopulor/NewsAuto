import os.path
import re
import json
import requests
from datetime import datetime,timedelta


def parse_one_page(html,current_time):
    pattern = re.compile('<div.*?desc">.*?<h4>.*?<a href="(.*?)".*?class="title">'
                         '(.*?)</a>.*?tail.*?time">(.*?)</span>.*?</div>', re.S)
    items = re.findall(pattern, html)
    date_format = "%Y-%m-%d %H:%M"
    for item in items:
        previous_time = current_time - timedelta(days=1)
        datee = datetime.strptime(item[2], date_format)
        previous_time2 = datetime.strptime(previous_time.strftime(date_format), date_format)
        if(datee>=previous_time2):
            yield {
                'title': item[1].replace("&quot;", "\""),
                'url': item[0],
                'time': item[2]
            }



def write_to_file(content, dir,filenameTag,date):
    if date is None:
        filename = filenameTag
    else:
        filename = filenameTag+date.strftime('%Y-%m-%d')
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open(dir + '\\'+filename+'.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def write_pic_file(url, dir,filenameTag,num):
    filename = filenameTag + str(num) +'.jpg'
    filedir = dir + '\\' + filename
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
        if not os.path.exists(filedir):
            r =requests.get(url)
            with open(filedir,'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except IOError as e:
            print(str(e))
