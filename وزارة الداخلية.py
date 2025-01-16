from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Configure Chrome options
chrome_options = Options()

# Initialize Chrome driver
try:
    chrome_service = ChromeService(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
except Exception as e:
    print(f"Error initializing the Chrome driver: {e}")
    exit(1)

# Navigate to the target URL
try:
    target_url = "https://moi.gov.eg/Account/ForgotActivationCode"
    driver.get(target_url)
except Exception as e:
    print(f"Error navigating to {target_url}: {e}")
    driver.quit()
    exit(1)

# User inputs
email_address = "أكتب إيميلك هنا"
national_id = "أكتب الرقم القومي بتاعك هنا"

try:
    # Locate and populate the email input field
    email_input_field = driver.find_element(By.CSS_SELECTOR, "#Email")
    email_input_field.send_keys(email_address)

    # Locate and populate the national ID input field
    national_id_input_field = driver.find_element(By.CSS_SELECTOR, "#Identity")
    national_id_input_field.send_keys(national_id)
except Exception as e:
    print(f"Error locating or populating input fields: {e}")
    driver.quit()
    exit(1)


# Function to attempt registration with all possible PIN codes
def attempt_registration():
    for pin_code in range(10000):
        formatted_pin_code = str(pin_code).zfill(4)

        try:
            # Locate the PIN code input field
            pin_code_input_field = driver.find_element(By.CSS_SELECTOR, "#PinCode")
            pin_code_input_field.click()
            pin_code_input_field.send_keys(formatted_pin_code)

            # Close any modal or informational messages
            modal_close_button = driver.find_element(
                By.CSS_SELECTOR, "#CodeModal > div.modal-body > div > i"
            )
            modal_close_button.click()

            # Submit the activation form
            submit_button = driver.find_element(
                By.CSS_SELECTOR, "#ActivationForm > div:nth-child(5) > button"
            )
            submit_button.click()

            # Wait for 1 second between attempts
            time.sleep(1)

            # Clear the PIN code input field for the next attempt
            pin_code_input_field.clear()
        except Exception as inner_error:
            print(
                f"Error during PIN code submission for {formatted_pin_code}: {inner_error}\
                  \nPlease now try to normally log-in through: https://moi.gov.eg"
            )


# Call the registration attempt function
attempt_registration()

# Close the driver after the script is done
driver.quit()
