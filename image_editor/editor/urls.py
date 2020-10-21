from django.urls import path
from .views import HomeView, UploadImageView, EditImageView


app_name = "editor"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('upload/', UploadImageView.as_view(), name="upload"),
    path('<int:id>/resize/', EditImageView.as_view(), name="resize")
    ]
