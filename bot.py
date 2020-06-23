from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
import time
from random import randint


class instagramBot:
    def __init__(self, username, password, link):
        self.username = username
        self.password = password
        self.link = link
        self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe')


    def login(self):
        driver = self.driver
        driver.get('http://www.instagram.com')
        time.sleep(5)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        x=1

        while x:
            self.comment_url(self.link)
            x+=1
            print(x)

    def comment_url(self, link):

        arq = open("lista_perfis.txt", "r")
        list = []
        linhas = arq.readlines()
        cont = 0
        for linha in linhas:
            list.append(linha)
            cont = cont +1
        arq.close()

        driver = self.driver
        driver.get(link)
        commentSection = ui.WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   commentSection)
        while (1 == 1):
            try:
                commentSection = ui.WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
                comment = list[randint(0,(cont-1))]
                commentSection.send_keys(comment)
                comment = list[randint(0, (cont-1))]
                commentSection.send_keys(' ')
                commentSection.send_keys(comment)
                comment = list[randint(0, (cont-1))]
                commentSection.send_keys(' ')
                commentSection.send_keys(comment)
                commentSection.send_keys(Keys.ENTER)
                time.sleep(randint(15,60))
                break
            except Exception:
                time.sleep(randint(15,50))


robo = instagramBot('username', 'password*','https://www.instagram.com/linkhere')
robo.login()

