import pymysql
import db_config as config

try:
    mydb = pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )

    if mydb.open:
        print("Connected!")

    with mydb.cursor() as mycursor:
        # Insert including studentId now
        insert_query = "INSERT INTO student (studentId, name, college) VALUES (%s, %s, %s)"
        insert_values = [
            (3, "Ameer", "VIT"),
            (4, "Asha", "SVECW")
        ]
        mycursor.executemany(insert_query, insert_values)
        mydb.commit()  # Commit changes

        # Fetch all students
        mycursor.execute("SELECT * FROM student")
        result = mycursor.fetchall()
        for row in result:
            print(row)

except pymysql.MySQLError as e:
    print(f"Database error: {e}")

finally:
    if 'mydb' in locals() and mydb.open:
        mydb.close()
        print("Connection closed!")
