import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleTopVendite(self,e):
        anno=self._view.ddAnno.value
        if anno=="Nessun Filtro" or anno==None:
            anno=None
        else:
            anno=int(anno)
        brand=self._view.ddBrand.value
        if brand=="Nessun Filtro" or brand==None:
            brand=None
        retailer=self._view.ddRetailer.value
        if retailer=="Nessun Filtro" or retailer==None:
            retailer=None
        else:
            retailer=int(retailer)
        vendite=self._model.getVendite(anno,brand,retailer)
        vendite.sort(key=lambda vendita:vendita.ricavo,reverse=True)
        i=0
        self._view.txtOut.controls.append(ft.Text(f"Sono state trovate {len(vendite)} vendite"))
        for vendita in vendite:
            if i>=5:
                break
            self._view.txtOut.controls.append(ft.Text(vendita))
            i+=1
        self._view.update_page()
    def handleAnalizzaVendite(self,e):
        anno=self._view.ddAnno.value
        if anno=="Nessun Filtro" or anno==None:
            anno=None
        else:
            anno=int(anno)
        brand=self._view.ddBrand.value
        if brand=="Nessun Filtro":
            brand=None
        retailer=self._view.ddRetailer.value
        if retailer=="Nessun Filtro" or retailer==None:
            retailer=None
        else:
            retailer=int(retailer)
        vendite=self._model.getVendite(anno,brand,retailer)
        ricavi=0
        retailer=set()
        prodotti=set()
        for vendita in vendite:
            ricavi+=vendita.ricavo
            retailer.add(vendita.retailer)
            prodotti.add(vendita.prodotto)
        self._view.txtOut.controls.append(ft.Text(f"Statistiche vendite:"))
        self._view.txtOut.controls.append(ft.Text(f"Giro d'affari: {ricavi}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero retailers coinvolti: {len(vendite)}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero retailers coinvolti: {len(retailer)}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero prodotti coinvolti: {len(prodotti)}"))
        self._view.update_page()

        self._view.update_page()
    def aggiungi_anni(self):
        self._view.ddAnno.options.append(ft.dropdown.Option("Nessun Filtro"))
        anni=self._model.getAnni()
        for anno in anni:
            self._view.ddAnno.options.append(ft.dropdown.Option(f"{anno}"))
        self._view.update_page()
    def aggiungi_brand(self):
        self._view.ddBrand.options.append(ft.dropdown.Option("Nessun Filtro"))
        brands = self._model.getBrand()
        for brand in brands:
            self._view.ddBrand.options.append(ft.dropdown.Option(f"{brand}"))
        self._view.update_page()
    def aggiungi_retailer(self):
        self._view.ddRetailer.options.append(ft.dropdown.Option("Nessun Filtro"))
        retailers = self._model.getRetailer()
        for retailer in retailers:
            self._view.ddRetailer.options.append(ft.dropdown.Option(key=retailer.code,text=retailer.name,data=retailer,on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self, e):
                self._retailer = e.control.data