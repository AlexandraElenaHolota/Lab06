import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer_name = None

    def populated_dd_anno(self):
        anni = self._model.leggi_date()
        for a in anni:
            self._view._dd_anno.options.append(ft.dropdown.Option(a[0]))
        self._view.update_page()


    def populated_dd_brand(self):
        brand = self._model.leggi_brand()
        for b in brand:
            self._view._dd_brand.options.append(ft.dropdown.Option(b[0]))
        self._view.update_page()

    def populated_dd_retailer(self):
        retailer = self._model.leggi_retailer()
        for r in retailer:
            self._view._dd_retailer.options.append(ft.dropdown.Option(key=r.Retailer_code, text = r.Retailer_name, data=retailer, on_click=self.read_retailer))
        self._view.update_page()


    def get_TopVendite(self, e):
        top_vendite = self._model.leggi_vendite(self._view._dd_anno.value, self._view._dd_brand.value, self._view._dd_retailer.value)
        self._view.lst_result.controls.clear()
        if len(top_vendite) == 0:
            self._view.lst_result.controls.append(ft.Text("Nessuna vendita con i filtri selezionati"))
        else:
            for vendita in top_vendite:
                self._view.lst_result.controls.append(ft.Text(vendita))
        self._view.update_page()


    def read_retailer(self, e):
        """event handler che legge il retailer scelto dal menu a tendina ogniqualvolta viene cliccata una opzione.
        In questo caso andiamo a leggere direttamente l'oggetto, contenuto nel campo data dell'opzione.
        """
        if self._view._dd_retailer.value is None:
            self._retailer_name = None
        else:
            self._retailer_name = self._view._dd_retailer.value



    def analizza_vendite(self, e):
        vendite = self._model.leggi_vendite(self._view._dd_anno.value, self._view._dd_brand.value, self._view._dd_retailer.value)
        numVendite = len(vendite)
        ricavo = self.ricavi(vendite)
        numProdotti = self.numProdotti(vendite)
        numRetailer = self.numRetailer(vendite)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("Statisiche vendite: "))
        self._view.lst_result.controls.append(ft.Text(f"Giro d'affari: {ricavo}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero vendite: {numVendite}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero retailers coinvolti: {numRetailer}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero prodotti: {numProdotti}"))
        self._view.update_page()

    def ricavi(self, vendite):
        ricavo = 0
        for v in vendite:
            ricavo += v.Ricavo
        return ricavo

    def numProdotti(self, vendite):
        prodotti = []
        for v in vendite:
            if v.Product_number not in prodotti:
                prodotti.append(v.Product_number)
        return len(prodotti)

    def numRetailer(self, vendite):
        retailer = []
        for v in vendite:
            if v.Retailer_code not in retailer:
                retailer.append(v.Retailer_code)
        return len(retailer)





