from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
import csv

options = webdriver.ChromeOptions()
service = Service(executable_path="C:\\Program Files (x86)\\Chromedriver\\chromedriver.exe")
options.add_argument('--headless')

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.nairaland.com/')

nairid = "//a[contains(@href, 'nairaland.com/787')]"

results = []
linTitle = "//div[@class='body']/h2"

for link in range(len(nairid)):
    links = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.XPATH, nairid))
    )
    links[link].click()
    name_e = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, linTitle))
    )
    p_text = driver.find_element(By.XPATH, "//p[@class='nocopy']").text
    p_users = driver.find_element(By.XPATH, "//p[@class='nocopy']").text 
    user_list = [user.strip() for user in p_users.split(',')]
    num_users = len(user_list)
    page_views = driver.find_element(By.XPATH,"//p[@class='bold']")
    views_match = re.search(r'(\d+) Views', page_views.text)
    views_count = int(views_match.group(1)) if views_match else 0


    nairPg = {
        'NamTit': name_e.text,
        'Views': views_count,
        'actusers':num_users,
        'guests': re.search(r'(\d+) guest', p_text).group(1) if re.search(r'(\d+) guest', p_text) else ''
    }

    results.append(nairPg)
    driver.back()

driver.quit()

file_name = 'Nairaland_data.csv'
file_exists = os.path.isfile(file_name)

with open(file_name, 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['NamTit', 'Views', 'actusers', 'guests'])

    # Write header only if the file is newly created
    if not file_exists:
        writer.writeheader()

    writer.writerows(results)
