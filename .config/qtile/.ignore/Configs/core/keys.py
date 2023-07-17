import os

from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from extras import float_to_front
from utils.config import cfg

if int(os.environ.get("QTILE_XEPHYR", 0)) > 0:
    mod, alt = "mod1", "control"
    restart = lazy.restart()
else:
    mod, alt = "mod4", "mod1"
    restart = lazy.reload_config()

if not cfg.term:
    cfg.term = guess_terminal()

keys = [Key(*key) for key in [  # type: ignore
    # switch between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),

    # move windows between columns
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # increase/decrease window size
    ([mod], "i", lazy.layout.grow()),
    ([mod], "m", lazy.layout.shrink()),

    # window management
    ([mod, "shift"], "space", lazy.layout.flip()),
    ([mod], "o", lazy.layout.maximize()),
    ([mod], "n", lazy.layout.normalize()),
    ([mod], "q", lazy.window.kill()),
    ([], "F11", lazy.window.toggle_fullscreen()),

    # floating window management
    ([mod], "space", lazy.window.toggle_floating()),
    ([mod], "c", lazy.window.center()),
    ([mod], "f", lazy.function(float_to_front)),

    # toggle between layouts
    ([mod], "Tab", lazy.next_layout()),

    # qtile stuff
    ([mod, "control"], "b", lazy.hide_show_bar()),
    ([mod, "control"], "pause", lazy.shutdown()),
    ([mod], "Pause", lazy.spawn("betterlockscreen -l")),
    ([mod, "control"], "r", restart),

    # terminal
    ([mod], "Return", lazy.spawn(cfg.term)),
    ([mod, "shift"], "Return", lazy.spawn(cfg.term2)),

    # app launcher
    ([mod, "shift"], "r", lazy.spawn("rofi -show drun")),
    ([mod], "r", lazy.spawn("rofi -show drun")),
    ([], "XF86Tools", lazy.spawn("nwggrid -p -o 0.4")),

    # apps
    ([], "XF86Mail", lazy.spawn("thunderbird-beta")),
    ([mod], "b", lazy.spawn(cfg.browser)),
    ([mod], "e", lazy.spawn(cfg.files)),

    
    # screenshot tool
    ([], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures/Screenshots")),
    # backlight
    ([mod], "XF86AudioLowerVolume", lazy.spawn("brightnessctl set 5%-")),
    ([mod], "XF86AudioRaiseVolume", lazy.spawn("brightnessctl set +5%")),

    # volume
    ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    # ([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    # ([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    
    # player
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),
    ([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    
    # waiting list
    
    # ([mod], "p", lazy.spawn("pavucontrol")),
    # ([mod], "v", lazy.spawn("roficlip"), desc="clipboard"),
    # ([mod], "o", lazy.spawn("sh -c ~/Scripts/colorpicker.sh")),
    
    # ([mod], "Escape", lazy.spawn("xkill")),
    #     Key(
    #     [mod, "shift"],
    #     "space",
    #     lazy.spawn(
    #         "dmenu_run -i -nb '#2A2F3A' -nf '#88c0d0' -sb '#88c0d0' -sf '#2A2F3A' -fn 'NotoMonoRegular:bold:pixelsize=20'"
    #     ),
    # ),
    # (
    #     [mod, "shift"],
    #     "p",
    #     lazy.spawn("sh -c ~/.config/rofi/scripts/power"),
    #     desc="powermenu",
    # ),
    
    # (
    #     ["mod1", "control"],
    #     "o",
    #     lazy.spawn(home + "/.config/qtile/scripts/picom-toggle.sh"),
    # ),
    
]]  # fmt: skip
