import os
import re
import socket
import subprocess
import iwlib
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
    Rule,
    ScratchPad,
    DropDown,
)
from libqtile.command import lazy


mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")

nordic_colors = {
    "bg": "#2A2F3A",
    "bg1": "#3B4252",
    "bg2": "#687591",
    "text": "#C8CED9",
    "text1": "#8E95A4",
    "primary": "#88c0d0",
    "secondary": "#D06F79",
    "orange": "#D06F79",
    "yellow": "#ebcb8b",
    "green": "#a3be8c",
    "purple": "#b48ead",
}

terminal = "kitty"
browser = "firefox"
fileManager = "thunar"
textEditor = "code"


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


#  █████   ████                     █████      ███                 █████
# ░░███   ███░                     ░░███      ░░░                 ░░███
#  ░███  ███     ██████  █████ ████ ░███████  ████  ████████    ███████   █████
#  ░███████     ███░░███░░███ ░███  ░███░░███░░███ ░░███░░███  ███░░███  ███░░
#  ░███░░███   ░███████  ░███ ░███  ░███ ░███ ░███  ░███ ░███ ░███ ░███ ░░█████
#  ░███ ░░███  ░███░░░   ░███ ░███  ░███ ░███ ░███  ░███ ░███ ░███ ░███  ░░░░███
#  █████ ░░████░░██████  ░░███████  ████████  █████ ████ █████░░████████ ██████
# ░░░░░   ░░░░  ░░░░░░    ░░░░░███ ░░░░░░░░  ░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░░
#                         ███ ░███
#                        ░░██████
#                         ░░░░░░

keys = [
    Key([mod], "q", lazy.window.kill()),
    # Key([mod], "w", ,
    Key([mod], "e", lazy.spawn(fileManager)),
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    Key([mod], "t", lazy.spawn(terminal)),
    # Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "p", lazy.spawn("pavucontrol")),
    Key([mod], "c", lazy.spawn(textEditor)),
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod], "v", lazy.spawn("roficlip"), desc="clipboard"),
    Key(
        [mod],
        "o",
        lazy.spawn("sh -c ~/Scripts/colorpicker.sh"),
        desc="color picker",
    ),
    Key([mod], "Escape", lazy.spawn("xkill")),
    # Key([mod], "Return", lazy.spawn("xterm")),
    Key([mod], "KP_Enter", lazy.spawn("alacritty")),
    Key([mod], "Pause", lazy.spawn("betterlockscreen -l")),
    Key([mod, "shift"], "Pause", lazy.shutdown()),
    # Key([mod, "shift"], "Return", lazy.spawn("pcmanfm")),
    Key(
        [mod, "shift"],
        "space",
        lazy.spawn(
            "dmenu_run -i -nb '#2A2F3A' -nf '#88c0d0' -sb '#88c0d0' -sf '#2A2F3A' -fn 'NotoMonoRegular:bold:pixelsize=20'"
        ),
    ),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn("sh -c ~/.config/rofi/scripts/power"),
        desc="powermenu",
    ),
    Key(
        ["mod1", "control"],
        "o",
        lazy.spawn(home + "/.config/qtile/scripts/picom-toggle.sh"),
    ),
    Key(["mod1", "control"], "u", lazy.spawn("pavucontrol")),
    Key(["mod1"], "w", lazy.spawn("garuda-welcome")),
    Key([mod2, "shift"], "Escape", lazy.spawn("lxtask")),
    Key([], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures/Screenshots")),
    Key(
        [mod2],
        "Print",
        lazy.spawn("flameshot full -p " + home + "/Pictures/Screenshots"),
    ),
    #
    # Function keys
    #
    Key([], "XF86Tools", lazy.spawn("nwggrid -p -o 0.4")),
    Key([], "XF86Mail", lazy.spawn("thunderbird-beta")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- ")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    #
    # Layout Keys
    #
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ### Treetab controls
    Key(
        [mod, "control"],
        "k",
        lazy.layout.section_up(),
        desc="Move up a section in treetab",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.section_down(),
        desc="Move down a section in treetab",
    ),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "home", lazy.window.toggle_floating()),
]

#    █████████
#   ███░░░░░███
#  ███     ░░░  ████████   ██████  █████ ████ ████████   █████
# ░███         ░░███░░███ ███░░███░░███ ░███ ░░███░░███ ███░░
# ░███    █████ ░███ ░░░ ░███ ░███ ░███ ░███  ░███ ░███░░█████
# ░░███  ░░███  ░███     ░███ ░███ ░███ ░███  ░███ ░███ ░░░░███
#  ░░█████████  █████    ░░██████  ░░████████ ░███████  ██████
#   ░░░░░░░░░  ░░░░░      ░░░░░░    ░░░░░░░░  ░███░░░  ░░░░░░
#                                             ░███
#                                             █████
#                                            ░░░░░

