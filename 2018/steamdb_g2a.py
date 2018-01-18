import time
import pymysql
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# driver = webdriver.PhantomJS
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
# driver = webdriver.Firefox()
driver.get("http://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=CAD")
driver.implicitly_wait(10)
rate = float(driver.find_element_by_class_name("uccResultAmount").text)

driver.get("http://g2a-services.com/counter-strike-global-offensive-steam-key-global-i10000016291021")

conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='tigersq888', db='mysql', charset='utf8')
cursor = conn.cursor()
cursor.execute("USE prod_g2a;")
cursor.execute("SELECT name FROM listapp_steam;")

count = 0
games_to_check = cursor.fetchall()

cursor.execute("DELETE FROM listapp_steam_g2a;")

for game in games_to_check:
    game_name = game[0] + " Steam Key GLOBAL"
    search_field = driver.find_element_by_id("search-field")
    search_field.clear()
    for char in list(game_name):
        time.sleep(0.1)
        if char != '\'':
            search_field.send_keys(char)
        else:
            break
    time.sleep(2)
    result_list = driver.find_element_by_id("search-games-list")
    results = result_list.find_elements_by_class_name("list-group-item")
    clicked = 0
    for result in results:
        name = result.find_element_by_class_name("list-group-item-text").text
        if name == game_name:
            result.click()
            driver.refresh()
            clicked = 1
            break
    if clicked == 0:
        cursor.execute("INSERT INTO listapp_steam_g2a (name_id, price, g2a_link) "
                       "VALUES (%s, %s, %s)", (game[0], "N/A", "N/A"))
        continue

    table = driver.find_element_by_id("history_table")
    rows = table.find_elements_by_tag_name("tr")
    try:
        price = rows[1].find_elements_by_tag_name("td")[1].text
    except IndexError:
        cursor.execute("INSERT INTO listapp_steam_g2a (name_id, price, g2a_link) "
                       "VALUES (%s, %s, %s)", (game[0], "N/A", "N/A"))
        continue
    else:
        p = list(price)
        del p[-1]
        del p[-1]
        price = "".join(p)
        price_converted = float(price) * rate
        price_converted = format(price_converted, '.2f')
        price_cad = "CDN$ " + str(price_converted)

        link = driver.find_element_by_id("get-to-marketplace").get_attribute("href")
        cursor.execute("INSERT INTO listapp_steam_g2a (name_id, price, g2a_link) "
                       "VALUES (%s, %s, %s)", (game[0], price_cad, link))
        conn.commit()
        print(link)

driver.close()
