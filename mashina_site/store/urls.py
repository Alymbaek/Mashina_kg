from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),

    path('', CarListViewSet.as_view({'get': 'list', 'post': 'create'}),name='car_list'),
    path('<int:pk>/', CarDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='car_detail'),

    path('marka/', MarkaViewSet.as_view({'get': 'list', 'post': 'create'}),name='marka_list'),
    path('marka/<int:pk>/', MarkaViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='marka_detail'),

    path('model/', ModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='model_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='model_detail'),

    path('car_photos/', CarPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_photos_list'),
    path('car_photos/<int:pk>/', CarPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='car_photos_detail'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='user_detail'),

    path('cart/', CartViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_list'),
    path('cart/<int:pk>/', CartViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='cart_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list',
                                           'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='review_detail'),

]