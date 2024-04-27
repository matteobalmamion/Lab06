import database.DAO as dao
class Model:
    def __init__(self):
        self._dao=dao.DAO()

    def getAnni(self):
        return self._dao.getAnni()
    def getBrand(self):
        return self._dao.getBrand()
    def getRetailer(self):
        return self._dao.getRetailer()
    def getVendite(self,anno,brand,retailer):
        return self._dao.getVendite(anno,brand,retailer)