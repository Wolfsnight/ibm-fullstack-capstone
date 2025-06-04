from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    path("register", views.registration, name="register"),
    path(route='login', view=views.login_user, name='login'),
    path("logout", views.logout_user, name="logout"),
    path('get_cars', views.get_cars, name='getcars'),
    path("get_dealers/", views.get_dealerships, name="get_dealers"),
    path(route='add_review', view=views.add_review, name='add_review'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
