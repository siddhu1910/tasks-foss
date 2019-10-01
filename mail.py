#code to send emails from cli instead of using gmail api using smtplib library 
from getpass import getpass
import smtplib
conn =smtplib.SMTP('smtp.gmail.com',587)
type(conn)
conn.ehlo()
conn.starttls()
d=input("your gmail id: ")
c=getpass("password: ")
conn.login(d,c)
a=input("to :")
b=input("description :")
conn.sendmail(d,a,b)
conn.quit()
()
print("email sent successfully")
