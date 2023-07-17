from libqtile.config import Screen
from libqtile import bar

from core.bars import init_widgets_list


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=35,
                opacity=1,
                background="000000",
                border_color="#282738",
                border_width=[0, 0, 0, 0],
                margin=[0, 8, 0, 8],
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=25,
                opacity=0.85,
                background="000000",
            )
        ),
    ]
