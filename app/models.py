from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    short_content = models.TextField(verbose_name="Краткое содержание")
    full_content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name="Изображение")
    author = models.ForeignKey(
        User, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Автор"
    )  


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey('Blog', on_delete=models.CASCADE, verbose_name="Статья")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default=datetime.now, verbose_name="Дата добавления")

    class Meta:
        ordering = ['-date']  # Сортировка по убыванию даты

    def __str__(self):
        return f"Комментарий от {self.author} к статье '{self.post.title}'"
  
class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    poster = models.ImageField(upload_to='video_posters/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title