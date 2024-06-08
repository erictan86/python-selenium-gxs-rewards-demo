# web based automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import sqlite3
import pandas as pd

PAY_FROM_CARD_DETAILS = {"gxs_debit_card": ("1234567890123456", "0000", "111")}

chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--start-maximized")  # start the browser maximized
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://e-station.axs.com.sg")


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__} function: {execution_time} seconds")
        return result

    return wrapper


def click_on_bills(xpath_to_click):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath_to_click))
    )
    driver.find_element(By.XPATH, xpath_to_click).click()
    print(f"xpath {xpath_to_click} clicked")
    time.sleep(0.3)


def click_on_general(xpath_to_click):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath_to_click))
    )
    driver.find_element(By.XPATH, xpath_to_click).click()
    print(f"xpath {xpath_to_click} clicked")
    time.sleep(0.35)


def click_on_iras(xpath_to_click):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath_to_click))
    )
    driver.find_element(By.XPATH, xpath_to_click).click()
    print(f"xpath {xpath_to_click} clicked")
    time.sleep(0.25)


def click_on_individual_income_tax(xpath_to_click):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath_to_click))
    )
    driver.find_element(By.XPATH, xpath_to_click).click()
    print(f"xpath {xpath_to_click} clicked")
    time.sleep(0.35)


def enter_details_on_iras(tax_reference_no, amount):
    tax_reference_no_radio_btn_xpath = '//*[@id="inputTypeReferenceNo"]'
    tax_reference_no_input_xpath = '//*[@id="referenceNo"]'
    amount_xpath = '//*[@id="amountPaidReferenceNo"]'
    add_to_payment_summary_xpath = '//*[@id="btnAddToPaymentSummaryTablet"]/a'
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, tax_reference_no_radio_btn_xpath))
    )
    driver.find_element(By.XPATH, tax_reference_no_radio_btn_xpath).click()
    driver.find_element(By.XPATH, tax_reference_no_input_xpath).send_keys(
        tax_reference_no
    )
    driver.find_element(By.XPATH, amount_xpath).send_keys(amount)
    driver.find_element(By.XPATH, add_to_payment_summary_xpath).click()
    print("details entered")
    time.sleep(0.5)


def click_enter_email_input():
    email_input_xpath = "/html/body/div[3]/div[2]/table/tbody/tr[4]/td[2]/a/span"
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, email_input_xpath))
    )
    driver.find_element(By.XPATH, email_input_xpath).click()
    print("email input clicked")
    time.sleep(0.4)


def enter_email_address(email: str):
    email_address_input_xpath = '//*[@id="eReceiptEmailAddress"]'
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, email_address_input_xpath))
    )
    driver.find_element(
        By.XPATH, email_address_input_xpath
    ).clear()  # clear email first if there is any
    driver.find_element(By.XPATH, email_address_input_xpath).send_keys(email)
    update_btn_xpath = '//*[@id="btnUpdateEReceiptEmailAddressMobile"]/a'
    driver.find_element(By.XPATH, update_btn_xpath).click()
    print("update btn clicked")
    time.sleep(0.3)


def proceed_to_pay():
    proceed_to_pay_xpath = '//*[@id="btnPayNow"]'
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, proceed_to_pay_xpath))
    )
    driver.find_element(By.XPATH, proceed_to_pay_xpath).click()
    print("proceed to pay clicked")
    time.sleep(0.2)


def click_on_debit_card(xpath_to_click):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath_to_click))
    )
    driver.find_element(By.XPATH, xpath_to_click).click()
    print(f"xpath {xpath_to_click} clicked")
    time.sleep(0.3)


def click_on_other_banks(xpath_to_click):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath_to_click))
    )
    driver.find_element(By.XPATH, xpath_to_click).click()
    print(f"xpath {xpath_to_click} clicked")
    time.sleep(0.3)


def enter_card_details_page(card_details):
    card_num, expiry_date, cvc = card_details
    card_num_xpath = '//*[@id="cardNo"]'
    expiry_date_xpath = '//*[@id="cardExpiry"]'
    cvc_xpath = '//*[@id="cvv"]'
    submit_btn_xpath = '//*[@id="btnSubmit"]'
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, card_num_xpath))
    )
    driver.find_element(By.XPATH, card_num_xpath).send_keys(card_num)
    driver.find_element(By.XPATH, expiry_date_xpath).send_keys(expiry_date)
    driver.find_element(By.XPATH, cvc_xpath).send_keys(cvc)
    driver.find_element(By.XPATH, submit_btn_xpath).click()
    print("card details entered")
    time.sleep(0.3)


def wait_for_payment_page_to_load():
    payment_iframe_xpath = '//*[@id="challengeFrame"]'
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, payment_iframe_xpath))
    )
    print("payment page loaded")


def grab_latest_otp_from_database(handle_id):
    time.sleep(15)
    conn = sqlite3.connect("/Users/thaimkoktan/Library/Messages/chat.db")
    gxs_df = pd.read_sql_query(
        f"SELECT text, handle_id, date FROM message WHERE handle_id = {handle_id} ORDER BY date DESC LIMIT 1",
        conn,
    )
    # getting the text data column into string
    msg_latest_string = gxs_df["text"][0]
    gxs_otp = msg_latest_string[4:10]
    print(f"gxs latest otp: {gxs_otp}")
    return gxs_otp


def enter_otp_page(otp):
    otp_input_xpath = '//*[@id="otpForm"]/table/tbody/tr[9]/td[3]/input'
    ok_btn_xpath = '//*[@id="submitOTP"]'
    payment_iframe_xpath = '//*[@id="challengeFrame"]'
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, payment_iframe_xpath))
    )
    payment_iframe = driver.find_element(By.XPATH, payment_iframe_xpath)
    driver.switch_to.frame(payment_iframe)
    driver.find_element(By.XPATH, otp_input_xpath).send_keys(otp)
    driver.find_element(By.XPATH, ok_btn_xpath).click()
    print("OTP submitted")
    time.sleep(0.3)


def wait_for_payment_completion_and_click_home():
    driver.switch_to.default_content()
    # to signal payment complete
    home_button_xpath = '//*[@id="btnHome"]'
    WebDriverWait(driver, 90).until(
        EC.element_to_be_clickable((By.XPATH, home_button_xpath))
    )
    print("payment complete")
    home_element = driver.find_element(By.XPATH, home_button_xpath)
    driver.execute_script(
        "arguments[0].click();", home_element
    )  # use javascript instead


@timer
def main():
    # adjust the num of times here if you would like to change it.
    num_of_times = 5
    for num in range(num_of_times):
        click_on_bills("/html/body/div[3]/table[1]/tbody/tr[2]/td[1]/a/div/img")
        click_on_general("/html/body/div[3]/table/tbody/tr[2]/td[1]/a/div/img")
        click_on_iras("/html/body/div[2]/div[2]/a[6]/div/img")
        click_on_individual_income_tax(
            "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/a"
        )
        enter_details_on_iras(tax_reference_no="your own NRIC number", amount="10")
        click_enter_email_input()
        enter_email_address(email="your own email address here")
        proceed_to_pay()
        click_on_debit_card('//*[@id="debit_card"]/div[2]')
        click_on_other_banks('//*[@id="dc_other"]/img[1]')
        enter_card_details_page(PAY_FROM_CARD_DETAILS["gxs_debit_card"])
        wait_for_payment_page_to_load()
        gxs_otp = grab_latest_otp_from_database('your own handle id') # your own handle id
        enter_otp_page(gxs_otp)
        wait_for_payment_completion_and_click_home()
        print(f"payment made for {num} times")

main()
