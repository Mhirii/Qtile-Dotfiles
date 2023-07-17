import os
import subprocess

# noinspection PyUnresolvedReferences
from core.keys import keys
# noinspection PyUnresolvedReferences
from core.groups import groups
from core.mods import mod
from core.float import float_rules
from core.screen import init_screens
from core.mouse import mouse
from libqtile import layout, hook

from core.layouts import init_layout_theme, init_layouts

auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "Qtile"

layout_theme = init_layout_theme()
layouts = init_layouts()
screens = init_screens()
mouse = mouse

main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules(),
    fullscreen_border_width=0,
    border_width=0,
)
