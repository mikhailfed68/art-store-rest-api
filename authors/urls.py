from django.urls import path

from authors import views

urlpatterns = [
    path('', views.api_root, name="api-root"),
    path('painters/', views.PainterListView.as_view(), name='painter-list'),
    path('painters/<int:pk>/', views.PainterDetailView.as_view(), name='painter-detail'),
]
