from django.http import HttpResponse
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def counter(count, key):
    answer = {}
    for i, a in DATA[key].items():
        answer[i] = float(a) * int(count)
    return answer


def pasta(request):
    context = {}
    count = request.GET.get('servings')
    if count is None:
        context['recipe'] = DATA['pasta']
        return render(request, 'calculator/index.html', context)
    else:
        context['recipe'] = counter(count, 'pasta')
        return render(request, 'calculator/index.html', context)


def buter(request):
    context = {}
    count = request.GET.get('servings')
    if count is None:
        context['recipe'] = DATA['buter']
        return render(request, 'calculator/index.html', context)
    else:
        context['recipe'] = counter(count, 'buter')
        return render(request, 'calculator/index.html', context)


def omlet(request):
    context = {}
    count = request.GET.get('servings')
    if count is None:
        context['recipe'] = DATA['omlet']
        return render(request, 'calculator/index.html', context)
    else:
        context['recipe'] = counter(count, 'omlet')
        return render(request, 'calculator/index.html', context)
