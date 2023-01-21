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


def service_helper(request):
    template_name = 'index.html'

    recipe = ''.join(filter(str.isalnum, (request.path)))
    get_recipe = DATA.get(recipe)

    if get_recipe is None:
        get_recipe = {}
        # если рецепт не найден, его дальнейшая обработка не имеет смысла
    else:
        servings = request.GET.get('servings')
        if not servings is None:
            person_count = int(servings)
            for key_ingridient in get_recipe.keys():
                get_recipe[key_ingridient] *= person_count
    context = {
        'recipe': get_recipe
    }
    return render(request, template_name, context)
