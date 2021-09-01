"""libraryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from music import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/profile/', views.profile_view, name='profile_page'),
    path('accounts/signup/', views.user_signup, name='user_signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.main_page, name='home'),
    path('admin/', admin.site.urls),
    path('song_list/', views.songs_list, name='list'),
    path('songs/new', views.SongCreate.as_view(), name='song_create'),
    path('musician/new', views.MusicianCreate.as_view(), name='musician_create'),
    path('musician_list/', views.MusicianList.as_view(), name='musician_list'),
    path('musician/<int:pk>', views.MusicianDetail.as_view(), name='musician_detail'),
    path('user_songs', views.UserSongList.as_view(), name='user_songs'),
    path('update/<int:pk>', views.SongUpdateView.as_view(), name='song_update'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
