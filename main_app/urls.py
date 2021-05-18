from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.ProfileDetail.as_view(), name="profile"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('profile/<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),
    path('profile/<int:pk>/update/city', views.UpdateProfile.as_view(), name='update_profile'),
    
    path('profile/<int:pk>/post_detail/', views.PostDetail.as_view(), name='post_detail'),
]