from pathlib import Path

from importlib_resources import files


def path_to_kivy_file() -> Path:
    # Reads contents with UTF-8 encoding and returns str.
    return files("ugy_inventory_client.ui.resources").joinpath("kivi.kv")
