from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from api.views.views_cbv import CategoryListAPIView,CategoryDetailAPIView,CategoryWithVacanciesListAPUView,ImageListAPIView,    ImageDetailAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),
    path('categories/<int:category_id>/images/', CategoryWithVacanciesListAPUView.as_view()),

    path('images/', ImageListAPIView.as_view()),
    path('images/<int:image_id>/', ImageDetailAPIView.as_view()),
    ]
urlpatterns+=staticfiles_urlpatterns()