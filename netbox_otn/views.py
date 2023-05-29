from netbox.views import generic
from . import forms, models, tables, filtersets
from django.db.models import Count
from utilities.utils import count_related

# OMS
class OMSView(generic.ObjectView):
    queryset = models.OMS.objects.all()

    def get_extra_context(self, request, instance):
        ochs=models.OCH.objects.restrict(request.user, 'view').filter(oms=instance)
        table = tables.OCHTable(ochs)
        table.configure(request)

        return {
            'och_table': table,
        }

class OMSListView(generic.ObjectListView):
    queryset = models.OMS.objects.annotate(
        och_count=count_related(models.OCH, 'oms'),
    )
    table = tables.OMSTable

class OMSEditView(generic.ObjectEditView):
    queryset = models.OMS.objects.all()
    form = forms.OMSForm

class OMSBulkDeleteView(generic.BulkDeleteView):
    queryset = models.OMS.objects.all()
    table = tables.OMSTable

class OMSBulkEditView(generic.BulkEditView):
    queryset = models.OMS.objects.all()
    #filterset = filters.CommunityFilterSet
    table = tables.OMSTable
    form = forms.OMSBulkEditForm

class OMSDeleteView(generic.ObjectDeleteView):
    queryset = models.OMS.objects.all()

# OCH
class OCHView(generic.ObjectView):
    queryset = models.OCH.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.OMSTable(instance.oms.all())
        table.configure(request)

        return {
            'oms_table': table,
        }

class OCHListView(generic.ObjectListView):
    queryset = models.OCH.objects.all()
    table = tables.OCHTable

class OCHEditView(generic.ObjectEditView):
    queryset = models.OCH.objects.all()
    form = forms.OCHForm

class OCHBulkDeleteView(generic.BulkDeleteView):
    queryset = models.OCH.objects.all()
    table = tables.OCHTable

class OCHBulkEditView(generic.BulkEditView):
    queryset = models.OCH.objects.all()
    #filterset = filters.CommunityFilterSet
    table = tables.OCHTable
    form = forms.OCHBulkEditForm

class OCHDeleteView(generic.ObjectDeleteView):
    queryset = models.OCH.objects.all()

# Channel Group
class ChannelGroupView(generic.ObjectView):
    queryset = models.ChannelGroup.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.ChannelTable(instance.channels.all())
        table.configure(request)

        return {
            'channel_table': table,
        }

class ChannelGroupListView(generic.ObjectListView):
    queryset = models.ChannelGroup.objects.annotate(
        channel_count=Count('channels')
    )
    table = tables.ChannelGroupTable
    filterset = filtersets.ChannelFilterSet
    filterset_form =forms.ChannelFilterForm

class ChannelGroupEditView(generic.ObjectEditView):
    queryset = models.ChannelGroup.objects.all()
    form = forms.ChannelGroupForm

class ChannelGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.ChannelGroup.objects.all()

# Channel
class ChannelView(generic.ObjectView):
    queryset = models.Channel.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.OCHTable(instance.och_channel.all())
        table.configure(request)

        return {
            'och_table': table,
        }

class ChannelListView(generic.ObjectListView):
    queryset = models.Channel.objects.all()
    table = tables.ChannelTable

class ChannelEditView(generic.ObjectEditView):
    queryset = models.Channel.objects.all()
    form = forms.ChannelForm

class ChannelDeleteView(generic.ObjectDeleteView):
    queryset = models.Channel.objects.all()

class ChannelBulkImportView(generic.BulkImportView):
    queryset = models.Channel.objects.all()
    model_form = forms.ChannelImportForm
    table = tables.ChannelTable
