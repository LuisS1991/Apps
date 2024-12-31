from Apps.Services import MinViviendaServices


class IndexController:
    def __init__(self):
        self.__minViviedaa = MinViviendaServices()

    def peticion_min_vivieda(self):
        return self.__minViviedaa.peticion_get()
