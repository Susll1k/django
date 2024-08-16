
from django.contrib import admin
from django.urls import path, include
from app.views import Login, SignUp, Logout, home, CreateCourse
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('singup/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('create/', CreateCourse.as_view(), name='create'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'), name='password_change_done')
]

