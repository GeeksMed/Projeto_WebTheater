from django.shortcuts import render
from projeto_webtheater.models.categoria import Categoria
from projeto_webtheater.models.categoriaDAO import CategoriaDAO
from projeto_webtheater.models.video import Video
from projeto_webtheater.models.videoDAO import VideoDAO


categorias = CategoriaDAO([
    Categoria(0, "Sakura", "Sobre flores de cerejeira.", r'img\sakura.jpg'),
    Categoria(1, "Nascer do Sol", "Sobre nascer do Sol.", r'img\nascer.jpg'),
    Categoria(2, "Disco", "Alguns discos.", r'img\disco.jpg'),
])

videos = VideoDAO([
    Video(0, 'Sakura', 'Flores de Cerejeira', r'img\sakura.jpg', r'videos\sakura.mp4', 0),
    Video(1, 'Nascer do Sol', 'Nascer do Sol na Floresta', r'img\nascer.jpg', r'videos\sunrise.mp4', 1),
    Video(2, 'Disco', 'Disco de Vinil', r'img\disco.jpg', r'videos\disco.mp4', 2),
])    


def home(request):
    return render(request, "index.html", {})


def inicial(request):
    categorias.verifica_tres_mais_por_categoria(videos)
    return render(request, 'inicial.html', {'categorias': categorias})


def video(request, id):
    for v in videos.videos_list:
        if v.id == int(id):
            return render(request, 'video.html', {})
    return render(request, '', {'msg': 'NAO ENCONTRADO'}), 404
