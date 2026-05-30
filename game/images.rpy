# Deklarasi gambar — selaras dengan DIALOG MPKT (2).md & paket ASET GAME P3LP MPKT F FG2

# Tinggi tampilan sprite (px) — menyeragamkan ukuran meski file PNG beda dimensi
define CHAR_H = 920
define CHAR_H_PAIR = 750

## Transform: kaki karakter di dasar layar; kotak dialog menutupi bagian bawah saja
## Sprite PNG menghadap kiri — xzoom -1 di posisi kiri supaya menghadap kanan (ke BG/meja)
transform kiri:
    xalign 0.12
    yalign 1.0
    yoffset 0
    xzoom -1.0
    zoom 1.0

## Posisi kanan: tetap arah asli PNG (menghadap kiri, ke tengah layar)
transform kanan:
    xalign 0.88
    yalign 1.0
    yoffset 0
    zoom 1.0

## Dua karakter di layar (S4 Demo Day) — tinggi sudah disamakan via CHAR_H_PAIR
transform kiri_demo:
    xalign 0.20
    yalign 1.0
    yoffset 0
    xzoom -1.0
    zoom 1.0

transform kanan_demo:
    xalign 0.80
    yalign 1.0
    yoffset 0
    zoom 1.0

## S5 Budi — sprite PNG sudah menghadap kanan; tanpa flip
transform kiri_s5:
    xalign 0.12
    yalign 1.0
    yoffset 0
    zoom 1.0

## Sprite grup Geri (lebih lebar)
transform kiri_grup:
    xalign 0.50
    yalign 1.0
    yoffset 0
    zoom 1.0

## Background — SKENARIO 1
image bg blck = "images/bg/blck.png"
image bg lab_komputer = "images/bg/lab_komputer.png"
image bg kantin_fasilkom = "images/bg/kantin_fasilkom.png"
image bg kantin_fasilkom_blur = "images/bg/kantin_fasilkom_blur.png"
image bg luar_gedung_fasilkom = "images/bg/luar_gedung_fasilkom.png"

## Background — SKENARIO 2
image bg lorong_fasilkom_sore = "images/bg/lorong_fasilkom_sore.png"
image bg kantin_fasilkom_s2 = "images/bg/kantin_fasilkom_s2.png"

## Background — SKENARIO 3
image bg kamar_kosan = "images/bg/kamar_kosan.png"
image bg kamar_kosan_malam = "images/bg/kamar_kosan_malam.png"

## Background — SKENARIO 4
image bg lorong_gedung_baru = "images/bg/lorong_gedung_baru.png"
image bg selasar_gedung_baru = "images/bg/selasar_gedung_baru.png"

## Background — SKENARIO 5
image bg balkon_lt5_malam = "images/bg/balkon_lt5_malam.png"

## UI — logo & judul (ASET GAME P3LP MPKT F FG2/UI)
image ui logo = "images/gui/logo.png"
image ui logo trans = "images/gui/logo_trans.png"
image ui title trans = "images/gui/title_trans.png"

## Splash — logo kecil di tengah
transform ui_logo_splash:
    xalign 0.5
    yalign 0.45
    zoom 0.38

## Menu utama — judul di area kanan (hindari sidebar kiri)
transform ui_title_menu:
    xalign 0.63
    yalign 0.44
    zoom 0.46

## Layar pilih skenario — judul di tengah, lebih kecil
transform ui_title_start:
    xalign 0.5
    yalign 0.38
    zoom 0.52

## Overlay ending
image bg overlay_merah = Solid("#5a1010")
image bg overlay_kuning = Solid("#5a4a10")
image bg overlay_hitam = Solid("#050505")

## Andi — S1
image andi sad:
    "images/characters/andi/sad.png"
    ysize CHAR_H
    fit "contain"

image andi defensive:
    "images/characters/andi/defensive.png"
    ysize CHAR_H
    fit "contain"

