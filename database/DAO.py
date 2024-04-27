from database.DB_connect import DBConnect
from model.Retailer import Retailer
from model.vendita import Vendita
class DAO():
    def __init__(self):
        pass

    def getVendite(self,anno,brand,retailer):
        cnx = DBConnect.get_connection()
        result = []
        verifica=set()
        query = """   select s.Retailer_code, p.Product_number,s.Date,s.Quantity,s.Unit_price,s.Unit_sale_price
                            from go_daily_sales as s, go_products as p 
                            where s.Product_number=p.Product_number and s.Retailer_code = COALESCE(%s, s.Retailer_code) and p.Product_brand = COALESCE(%s, p.Product_brand) and year(s.Date)=COALESCE(%s,year(s.Date))"""
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query,(retailer,brand,anno,))
            for row in cursor:
                vendita=Vendita(row["Retailer_code"],row["Product_number"],row["Date"],row["Quantity"],row["Unit_sale_price"],row["Unit_price"],row["Unit_sale_price"]*row["Quantity"])
                val=len(verifica)
                verifica.add(vendita)
                val2=len(verifica)
                if val==val2:
                    continue
                result.append(vendita)
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nell'apertura del DB")
            return None
    def getAnni(self):
        cnx=DBConnect.get_connection()
        result=[]
        query="""   select year(Date) as Year 
                    from go_daily_sales"""
        if cnx is not None:
            cursor=cnx.cursor()
            cursor.execute(query)
            for row in cursor:
                if row[0] in result:
                    continue
                result.append(row[0])
            cursor.close()
            cnx.close()
            result.sort()
            return result
        else:
            print("Errore nell'apertura del DB")
            return None
    def getRetailer(self):
        cnx=DBConnect.get_connection()
        result=[]
        query="""   select * 
                    from go_retailers"""
        if cnx is not None:
            cursor=cnx.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor:
                ret=Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"])
                if ret in result:
                    continue
                result.append(ret)
            cnx.close()
            result.sort(key=lambda Retailer:Retailer.name)
            return result
        else:
            print("Errore nell'apertura del DB")
            return None
    def getBrand(self):
        cnx=DBConnect.get_connection()
        result=[]
        query="""   select Product_brand as brand 
                    from go_products"""
        if cnx is not None:
            cursor=cnx.cursor()
            cursor.execute(query)
            for row in cursor:
                if row[0] in result:
                    continue
                result.append(row[0])
            cursor.close()
            cnx.close()
            result.sort()
            return result
        else:
            print("Errore nell'apertura del DB")
            return None