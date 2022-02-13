import logging
from django.core.paginator import InvalidPage

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from ...models import Filmwork

logger = logging.getLogger("Paginator Logger")
logger.setLevel(logging.DEBUG)


class MoviesListApi(BaseListView):
    model = Filmwork
    http_method_names = ['get']  # Список методов, которые реализует обработчик
    paginate_by = 50

    def get_queryset(self):
        context = Filmwork.objects.all().order_by('title').values('id', 'title', 'description', 'creation_date',
                                                                  'rating', 'type', ) \
            .annotate(genres=ArrayAgg('genres__name', distinct=True),
                      actors=ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='actor'), distinct=True),
                      directors=ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='director'),
                                         distinct=True),
                      writers=ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='writer'), distinct=True), )
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )

        try:
            next_page = page.next_page_number()
        except InvalidPage as e:
            next_page = None

        try:
            prev_page = page.previous_page_number()
        except InvalidPage as e:
            prev_page = None

        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': prev_page,
            'next': next_page,
            'results': list(queryset),
        }
        return context

    @staticmethod
    def render_to_response(context, **response_kwargs):
        return JsonResponse(context)
