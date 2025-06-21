from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import os
import time

# Set path to your ChromeDriver
path = "C:/Windows/Chromedriver/chromedriver.exe"

# Set up driver
service = Service(path)
driver = webdriver.Chrome(service=service)

# Open the form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSe-4QoYHJcIH05WSyMG1Ol8WeWo3eTij3BtAWOQz_y1Fdh4YA/viewform"
driver.get(form_url)
time.sleep(5)  # Wait for form to load

def fill_form(name, fav_rest, email, opt, drop):
    textbox_xpath = '//input[@type="text"]'
    textboxes = driver.find_elements(By.XPATH, textbox_xpath)

    input_data = [name, fav_rest]
    for i in range(len(input_data)):
        textboxes[i].clear()
        textboxes[i].send_keys(input_data[i])
    
    # time.sleep(3)

    email_xpath = '//input[@type="email"]'
    email_textbox = driver.find_element(By.XPATH, email_xpath)

    email_textbox.send_keys(email)

    # time.sleep(3)
    
    radiobutton_xpath = '//div[@role="radio"]'
    radiobutton = driver.find_elements(By.XPATH, radiobutton_xpath)

    for radio in radiobutton:
        if radio.get_attribute("data-value") == opt:
            radio.click()

    # time.sleep(3)
    
    listbox_xpath = '//div[@role="listbox"]'
    listbox = driver.find_element(By.XPATH, listbox_xpath)
    listbox.click()

    time.sleep(3)

    dropdown_xpath = '//div[@role="option"]/span'
    dropdown = driver.find_elements(By.XPATH, dropdown_xpath)

    for dropdown_opt in dropdown:
        if dropdown_opt.text.strip() == drop:
            dropdown_opt.click()
            break

    # time.sleep(3)

    submit_xpath = '//div[@role="button" and @aria-label="Submit"]'
    submit = driver.find_element(By.XPATH, submit_xpath)
    submit.click()

    # time.sleep(3)

    submit_another_xpath = '//a[text()="Submit another response"]'
    submit_another = driver.find_element(By.XPATH, submit_another_xpath)
    submit_another.click()

    time.sleep(3)

def main():
    csv_path = os.path.join(os.path.dirname(__file__), 'data.csv')

    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            fill_form(
                row['Name'], 
                row['Favourite restaurant'], 
                row['Email'], 
                row['Dietary preference'], 
                row['What do you like the most']
            )
    
    
    # fill_form("Aditya", "OvenStory", "aditya_k@example.com", "Vegetarian", "Pizza")

main()

print("Automation process completed")