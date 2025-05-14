from django.conf import settings  
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('registration/', views.registration, name='registration'),
    path('links/', views.links, name='links'),
    path(
        'login/',
        LoginView.as_view(
            template_name='app/login.html',
            authentication_form=views.BootstrapAuthenticationForm,  # Убедитесь, что форма определена в views.py
            extra_context={
                'title': 'Авторизация',
                'year': views.current_year()  # Рекомендуется вынести в функцию во views.py
            }
        ),
        name='login'
    ),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/', views.blog_list, name='blog_list'),
    path('newpost/', views.new_post, name='new_post'),
    path('video/', views.videopost, name='videopost'),
]

# Обработка медиафайлов в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)