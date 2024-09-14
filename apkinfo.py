#!/usr/bin/env python3
from apkinfo.main import main, clean_up
from rich.console import Console
from apkinfo.utils import Utils
utils = Utils()

console = Console()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clean_up()
        with console.status("Decompiling APK ", spinner="dots2"):
            utils.logError("Performing cleanup")
        exit(0)
