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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def service_assistant(request):
    recipe = ''.join(filter(str.isalnum, request.path))
    recipe_ingridients = DATA.get(recipe)
    servings = request.GET.get('servings')
    if not servings is None and not recipe_ingridients is None:
        person_count = int(servings)
        for ingridient in recipe_ingridients:
            recipe_ingridients[ingridient] *= person_count
    context = {
        'recipe': recipe_ingridients
    }
    return render(request, 'index.html', context)
