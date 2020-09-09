from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from recipe_app.models import Author, Recipe
from recipe_app.forms import AddAuthorForm, AddRecipeForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

@login_required
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

    # put into index?

@login_required
def recipe_edit(request, id):
    edit = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = AddRecipeForm(request.POST, instance=edit)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('recipe', edit.pk)
    else:
        form = AddRecipeForm(instance=edit)
        return render(request, 'standard_form.html', {'form': form})
    # else:
        # return HttpResponseForbidden("You do not have permission to edit this recipe")






@login_required
def author_form_view(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password')
            )
            Author.objects.create(
                name=data.get('name'),
                bio=data.get('bio'),
                user=user
            )
            return HttpResponseRedirect('/')
    # Testing to see if user is staff
    if not request.user.is_staff:
        # if not, the user can't submit an author
        form = None
        error = 'Sorry, only staff can create authors!'
    # if the user is staff, they can fill out the form
    else:
        error = None
        form = AddAuthorForm()
    return render(request, 'standard_form.html', {'form': form, 'error':error})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                # If redirected to login from another page, user gets sent there, otherwise they are sent home
                return HttpResponseRedirect(request.GET.get('next', '/'))

    form = LoginForm()
    return render(request, 'standard_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
