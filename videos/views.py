from django.shortcuts import render
from .models import *

# Create your views here.
def convertir_popularvideo(qs):
    convert = str(qs.url)
    try: 
        embed = f"https://www.youtube.com/embed/{convert.split('=')[1]}"
        qs.url = embed
        qs.save()
    except:
        print("URL Invalida")
        
    return {"titulo": qs.titulo, "url": qs.url, "dsc": qs.dsc}

def home(request):
    popular_video = PopularVideo.objects.all().last()
    videos = Videos.objects.all().reverse()[:6]

    contexto = {
        "popular_video": convertir_popularvideo(popular_video),
        "videos": videos,

    }

    return render(request, 'index.html', contexto)