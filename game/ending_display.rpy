# Tampilan ending: BG skenario + karakter + efek warna (bad / neutral / good)

init python:
    def _hide_ending_fx_on_scene(old_scene=None):
        renpy.hide_screen("ending_fx")

    if _hide_ending_fx_on_scene not in config.scene_callbacks:
        config.scene_callbacks.append(_hide_ending_fx_on_scene)

    def _ending_at(name):
        return getattr(renpy.store, name, renpy.store.kiri)

screen ending_fx(kind):
    # Full screen; di bawah say/menu agar teks & pilihan tetap terbaca
    zorder -10
    modal False

    if kind == "bad":
        add Solid("#1a0808") xalign 0.5 yalign 0.5 xsize config.screen_width ysize config.screen_height alpha 0.28

    elif kind == "good":
        add Solid("#fff6e0") xalign 0.5 yalign 0.5 xsize config.screen_width ysize config.screen_height alpha 0.18

    elif kind == "neutral":
        add Solid("#5c5c5a") xalign 0.5 yalign 0.5 xsize config.screen_width ysize config.screen_height alpha 0.26

# Satu karakter
label ending_frame(kind, bg, sprite, at_name="kiri"):
    python:
        renpy.scene()
        renpy.show(bg)
        renpy.show(sprite, at_list=[_ending_at(at_name)])
    with dissolve
    show screen ending_fx(kind)
    return

# Dua karakter (S4)
label ending_frame_dual(kind, bg, sprite_a, at_a, sprite_b, at_b):
    python:
        renpy.scene()
        renpy.show(bg)
        renpy.show(sprite_a, at_list=[_ending_at(at_a)])
        renpy.show(sprite_b, at_list=[_ending_at(at_b)])
    with dissolve
    show screen ending_fx(kind)
    return
