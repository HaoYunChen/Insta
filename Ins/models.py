from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

from imagekit.models import ProcessedImageField

# Create your models here.
class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True,
    )

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self) # set myself as self
        return followers

    def is_followed_by(self, user): # am i getting followed by this user
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()

    def get_absolute_url(self):
        return reverse("user_detail", args = [str(self.id)])

class Post(models.Model):
    author = models.ForeignKey(
        InstaUser,
        on_delete = models.CASCADE,
        related_name = 'my_posts'
    )
    title = models.TextField(blank = True, null = True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True,
    )

    def get_like_count(self):
        return self.likes.count()

    def get_comment_count(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse("post_detail", args = [str(self.id)])

#like1 -> irving like post 1
#like2 -> peepoo like post 1

class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'likes' # use this to find all the likes relationships

    )
    user = models.ForeignKey(
        InstaUser,
        on_delete = models.CASCADE,
        related_name = 'likes'
    )

    class Meta:
        unique_together = ("post", "user") # they can be together once

    def __str__(self):
        return 'Like: ' + self.user.username + ' likes ' + self.post.title

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'comments'
    )

    user = models.ForeignKey(
        InstaUser, 
        on_delete = models.CASCADE,
    )

    posted_on = models.DateTimeField(auto_now_add=True, editable=False)
    comment_text = models.TextField(blank = True, null = True)

    def __str__(self):
        return 'Comment: ' + self.user.username + ' comments on ' + self.post.title

# A followed B, creator: A, following: B
# A.friendship_creator_set ----> get all the connection sets where A are the creators
class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False) # creation time, not that useful but o-well :D
    creator = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE, # if I delete A, this relationship will also get deleted
        related_name="friendship_creator_set")
    following = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friend_set")

    def __str__(self):
        return self.creator.username + ' follows ' + self.following.username