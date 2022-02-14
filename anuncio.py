class Anuncio(): 
	#pass
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1 
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo 
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo


class Video():
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        self.__ancho = 1
        self.__alto = 1
        self.__url_archivo = url_archivo 
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        self.__duracion = duracion if duracion > 0 else 5

class Display():
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

class Social():
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")





