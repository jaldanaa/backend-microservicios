from rest_framework import pagination


class PublicacionPagination(pagination.PageNumberPagination):
    page_size = 10  # the no. of company objects you want to send in one go