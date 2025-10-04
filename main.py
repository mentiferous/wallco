from pathlib import Path

from rich import box
from rich.console import Console
from rich.table import Table

WALLPAPER_DIR = Path("wallpapers")

wallpaper_count = len(list(WALLPAPER_DIR.iterdir()))

table = Table(box=box.MINIMAL)

table.add_column("wallco", justify="center")

table.add_row(f"{wallpaper_count} wallpapers")

console = Console()

console.print(table)
