# netbox_otn
Manage OTN Networks in Netbox

The netbox_otn plugin is made for OTN / DWDM engineers to support you to keep track of the different trails in your optical networks. Main function is to plan optical channels by select a free channel.

![netbox_otn concept](https://github.com/chwichmann/netbox_otn/blob/main/images/Netbox_Concept.jpg?raw=true)

## OMS - Optical Multiplexer Sections
The top layer of OTN is the Optical Multiplexer Section (OMS). OMS Trails keep the Optical Channels (OCH) together and are in-between two ports on devices where the channel mix can change (usaly between two ROADM, a Mux and ROADM or two Mux). You can link a circuit to an OMS trail.

## OCH - Optical Channel


