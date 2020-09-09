from django import forms
from recipe_app.models import Author, Recipe

class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=80)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'description', 'timeRequired', 'instructions']
    
    # title = forms.CharField(max_length=100)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    # description = forms.CharField(widget=forms.Textarea)
    # timeRequired = forms.CharField(max_length=30)
    # instructions = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
