from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_otn'

router = NetBoxRouter()
router.register('oms', views.OMSViewSet)
router.register('och', views.OCHViewSet)
router.register('channelgroup', views.ChannelGroupViewSet)
router.register('channel', views.ChannelViewSet)

urlpatterns = router.urls