groups = [
    #                         󰇰    󰃮  󰆍  󰊫  󰓅  󰓇  󰡳 󰡵 󰡴  󰾆 󰾅 󰨞
    # 󰫃 󰫄 󰫅 󰫆 󰫇 � 󰭟 󰭦 󰮯 󰯉 󰲍 󰵮 󰸘 󰸗 󱉫 󱉬 󱉨 󱎂 󱓝
    # 󰸶 󰸸 󰸷 󰸴 󰸵 󰸳 󱂈 󱂉 󱂊 󱂋 󱂌 󱂍 󱂎 󱂏 󱂐 󱂑 󱉽 󱉼
    Group(
        "a",
        label="",
        init=True,
        spawn="kitty"
        # matches=[Match(wm_class=["Kitty"])],
        # exclusive=True
    ),
    Group(
        "s",
        label="",
        init=True,
    ),
    Group(
        "d",
        label="󰨞",
        init=True,
    ),
    Group("f", label=" ", init=True),
    Group("1", label="󰏃", init=True),
    Group("2", label="󰏃", init=True),
    Group("3", label="󰏃", init=True),
    Group("4", label="󰏃", init=True),
    Group("5", label="󰏃", init=True),
    Group("6", label="󰏃", init=True),
    Group("7", label=" 󰒘", init=True),
    Group("8", label="", init=True),
    Group("9", label="󰊫", init=True),
    Group("0", label="󰓇", init=True),
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
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([mod, "mod1"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                lazy.group[i.name].toscreen(),
            ),
        ]
    )


#  ████                                            █████
# ░░███                                           ░░███
#  ░███   ██████   █████ ████  ██████  █████ ████ ███████    █████
#  ░███  ░░░░░███ ░░███ ░███  ███░░███░░███ ░███ ░░░███░    ███░░
#  ░███   ███████  ░███ ░███ ░███ ░███ ░███ ░███   ░███    ░░█████
#  ░███  ███░░███  ░███ ░███ ░███ ░███ ░███ ░███   ░███ ███ ░░░░███
#  █████░░████████ ░░███████ ░░██████  ░░████████  ░░█████  ██████
# ░░░░░  ░░░░░░░░   ░░░░░███  ░░░░░░    ░░░░░░░░    ░░░░░  ░░░░░░
#                   ███ ░███
#                  ░░██████
#                   ░░░░░░


def init_layout_theme():
    return {
        "margin": 4,
        "border_width": 2,
        "border_focus": nordic_colors["primary"],
        "border_normal": nordic_colors["bg"],
    }


layout_theme = init_layout_theme()


layouts = [
    layout.Columns(
        margin=[4, 8, 4, 4],
        border_focus=nordic_colors["primary"],
        border_normal=nordic_colors["bg1"],
        border_width=2,
    ),
    layout.Tile(
        add_after_last=True,
        margin=4,
        border_focus=nordic_colors["primary"],
        border_normal=nordic_colors["bg"],
        border_width=2,
    ),
    layout.MonadTall(
        border_focus=nordic_colors["primary"],
        border_normal=nordic_colors["bg"],
        margin=4,
        border_width=2,
    ),
]

# ScratchPads
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term", "alacritty", width=0.8, height=0.7, x=0.1, y=0.1, opacity=1
            ),
            DropDown("fm", "pcmanfm", width=0.4, height=0.5, x=0.3, y=0.1, opacity=0.5),
        ],
    )
)

# Extend keys for scratchPad
keys.extend(
    [
        Key(["control"], "Return", lazy.group["scratchpad"].dropdown_toggle("term")),
        # Key(["control"], "s", lazy.group['scratchpad'].dropdown_toggle('fm')),
    ]
)


#  ███████████
# ░░███░░░░░███
#  ░███    ░███  ██████   ████████
#  ░██████████  ░░░░░███ ░░███░░███
#  ░███░░░░░███  ███████  ░███ ░░░
#  ░███    ░███ ███░░███  ░███
#  ███████████ ░░████████ █████
# ░░░░░░░░░░░   ░░░░░░░░ ░░░░░


def init_widgets_defaults():
    return dict(
        font="JetbrainsMono Nerd Font Bold",
        fontsize=9,
        padding=2,
        background=nordic_colors["bg1"],
    )


widget_defaults = init_widgets_defaults()


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


