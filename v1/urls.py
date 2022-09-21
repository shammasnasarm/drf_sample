from django.urls import path, include
from .views import *

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'tests',SampleFunctionViewSet)

urlpatterns = [
    #path('', include(router.urls)),



    ######### Function Based View Calling #############
    path('categories/',CategoriesView),
    path('category/<int:id>/', CategoryView),


    ######### Class Based View Calling ##########
    path('products/', ProductsView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)