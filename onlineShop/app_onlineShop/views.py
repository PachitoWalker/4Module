from django.shortcuts import render

# Create your views here.


# подключаем объект для выполнения http запросов
from django.http import HttpResponse

# Файл, отображающий файл index.html
def index(request):
    return render(request, 'index.html')   # render позволяет срендерить(отобразить) страницу в браузере, request - запрос, на который мы отвечаем, index.html - что отобразить

# функция, отображающая файл top-sellers.html
def top_sellers(request):
    return render(request, 'top-sellers.html')