"""Mod loader — discovers and imports all ff8000.mods.* packages in alphabetical order.

Mods that depend on other mods being initialised first should simply import them
at the top of their own __init__.py; Python's import cache (sys.modules) ensures
each mod is only executed once regardless of how many times it is imported.
"""

import importlib
import pkgutil

import ff8000.mods
from .get_logger import get_logger

logger = get_logger(__name__)


def load_all_mods() -> None:
    """Import every installed ff8000.mods.* subpackage in alphabetical order."""
    entries = sorted(
        pkgutil.iter_modules(ff8000.mods.__path__, prefix="ff8000.mods."),
        key=lambda e: e[1],
    )

    if not entries:
        logger.warning("No mods found under ff8000.mods — is at least ff8000.mods._ installed?")
        return

    for _finder, name, _ispkg in entries:
        logger.debug("Loading mod: %s", name)
        importlib.import_module(name)
        logger.info("Loaded mod: %s", name)
