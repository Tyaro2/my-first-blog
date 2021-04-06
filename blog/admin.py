from django.contrib import admin
from .models import Post, Comment, User, FriendShip

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(FriendShip)


# Register your models here.
