from rest_framework import serializers
from .models import Author, Members, Books, BorrowRecords

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author_name', 'email']

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'name', 'email', 'phone_number']

class BooksSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = ['id', 'title', 'author']

class BorrowRecordsSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField()
    book = serializers.StringRelatedField()

    class Meta:
        model = BorrowRecords
        fields = ['id', 'borrow_date', 'return_date', 'member', 'book']
        read_only_fields = ['borrow_date']