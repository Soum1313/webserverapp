import mysql.connector
db_conn = mysql.connector.connect(host = "rds-instance.cnv2wno0u3ig.us-east-2.rds.amazonaws.com", port = "3306", user="root", password="VjuCSE20", database="mydb")
if(db_conn):
    print("Connection Successfull")
else:
    print("Connection Failed")

db_cursor =db_conn.cursor()
choice=int(input("Enter your Operation"))
if (choice==1):
    db_cursor.execute("insert into donations values(102 , 'Sam' , 'Parag Org' , '5 Meals' , 'Vijayawada' , '01-07-2022',987)")
    print("successfully inserted")
elif (choice==2):
    db_cursor.execute("Update donations set donorname = 'Soumya Prasad' where donationid = 101")
elif (choice==3):
    db_cursor.execute("delete from donations where donationid = 101")
elif(choice==4):
    db_cursor.execute("Select * from donations")
    result = db_cursor.fetchall()
    for rec in result :
        print(rec)
db_conn.commit()




#db_cursor.execute("insert into donations values(101 , 'Soumya' , 'Parag Org' , '5 Meals' , 'Vijayawada' , '01-07-2022',96687)")
#db_cursor.execute("Update donations set donorname = 'Soumya Prasad' where donationid = 101")
# db_cursor.execute("delete from donations where donationid = 101")
# db_cursor.execute("Select * from donations")
# result = db_cursor.fetchall()
# for rec in result :
#     print(rec)
# db_conn.commit()