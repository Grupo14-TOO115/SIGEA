from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'paginas/home.html')
def documentos_anexos(request):
    return render(request, 'consultar_documentos_anexos/consultar.html')