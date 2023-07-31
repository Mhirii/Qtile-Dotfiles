import core.groups
from core.apps import *
from libqtile.config import Key
from libqtile.lazy import lazy
from core.groups import groups

mod = "mod4"
mod1 = "alt"
mod2 = "control"


keys = [
    Key(*key)
    for key in [
        # Apps
        ([mod], "e", lazy.spawn(FILEMANAGER)),
        ([mod], "t", lazy.spawn(TERM_EMULATOR)),
        ([mod, "shift"], "t", lazy.spawn(TERM_EMULATOR_TWO)),
        ([mod, "control"], "t", lazy.spawn(TERM_EMULATOR_THREE)),
        ([mod], "c", lazy.spawn(EDITOR)),
        ([mod], "b", lazy.spawn(BROWSER)),
        ([mod], "m", lazy.spawn(MUSIC_PLAYER)),
        ([], "XF86Mail", lazy.spawn(MAIL)),
        ([mod2, "shift"], "Escape", lazy.spawn("lxtask")),
        # launchers
        ([mod], "r", lazy.spawn(ROFI)),
        ([mod], "space", lazy.spawn(DMENU)),
        # utility
        ([mod], "v", lazy.spawn(CLIPBOARD)),
        ([mod], "prior", lazy.spawn(COLORPICKER)),
        ([mod], "p", lazy.spawn(ROFIPOWER)),
        ([mod], "w", lazy.spawn("sh ~/Scripts/wallpaper.sh")),
        ([mod], "Escape", lazy.spawn("xkill")),
        ([mod, "control"], "p", lazy.spawn("pavucontrol")),
        ([], "Print", lazy.spawn(SCREENSHOT)),
        # wm
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        ([mod], "left", lazy.layout.left()),
        ([mod], "right", lazy.layout.right()),
        ([mod], "down", lazy.layout.down()),
        ([mod], "up", lazy.layout.up()),
        ([mod, "shift"], "h", lazy.layout.shuffle_left()),
        ([mod, "shift"], "l", lazy.layout.shuffle_right()),
        ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        ([mod, "shift"], "left", lazy.layout.shuffle_left()),
        ([mod, "shift"], "right", lazy.layout.shuffle_right()),
        ([mod, "shift"], "down", lazy.layout.shuffle_down()),
        ([mod, "shift"], "up", lazy.layout.shuffle_up()),
        (
            [mod, "control"],
            "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        (
            [mod, "control"],
            "h",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        (
            [mod, "control"],
            "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        (
            [mod, "control"],
            "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        # increase/decrease window size
        ([mod, "control"], "i", lazy.layout.grow()),
        ([mod, "control"], "m", lazy.layout.shrink()),
        # window management
        ([mod], "n", lazy.layout.normalize()),
        ([mod], "q", lazy.window.kill()),
        ([], "F11", lazy.window.toggle_fullscreen()),
        ([mod], "y", lazy.window.toggle_floating()),
        ([mod], "Tab", lazy.next_layout()),
        # qtile stuff
        ([mod], "Pause", lazy.spawn("betterlockscreen -l")),
        ([mod, "control"], "Pause", lazy.shutdown()),
        ([mod, "control"], "b", lazy.hide_show_bar()),
        ([mod, "control"], "r", lazy.restart()),
        # fn keys
        ([], "XF86Tools", lazy.spawn("nwggrid -p -o 0.4")),
        ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
        ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- ")),
        ([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        ([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
        ([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
        ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
        ([], "XF86AudioNext", lazy.spawn("playerctl next")),
        ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
        ([], "XF86AudioStop", lazy.spawn("playerctl stop")),
        # Key(
        #     ["mod1", "control"],
        #     "o",
        #     lazy.spawn(home + "/.config/qtile/scripts/picom-toggle.sh"),
        # ),
        # Key([], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures/Screenshots")),
    ]
]

for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
            Key(
                ["mod1"],
                "Tab",
                lazy.group.next_window(),
            ),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            Key([mod, "mod1"], i.name, lazy.window.togroup(i.name)),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                lazy.group[i.name].toscreen(),
            ),
        ]
    )
