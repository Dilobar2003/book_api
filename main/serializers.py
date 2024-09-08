from rest_framework import serializers

from .models import AuthorModel, BookModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
       model = AuthorModel
       fields = ['id', 'name', 'birth_date']



class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = BookModel
        fields = ['id', 'title', 'author', 'publication_date', 'isbn', 'genre']