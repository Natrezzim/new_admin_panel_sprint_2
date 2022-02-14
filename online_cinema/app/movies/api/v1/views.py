import logging

from django.contrib.postgres.aggregates import ArrayAgg
from django.core.paginator import InvalidPage
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import DetailView
from django.views.generic.list import BaseListView

from ...models import Filmwork

logger = logging.getLogger("Paginator Logger")
logger.setLevel(logging.DEBUG)


def aggregate_person(role: str):
    if role == 'actors':
        return ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='actor'), distinct=True)
    elif role == 'directors':
        return ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='director'), distinct=True)
    elif role == 'writers':
        return ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='writer'), distinct=True)


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    @staticmethod
    def get_queryset():
        context = Filmwork.objects.all().order_by('title').values('id', 'title', 'description', 'creation_date',
                                                                  'rating', 'type', ).annotate(
            genres=ArrayAgg('genres__name', distinct=True),
            actors=aggregate_person('actors'),
            directors=aggregate_person('directors'),
            writers=aggregate_person('writers'), )
        return context

    @staticmethod
    def render_to_response(context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )

        if page.has_next():
            next_page = page.next_page_number()
        else:
            next_page = None

        if page.has_previous():
            prev_page = page.previous_page_number()
        else:
            prev_page = None

        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': prev_page,
            'next': next_page,
            'results': list(queryset),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, DetailView):
    def get_context_data(self, *, object_list=None, **kwargs):
        return kwargs['object']
