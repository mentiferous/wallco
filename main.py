import sys
from pathlib import Path

from rich import box
from rich.console import Console
from rich.table import Table

WALLPAPER_DIR = Path("wallpapers")

console = Console()

if not WALLPAPER_DIR.is_dir():
    console.print("[!] The wallpaper directory was not found", style="bold red")
    sys.exit(1)

wallpaper_ct = sum(1 for _ in WALLPAPER_DIR.iterdir())

table = Table(box=box.MINIMAL)

table.add_column("wallco", justify="center")

table.add_row(f"{wallpaper_ct} wallpapers")

console.print(table)
