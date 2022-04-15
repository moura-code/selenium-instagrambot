from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Search(object):

    def __init__(self):
        self.chrome = Options()
        self.chrome.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/?hl=es")

    def login(self, gmail, passord):
        self.driver.implicitly_wait(99)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(gmail)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(passord)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        self.driver.implicitly_wait(88)
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        self.driver.implicitly_wait(99)
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    def follow(self,person):
        self.driver.implicitly_wait(99)
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(person)
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div/div[2]').click()
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
    
    def main(self,person,passord,):
        self.login('jcaladomoura@gmail.com', '225236Cm.')
        self.follow('fercalado')

    


a = Search()
a.main()
