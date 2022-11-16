from django.db import models


# creating table Users in my_db
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=80, blank=True, null=False)
    nickname = models.CharField(max_length=80, blank=True, null=False)
    bio = models.CharField(max_length=100)
    link = models.CharField(max_length=40)
    # avatar = models.ImageField()
    email = models.EmailField(max_length=50)
    create_at = models.DateTimeField(auto_created=True)

    def __repr__(self):
        return f'<User @{self.username}: {self.nickname}>'
