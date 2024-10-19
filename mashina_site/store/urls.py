from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', CarListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', CarDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='product_detail'),

    path('profile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('profile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                         'delete': 'destroy'}), name='user_detail'),

    path('marka/', MarkaViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('marka/<int:pk>/', MarkaViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                 'delete': 'destroy'}), name='category_detail'),

    path('model/', ModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                 'delete': 'destroy'}), name='product_detail'),

    path('car_photos/', CarPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('car_photos/<int:pk>/', CarPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                          'delete': 'destroy'}), name='user_detail'),

    path('cart/', CartViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('cart/<int:pk>/', CartViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='category_detail'),

    path('review', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                   'delete': 'destroy'}), name='product_detail'),

    ]
