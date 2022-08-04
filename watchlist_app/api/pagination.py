from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 3 # each page includes 3 
    page_query_param = 'p' # search (?p=) instead of ?page=
    page_size_query_param = 'size' # user define the page_size (?size=6) it will load 6 instead of 3
    max_page_size = 10 # even if user define size grater than 10 it will show 10
    last_page_strings = 'end' # go to last page (?p=end)

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5 # each page includes 5 
    max_limit = 10 # skip first 10 elemnt then load from 11
    limit_query_param = 'limit' # let user limit it
    offset_query_param = 'start' # let user define the ofest

class WatchListCPagination(CursorPagination):
    page_size = 5 
    ordering = 'created'
    cursor_query_param = 'record' # name cursor (?record=)