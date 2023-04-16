from django.urls import path
from . import views

urlpatterns = [
    path('variants/', views.VariantListView.as_view(), name='variant_list'),
    path('variants/add/', views.AddVariantView.as_view(), name='add_variant'),
]
