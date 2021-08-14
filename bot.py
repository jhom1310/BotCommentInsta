<<<<<<< HEAD

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from random import randint

class Bot:
    def __init__(self, usarname, password, link):
        self.username = usarname
        self.password = password
        self.link = link
        self.driver = webdriver.Firefox(executable_path='geckodriver.exe')


    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(3)
        input_user = self.driver.find_element_by_xpath("//input[@name='username']")
        input_user.clear()
        input_user.send_keys(self.username)
        input_pass = self.driver.find_element_by_xpath("//input[@name='password']")
        input_pass.clear()
        input_pass.send_keys(self.password)
        input_pass.send_keys(Keys.ENTER)
        time.sleep(5)

        self.comment()

    def comment(self):
        arq = open('arrobas.txt', 'r')
        list = []
        linhas = arq.readlines()

        for linha in linhas:
            list.append(linha)
        arq.close()

        self.driver.get(self.link)

        while(True):
            try:
                self.driver.find_element_by_class_name("Ypffh").click()
                text_comment = self.driver.find_element_by_class_name("Ypffh")
                comment_list = list[randint(0, len(list) - 1)]
                text_comment.send_keys(comment_list)
                text_comment.send_keys(' ')
                comment_list = list[randint(0, len(list) - 1)]
                text_comment.send_keys(comment_list)
                text_comment.send_keys(Keys.ENTER)
                time.sleep(randint(20,60))
            except Exception as e:
                print(e)

bot = Bot('username', 'password', 'link')
bot.login()
