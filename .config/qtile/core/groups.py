from libqtile.config import Group
from core import apps
from core.matches import (
    code_editors,
    browsers,
    terminals,
    file_browsers,
    password_managers,
    git_managers,
    music_players,
    mail_clients,
)

groups = [
    #                         󰇰    󰃮  󰆍  󰊫  󰓅  󰓇  󰡳 󰡵 󰡴  󰾆 󰾅 󰨞
    # 󰫃 󰫄 󰫅 󰫆 󰫇 � 󰭟 󰭦 󰮯 󰯉 󰲍 󰵮 󰸘 󰸗 󱉫 󱉬 󱉨 󱎂 󱓝 󰏃 󰫢
    # 󰸶 󰸸 󰸷 󰸴 󰸵 󰸳 󱂈 󱂉 󱂊 󱂋 󱂌 󱂍 󱂎 󱂏 󱂐 󱂑 󱉽 󱉼
    # greek αβγδεζηθικ ΑΒΓΔΕΖΗΘΙΚ
    # roman ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ
    Group("a", label="", init=True, spawn=apps.TERM_EMULATOR),
    Group("s", label="", init=True, matches=browsers, spawn=apps.BROWSER),
    Group("d", label="󰨞", init=True, matches=code_editors, spawn=apps.EDITOR),
    Group("f", label="", init=True, matches=file_browsers, spawn=apps.FILEMANAGER),
    Group("1", label="Ⅰ", init=True),
    Group("2", label="Ⅱ", init=True),
    Group("3", label="Ⅲ", init=True),
    Group("4", label="Ⅳ", init=True),
    Group("5", label="Ⅴ", init=True),
    Group("6", label="Ⅵ", init=True),
    Group("7", label="Ⅶ", init=True),
    Group("8", label="Ⅷ", init=True),
    Group("9", label="󰑍", init=True),
    Group("0", label="󰓇", init=True, matches=music_players),
    Group("u", label="󰒘", init=True, matches=password_managers),
    Group("i", label="", init=True, matches=git_managers),
    Group("o", label="", init=True, matches=mail_clients, spawn=apps.MAIL),
    Group("p", label="󰐣", init=True),
]
