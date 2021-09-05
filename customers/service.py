# from django_filters import rest_framework as filters
# from .models import UserContacts
#
#
# class CharFilterInFilter(filters.CharFilter):
#     pass
#
# class UserContactsFilter(filters.FilterSet):
#     first_name = CharFilterInFilter(field_name='first_name')
#     phone = CharFilterInFilter(field_name='phone')
#
#     class Meta:
#         model = UserContacts
#         fields = ['first_name', 'phone']