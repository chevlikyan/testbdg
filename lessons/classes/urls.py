from django.urls import path
from .views import *

urlpatterns = [
    path('categories_list', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('', ClassListView.as_view(), name='class-list'),
    path('classes/create/', ClassCreateView.as_view(), name='class-create'),
    path('classes/<slug:slug>/', ClassDetailView.as_view(), name='class-detail'),
    path('classes/<slug:slug>/edit/', ClassUpdateView.as_view(), name='class-edit'),
    path('classes/<slug:slug>/delete/', ClassDeleteView.as_view(), name='class-delete'),
    path('new_category', CategoryCreateView.as_view(), name='category-create')
]
