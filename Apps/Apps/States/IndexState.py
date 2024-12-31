import reflex as rx
from typing import List
from Apps.Models.Llamado import Llamado
from Apps.Controllers import IndexController


class IndexState(rx.State):
    listado: List[Llamado] = []
    _indexController = IndexController()

    def obtener_datos_min_vivienda(self):
        self.listado = self._indexController.peticion_min_vivieda()

    def obtener_datos_anv(self):
        print("ministerio de anv")

    def obtener_datos_bhu(self):
        print("ministerio de bhu")
