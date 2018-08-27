import datetime

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated'
    ),
    # 'DEFAULT_PAGINATION_CLASS':(
    #     'restapi.restconf.pagination.CustomAPIPagination'
    # ),
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'rest_framework.filters.SearchFilter',
    #     'rest_framework.filters.OrderingFilter',
    # ),
    # 'SEARCH_PARAM': 'q',
    # 'ORDERING_PARAM': 'ordering',
}