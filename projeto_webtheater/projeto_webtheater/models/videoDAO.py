from projeto_webtheater.models.video import Video

class VideoDAO:
    __videos_list: list

    def __init__(self, videos_list: list) -> None:
        self.__videos_list = videos_list

    @property
    def videos_list(self) -> list:
        return self.__videos_list

    @videos_list.setter
    def videos_list(self, videos_list: list) -> None:
        self.__videos_list = videos_list