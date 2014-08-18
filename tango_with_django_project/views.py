from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Tango with Django</h1><ul><li><a href='/rango/'>Rango</a></li></ul>")