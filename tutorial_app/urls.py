from django.contrib import admin 
# Admin Page at:
# localhost:8000/admin
from django.urls import path, include 
#path is used for urls
#include is used to add urls from django apps
from django.views.generic import TemplateView
#TemplateView is used to render html pages
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
#on "localhost:8000/" you will get the index.html file
    path('admin/', admin.site.urls),
#on "localhost:8000/admin" you will get the django admin page
    path('User/', include('tutorial_auth.urls')),
#on "localhost:8000/User/" you will be able to use the urls from tutorial_auth
#example : "localhost:8000/User/users"
#"users/" is the url from tutorial_auth
    path('api-token-auth/', obtain_jwt_token),
#at "localhost:8008/api-token-auth/" you will be able to log in
#and return the jwt token and the rest of informations about the user
    path('api-token-refresh/', refresh_jwt_token),
]
