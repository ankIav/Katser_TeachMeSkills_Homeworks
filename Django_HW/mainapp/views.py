from django.shortcuts import render
from django.db import connection

# from .utils import get_posts
# from .utils import paginate
from .models import Posts, Users


def index(request):

    qwery = (
        f'SELECT U.nickname, U.username, P.post, P.id'
        f' FROM mainapp_users U JOIN mainapp_posts P on U.id = P.user_id_id '
        f'ORDER BY P.create_at DESC'
    )

    with connection.cursor() as cursor:
        cursor.execute(qwery)
        row = cursor.fetchall()

    return render(
        request, 'mainapp/index.html', {'row': row}
    )


def posts(request, user: str, post_id: int):
    qwery = (
        f'SELECT U.nickname, U.username, P.post, P.create_at, P.id '
        f'FROM mainapp_users U JOIN mainapp_posts P on U.id = P.user_id_id '
        f'WHERE P.id = %s' % post_id
    )

    with connection.cursor() as cursor:
        cursor.execute(qwery)
        row = cursor.fetchall()

    return render(
            request, 'mainapp/posts.html', {'row': row}
    )


def profile(request, user: str):
    qwery = (
            f'SELECT U.nickname, U.username, U.bio, U.link, U.birthday, U.create_at, P.post, P.create_at, P.id '
            f'FROM mainapp_users U JOIN mainapp_posts P on U.id = P.user_id_id '
            f'WHERE U.username = "%s"'
            f'ORDER BY P.create_at DESC' % user
    )

    with connection.cursor() as cursor:
        cursor.execute(qwery)
        row = cursor.fetchall()

    return render(
            request, 'mainapp/profile.html', {'row': row}
    )