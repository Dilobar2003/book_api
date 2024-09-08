from django.db import models



class AuthorModel(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()


    def __str__(self):
        return self.name
    

class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(AuthorModel, related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100)


    def __str__(self):
        return self.title
    