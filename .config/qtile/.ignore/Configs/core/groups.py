from libqtile.config import Group, Key
from libqtile.lazy import lazy

from core import bar
from core.keys import keys, mod
from utils.match import wm_class

groups, tag = [], bar.tags

for i, (key, layout, matches) in enumerate([
    ("a", None, wm_class("kitty")),
    ("s", None, wm_class("brave-browser", "firefox")),
    ("d", None, wm_class("code")),
    ("f", None, wm_class("kitty")),
    ("1", None, None),
    ("2", None, None),
    ("3", None, None),
    ("4", None, None),

]):  # fmt: skip
    groups.append(Group(key, matches, layout=layout, label=tag[i]))

for group in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], group.name, lazy.group[group.name].toscreen(toggle=True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name)),
    ])  # fmt: skip
