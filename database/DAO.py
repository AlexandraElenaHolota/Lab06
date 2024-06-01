from database import DB_connect
from database.DB_connect import DBConnect
from model.Vendite import Vendite
from model.retailer import Retailer


class DAO():

    def leggi_date(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT YEAR(gds.Date)
                        FROM go_daily_sales gds"""
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None

    def leggi_brand(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """select DISTINCT  gp.Product_brand  
                        from go_products gp """
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None

    def leggi_retail(self, retailers_map):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            result = set()
            cursor = cnx.cursor(dictionary=True)
            query = """select  * 
                        from go_retailers gr  """
            cursor.execute(query)
            for row in cursor.fetchall():
                read_retailer = Retailer(**row)
                result.add(read_retailer)
                retailers_map[read_retailer.Retailer_code]=read_retailer
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None

    def leggi_vendite(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            result = []
            cursor = cnx.cursor(dictionary=True)
            query = """select gds.`Date`, gds.Retailer_code , gds.Product_number , (gds.Quantity*gds.Unit_sale_price) as Ricavo
            from go_daily_sales gds 
            join go_products gp 
            on gds.Product_number = gp.Product_number 
            where gp.Product_brand = %s or gds.Retailer_code = %s or YEAR (gds.`Date`)=%s"""
            cursor.execute(query, (brand, retailer, anno))
            for row in cursor:
                result.append(Vendite(row['Date'], row["Retailer_code"], row["Product_number"], row['Ricavo']))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None





