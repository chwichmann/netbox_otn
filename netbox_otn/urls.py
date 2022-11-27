from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
        # OMS
        path('oms/', views.OMSListView.as_view(), name='oms_list'),
        path('oms/add/', views.OMSEditView.as_view(), name='oms_add'),
        path('oms/<int:pk>/', views.OMSView.as_view(), name='oms'),
        path('oms/<int:pk>/edit/', views.OMSEditView.as_view(), name='oms_edit'),
        path('oms/<int:pk>/delete/', views.OMSDeleteView.as_view(), name='oms_delete'),
        path('oms/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='oms_changelog', kwargs={
            'model': models.OMS
            }),

        # OCH
        path('och/', views.OCHListView.as_view(), name='och_list'),
        path('och/add/', views.OCHEditView.as_view(), name='och_add'),
        path('och/<int:pk>/', views.OCHView.as_view(), name='och'),
        path('och/<int:pk>/edit/', views.OCHEditView.as_view(), name='och_edit'),
        path('och/<int:pk>/delete/', views.OCHDeleteView.as_view(), name='och_delete'),
        path('och/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='och_changelog', kwargs={
            'model': models.OCH
            }),

        # ChannelGroup
        path('channelgroup/', views.ChannelGroupListView.as_view(), name='channelgroup_list'),
        path('channelgroup/add/', views.ChannelGroupEditView.as_view(), name='channelgroup_add'),
        path('channelgroup/<int:pk>/', views.ChannelGroupView.as_view(), name='channelgroup'),
        path('channelgroup/<int:pk>/edit/', views.ChannelGroupEditView.as_view(), name='channelgroup_edit'),
        path('channelgroup/<int:pk>/delete/', views.ChannelGroupDeleteView.as_view(), name='channelgroup_delete'),
        path('channelgroup/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='channelgroup_changelog', kwargs={
            'model': models.ChannelGroup
            }),

        # Channel
        path('channel/', views.ChannelListView.as_view(), name='channel_list'),
        path('channel/add/', views.ChannelditView.as_view(), name='channel_add'),
        path('channel/<int:pk>/', views.ChannelView.as_view(), name='channel'),
        path('channel/<int:pk>/edit/', views.ChannelEditView.as_view(), name='channel_edit'),
        path('channel/<int:pk>/delete/', views.ChannelDeleteView.as_view(), name='channel_delete'),
        path('channel/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='channel_changelog', kwargs={
            'model': models.Channel
            }),

        )
