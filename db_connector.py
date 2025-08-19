import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Basha@8230",
    database="demo"
)

if(mydb.open):
    print("Connected!")

mycursor = mydb.cursor()

mycursor.execute("insert into student values ('Ameer','VIT'),('Asha','SVECW');")

mycursor.execute("select * from student")

result = mycursor.fetchall()

for i in result:
    print(i)