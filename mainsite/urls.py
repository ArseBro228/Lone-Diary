from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

# from .views import ResetPasswordView
from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('login', LoginView.as_view(), name='mainsite_login'),
                  path("mainsite/post/<str:title>", views.post, name="post"),
                  path('logout', LogoutView.as_view(), name='mainsite_logout'),
                  path('register', views.RegisterUser.as_view(), name='register'),
                  # path('password_reset',ResetPasswordView.as_view(), name = 'password_reset'),
                  path('news', views.news, name='news'),
                  path('profile', views.profile, name='profile'),
                  path('', include('django.contrib.auth.urls')),
                  path('subjects', views.subjects, name='subjects'),
                  path('add_post/<course_id>', views.add_post, name='add_post'),
                  path('contacts', views.contacts, name='contacts'),
                  path('posts/<int:course_id>', views.posts, name='posts'),

              ] + static(settings.STATIC_URL)
