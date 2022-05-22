from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.LandingPageView.as_view(), name='catalog-index'),
    path('materials/', views.MaterialListView.as_view(), name='catalog-materials'),
    path('entry/', views.MaterialCreateView, name='catalog-entry'),
    path('entry_success/', views.MaterialSuccessView, name='catalog-success'),
    path('materials/<pk>/', views.MaterialDetailView.as_view(), name='catalog-detail'),
    path('search/', views.MaterialSearchView.as_view(), name='catalog-search'),
    path('login/', LoginView.as_view(), name='catalog-login'),
    path('logout/', LogoutView.as_view(), name='catalog-logout'),
    path('history/', views.MaterialHistoryView.as_view(), name='catalog-history'),
]