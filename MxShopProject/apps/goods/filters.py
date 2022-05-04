from django_filters.rest_framework.filterset import FilterSet
from django_filters import filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(FilterSet):
    """
    自定义商品过滤器
    """
    pricemin = filters.NumberFilter(field_name="shop_price", lookup_expr="gte")
    pricemax = filters.NumberFilter(field_name="shop_price", lookup_expr="lte")
    top_category = filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ["pricemin", "pricemax", "is_hot", "is_new"]
