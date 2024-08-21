import requests
import re
import datetime
import os
from method import write_pic_file,write_to_file

current_day = datetime.date.today();
parent_directory = os.path.dirname(os.getcwd())
download_dir0 = parent_directory + '\\DownLoadFile'+'\\'+current_day.strftime('%Y-%m-%d')
if not os.path.exists(download_dir0):
    os.mkdir(download_dir0)
download_dir1 = download_dir0 + '\\cnBeta'
if not os.path.exists(download_dir1):
    os.mkdir(download_dir1)
url = 'https://www.163.com/dy/article/JA4QRILC0511BLFD.html?spss=dy_author'
header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
r = requests.get(url=url, headers=header)
pattern = re.compile('<div class="post_body">.*?<p id=".*?">(.*?)</p>\n.*?</div>', re.S)
items = re.findall(pattern, r.text)
bodys = items[0].split("</p>")
picsrc = []
title = '美国飞机'
content = ''
for body in bodys:
    if (True if re.match('<p class=".*?"><img src.*?',body) else False):
        cur = body.split("src=\"")[1]
        picsrc.append(cur.split("\"")[0])
    elif (True if re.match('<p id=.*?>',body) else False):
        cc = body.split("\">")[1]
        content=content+cc
    else:
        content=content+body


nn = 1
for pico in picsrc:
    write_pic_file(pico,download_dir1+'\\'+title,title,nn)
    nn = nn+1

write_to_file(content,download_dir1+'\\'+title,title+'content',None)
write_to_file(picsrc,download_dir1+'\\'+title,title+'picsrc',None)






print("sad")