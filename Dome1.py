# 导入webdriver包
from selenium import webdriver
import time


def open_url(url):
    driver = webdriver.Chrome()  # 初始化一个Chrome浏览器实例
    driver.maximize_window()  # 最大化浏览器
    driver.get(url)
    time.sleep(5)  # 暂停5秒钟


if __name__ == '__main__':
    open_url("https://www.baidu.com")
