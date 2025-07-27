driver = webdriver.Chrome()
driver.get(
    "https://www.amazon.com/ax/claim?arb=6ef7ea52-743d-4bf6-b2bb-8349935be4ea&openid.assoc_handle=usflex&openid.mode=checkid_setup&policy_handle=Retail-Checkout&openid.return_to=https%3A%2F%2Fwww.amazon.com%3F&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
)

email_input = driver.find_element(By.ID, "ap_email_login")
email_input.send_keys("Enter your email here")
continue_button = driver.find_element(By.CLASS_NAME, "a-button-input")
continue_button.click()

password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys("Enter your password here")
from selenium.webdriver.common.keys import Keys
signin_button = driver.find_element(By.ID, "signInSubmit")
signin_button.click()

try:
    otp_input = driver.find_element(By.ID, "input-box-otp")
    otp_code = input("Enter otp: ")
    otp_input.send_keys(otp_code)
    
    otp_buttons = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "a-button-input"))
    )
    for btn in otp_buttons:
        if btn.get_attribute("aria-labelledby") == "cvf-submit-otp-button-announce":
            btn.click()
except Exception as e:
    print("skipping otp verification...")
    
driver.get("https://www.amazon.com/Apple-iPhone-Version-256GB-Titanium/dp/B0DPDK3JVN/ref=sr_1_1?crid=2FEHC87V4OP93&dib=eyJ2IjoiMSJ9.khqJo1RRIw_uAr9hSrYIa7W90AymleIu28BYNsLwejjXMHKYANSEusourBg4fQPNXIMJCnO_g64d9IwGu0_2PtHlpXG9IkzoPo4wzQLF6kAOxEhlPo2FVyDl_kpz9iKKsKkMcKS3WjKOlzhPbsjV5EUu4llTIcQH7n8opES73fsfZWjinC4WS08fVypz46XxD1uAH8r-EA6sFcWkWrWLewKJ90KmF4SpRIZxPLAX2ZY.eeLy1T-6Ni85bkx_TZI9_vjgCR2zk2Mcs--CecIZIB4&dib_tag=se&keywords=Apple%2BiPhone%2B16%2BPro%2BMax%2C%2BUS%2BVersion%2C%2B256GB%2C%2BBlack%2BTitanium%2B-%2BUnlocked%2B(Renewed)&qid=1749658774&sprefix=apple%2Biphone%2B16%2Bpro%2Bmax%2C%2Bus%2Bversion%2C%2B256gb%2C%2Bblack%2Btitanium%2B-%2Bunlocked%2Brenewed%2B%2Caps%2C1269&sr=8-1&th=1")

add_to_cart = driver.find_element(By.ID, "add-to-cart-button")
add_to_cart.click()
     
no_thanks = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "a-button-input"))
)
for btn in no_thanks:
    if btn.get_attribute("aria-labelledby") == "attachSiNoCoverage-announce":
        btn.click()
        print("Item added to cart.")
        break
