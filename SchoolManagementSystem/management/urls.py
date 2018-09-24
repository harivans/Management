from django.conf.urls import url
from management import views


urlpatterns = [
    
    url(r'^$', views.index, name="Index"),
    url(r'^about/', views.about, name="About"),
    url(r'^gallery/', views.gallery, name="gallery"),
    url(r'^register/', views.register, name="Register"),
    url(r'^login/', views.Login, name="Login"),
    url(r'^home/', views.home, name="Home"),
    url(r'^logout/', views.Logout, name="Logout"),
    url(r'^add_faculty/', views.add_faculty, name="Add faculty"),
    url(r'^invalid_user/', views.invalid_user, name="Add faculty"),
]