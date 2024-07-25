from django.shortcuts import render


def index(request):
    
    context = {
        'title': 'Главная страница',
        'content': 'Вы на главной странице сайта!',
    }

    return render(request, 'main/index.html', context)