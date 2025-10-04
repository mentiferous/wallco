from os import listdir

from rich import box
from rich.console import Console
from rich.table import Table

WALLPAPER_DIR = "wallpapers"

wallpaper_count = len(listdir(WALLPAPER_DIR))

table = Table(box=box.MINIMAL)

table.add_column("wallco", justify="center")

table.add_row(f"/{WALLPAPER_DIR} {wallpaper_count}")

console = Console()

console.print(table)
