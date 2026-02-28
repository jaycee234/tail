from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Author, Members, Books, BorrowRecords
from .serializers import AuthorSerializer, MembersSerializer, BooksSerializer, BorrowRecordsSerializer

class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MembersListCreateAPIView(ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class MembersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class BorrowRecordsListCreateAPIView(ListCreateAPIView):
    queryset = BorrowRecords.objects.all()
    serializer_class = BorrowRecordsSerializer


class BorrowRecordsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BorrowRecords.objects.all()
    serializer_class = BorrowRecordsSerializer

class BooksListCreateAPIView(ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer



# Create your views here.
