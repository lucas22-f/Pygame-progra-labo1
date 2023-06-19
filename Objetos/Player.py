
import pygame

class Player:
    def __init__(self,nombre,puntaje,tiempo) -> None:
        self._nombre = nombre
        self._puntaje = puntaje
        self._tiempo = tiempo


    @property
    def get_nombre(self):
        return self._nombre
    @property
    def get_puntaje(self):
        return self._puntaje
    @property
    def get_tiempo(self):
        return self._tiempo
    
    def retornar_dic(self):
        dic = {}
        dic["nombre"] = self.get_nombre
        dic["puntaje"] = self.get_puntaje
        dic["tiempo"] = self.get_tiempo
        return dic
    
