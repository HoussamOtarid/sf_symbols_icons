"""SF Symbols Icons Integration."""
import os
import json
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "sf_symbols_icons"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the SF Symbols Icons integration."""
    # Load icons.json
    icons_json_path = os.path.join(os.path.dirname(__file__), 'icons.json')
    
    if not os.path.exists(icons_json_path):
        return False
        
    with open(icons_json_path, 'r') as f:
        icons_data = json.load(f)

    # Register icons with Home Assistant
    def get_icon_path(name):
        return f"custom_components/{DOMAIN}/icons/{name}.svg"

    icons = {
        f"sf:{icon['name']}": get_icon_path(icon['name'])
        for icon in icons_data
    }

    hass.data[DOMAIN] = {"icons": icons}
    
    # Register the icons namespace
    if not hasattr(hass.data, "custom_icons"):
        hass.data["custom_icons"] = {}
    
    hass.data["custom_icons"]["sf"] = icons

    return True
