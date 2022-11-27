from extras.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_otn:oms_list",
        link_text="OMS Trails",
    ),

    PluginMenuItem(
        link="plugins:netbox_otn:och_list",
        link_text="OCH Trails",
    ),

    PluginMenuItem(
        link="plugins:netbox_otn:channel_list",
        link_text="WDM Channels",
    ),

    PluginMenuItem(
        link="plugins:netbox_otn:channelgroup_list",
        link_text="WDM Channel Groups",
    ),

)