image andi cry:
    "images/characters/andi/cry.png"
    ysize CHAR_H
    fit "contain"

image andi surprised:
    "images/characters/andi/surprised.png"
    ysize CHAR_H
    fit "contain"

image andi normal:
    "images/characters/andi/normal.png"
    ysize CHAR_H
    fit "contain"

image andi relieved:
    "images/characters/andi/relieved.png"
    ysize CHAR_H
    fit "contain"

## Andi — S4
image andi panic:
    "images/characters/andi/panic.png"
    ysize CHAR_H_PAIR
    fit "contain"

image andi exhausted:
    "images/characters/andi/exhausted.png"
    ysize CHAR_H_PAIR
    fit "contain"

image andi normal s4:
    "images/characters/andi/normal.png"
    ysize CHAR_H_PAIR
    fit "contain"

## Laras — S2
image laras sad:
    "images/characters/laras/sad.png"
    ysize CHAR_H
    fit "contain"

image laras shocked:
    "images/characters/laras/shocked.png"
    ysize CHAR_H
    fit "contain"

image laras tense:
    "images/characters/laras/tense.png"
    ysize CHAR_H
    fit "contain"

image laras open:
    "images/characters/laras/open.png"
    ysize CHAR_H
    fit "contain"

image laras relieved:
    "images/characters/laras/relieved.png"
    ysize CHAR_H
    fit "contain"

image laras alarmed:
    "images/characters/laras/alarmed.png"
    ysize CHAR_H
    fit "contain"

image laras guilty:
    "images/characters/laras/guilty.png"
    ysize CHAR_H
    fit "contain"

image laras flat:
    "images/characters/laras/flat.png"
    ysize CHAR_H
    fit "contain"

image laras cold:
    "images/characters/laras/cold.png"
    ysize CHAR_H
    fit "contain"

## Laras — S4
image laras cry:
    "images/characters/laras/cry.png"
    ysize CHAR_H_PAIR
    fit "contain"

image laras sad_s4:
    "images/characters/laras/sad_s4.png"
    ysize CHAR_H_PAIR
    fit "contain"

image laras normal:
    "images/characters/laras/normal.png"
    ysize CHAR_H_PAIR
    fit "contain"

## Geri — S3
image geri read_receipt:
    "images/characters/geri/read_receipt.png"
    ysize CHAR_H_PAIR
    fit "contain"

image geri sad:
    "images/characters/geri/geri_dm.png"
    ysize CHAR_H
    fit "contain"

image geri closed_off:
    "images/characters/geri/geri_dm.png"
    ysize CHAR_H
    fit "contain"

image geri cry:
    "images/characters/geri/geri_dm.png"
    ysize CHAR_H
    fit "contain"

image geri grateful:
    "images/characters/geri/geri_dm.png"
    ysize CHAR_H
    fit "contain"

image geri surprised:
    "images/characters/geri/geri_dm.png"
    ysize CHAR_H
    fit "contain"

image geri normal:
    "images/characters/geri/geri_dm.png"
    ysize CHAR_H
    fit "contain"

image geri offended:
    "images/characters/geri/geri_dm.png"
    ysize CHAR_H
    fit "contain"

## Budi — S5
image budi blank_stare:
    "images/characters/budi/blank_stare.png"
    ysize CHAR_H
    fit "contain"

image budi cornered:
    "images/characters/budi/cornered.png"
    ysize CHAR_H
    fit "contain"

image budi breakdown:
    "images/characters/budi/breakdown.png"
    ysize CHAR_H
    fit "contain"

image budi bitter:
    "images/characters/budi/bitter.png"
    ysize CHAR_H
    fit "contain"

image budi exhausted:
    "images/characters/budi/exhausted.png"
    ysize CHAR_H
    fit "contain"

image budi held:
    "images/characters/budi/held.png"
    ysize CHAR_H
    fit "contain"
