import sqlite3

db = sqlite3.connect("test.db")
vdb = db.cursor()
# db.execute("CREATE TABLE people(name, year)")
# vdb.execute("""INSERT INTO people VALUES
#                     ('Valera', 14)""")
# db.commit()

res = vdb.execute("SELECT year FROM people")
print(*res)
