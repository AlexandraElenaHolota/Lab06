from database.DAO import DAO


class Model:
    def __init__(self):
        self.DAO = DAO()
        self.retails_map = {}
    def leggi_date(self):
        return self.DAO.leggi_date()

    def leggi_brand(self):
        return self.DAO.leggi_brand()

    def leggi_retailer(self):
        return self.DAO.leggi_retail(self.retails_map)

    def leggi_vendite(self, anno, brand, retailer):
        vendite = self.DAO.leggi_vendite(anno, brand, retailer)
        vendite.sort(reverse=True)
        return vendite
