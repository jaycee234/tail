from django.contrib import admin
from .models import Author, Members, Books, BorrowRecords

# Register your models here.
admin.site.register(Author)
admin.site.register(Members)
admin.site.register(Books)
admin.site.register(BorrowRecords)
