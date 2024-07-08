from enum import Enum


class Rol(Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    GUEST = "GUEST"


class Category(Enum):
    PADEL = "Padel"
    REPOSTERIA = "Reposteria"
    PIZARRAS = "Pizarras"
    QR = "QR"
    LLAVEROS = "Llaveros"
    MARCOS = "Marcos"
    DISEÑOS = "Diseños"
    MACETAS = "Macetas"
    CUADROS = "Cuadros"
    SOPORTES = "Soportes"
