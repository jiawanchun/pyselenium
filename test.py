#coding=utf-8
from time import sleep
from pyselenium import PySelnium

dr = PySelnium('chrome')
dr.max_window()
dr.open('http://admin.ksudi.com')
# dr.clear_type('id->kw','12')
# dr.click('id->su')
dr.js_click('#weblogin')
sleep(2)
dr.quit()