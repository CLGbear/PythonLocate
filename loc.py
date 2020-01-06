import geocoder
import mysql.connector
sqlPass = input()
g = geocoder.ip('me')
print(g.city)
print(g.state)
print(g.country)
print(g.postal)
print(int(g.postal))


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=sqlPass

)
print(mydb)
