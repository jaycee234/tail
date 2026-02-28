from django.contrib import admin
from django.urls import path
from .views import AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView, MembersListCreateAPIView, MembersRetrieveUpdateDestroyAPIView, BooksListCreateAPIView, BooksRetrieveUpdateDestroyAPIView, BorrowRecordsListCreateAPIView, BorrowRecordsRetrieveUpdateDestroyAPIView

urlpatterns = [

    path('author/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('author/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),

    path('members/', MembersListCreateAPIView.as_view(), name='members-list-create'),
    path('members/<int:pk>/', MembersRetrieveUpdateDestroyAPIView.as_view(), name='members-detail'),

    path('books/', BooksListCreateAPIView.as_view(), name='books-list-create'),
    path('books/<int:pk>/', BooksRetrieveUpdateDestroyAPIView.as_view(), name='books-detail'),

    path('borrow-records/', BorrowRecordsListCreateAPIView.as_view(), name='borrow-records-list-create'),
    path('borrow-records/<int:pk>/', BorrowRecordsRetrieveUpdateDestroyAPIView.as_view(), name='borrow-records-detail'),

]