from netbox.filtersets import NetBoxModelFilterSet
from .models import Channel

class ChannelFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Channel
        fields = ('id', 'name')

        def search(self, queryset, name, value):
            return queryset.filter(name__icontains=value)