def init_widgets_list():
    widgets_list = [
        widget.Spacer(
            length=8,
            background=nordic_colors["bg"],
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord//launch_Icon.png",
            margin=2,
            background=nordic_colors["bg"],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("jgmenu_run")},
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/6.png",
        ),
        widget.GroupBox(
            font="JetBrainsMono Nerd Font Bold",
            fontsize=16,
            borderwidth=3,
            highlight_method="block",
            active=nordic_colors["bg2"],
            block_highlight_text_color=nordic_colors["primary"],
            highlight_color="#4B427E",
            inactive=nordic_colors["bg"],
            foreground="#4B427E",
            background=nordic_colors["bg1"],
            this_current_screen_border=nordic_colors["bg1"],
            this_screen_border=nordic_colors["bg1"],
            other_current_screen_border=nordic_colors["bg1"],
            other_screen_border=nordic_colors["bg1"],
            urgent_alert_method="block",
            urgent_border="#af5555",
            rounded=True,
            disable_drag=True,
        ),
        widget.Spacer(
            length=8,
            background=nordic_colors["bg1"],
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/5.png",
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/layout.png",
            background=nordic_colors["bg"],
        ),
        widget.CurrentLayout(
            background=nordic_colors["bg"],
            foreground=nordic_colors["primary"],
            fmt="{}",
            font="JetBrainsMono Nerd Font Bold",
            fontsize=14,
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/4.png",
        ),
        # widget.WindowName(
        #     background=nordic_colors["bg1"],
        #     format="{name}",
        #     font="JetBrainsMono Nerd Font Bold",
        #     foreground=nordic_colors["primary"],
        #     empty_group_string="Desktop",
        #     fontsize=14,
        #     max_chars=32,
        # ),
        widget.Spacer(),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/3.png",
        ),
        widget.Systray(
            background=nordic_colors["bg"],
            fontsize=2,
        ),
        widget.TextBox(
            text=" ",
            background=nordic_colors["bg"],
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/6.png",
            background="#353446",
        ),
        # widget.Wallpaper(
        #     fontsize=14,
        #     background=nordic_colors["bg1"],
        #     foreground=nordic_colors["primary"],
        #     font="JetBrainsMono Nerd Font Bold",
        #     directory="~/Pictures/Wallpapers/",
        # ),
        # widget.Image(
        #     filename="~/.config/qtile/AssetsNord/1.png",
        # ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/Misc/ram.png",
            background=nordic_colors["bg1"],
        ),
        widget.Spacer(
            length=-7,
            background=nordic_colors["bg1"],
        ),
        widget.CPU(
            background=nordic_colors["bg1"],
            format=" {load_percent}%",
            # measure_mem="G",
            foreground=nordic_colors["primary"],
            font="JetBrainsMono Nerd Font Bold",
            fontsize=14,
            update_interval=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
        ),
        widget.Memory(
            background=nordic_colors["bg1"],
            format="{MemUsed: .0f}{mm}",
            # measure_mem ="G",
            foreground=nordic_colors["primary"],
            font="JetBrainsMono Nerd Font Bold",
            fontsize=14,
            update_interval=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/1.png",
        ),
        widget.Volume(
            font="JetBrainsMono Nerd Font Bold",
            theme_path="~/.config/qtile/AssetsNord/Volume/",
            emoji=True,
            fontsize=14,
            background=nordic_colors["bg1"],
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
        ),
        widget.Spacer(
            length=-5,
            background=nordic_colors["bg1"],
        ),
        widget.Volume(
            font="JetBrainsMono Nerd Font Bold",
            background=nordic_colors["bg1"],
            foreground=nordic_colors["primary"],
            fontsize=14,
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/1.png",
        ),
        widget.Clock(
            format="%A %d",
            background=nordic_colors["bg1"],
            foreground=nordic_colors["primary"],
            font="JetBrainsMono Nerd Font Ultra-Bold",
            fontsize=14,
        ),
        widget.Image(
            filename="~/.config/qtile/AssetsNord/5.png",
            background=nordic_colors["bg1"],
        ),
        widget.Clock(
            format="%I:%M",
            background=nordic_colors["bg"],
            foreground=nordic_colors["primary"],
            font="JetBrainsMono Nerd Font Ultra-Bold",
            fontsize=16,
        ),
        widget.Spacer(
            length=8,
            background=nordic_colors["bg"],
        ),
    ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=32,
                opacity=1,
                background="000000",
                border_color="#282738",
                border_width=[0, 0, 0, 0],
                margin=[4, 4, 0, 4],
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen2(),
                size=25,
                opacity=0.85,
                background="000000",
            )
        ),
    ]


screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []


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
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(title="branchdialog"),
        Match(title="Open File"),
        Match(title="pinentry"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="lxpolkit"),
        Match(wm_class="Lxpolkit"),
        Match(wm_class="yad"),
        Match(wm_class="Yad"),
        Match(wm_class="Cairo-dock"),
        Match(wm_class="cairo-dock"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "Qtile"
