import time
import pymysql

conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='tigersq888', db='mysql', charset='utf8')
cursor = conn.cursor()
cursor.execute("USE prod_g2a;")
cursor.execute("SELECT * FROM listapp_humbleg2a;")

games_to_check = cursor.fetchall()

for g2aTuple in games_to_check:
    cursor.execute("SELECT * FROM listapp_humble WHERE name=%s;", g2aTuple[3])
    humbleTuple = cursor.fetchall()[0]
    g2aPrice = g2aTuple[1]
    if g2aPrice != "N/A":
        g2aPrice = float(g2aPrice[5:])
        humblePrice = float(humbleTuple[3][5:])  # exists if g2aPrice exists
        margin = (g2aPrice * 0.892 - 0.43) - humblePrice
        marginPercent = margin / humblePrice * 100
        margin = round(margin,2)
        marginPercent = (round(marginPercent,2))
        cursor.execute("UPDATE listapp_humbleg2a SET margin_num=%s, margin_percent=%s where name_id=%s",
                       (margin, marginPercent, g2aTuple[3]))
    else:
        cursor.execute("UPDATE listapp_humbleg2a SET margin_num=%s, margin_percent=%s where name_id=%s",
                       ("-100.00", "-100.00", g2aTuple[3]))
        conn.commit()





