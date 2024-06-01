from database.DAO import DAO

date = DAO.leggi_date()

for d in date:
    print(d)
