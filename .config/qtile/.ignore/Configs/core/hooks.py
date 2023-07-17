import asyncio

from libqtile import hook

from core.bar import bar


@hook.subscribe.startup
def startup():
    if bar and not sum(bar.margin):
        bar.window.window.set_property(
            name="WM_NAME",
            value="QTILE_BAR",
            type="STRING",
            format=8,
        )


@hook.subscribe.client_new
async def client_new(client):
    await asyncio.sleep(0.5)
    if client.name == "Spotify":
        client.togroup("e")


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])
