from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
    )


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class PostPageNumberPagination(PageNumberPagination):
    page_size = 2    