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
driver.get("https://www.humblebundle.com/store/search?sort=bestselling&filter=onsale&drm=steam")
time.sleep(10)

conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='tigersq888', db='mysql', charset='utf8')
cursor = conn.cursor()
cursor.execute("USE prod_g2a;")
cursor.execute("DELETE FROM listapp_humbleg2a;") # table has foreign key
cursor.execute("DELETE FROM listapp_humble")

count = 0
while (count < 100):
    containers = driver.find_elements_by_class_name("entity-block-container")
    for container in containers:
        name = container.find_element_by_class_name("entity-title").text
        link = container.find_element_by_class_name("entity-link").\
            get_attribute("href")
        discount = container.find_element_by_class_name("discount-percentage").text
        price_usd = "USD " + container.find_element_by_class_name("price").text
        cursor.execute("INSERT INTO listapp_humble \
                        (name, humble_link, discount, price) "
                       "VALUES (%s, %s, %s, %s)",
                       (name, link, discount, price_usd))
        count += 1
        conn.commit()
    driver.find_element_by_class_name("grid-next").click()
    time.sleep(10)
driver.quit()


