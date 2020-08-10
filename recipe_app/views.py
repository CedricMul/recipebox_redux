from django.shortcuts import render, HttpResponseRedirect
from recipe_app.models import Author, Recipe
from recipe_app.forms import AddAuthorForm, AddRecipeForm

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author_detail.html', {
        'author': author,
        'recipes': recipes
        })

def recipe_form_view(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                timeRequired=data['timeRequired'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect('/')
    form = AddRecipeForm()
    return render(request, 'standard_form.html', {'form': form})

def author_form_view(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect('/')
    form = AddAuthorForm()
    return render(request, 'standard_form.html', {'form': form})
