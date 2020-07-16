from django.contrib import admin
from Ins.models import Post, InstaUser, Like, UserConnection, Comment # so that I can see these in admin page

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)
admin.site.register(Comment)