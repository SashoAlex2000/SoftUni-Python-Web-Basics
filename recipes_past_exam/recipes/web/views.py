from django.shortcuts import render, redirect

from recipes.web.forms import RecipeAddForm, RecipeEditForm, RecipeDeleteForm
from recipes.web.models import Recipe


# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    recipes_count = len(recipes)

    context = {
        'recipes': recipes,
        'count': recipes_count,
    }

    return render(request,
                  'index.html',
                  context)


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeAddForm()
    else:
        form = RecipeAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request,
                  'create.html',
                  context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = RecipeEditForm(instance=recipe)
    else:
        form = RecipeEditForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request,
                  'edit.html',
                  context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = RecipeDeleteForm(instance=recipe)
    else:
        form = RecipeDeleteForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(
        request,
        'delete.html',
        context,
    )


def details_recipe(request, pk):
    current_recipe = Recipe.objects.filter(pk=pk).get()

    ingredients = [x for x in current_recipe.ingredients.split(', ')]

    context = {
        'recipe': current_recipe,
        'ingredients': ingredients,
    }

    return render(request,
                  'details.html',
                  context)

