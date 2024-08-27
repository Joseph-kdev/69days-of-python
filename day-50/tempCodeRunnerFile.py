WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
# )

# language_picker = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
# language_picker.click()