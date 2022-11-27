"""Plugin declaration for netbox_otn.

(c) 2022 Christian Wichmann
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from extras.plugins import PluginConfig


class OtnConfig(PluginConfig):
    """Plugin configuration for the netbox_otn plugin."""

    name = "netbox_otn"
    verbose_name = "OTN"
    author = "Christian Wichmann"
    author_email = "christian.wichmann@outlook.com"
    description = "A plugin for NetBox to add the OTN Layer"
    version = "0.1.1"
    base_url = "otn"
    required_settings = []
    default_settings = {}
    caching_config = {}


config = OtnConfig  # pylint:disable=invalid-name
