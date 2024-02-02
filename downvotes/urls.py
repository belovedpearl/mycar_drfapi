from django.urls import path
from downvotes import views

urlpatterns = [
    path('downvotes/', views.DownvoteListView.as_view()),
    path('downvotes/<int:pk>/', views.DownvoteDetail.as_view()),
]
