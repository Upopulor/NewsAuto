import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from method import *
import datetime

current_time = datetime.datetime.now()
current_day = datetime.date.today();
parent_directory = os.path.dirname(os.getcwd())
download_dir = parent_directory + '\\DownLoadFile'

url = 'https://www.163.com/dy/media/T1477039371434.html'
header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
r = requests.get(url=url, headers=header)
for item in parse_one_page(r.text,current_time):
        print(item)
        write_to_file(item,download_dir,'title',current_day)

