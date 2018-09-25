import pymysql
import smtplib
from email.mime.text import MIMEText

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('g2aFeedback1@gmail.com','Daddydadwe5')

conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='tigersq888', db='mysql', charset='utf8')
cursor = conn.cursor()
cursor.execute("USE prod_g2a;")

cursor.execute("SELECT count(*) FROM listapp_feedback")
totalNum = cursor.fetchall()
totalNum = totalNum[0][0]

for i in range (0,totalNum):
    cursor.execute("select * from listapp_feedback order by date limit 1;")
    data = cursor.fetchall()
    content = data[0][2]  #0 is index
    date = data[0][1]

    msg = MIMEText(str(content) + '\n' + '\n'+ str(date))
    msg['Subject'] = "Feedback from Prod"
    msg['From'] = "g2aFeedback1@gmail.com"
    msg['To'] = "stevenhuang98@gmail.com"
    mail.sendmail('g2aFeedback1@gmail.com', 'sstevenhuang98@gmail.com', msg.as_string())

    cursor.execute("delete from listapp_feedback order by date limit 1;")
    conn.commit()

mail.close()