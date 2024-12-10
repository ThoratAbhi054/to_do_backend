import django_filters

from iam.user.models import UserProfile


class UserFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id", lookup_expr="exact")
    username = django_filters.CharFilter(
        field_name="user__username", lookup_expr="exact"
    )
    first_name = django_filters.CharFilter(
        field_name="user__first_name", lookup_expr="exact"
    )
    last_name = django_filters.CharFilter(
        field_name="user__last_name", lookup_expr="exact"
    )
    email = django_filters.CharFilter(field_name="user__email", lookup_expr="exact")
    contact_no = django_filters.CharFilter(field_name="contact_no", lookup_expr="exact")
    city = django_filters.CharFilter(field_name="city", lookup_expr="exact")

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "contact_no",
            "city",
        ]
