from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination):
    class_size = 10