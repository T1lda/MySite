from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Comment
from .models import Blog

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Email')
    rating = forms.ChoiceField(
        label='Оценка сайта',
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    improvements = forms.MultipleChoiceField(
        label='Что улучшить?',
        choices=[
            ('design', 'Дизайн'),
            ('speed', 'Скорость'),
            ('content', 'Контент'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    feedback = forms.CharField(
        label='Пожелания',
        widget=forms.Textarea,
        min_length=10,
        max_length=500
    )

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)  # Поле text будет доступно для ввода
        labels = {'text': 'Комментарий'}
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_content', 'full_content', 'image']
        labels = {
            'title': 'Заголовок',
            'short_content': 'Краткое содержание',
            'full_content': 'Полное содержание',
            'image': 'Изображение'
        }