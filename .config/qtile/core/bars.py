from libqtile import widget, qtile
from assets.themes import theme, icon, accent
from core.apps import TERM_EMULATOR
from libqtile.command import lazy

bar_using_images = [
    widget.Spacer(
        length=8,
        background=theme["bg"],
    ),
    widget.Image(
        filename=icon["launch"],
        margin=2,
        background=theme["bg"],
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("jgmenu_run")},
    ),
    widget.Image(
        filename=icon["circle2"],
    ),
    widget.GroupBox(
        font="JetBrainsMono Nerd Font Bold",
        fontsize=16,
        borderwidth=3,
        highlight_method="block",
        active=theme["bg2"],
        block_highlight_text_color=theme["1"],
        highlight_color="#4B427E",
        inactive=theme["bg"],
        foreground="#4B427E",
        background=theme["bg1"],
        this_current_screen_border=theme["bg1"],
        this_screen_border=theme["bg1"],
        other_current_screen_border=theme["bg1"],
        other_screen_border=theme["bg1"],
        urgent_alert_method="block",
        urgent_border="#af5555",
        rounded=True,
        disable_drag=True,
    ),
    widget.Spacer(
        length=8,
        background=theme["bg1"],
    ),
    widget.Image(
        filename=icon["wave1"],
    ),
    widget.Image(
        filename=icon["layout"],
        background=theme["bg"],
    ),
    widget.CurrentLayout(
        background=theme["bg"],
        foreground=theme["1"],
        fmt="{}",
        font="JetBrainsMono Nerd Font Bold",
        fontsize=16,
    ),
    widget.Image(
        filename=icon["circle2"],
    ),
    widget.Spacer(
        background=theme["bg1"],
    ),
    widget.Image(
        filename=icon["circle1"],
    ),
    widget.Systray(
        background=theme["bg"],
        fontsize=2,
    ),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    widget.Image(
        filename=icon["wave2"],
        background="#353446",
    ),
    widget.Image(
        filename=icon["ram"],
        background=theme["bg1"],
    ),
    widget.Spacer(
        length=-7,
        background=theme["bg1"],
    ),
    widget.CPU(
        background=theme["bg1"],
        format=" {load_percent}%",
        # measure_mem="G",
        foreground=theme["1"],
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    ),
    widget.Memory(
        background=theme["bg1"],
        format="{MemUsed: .0f}{mm}",
        # measure_mem ="G",
        foreground=theme["1"],
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    ),
    widget.Image(
        filename=icon["slash1"],
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font Bold",
        theme_path=icon["volume"],
        emoji=True,
        fontsize=14,
        background=theme["bg1"],
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.Spacer(
        length=-5,
        background=theme["bg1"],
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font Bold",
        background=theme["bg1"],
        foreground=theme["1"],
        fontsize=14,
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.Image(
        filename=icon["slash1"],
    ),
    widget.Clock(
        format="%A %d",
        background=theme["bg1"],
        foreground=theme["1"],
        font="JetBrainsMono Nerd Font Ultra-Bold",
        fontsize=14,
    ),
    widget.Image(
        filename=icon["circle1"],
        background=theme["bg1"],
    ),
    widget.Clock(
        format="%I:%M",
        background=theme["bg"],
        foreground=theme["1"],
        font="JetBrainsMono Nerd Font Ultra-Bold",
        fontsize=16,
    ),
    widget.Spacer(
        length=8,
        background=theme["bg"],
    ),
]


def seperator_pipe(bg, fg):
    return widget.TextBox(text='', fontsize=25, padding=0, background=bg, foreground=fg,
                          font='SauceCodeMono Nerd Font')


def seperator_pipe_reverse(bg, fg):
    return widget.TextBox(text='', fontsize=25, padding=0, background=bg, foreground=fg,
                          font='SauceCodeMono Nerd Font')


def slash(bg, fg):
    return widget.TextBox(text='  ', fontsize=25, padding=0, background=bg, foreground=fg,
                          font='SauceCodeMono Nerd Font')


catppuccin_mocha = [
    widget.Spacer(
        length=8,
        background=theme["bg"],
    ),
    widget.TextBox(
        text=' ',
        fontsize=18,
        padding=4,
        background=theme["bg"],
        foreground=accent,
        font='SauceCodeMono Nerd Font',
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("jgmenu_run")},
    ),
    seperator_pipe(theme["bg1"], theme["bg"]),
    widget.GroupBox(
        font="JetBrainsMono Nerd Font Bold",
        fontsize=18,
        borderwidth=3,
        highlight_method="block",
        background=theme["bg1"],
        inactive=theme["bg2"],
        active=theme["bg3"],
        block_highlight_text_color=accent,
        highlight_color="#4B427E",
        foreground="#4B427E",
        this_current_screen_border=theme["bg1"],
        this_screen_border=theme["bg1"],
        other_current_screen_border=theme["bg1"],
        other_screen_border=theme["bg1"],
        urgent_alert_method="block",
        urgent_border="#af5555",
        rounded=True,
        hide_unused=False,
        disable_drag=True,
    ),
    widget.Spacer(
        length=8,
        background=theme["bg1"],
    ),
    seperator_pipe(theme["bg"], theme["bg1"]),
    widget.TextBox(
        text=" 󰙀 ",
        background=theme["bg"],
        foreground=theme["1"],
        fontsize=14,
    ),
    widget.CurrentLayout(
        background=theme["bg"],
        foreground=theme["1"],
        fmt="{}",
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
    ),
    seperator_pipe(theme["bg1"], theme["bg"]),
    widget.Spacer(
        background=theme["bg1"],
    ),
    seperator_pipe_reverse(theme["bg1"], theme["bg"]),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    widget.Systray(
        padding = 4,
        background=theme["bg"],
        fontsize=2,
    ),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    seperator_pipe_reverse(theme["bg"], theme["bg1"]),

    widget.CPU(
        background=theme["bg1"],
        format="  {load_percent}%",
        foreground=theme["5"],
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    ),
    widget.Spacer(
        length=16,
        background=theme["bg1"],
    ),

    widget.Memory(
        background=theme["bg1"],
        # format=" {MemPercent: .0f}{mm}",
        format=" {MemPercent}%",
        foreground=theme["5"],
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    ),

    widget.Spacer(
        length=16,
        background=theme["bg1"],
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font Bold",
        emoji=True,
        theme_path=icon["volume"],
        fontsize=14,
        background=theme["bg1"],
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.Spacer(
        length=-10,
        background=theme["bg1"],
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font Bold",
        background=theme["bg1"],
        foreground=theme["5"],
        fontsize=14,
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.Spacer(
        length=8,
        background=theme["bg1"],
    ),
    seperator_pipe_reverse(theme["bg1"], theme["bg"]),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    widget.Clock(
        format="%A %d ",
        background=theme["bg"],
        foreground=theme["1"],
        font="JetBrainsMono Nerd Font Ultra-Bold",
        fontsize=16,
    ),
    widget.Clock(
        format="%I:%M",
        background=theme["bg"],
        foreground=theme["1"],
        font="JetBrainsMono Nerd Font Ultra-Bold",
        fontsize=16,
    ),
    widget.Spacer(
        length=8,
        background=theme["bg"],
    ),
]


def init_widgets_list():
    # widgets_list = bar_using_images
    widgets_list = catppuccin_mocha
    return widgets_list
