#!/usr/bin/env python3
#this belongs in root /launch.py - Version: 1
# X-Seti - September23 2026 - Hex Workshop - Launcher

"""
Launcher - Standalone entry point for Hex Workshop.

Usage:
    python3 launch.py [file]

On WSL2:
    Auto-sets QT_QPA_PLATFORM=xcb and DISPLAY if not already set.
"""

import sys
import os
from pathlib import Path

##Methods list -
# configure_display
# launch_hex_workshop
# main

root_dir = Path(__file__).parent.resolve()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))


def configure_display(): #vers 1
    """Set Qt platform and DISPLAY for WSL2 and Wayland environments."""
    if 'QSG_RHI_BACKEND' not in os.environ:
        os.environ['QSG_RHI_BACKEND'] = 'opengl'

    is_wsl = False
    try:
        with open('/proc/version', 'r') as f:
            is_wsl = 'microsoft' in f.read().lower()
    except OSError:
        pass

    if is_wsl:
        if 'QT_QPA_PLATFORM' not in os.environ:
            os.environ['QT_QPA_PLATFORM'] = 'xcb'
        if 'DISPLAY' not in os.environ:
            os.environ['DISPLAY'] = ':0'
        print("[launch] WSL2 detected - QT_QPA_PLATFORM=xcb, DISPLAY=:0")
    elif os.environ.get('WAYLAND_DISPLAY') and 'QT_QPA_PLATFORM' not in os.environ:
        os.environ['QT_QPA_PLATFORM'] = 'xcb'


def launch_hex_workshop(): #vers 1
    """Start Hex Workshop, opening argv[1] if given."""
    from PyQt6.QtWidgets import QApplication
    from apps.components.Hex_Editor.hex_workshop import open_hex_workshop
    app = QApplication(sys.argv)
    path = sys.argv[1] if len(sys.argv) > 1 else None
    w = open_hex_workshop(file_path=path)   # keep window referenced
    return app.exec()


def main(): #vers 1
    configure_display()
    try:
        return launch_hex_workshop()
    except ImportError as e:
        print(f"ERROR: Failed to import Hex Workshop: {e}")
        print(f"  Root: {root_dir}")
        print("  Install PyQt6:  pip install PyQt6")
        return 1
    except Exception as e:
        print(f"ERROR: Failed to start Hex Workshop: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
