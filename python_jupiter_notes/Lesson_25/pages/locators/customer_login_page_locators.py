from selenium.webdriver.common.by import By


email_input_loc = (By.ID, 'email')
password_input_loc = (By.NAME, 'login[password]')
send_button_loc = (By.CSS_SELECTOR, '.action.login.primary')
error_message_loc = (By.CLASS_NAME, 'message-error')