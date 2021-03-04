import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

from .models import Book, Category


class UserType(DjangoObjectType):
    class Meta:
        model = User


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(object):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID())

    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.ID())

    all_users = graphene.List(UserType)

    def resolve_all_books(self, info, **kwargs):
        # Querying a list of book
        return Book.objects.all()

    def resolve_book(self, info, id):
        # Querying a single book
        return Book.objects.get(pk=id)

    def resolve_all_categories(self, info, **kwargs):
        # Querying a list of category
        return Category.objects.all()

    def resolve_category(self, info, id):
        # Querying a single book
        return Category.objects.get(pk=id)

    def resolve_all_users(self, info, **kwargs):
        # Querying a list of user
        return User.objects.all()


class CreateBook(graphene.Mutation):
    # Let's define the arguments we can pass the create method
    class Arguments:
        title = graphene.String()
        authors = graphene.List(graphene.ID)
        category_id = graphene.Int()
        price = graphene.Float()
        amount = graphene.Int()

    book = graphene.Field(BookType)

    def mutate(self, info, title, category_id, price, amount, authors=None):
        book = Book.objects.create(
            title=title,
            category_id=category_id,
            price=price,
            amount=amount
        )
        if authors is not None:
            authors_set = []
            for author_id in authors:
                author_object = User.objects.get(pk=author_id)
                authors_set.append(author_object)
            book.authors.set(authors_set)

        book.save()
        # return an instance of the Mutation
        return CreateBook(
            book=book
        )


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        authors = graphene.List(graphene.ID)
        category_id = graphene.Int()
        price = graphene.Float()
        amount = graphene.Int()

    book = graphene.Field(BookType)

    def mutate(self, info, id, title=None, authors=None, category_id=None, price=None, amount=None):
        book = Book.objects.get(pk=id)
        book.title = title if title is not None else book.title
        book.category_id = category_id if category_id is not None else book.category_id
        book.price = price if price is not None else book.price
        book.amount = amount if amount is not None else book.amount

        if authors is not None:
            authors_set = []
            for author_id in authors:
                author_object = User.objects.get(pk=author_id)
                authors_set.append(author_object)
            book.authors.set(authors_set)

        book.save()

        return UpdateBook(
            book=book
        )


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    def mutate(self, info, id):
        book = Book.objects.get(pk=id)

        if book is not None:
            book.delete()
        return DeleteBook(book=book)


#  Wiring up the mutations
class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()
