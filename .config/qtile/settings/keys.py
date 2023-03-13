
# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy

@lazy.window.function 
def resize_floating_window(window, width: int = 0, height: int = 0): 
    window.cmd_set_size_floating(window.width + width, window.height + height)

mod = "mod4"
alt = "mod1"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "Down", lazy.layout.down()),
    ([mod], "Up", lazy.layout.up()),
    ([mod], "Left", lazy.layout.left()),
    ([mod], "Right", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "Left", lazy.layout.grow_left()),
    ([mod, "control"], "Right", lazy.layout.grow_right()),

    # Move tiled windows
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    ([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    ([mod, "shift"], "Right", lazy.layout.shuffle_right()),

    # Toggle between different layouts as defined below
    ([mod, "shift"], "Tab", lazy.next_layout()),
    # ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Alternate beetwen workspaces
    ([mod], "Tab", lazy.screen.toggle_group()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    #([mod], "`", lazy.next_screen()),
    #([mod], "+", lazy.prev_screen()),

    # Restart Qtile
    ([mod, alt], "r", lazy.restart()),
    ([mod, alt], "q", lazy.shutdown()),

    # Windows status
    ([mod], "f", lazy.window.toggle_fullscreen()),
    ([mod], "s", lazy.window.toggle_floating()),

    # Resize floating window

    ([mod, "control"], "j", resize_floating_window(height=10)), 
    ([mod, "control"], "k", resize_floating_window(height=-10)),
    ([mod, "control"], "h", resize_floating_window(width=-10)),
    ([mod, "control"], "l", resize_floating_window(width=10)),
    ([mod, "control"], "Down", resize_floating_window(height=10)), 
    ([mod, "control"], "Up",   resize_floating_window(height=-10)),
    ([mod, "control"], "Left", resize_floating_window(width=-10)),
    ([mod, "control"], "Right",resize_floating_window(width=10)),

    # Move floating window

    ([mod, alt], "j", lazy.window.move_floating(0, 10)), 
    ([mod, alt], "k", lazy.window.move_floating(0, -10)),
    ([mod, alt], "h", lazy.window.move_floating(-10, 0)),
    ([mod, alt], "l", lazy.window.move_floating(10, 0)),
    ([mod, alt], "Down", lazy.window.move_floating(0, 10)), 
    ([mod, alt], "Up",   lazy.window.move_floating(0, -10)),
    ([mod, alt], "Left", lazy.window.move_floating(-10, 0)),
    ([mod, alt], "Right",lazy.window.move_floating(10, 0)),

    # ------------ App Configs ------------

    # Menu
    ([mod], "d", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, alt], "d", lazy.spawn("rofi -show")),

    # Browser
    ([mod, alt], "f", lazy.spawn("firefox")),

    # File Explorer
    ([mod, alt], "a", lazy.spawn("caja")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    #([mod], "r", lazy.spawn("redshift -O 2400")),
    #([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    #([mod], "s", lazy.spawn("scrot")),
    #([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]



