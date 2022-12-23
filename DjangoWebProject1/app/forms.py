"""
Definition of forms.
"""

from cProfile import label
from tkinter import Label
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class AnketaForm(forms.Form):
    name = forms.CharField(label ='Ваше имя', min_length=2)
    city = forms.CharField(label ='Ваш город', min_length=2)
    job = forms.CharField(label = 'Ваша работа', min_length=2)
    gender = forms.ChoiceField(label='Ваше пол',
                             choices=[('1', 'Мужской'), ('2', 'Женский')],
                             widget = forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Вы пользуетесь интернетом',
                             choices=[('1', 'Каждый день'), 
                             ('2', 'Несколько раз в день'),
                             ('3', 'Несколько раз в неделю')]) 
    email = forms.EmailField(label='Ваш email', min_length=7)
    notice = forms.BooleanField(label='Хотите получать новости?', required = False)
    message = forms.CharField(label='Коротко о себе', widget=forms.Textarea(attrs={'rows':12,'cols':20}))



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)

