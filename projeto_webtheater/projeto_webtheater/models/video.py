import datetime


class Video():
    __id: int
    __titulo: str
    __breve_descricao: str
    __url_imagem_apresentacao: str
    __url_video: str
    __data_publicacao: datetime
    __categoria_id: int
    __qt_visualizacao: int
    __qt_curtidas: int
    __comentarios: list

    def __init__(self, id, titulo, breve_descricao, url_imagem_apresentacao, url_video, categoria_id) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__breve_descricao = breve_descricao
        self.__url_imagem_apresentacao = url_imagem_apresentacao
        self.__url_video = url_video
        self.__categoria_id = categoria_id
        self.__data_publicacao = datetime.datetime.today()
        self.__qt_visualizacao = 0
        self.__qt_curtidas = 0
        self.__comentarios = []

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def breve_descricao(self):
        return self.__breve_descricao

    @breve_descricao.setter
    def breve_descricao(self, breve_descricao):
        self.__breve_descricao = breve_descricao

    @property
    def url_imagem_apresentacao(self):
        return self.__url_imagem_apresentacao
    
    @url_imagem_apresentacao.setter
    def url_imagem_apresentacao(self, url_imagem_apresentacao):
        self.__url_imagem_apresentacao = url_imagem_apresentacao

    @property
    def url_video(self):
        return self.__url_video
    
    @url_video.setter
    def url_video(self, url_video):
        self.__url_video = url_video

    @property
    def data_publicacao(self):
        return self.__data_publicacao
    
    @data_publicacao.setter
    def data_publicacao(self, data_publicacao):
        self.__data_publicacao = data_publicacao

    @property
    def categoria_id(self):
        return self.__categoria_id
    
    @categoria_id.setter
    def categoria_id(self, categoria_id):
        self.__categoria_id = categoria_id

    @property
    def qt_visualizacao(self):
        return self.__qt_visualizacao
    
    @qt_visualizacao.setter
    def qt_visualizacao(self, qt_visualizacao):
        self.__qt_visualizacao = qt_visualizacao

    @property
    def qt_curtidas(self):
        return self.__qt_curtidas
    
    @qt_curtidas.setter
    def qt_curtidas(self, qt_curtidas):
        self.__qt_curtidas = qt_curtidas

    @property
    def comentarios(self):
        return self.__comentarios

    @comentarios.setter
    def comentarios(self, comentarios):
        self.__comentarios = comentarios