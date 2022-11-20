"""This module for somme additional defs to views"""
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage


def get_posts(request):
    """
    Returns all posts by date
    :param request: Obj request
    :return: posts
    """
    from .models import Users

    pk = request.COOKIES.get('main_page')

    if pk:
        try:
            return Users.objects.get(pk=int(pk))
        except Users.DoesNotExist:
            return None


def paginate(
        obj: object,
        size: int,
        request: object,
        context: dict,
        var_name: str = 'object_list'
) -> dict:
    """
    Paginate objs provided by views
    :param obj:
    :param size:
    :param request:
    :param context:
    :param var_name:
    :return:
    """

    paginator = Paginator(obj, size)
    page = request.GET.get('page', '1')

    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context
