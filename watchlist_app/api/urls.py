from django.urls import path,include
from watchlist_app.api.views import (WatchDetailAV, WatchListAV, StreamPlatformAV,
StreamPlatformDetailAV,ReviewDetail,ReviewList,ReviewCreate,StreamPlatformVS,UserReview,WatchListGV)

from rest_framework.routers import DefaultRouter # with viewset

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')
# steam is the url 

urlpatterns = [
    path('movie/',WatchListAV.as_view(), name='movie-list'),
    path('movie/<int:pk>/',WatchDetailAV.as_view(), name='movie-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),

    path('',include(router.urls)),

    # path('Stream/',StreamPlatformAV.as_view(), name='stream'),
    # path('Stream/<int:pk>/',StreamPlatformDetailAV.as_view(), name='stream-detail'),

    # path('review/',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),

    path('Stream/<int:pk>/review/',ReviewList.as_view(),name='review-list'),
    path('Stream/<int:pk>/review-create/',ReviewCreate.as_view(),name='create-review-list'),
    path('Stream/review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),

    path('reviews/', UserReview.as_view(), name='user-review-detail'),
]