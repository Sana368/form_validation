from django.urls import path
from.import views
urlpatterns=[
    path('login_view/',views.login_view,name='login_view'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('logout_view/',views.logout_view,name='logout_view')
]