from projeto_webtheater.models.categoria import Categoria

class CategoriaDAO():
    __categoria_list: list

    def __init__(self, categoria_list: list) -> None:
        self.__categoria_list = categoria_list

    @property
    def categoria_list(self) -> list:
        return self.__categoria_list

    @categoria_list.setter
    def categoria_list(self, categoria_list: list) -> None:
        self.__categoria_list = categoria_list

    def verifica_tres_mais_por_categoria(self, lista_videos):
        if self.__categoria_list is not None:
            for categoria in self.__categoria_list:
                tres = []
                videos = lista_videos.videos_list
                for video in videos:
                    if video.categoria_id == categoria.id:
                        if len(tres) <= 3:
                            tres.append(video)
                        else:
                            menor = tres[0]
                            for index, v in enumerate(tres):
                                if v.curtidas > menor.curtidas:
                                    tres[index] = menor
                categoria.tres_mais = tres
