"""SF Symbols Icons Integration."""
import os
import json
import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "sf_symbols_icons"
_LOGGER = logging.getLogger(__name__)

def get_icon_path(icon_name: str) -> str:
    """Get the path for a specific icon."""
    return f"/local/custom_components/sf_symbols_icons/icons/{icon_name}.svg"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the SF Symbols Icons integration."""
    _LOGGER.debug("Starting SF Symbols Icons setup")
    
    # Load icons.json
    icons_json_path = os.path.join(os.path.dirname(__file__), 'icons.json')
    _LOGGER.debug("Looking for icons.json at: %s", icons_json_path)
    
    try:
        with open(icons_json_path, 'r') as f:
            icons_data = json.load(f)
            _LOGGER.info("Successfully loaded icons.json with %d icons", len(icons_data))
    except FileNotFoundError:
        _LOGGER.error("icons.json not found at %s", icons_json_path)
        return False
    except json.JSONDecodeError as e:
        _LOGGER.error("Failed to parse icons.json: %s", str(e))
        return False

    # Create mapping of icon names to paths
    icons = {
        f"sf:{icon['name']}": get_icon_path(icon['name'])
        for icon in icons_data
    }
    _LOGGER.debug("Created icon mapping with %d icons", len(icons))

    # Register icons in both locations for compatibility
    if not hasattr(hass.data, "custom_icons"):
        _LOGGER.debug("Initializing custom_icons in hass.data")
        hass.data["custom_icons"] = {}
    
    hass.data[DOMAIN] = {"icons": icons}
    hass.data["custom_icons"]["sf"] = icons
    
    _LOGGER.info("SF Symbols Icons integration setup complete with %d icons", len(icons))
    _LOGGER.debug("First few icons registered: %s", list(icons.keys())[:5])

    return True
