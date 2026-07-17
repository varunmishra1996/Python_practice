from selenium import webdriver; from selenium.webdriver.common.by import By; from selenium.webdriver.common.keys import Keys; from selenium.webdriver.support.ui import WebDriverWait; from selenium.webdriver.support import expected_conditions as EC; import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.naukri.com/nlogin/login")

wait = WebDriverWait(driver, 20)

try:
    # Login - Email/Username field
    wait.until(EC.presence_of_element_located((By.ID, "usernameField"))).send_keys("mishravarun583@gmail.com")

    # Login - Password field
    wait.until(EC.presence_of_element_located((By.ID, "passwordField"))).send_keys("Varun@1996")

    # Login - Submit button
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    time.sleep(5)  # let login complete/page redirect

    # Click "View profile" button
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='View profile']"))).click()

    # Click the edit icon for the relevant widget/section
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='widgetHead']//span[@class='edit icon']"))).click()

    # Append a dot to the resume headline textarea
    textarea = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='resumeHeadlineTxt']")))
    textarea.send_keys(Keys.END)
    textarea.send_keys(".")

    # Click Save button
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Save'])[1]"))).click()

    time.sleep(3)
    print("Script completed. Current URL:", driver.current_url)

finally:
    driver.quit()
