import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

from library.models import Book, Category


class UserType(DjangoObjectType):
    class Meta:
        model = User

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_users = graphene.List(UserType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
