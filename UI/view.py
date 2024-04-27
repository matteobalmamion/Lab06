import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab 06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self.ddAnno = ft.Dropdown(hint_text="anno",options=[])
        self._controller.aggiungi_anni()
        self.ddBrand=ft.Dropdown(hint_text="brand",options=[])
        self._controller.aggiungi_brand()
        self.ddRetailer=ft.Dropdown(hint_text="retailer",options=[],width=450)
        self._controller.aggiungi_retailer()
        row1=ft.Row([self.ddAnno,self.ddBrand,self.ddRetailer],alignment=ft.MainAxisAlignment.CENTER)
        # ROW 2
        self.btnTopVendite= ft.ElevatedButton(text="Top Vendite", on_click=self._controller.handleTopVendite)
        self.btnAnalizzaVendite=ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.handleAnalizzaVendite)
        row2 = ft.Row([self.btnTopVendite, self.btnAnalizzaVendite],
                      alignment=ft.MainAxisAlignment.CENTER)


        # List View where the reply is printed
        self.txtOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.add(row1,row2,self.txtOut)


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
