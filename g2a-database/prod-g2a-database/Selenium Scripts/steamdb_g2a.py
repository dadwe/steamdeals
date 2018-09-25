#!/user/bin/env python
# -*- coding: utf-8 -*-

import time
import pymysql
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def search():
    search_field = driver.find_element_by_tag_name("input")
    # search_field.click()
    time.sleep(2)
    search_field = driver.find_element_by_tag_name("input")
    search_field.clear()
    for char in list(game_name):
        time.sleep(0.1)
        if char != '\'':
            search_field.send_keys(char)
        else:
            break
    time.sleep(3)
    result_list = driver.find_element_by_class_name("fullscreen-search-results")
    results = result_list.find_elements_by_class_name("Card__base")
    found = 0
    for result in results:
        name = result.find_element_by_class_name("Card__title").text
        if name.lower() == game_name.lower() or len(results) == 1:
            link = result.get_attribute("href")
            price = result.find_element_by_class_name("Card__price-cost").text
            price = price.replace("USD", "")
            #price = price.replace("From ", "")
            #price = price.replace("$", "")
            price = float(price) * rate
            price = format(price, '.2f')
            price = "CAD $" + str(price)
            cursor.execute("INSERT INTO listapp_steam_g2a (name_id, price, g2a_link) "
                           "VALUES (%s, %s, %s)", (game[0], price, link))
            found = 1
            conn.commit()
            print(link)
            break
    return found

# driver = webdriver.PhantomJS
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
# driver = webdriver.Firefox()
#driver.delete_all_cookies()
driver.get("http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CAD")
driver.implicitly_wait(10)
rate = float(driver.find_element_by_class_name("uccResultAmount").text)

driver.get("https://www.g2a.com/")
driver.set_window_position(0,0)
driver.set_window_size(1000,1000)

# driver.find_element_by_class_name("topbar-toolbar-search").click()
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='tigersq888', db='mysql', charset='utf8')
cursor = conn.cursor()
cursor.execute("USE prod_g2a;")
cursor.execute("SELECT name FROM listapp_steam;")

time.sleep(5)
driver.find_element_by_class_name("topbar-toolbar-search").click()
time.sleep(2)
count = 0
games_to_check = cursor.fetchall()

cursor.execute("DELETE FROM listapp_steam_g2a;")

for game in games_to_check:
    game_name = game[0] + " Steam Key GLOBAL"
    game_name = game_name.replace("™", "")
    game_name = game_name.replace("®", "")

    if search() == 0:
        game_name = game_name.replace("Steam Key", "Key Steam")
        if search() == 0:
            cursor.execute("INSERT INTO listapp_steam_g2a (name_id, price, g2a_link) "
                           "VALUES (%s, %s, %s)", (game[0], "N/A", "N/A"))
            continue
driver.close()
