from django.db import models


# creating table Users in BLOG schema
class Users(models.Model):
    """User model"""

    class Meta:
        verbose_name = u'User'
        verbose_name_plural = u'Users'

    id = models.AutoField(primary_key=True)
    username = models.CharField(
        verbose_name=u'Username',
        max_length=80,
        editable=True,
        unique=True,
        blank=False,
    )
    nickname = models.CharField(
        verbose_name=u'Nickname',
        max_length=80,
        editable=True,
        blank=False,
    )
    bio = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        editable=True,
    )
    link = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        editable=True,
    )
    email = models.EmailField(max_length=50, unique=True, blank=False)
    birthday = models.DateField(blank=True, null=True)
    create_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __repr__(self):
        return f'<User @{self.username}: {self.nickname}>'


# creating table Posts in BLOG schema
class Posts(models.Model):
    """Post model"""

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'

    id = models.AutoField(primary_key=True)
    post = models.CharField(max_length=200, blank=True, editable=True)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    user_id = models.ForeignKey(
        'Users', verbose_name="User's id", blank=False,
        on_delete=models.PROTECT,
    )

    def __repr__(self):
        return (
            f'<Username @{self.user_id.username} Post #{self.id}:'
            f'\n{self.post}\t{self.create_at}>'
        )

