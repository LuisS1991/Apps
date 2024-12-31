import requests
from bs4 import BeautifulSoup
from Apps.Services.ServiceWebScraping import ServiceWebScraping
from Apps.Models import Llamado


class MinViviendaServices(ServiceWebScraping):
    def __init__(self) -> None:
        self.urlBase = (
            "https://www.gub.uy/ministerio-vivienda-ordenamiento-territorial/llamados"
        )
        self.resultado: list[Llamado] = []

    def peticion_get(self):
        response = requests.get(self.urlBase, self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser", fromEncoding="utf-8")
            llamados = soup.find_all("div", class_="Box-overlay")
            for llamdo in llamados:
                ancla = llamdo.find("a", class_="Box-title")
                state = llamdo.find("p", class_="Box-text")
                if state is not None and state.text != "Finalizado":
                    self.resultado.append(
                        Llamado(
                            nombre=ancla.text,
                            vigencia=state.text,
                            link=ancla.get("href"),
                        )
                    )
        return self.resultado


"""                  
    def PeticionGet(self):
        response = requests.get(self.urlBase,self.headers)
        if response.status_code ==200:
            soup = BeautifulSoup(response.text,'html.parser',fromEncoding='utf-8')
            productos = soup.find_all("div",class_="ui-search-result__wrapper")

            for producto in productos:
                nombre = producto.find("h2",class_="poly-box")
                precio = producto.find("div",class_="poly-component__price")
                img = producto.find("img",class_="poly-component__picture")
                self.resultado.append({'nombre':nombre.text,'precio':precio.text,'img':img.get('data-src')})
        else:
          return {'respuesta':"algo fallo"}
        
        return  {"proveedor":self.proveedor,"naumaticos":self.resultado}
        #fin """
