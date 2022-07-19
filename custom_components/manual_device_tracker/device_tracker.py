"""Manually updated device tracker"""
from __future__ import annotations
from collections.abc import Callable
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

def setup_scanner(
    hass: HomeAssistant,
    config: ConfigType,
    see: Callable[..., None],
    discovery_info: DiscoveryInfoType | None = None,
) -> bool:
    return True
