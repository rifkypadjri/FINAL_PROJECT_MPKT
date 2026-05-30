# Pemetaan aset sesuai DIALOG MPKT (2).md
# File audio di folder game/audio/ mengikuti nama di dokumen.

init -1 python:
    # Nama file di skrip -> file aktual di game/audio/
    AUDIO_ALIASES = {
        "bgm_hectic.mp3": "bgm_hectic.mp3",
        "bgm_focus.mp3": "bgm_focus.mp3",
        "bgm_warm.mp3": "bgm_warm.wav",
        "bgm_melancholy.mp3": "bgm_melancholy.wav",
        "bgm_badend.mp3": "bgm_badend.wav",
        "bgm_quiet_ambient.mp3": "bgm_quiet_ambient.wav",
        "bgm_gentle.mp3": "bgm_gentle.wav",
        "bgm_open.mp3": "bgm_open.wav",
        "bgm_crisis_night.mp3": "bgm_crisis_night.mp3",
        "bgm_tense_night.mp3": "bgm_tense_night.mp3",
        "bgm_conflict.mp3": "bgm_conflict.mp3",
        "bgm_hectic_corridor.mp3": "bgm_hectic_corridor.mp3",
        "sfx_correct.mp3": "sfx_correct.mp3",
        "sfx_wrong.mp3": "sfx_wrong.wav",
        "sfx_badend.mp3": "sfx_badend.wav",
        "sfx_tricky.mp3": "sfx_tricky.wav",
        "sfx_neutralend.mp3": "sfx_neutralend.wav",
        # SFX opsional (⭐) — memakai placeholder dari paket audio yang ada
        "sfx_goodend.mp3": "sfx_goodend.mp3",
        "sfx_stomach_growl.mp3": "sfx_stomach_growl.mp3",
        "sfx_laptop_slam.mp3": "sfx_laptop_slam.wav",
        "sfx_rain_ambient.mp3": "sfx_rain_ambient.wav",
        "sfx_footsteps_slow.mp3": "sfx_footsteps_slow.wav",
        "sfx_wind_ambient.mp3": "sfx_wind_ambient.mp3",
        "sfx_phone_vibrate.mp3": "sfx_phone_vibrate.mp3",
    }
