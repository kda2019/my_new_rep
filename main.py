import peewee
print(10)
db = peewee.sqlite3('data.db')

class User(peewee.Model):
    pass