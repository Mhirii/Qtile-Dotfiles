from libqtile import layout
from assets.themes import theme


def init_layout_theme():
    return {
        "margin": 4,
        "border_width": 2,
        "border_focus": theme["1"],
        "border_normal": theme["bg"],
    }


def init_layouts():
    layouts = [
        layout.Tile(
            add_after_last=True,
            margin=8,
            border_focus=theme["1"],
            border_normal=theme["bg"],
            border_width=2,
        ),
        layout.Columns(
            margin=[4, 8, 4, 4],
            border_focus=theme["1"],
            border_normal=theme["bg1"],
            border_width=2,
        ),

        layout.MonadTall(
            border_focus=theme["1"],
            border_normal=theme["bg"],
            margin=4,
            border_width=2,
        ),
    ]
    return layouts
