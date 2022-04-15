class Categoria():
    __id: int
    __titulo: str
    __descricao: str
    __url_ilustracao: str
    __tres_mais: list

    def __init__(self, id, titulo, descricao, url_ilustracao) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__url_ilustracao = url_ilustracao
        self.__tres_mais = []

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
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def url_ilustracao(self):
        return self.__url_ilustracao

    @url_ilustracao.setter
    def url_ilustracao(self, url_ilustracao):
        self.__url_ilustracao = url_ilustracao

    @property
    def tres_mais(self):
        return self.__tres_mais

    @tres_mais.setter
    def tres_mais(self, tres_mais):
        self.__tres_mais = tres_mais