from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Book(models.Model):
    """
    The Book model which is related to the User model ManyToMany.
    All fields are required
    """
    title = models.CharField(_('title'), max_length=150, db_index=True)
    authors = models.ManyToManyField(User, related_name='books', verbose_name='authors')
    price = models.FloatField(_('price'))
    image = models.ImageField(_('image'), help_text='Cover book')
    amount = models.PositiveIntegerField(_('amount'))


    def __str__(self):
        """
        Return the title of the book
        """
        return self.title


    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
