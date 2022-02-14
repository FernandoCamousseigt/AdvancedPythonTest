from datetime import date

from anuncio import Display, Social, Video

class Campana():
    #pass
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino 

        #se recibe la lista de anuncios y se llama al metodo __obtener_instancia_anuncio para instanciar cada uno segun su tipo
        self.__anuncios = [self.__obtener_instancia_anuncio(a) for a in anuncios]

    def __obtener_instancia_anuncio(self, anuncio: dict):
#Recordar que el metodo GET de los duccionarios permite consultar una clave y en el caso de no existir, retorna el 2do argumento.
#Ej: anuncio.get("ancho", 0), devuelve el ancho registrado, y si no existe o no se especificó, entrega 0.

        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = anuncio.get("duracion", 0)

#Aquí se realiza el instanciado según el tipo
        if tipo_anuncio == "video":
            return Video(url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_clic, url_clic, sub_tipo)
        else:
            return Display(ancho, alto, url_clic, url_clic, sub_tipo)

    @property
    def nombre(self) -> str:
        return self.__nombre

    #@nombre.setter

