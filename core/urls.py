
from django.contrib import admin
from django.urls import path
from app.views import Login, SignUp, Logout, home, CreateCourse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('singup/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('create/', CreateCourse.as_view(), name='create')

]
