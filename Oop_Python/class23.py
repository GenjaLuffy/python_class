import sqlite3
con = sqlite3.connect('mydatabase.db')
cursor = con.cursor()

# cursor.execute('''
#     Create Table if not exists users(
#                id integer primary key,
#                username text not null,
#                age nteger,
#                email text unique
#                )
#     '''
# )
# con.commit()

# user = [
#     ('Bob',25,'bob@example.com'),
#     ('Charile',35,'charile@example.com')
# ]
# cursor.executemany("insert into users (username,age,email) values (?,?,?)",user)

# con.commit()

# cursor.execute("select * from users")
# rows = cursor.fetchall()
# for rows in rows:
#     print(rows)


# cursor.execute("select * from users where age > 30")
# rows = cursor.fetchall()
# for rows in rows:
#     print(rows)


cursor.execute("update users set age = 31 where id = 3")
con.commit()


cursor.execute("delete from users where id = 3")
con.commit()
