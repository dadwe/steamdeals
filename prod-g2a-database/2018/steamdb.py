import time
import pymysql
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
# driver = webdriver.PhantomJS()
# driver = webdriver.Firefox()
driver.get("https://steamdb.info/sales/?min_discount=60&min_rating=80&cc=ca")
time.sleep(10)

show_all_container = driver.find_element_by_class_name('dataTables_length')
show_all_dropdown = show_all_container.find_element_by_tag_name('select')
show_all_dropdown.click()
time.sleep(3)
show_all_options = show_all_dropdown.find_elements_by_tag_name('option')

for option in show_all_options:
    if option.text == "All":
        option.click()
        time.sleep(2)
        break

odd_apps = driver.find_elements_by_class_name('app')
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='tigersq888', db='mysql', charset='utf8')
cursor = conn.cursor()
cursor.execute("USE prod_g2a;")
cursor.execute("DELETE FROM listapp_steam_g2a;")
cursor.execute("DELETE FROM listapp_steam")

for app in odd_apps:
    name = app.find_element_by_class_name('b').text
    link = app.find_element_by_class_name('b').get_attribute('href')
    data = app.find_elements_by_tag_name('td')
    discount = data[3].text
    price = data[4].text
    rating = data[5].text
    cursor.execute("INSERT INTO listapp_steam (name, steam_link, discount, price, rating) "
                   "VALUES (%s, %s, %s, %s, %s)",
                   (name, link, discount, price, rating))

conn.commit()
driver.quit()
