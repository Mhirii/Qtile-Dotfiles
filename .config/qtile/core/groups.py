from libqtile.config import Group
from core import apps
from core.matches import code_editors, browsers, terminals, file_browsers, password_managers, git_managers, \
    music_players, mail_clients

groups = [
    #                         󰇰    󰃮  󰆍  󰊫  󰓅  󰓇  󰡳 󰡵 󰡴  󰾆 󰾅 󰨞
    # 󰫃 󰫄 󰫅 󰫆 󰫇 � 󰭟 󰭦 󰮯 󰯉 󰲍 󰵮 󰸘 󰸗 󱉫 󱉬 󱉨 󱎂 󱓝 󰏃
    # 󰸶 󰸸 󰸷 󰸴 󰸵 󰸳 󱂈 󱂉 󱂊 󱂋 󱂌 󱂍 󱂎 󱂏 󱂐 󱂑 󱉽 󱉼
    Group("a", label="", init=True, spawn=apps.TERM_EMULATOR),
    Group("s", label="", init=True, matches=browsers, spawn=apps.BROWSER),
    Group("d", label="󰨞", init=True, matches=code_editors, spawn=apps.EDITOR),
    Group("f", label=" ", init=True, matches=file_browsers, spawn=apps.FILEMANAGER),
    Group("1", label="󰏃", init=True),
    Group("2", label="󰏃", init=True),
    Group("3", label="󰏃", init=True),
    Group("4", label="󰏃", init=True),
    Group("5", label="󰏃", init=True),
    Group("6", label="󰏃", init=True),
    Group("7", label=" 󰒘", init=True, matches=password_managers),
    Group("8", label="", init=True, matches=git_managers),
    Group("9", label="", init=True, matches=mail_clients, spawn=apps.MAIL),
    Group("0", label="󰓇", init=True, matches=music_players),
]
