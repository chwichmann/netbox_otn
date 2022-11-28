from extras.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_otn:oms_list",
        link_text="Optical Multiplexer Sections",
    ),

    PluginMenuItem(
        link="plugins:netbox_otn:och_list",
        link_text="Optical Channels",
    ),

    PluginMenuItem(
        link="plugins:netbox_otn:channel_list",
        link_text="Channels",
    ),

    PluginMenuItem(
        link="plugins:netbox_otn:channelgroup_list",
        link_text="Channel Groups",
    ),
)
