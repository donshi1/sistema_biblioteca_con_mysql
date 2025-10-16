# models.py

from datetime import date

class Libro:
    def __init__(self, id, titulo, autor, anio, disponible):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disponible = disponible

    # Métodos getter para acceder a los atributos encapsulados
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor

    def is_disponible(self):
        return self.__disponible

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"ID: {self.__id} | Título: {self.__titulo} | Autor: {self.__autor} | Año: {self.__anio} | Estado: {estado}"

class Usuario:
    def __init__(self, id, nombre, tipo):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
    
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Tipo: {self.__tipo}"