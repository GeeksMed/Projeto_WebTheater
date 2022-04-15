from django.shortcuts import render
from projeto_webtheater.models.categoria import Categoria
from projeto_webtheater.models.categoriaDAO import CategoriaDAO
from projeto_webtheater.models.video import Video
from projeto_webtheater.models.videoDAO import VideoDAO


categorias = CategoriaDAO([
    Categoria(0, "Sakura", "Sobre flores de cerejeira.", r'images\sakura.jpg'),
    Categoria(1, "Nascer do Sol", "Sobre nascer do Sol.", r'images\nascer.jpg'),
    Categoria(2, "Disco", "Alguns discos.", r'images\disco.jpg'),
])

videos = VideoDAO([
    Video(0, 'Sakura', 'Flores de Cerejeira', r'images\sakura.jpg', r'videos\sakura.mp4', 0),
    Video(1, 'Nascer do Sol', 'Nascer do Sol na Floresta', r'images\nascer.jpg', r'videos\sunrise.mp4', 1),
    Video(2, 'Disco', 'Disco de Vinil', r'images\disco.jpg', r'videos\disco.mp4', 2),
])    


def home(request):
    return render(request, "index.html", {})


def inicial(request):
    categorias.verifica_tres_mais_por_categoria(videos)
    return render(request, 'inicial.html', {'categorias': categorias.categoria_list})


def video(request, id):
    videos_lista = videos.videos_list
    for v in videos_lista:
        if v.id == int(id):
            return render(request, 'video.html', {'video': v})
    return render(request, 'index.html', {'msg': 'NAO ENCONTRADO'})
