# Kamu dapat taruh script game mu di file ini.

init python:
    def safe_music(filename, fadeout=1.0, fadein=1.0):
        paths = ["audio/" + filename, filename]
        for path in paths:
            if renpy.loadable(path):
                renpy.music.play(path, channel="music", fadeout=fadeout, fadein=fadein)
                return
        renpy.music.stop(channel="music", fadeout=fadeout)

    def safe_sound(filename):
        paths = ["audio/" + filename, filename]
        for path in paths:
            if renpy.loadable(path):
                renpy.sound.play(path)
                return

# Placeholder visual. Ganti file ini dengan deklarasi image asli saat aset sudah tersedia.
image bg blck = Solid("#111111")
image bg lab_komputer = Solid("#253447")
image bg kantin_fasilkom = Solid("#4d3a24")
image bg luar_gedung_fasilkom = Solid("#2f4a3d")
image bg lorong_fasilkom_sore = Solid("#463a52")
image bg kamar_kosan = Solid("#2a2438")
image bg kamar_kosan_malam = Solid("#1e1a2e")
image bg lorong_gedung_baru = Solid("#3d4a5c")
image bg selasar_gedung_baru = Solid("#4a5d6e")
image bg balkon_lt5_malam = Solid("#0f1520")
image bg overlay_merah = Solid("#5a1010")
image bg overlay_kuning = Solid("#5a4a10")
image bg overlay_hitam = Solid("#050505")

image andi sad = Text("Andi - sad", size=44, color="#ffffff")
image andi defensive = Text("Andi - defensive", size=44, color="#ffffff")
image andi cry = Text("Andi - cry", size=44, color="#ffffff")
image andi surprised = Text("Andi - surprised", size=44, color="#ffffff")
image andi normal = Text("Andi - normal", size=44, color="#ffffff")
image andi panic = Text("Andi - panic", size=44, color="#ffffff")
image andi exhausted = Text("Andi - exhausted", size=44, color="#ffffff")

image laras sad = Text("Laras - sad", size=44, color="#ffffff")
image laras shocked = Text("Laras - shocked", size=44, color="#ffffff")
image laras tense = Text("Laras - tense", size=44, color="#ffffff")
image laras open = Text("Laras - open", size=44, color="#ffffff")
image laras relieved = Text("Laras - relieved", size=44, color="#ffffff")
image laras alarmed = Text("Laras - alarmed", size=44, color="#ffffff")
image laras guilty = Text("Laras - guilty", size=44, color="#ffffff")
image laras flat = Text("Laras - flat", size=44, color="#ffffff")
image laras cry = Text("Laras - cry", size=44, color="#ffffff")

image geri read_receipt = Text("Geri - read_receipt", size=44, color="#ffffff")
image geri sad = Text("Geri - sad", size=44, color="#ffffff")
image geri closed_off = Text("Geri - closed_off", size=44, color="#ffffff")
image geri cry = Text("Geri - cry", size=44, color="#ffffff")
image geri grateful = Text("Geri - grateful", size=44, color="#ffffff")
image geri surprised = Text("Geri - surprised", size=44, color="#ffffff")
image geri normal = Text("Geri - normal", size=44, color="#ffffff")
image geri offended = Text("Geri - offended", size=44, color="#ffffff")

image budi blank_stare = Text("Budi - blank_stare", size=44, color="#ffffff")
image budi cornered = Text("Budi - cornered", size=44, color="#ffffff")
image budi breakdown = Text("Budi - breakdown", size=44, color="#ffffff")
image budi bitter = Text("Budi - bitter", size=44, color="#ffffff")
image budi exhausted = Text("Budi - exhausted", size=44, color="#ffffff")
image budi held = Text("Budi - held", size=44, color="#ffffff")

transform kiri:
    xalign 0.2
    yalign 0.8

transform kanan:
    xalign 0.8
    yalign 0.8

define k = Character("Kiran", color="#9ad7ff")
define a = Character("Andi", color="#ffd08a")
define l = Character("Laras", color="#d6b2ff")
define g = Character("Geri", color="#8aff9a")
define b = Character("Budi", color="#ff9a9a")

label start:

    scene bg blck with dissolve

    "First Aid untuk Jiwa"
    "P3LP Fasilkom UI"

    menu:
        "Pilih skenario."

        "Skenario 1 - Deadline":
            jump scene_01_intro

        "Skenario 2 - Duka di Lorong":
            jump scene_02_intro

        "Skenario 3 - Matil":
            jump scene_03_intro

        "Skenario 4 - Demo Day":
            jump scene_04_intro

        "Skenario 5 - Lelah":
            jump scene_05_intro

    return

label scene_01_intro:

    scene bg lab_komputer with dissolve
    $ safe_music("bgm_hectic.mp3")

    "Hari ini adalah deadline pengumpulan tugas PBP."
    "Kamu datang ke lab komputer untuk menyelesaikan bagian yang belum selesai, bergabung dengan teman-teman yang juga sedang ngebut."
    "Di antara keramaian itu, kamu melihat Andi, matanya merah, tangannya gemetar, mukanya tampak kosong menatap layar."
    "Error log yang sama berulang di layarnya sudah berjam-jam."

    show andi sad at kiri with dissolve

    jump pilihan_01_andi

label pilihan_01_andi:

    "Kamu memperhatikan Andi sebentar. Deadline tinggal beberapa jam lagi, dan tugasmu sendiri belum selesai."

    menu:
        "Apa yang kamu lakukan?"

        "Lanjut ngerjain tugas PBP. Deadline tinggal beberapa jam lagi.":
            jump cabang_01a_andi

        "Dekati Andi dulu untuk lihat kondisinya lebih dekat.":
            jump cabang_01b_andi

label cabang_01a_andi:

    $ safe_music("bgm_melancholy.mp3")

    "Kamu mengalihkan pandangan kembali ke layar laptopmu."
    "\"Andi mungkin cuma lagi mikir keras atau stuck biasa,\" pikirmu dalam hati."
    "Kamu tenggelam kembali dalam baris-baris kode PBP-mu, berusaha mengejar submission di Scele tepat waktu."
    "Dua jam berlalu. Saat kamu akhirnya berhasil push terakhir ke repository, kamu menoleh ke arah tempat duduk Andi."
    "Dia sudah tidak ada di sana. Laptopnya masih terbuka, tapi layarnya mati."

    jump bad_end_01a

label bad_end_01a:

    scene bg overlay_merah with dissolve
    hide andi
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 01A - Kamu kehilangan momen itu."
    "Keesokan harinya, kamu mendengar kabar bahwa Andi ditemukan pingsan di depan lift sore itu, kelelahan dan dehidrasi parah setelah tidak makan dan tidak tidur lebih dari 30 jam."
    "Rasa sungkan dan suasana lab yang sibuk membuatnya merasa tidak ada tempat untuk meminta bantuan."
    "Pesan Edukatif: Tahap pertama dalam P3LP adalah Memperhatikan (Look). Perhatian selama beberapa detik bisa berarti sangat banyak."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 01":
            scene bg lab_komputer with dissolve
            $ safe_music("bgm_hectic.mp3")
            show andi sad at kiri
            jump pilihan_01_andi

        "Kembali ke pilihan skenario":
            jump start

label cabang_01b_andi:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_focus.mp3")

    "Kamu mendekat ke meja Andi. Dari jarak ini kondisinya lebih jelas, mata merah, tangan sedikit gemetar, layar penuh error log yang sama sejak entah kapan."

    show andi defensive at kiri with dissolve

    k "Eh, keliatannya lo lagi lemes banget deh. Lagi ada masalah?"
    a "Eh, Kiran... iya, gue nggak apa-apa kok. Cuma agak pusing aja dikit, ini logic-nya nggak dapet-dapet dari tadi malam..."
    "Andi mencoba menyembunyikan kondisinya, tapi kamu sudah melihat layarnya, error log yang sama terus berulang berjam-jam."

    jump pilihan_02_andi

label pilihan_02_andi:

    "Andi bilang nggak apa-apa, tapi kondisi fisiknya jelas bicara lain."

    menu:
        "Respons kamu?"

        "\"Sini gue liat kodenya, harusnya pake try-catch aja di bagian ini biar nggak crash.\"":
            jump cabang_02a_andi

        "\"Dari semalam? Lu udah istirahat atau makan belum? Muka lu kelihatan pucat banget, Ndi.\"":
            jump cabang_02b_andi

label cabang_02a_andi:

    $ safe_sound("sfx_wrong.mp3")
    $ renpy.music.stop(channel="music", fadeout=1.0)

    "Andi membiarkanmu melihat kodenya, tapi dia tetap diam dan tidak fokus saat kamu menjelaskan. Dia hanya mengangguk tanpa benar-benar paham."

    show andi sad at kiri with dissolve

    "Tiba-tiba, Andi menutup laptopnya dengan keras dan berdiri meninggalkan lab tanpa sepatah kata pun."

    jump bad_end_01b

label bad_end_01b:

    scene bg overlay_merah with dissolve
    hide andi
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 01B - Andi merasa semakin kecil."
    "Andi merasa \"bodoh\" karena harus dibantu untuk hal yang menurutnya sepele, tapi dia tidak sanggup menyelesaikannya."
    "Dia pergi membawa rasa malu itu sendirian."
    "Pesan Edukatif: Jika kondisi fisik dan emosional seseorang sedang sangat tidak stabil, fokuslah pada prinsip Listen terlebih dahulu."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 02":
            scene bg lab_komputer with dissolve
            $ safe_music("bgm_focus.mp3")
            show andi defensive at kiri
            jump pilihan_02_andi

        "Kembali ke pilihan skenario":
            jump start

label cabang_02b_andi:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_warm.mp3")

    k "Dari semalam? Lu udah istirahat atau makan belum? Muka lu kelihatan pucat banget, Ndi."

    show andi cry at kiri with dissolve

    "Andi terdiam sejenak, lalu menghela napas panjang."
    a "Belum... gue cuma minum kopi dari kemarin sore. Takut nggak sempet kelar kalau istirahat."
    "Baru kali ini dia mengakui kondisinya dengan jujur."

    jump pilihan_03_andi

label pilihan_03_andi:

    "Andi sudah jujur soal kondisinya. Sekarang dia butuh sesuatu yang konkret."

    menu:
        "Langkah berikutnya?"

        "\"Ya udah, mending kita ke kantin bentar. Gue temenin makan, logic mah urusan nanti, yang penting perut lu isi dulu.\"":
            jump cabang_03a_andi

        "\"Ndi, lu udah stuck kelamaan. Coba stop dulu 15 menit, kita jalan bentar ke bawah, cari udara seger atau cuci muka.\"":
            jump cabang_03b_andi

label cabang_03a_andi:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_warm.mp3")

    show andi surprised at kiri with dissolve
    "Andi ragu sejenak melihat laptopnya, tapi perutnya berbunyi."

    show andi normal at kiri with dissolve
    a "Iya sih... kalau gue pingsan juga tugasnya nggak bakal kelar."
    "Andi menutup laptopnya. Kalian berjalan ke kantin Fasilkom."

    scene bg kantin_fasilkom with dissolve
    "Di kantin, Andi mulai terlihat lebih segar setelah makan dan minum air putih."
    a "Makasih ya, Kiran. Gue tadi beneran udah blank banget. Habis ini gue mau tidur sejam dulu, baru lanjut deploy lagi."

    jump good_end_01

label good_end_01:

    scene bg kantin_fasilkom with dissolve
    $ safe_music("bgm_warm.mp3")

    "Good Ending 01 - Yang penting perut diisi dulu."
    "Andi berhasil memenuhi kebutuhan dasarnya. Setelah makan dan beristirahat sejenak, kepanikannya mereda."
    "Tugasnya belum selesai, tapi kondisinya sudah jauh lebih baik untuk melanjutkan."
    "Pesan Edukatif: Langkah P3LP terbaik untuk stres harian bisa sesederhana memastikan kebutuhan fisik dasar terpenuhi dan memberi dukungan sosial yang nyata."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Mainkan skenario lain":
            jump start

        "Selesai":
            return

label cabang_03b_andi:

    $ safe_music("bgm_warm.mp3")

    k "Ndi, lu udah stuck kelamaan. Coba stop dulu 15 menit, kita jalan bentar ke bawah, cari udara seger atau cuci muka. Kadang solusinya justru muncul pas pikiran kita lagi rest, bukan pas lagi dipaksa melototin error."

    show andi defensive at kiri with dissolve
    "Andi sempat ragu karena panik mengejar deadline. Kamu meyakinkannya bahwa jeda singkat justru akan mempercepat debugging nanti."

    show andi normal at kiri with dissolve
    a "...oke deh. 15 menit doang ya."

    scene bg luar_gedung_fasilkom with dissolve
    "Setelah berjalan keluar dan menghirup udara luar, Andi terlihat sedikit lebih ringan."

    jump alt_end_01

label alt_end_01:

    scene bg luar_gedung_fasilkom with dissolve
    $ safe_music("bgm_warm.mp3")

    "Alternative Ending 01 - Kepalanya sedikit lebih jernih sekarang."
    "Kodenya belum selesai, tapi kepanikan yang membuat Andi blank tadi sudah jauh berkurang. Dia kembali ke lab dengan kepala yang lebih jernih."
    "Pesan Edukatif: Link dalam P3LP tidak selalu berarti rujukan ke pihak luar. Self-help sederhana seperti jeda singkat juga bisa membantu."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Mainkan skenario lain":
            jump start

        "Selesai":
            return

label scene_02_intro:

    scene bg lorong_fasilkom_sore with dissolve
    $ safe_music("bgm_quiet_ambient.mp3")

    "Kelas terakhir baru saja selesai. Kamu berjalan melewati lorong yang mulai sepi, teman-teman lain sudah buru-buru pulang."
    "Di ujung koridor, kamu melihat Laras. Dia duduk mematung di bangku panjang, matanya sembab, tangannya menggenggam ponsel yang layarnya mati."
    "Kamu tahu Laras baru kehilangan salah satu anggota keluarganya minggu lalu. Tapi ini pertama kalinya kamu melihat dia tampak sepecah ini di kampus."

    show laras sad at kiri with dissolve

    jump pilihan_01_laras

label pilihan_01_laras:

    "Kamu berdiri beberapa langkah dari Laras."

    menu:
        "Apa yang kamu lakukan?"

        "Langsung pulang. Kamu merasa tidak enak mengganggu privasi orang yang sedang berduka.":
            jump cabang_01a_laras

        "Hampiri dengan ceria dan ajak cari seblak agar mood naik.":
            jump cabang_01b_laras

        "Pelankan langkah, duduk di sampingnya dengan jarak yang sopan, dan tunggu sampai dia sadar kamu ada.":
            jump cabang_01c_laras

        "Hampiri lalu langsung tanya apakah tangisnya berhubungan dengan kabar duka minggu lalu.":
            jump cabang_01d_laras

label cabang_01a_laras:

    $ safe_sound("sfx_wrong.mp3")
    $ renpy.music.stop(channel="music", fadeout=1.0)

    "Kamu memperlambat langkah sebentar, melirik ke arah Laras, lalu memutuskan untuk tidak ikut campur."
    "\"Pasti dia butuh ruang. Nggak enak ganggu orang lagi sedih,\" pikirmu."
    "Kamu terus berjalan pulang."

    jump bad_end_02a

label bad_end_02a:

    scene bg overlay_merah with dissolve
    hide laras
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 02A - Kamu tidak ada di sana."
    "Keesokan harinya, Laras tidak masuk kuliah. Notifikasinya semua dimatikan."
    "Belakangan kamu dengar dari teman bersama bahwa dia menarik diri dari semua grup, dia bilang tidak ada yang peduli."
    "Pesan Edukatif: Look dalam P3LP juga berarti menyadari tanda isolasi sosial dan memilih untuk hadir."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 01":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_quiet_ambient.mp3")
            show laras sad at kiri
            jump pilihan_01_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_01b_laras:

    $ safe_sound("sfx_wrong.mp3")
    $ renpy.music.stop(channel="music")

    show laras shocked at kiri with dissolve
    k "Laras! Kok bengong aja? Hujan-hujan gini mending kita cari seblak yuk biar mood naik!"

    show laras flat at kiri with dissolve
    l "Maaf, aku lagi nggak pengen makan seblak."
    "Dia bangkit dan pergi tanpa menoleh lagi."

    jump bad_end_02b

label bad_end_02b:

    scene bg overlay_merah with dissolve
    hide laras
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 02B - Rasa sakitnya tidak kamu anggap serius."
    "Laras tidak marah padamu. Tapi candaanmu membuatnya merasa kesedihannya tidak layak diakui."
    "Pesan Edukatif: Candaan atau keceriaan yang dipaksakan saat seseorang sedang berduka bisa menjadi bentuk minimizing."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 01":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_quiet_ambient.mp3")
            show laras sad at kiri
            jump pilihan_01_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_01d_laras:

    $ safe_sound("sfx_wrong.mp3")
    $ safe_music("bgm_quiet_ambient.mp3")

    show laras tense at kiri with dissolve
    "Kamu menghampiri Laras pelan-pelan dan duduk di sebelahnya."
    k "Laras, kamu kenapa nangis? Ada hubungan sama kabar duka minggu lalu ya?"
    l "Aku... aku nggak apa-apa."
    "Dia merapikan tasnya dan pergi dengan langkah cepat, bukan karena tidak butuh bantuan, tapi karena merasa terpojok."

    jump bad_end_02d

label bad_end_02d:

    scene bg overlay_merah with dissolve
    hide laras
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 02D - Terlalu cepat masuk."
    "Laras bukan tidak mau cerita. Dia hanya belum siap, dan pertanyaanmu yang langsung menunjuk ke luka terdalamnya membuatnya merasa dipojokkan."
    "Pesan Edukatif: Jangan memaksa helpee bercerita, apalagi langsung menyentuh detail peristiwa traumatis."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 01":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_quiet_ambient.mp3")
            show laras sad at kiri
            jump pilihan_01_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_01c_laras:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_gentle.mp3")

    "Kamu memperlambat langkah dan duduk di sebelah Laras, tidak terlalu dekat, tidak terlalu jauh. Tidak langsung ngomong apa-apa."
    "Beberapa detik berlalu. Lalu Laras menoleh. Air matanya jatuh lagi begitu dia sadar ada yang menemaninya."

    show laras open at kiri with dissolve
    l "Eh, Kiran... aku... aku nggak tahu harus gimana sekarang. Rasanya hampa banget."

    jump pilihan_02_laras

label pilihan_02_laras:

    "Laras baru saja membuka dirinya, sedikit. Respons kamu berikutnya menentukan apakah dia merasa cukup aman untuk terus bercerita."

    menu:
        "Respons kamu?"

        "\"Aku paham kok rasanya. Waktu kakekku meninggal tahun lalu, aku juga kayak gini. Tapi lama-lama aku bisa menghadapinya kok, semangat ya!\"":
            jump cabang_02a_laras

        "\"Nggak apa-apa kalau kamu merasa hampa sekarang, Ras. Itu perasaan yang wajar setelah apa yang kamu lewati. Aku di sini kalau kamu mau cerita.\"":
            jump cabang_02b_laras

        "\"Jangan sedih terus, Laras. Keluarga kamu di sana pasti nggak mau lihat kamu nangis begini. Kamu harus kuat demi kuliah kamu.\"":
            jump cabang_02c_laras

        "\"Mending kamu tidur aja sekarang, Ras. Besok pagi pasti rasanya udah lebih mendingan.\"":
            jump cabang_02d_laras

label cabang_02a_laras:

    $ safe_sound("sfx_wrong.mp3")

    show laras flat at kiri with dissolve
    k "Aku paham kok rasanya. Waktu kakekku meninggal tahun lalu, aku juga kayak gini. Tapi lama-lama aku bisa menghadapinya kok, semangat ya!"
    "Laras berhenti menangis. Bukan karena lebih baik, tapi karena percakapan sudah berpindah ke kamu."
    "Dia mendengarkan, mengangguk sopan, tapi semakin lama semakin diam."

    jump neutral_end_02a

label neutral_end_02a:

    "Neutral Ending 02A - Kamu yang bicara. Dia yang butuh didengar."
    "Laras akhirnya pamit dengan senyum tipis. Masalahnya tidak tersalurkan, fokus beralih ke cerita kakekmu, dan duka Laras tetap terlipat rapi di balik sopan santunnya."
    "Pesan Edukatif: Membandingkan pengalaman duka bisa membuat pusat perhatian bergeser dari helpee ke penolong."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 02":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_gentle.mp3")
            show laras open at kiri
            jump pilihan_02_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_02c_laras:

    $ safe_sound("sfx_wrong.mp3")
    $ renpy.music.stop(channel="music", fadeout=1.0)

    show laras guilty at kiri with dissolve
    k "Jangan sedih terus, Laras. Keluarga kamu di sana pasti nggak mau lihat kamu nangis begini. Kamu harus kuat demi kuliah kamu."
    "Laras menunduk lebih dalam. Air matanya berhenti, tapi bukan karena mereda."
    "Dia berhenti karena tiba-tiba merasa bersalah sudah menangis."

    jump bad_end_02c

label bad_end_02c:

    scene bg overlay_merah with dissolve
    hide laras
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 02C - Dia berhenti menangis, tapi bebannya bertambah."
    "Laras merasa gagal menjadi mahasiswa yang kuat. Tangisannya tersedak, tapi perasaan hampanya tidak ke mana-mana."
    "Pesan Edukatif: Tuntutan untuk harus kuat atau jangan sedih adalah bentuk toxic positivity."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 02":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_gentle.mp3")
            show laras open at kiri
            jump pilihan_02_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_02d_laras:

    $ safe_sound("sfx_wrong.mp3")

    show laras flat at kiri with dissolve
    k "Mending kamu tidur aja sekarang, Ras. Besok pagi pasti rasanya udah lebih mendingan."
    l "Iya, mungkin kamu benar."
    "Nadanya hampa. Dia merasa percakapan ini buru-buru ingin kamu akhiri."

    jump neutral_end_02b

label neutral_end_02b:

    "Neutral Ending 02B - Solusi diberikan sebelum perasaannya didengar."
    "Laras pulang. Perasaan hampanya tidak tersalurkan. Besok paginya, kondisinya tidak lebih baik, dia hanya lebih pandai menyembunyikannya."
    "Pesan Edukatif: Dengarkan sampai tuntas dulu sebelum menawarkan solusi apapun."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 02":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_gentle.mp3")
            show laras open at kiri
            jump pilihan_02_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_02b_laras:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_warm.mp3")

    k "Nggak apa-apa kalau kamu merasa hampa sekarang, Ras. Itu perasaan yang wajar setelah apa yang kamu lewati. Aku di sini kalau kamu mau cerita."

    show laras open at kiri with dissolve
    "Laras menutup matanya sebentar. Lalu mulai bicara, perlahan, terputus-putus, tentang minggu lalu, tentang betapa semuanya terasa tidak nyata."
    "Setelah beberapa waktu bercerita, Laras menghela napas panjang. Dia mengaku belum makan seharian, dan takut pulang ke kosan yang sepi."

    jump pilihan_03_laras

label pilihan_03_laras:

    "Laras sudah cukup terbuka untuk menerima bantuan. Langkah apa yang paling tepat sekarang?"

    menu:
        "Langkah berikutnya?"

        "\"Kamu udah parah banget nih, Ras. Besok pagi pokoknya aku anter ke psikiater, ini udah masuk gejala depresi.\"":
            jump cabang_03a_laras

        "\"Malam ini, mau aku temenin makan dulu, atau mau aku hubungi teman dekatmu buat nemenin di kosan biar kamu nggak sendirian?\"":
            jump cabang_03b_laras

        "\"Ya udah kalau gitu kamu istirahat aja ya, aku pulang duluan. Kabari aja kalau butuh apa-apa.\"":
            jump cabang_03c_laras

        "\"Kamu telepon orang tua kamu sekarang juga, minta dijemput pulang aja. Di kampus malah makin stres.\"":
            jump cabang_03d_laras

label cabang_03a_laras:

    $ safe_sound("sfx_wrong.mp3")
    $ renpy.music.stop(channel="music")

    show laras alarmed at kiri with dissolve
    k "Kamu udah parah banget nih, Ras. Besok pagi pokoknya aku anter ke psikiater, ini udah masuk gejala depresi."
    l "Psikiater? Depresi? Aku cuma lagi sedih, Ran, aku nggak gila!"

    jump bad_end_02e

label bad_end_02e:

    scene bg overlay_merah with dissolve
    hide laras
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 02E - Kata-kata itu tidak mudah dilupakan."
    "Laras pergi dengan kecemasan baru: takut dirinya gila, takut dicap dengan label yang tidak dia minta."
    "Di masa depan, dia akan dua kali berpikir sebelum meminta bantuan."
    "Pesan Edukatif: First aider bukan psikolog. Rujukan ke profesional harus dilakukan secara kolaboratif dan bertahap."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 03":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_warm.mp3")
            show laras open at kiri
            jump pilihan_03_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_03c_laras:

    show laras flat at kiri with dissolve
    k "Ya udah kalau gitu kamu istirahat aja ya, aku pulang duluan. Kabari aja kalau butuh apa-apa."
    l "Iya, makasih ya."
    "Kamu pergi. Dia tetap duduk di bangku itu."

    jump neutral_end_02c

label neutral_end_02c:

    "Neutral Ending 02C - Kamu sudah mendengar, tapi meninggalkan tanpa arahan."
    "Laras pulang sendirian dengan perut kosong. Karena tidak ada tawaran konkret, dia tidak tahu harus berbuat apa selanjutnya."
    "Malam itu terasa sangat panjang."
    "Pesan Edukatif: Tawarkan opsi konkret yang bisa langsung diterima atau ditolak."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 03":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_warm.mp3")
            show laras open at kiri
            jump pilihan_03_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_03d_laras:

    $ safe_sound("sfx_wrong.mp3")

    show laras tense at kiri with dissolve
    k "Kamu telepon orang tua kamu sekarang juga, minta dijemput pulang aja. Di kampus malah makin stres."
    l "Aku nggak mau bikin mereka makin sedih kalau lihat aku kayak gini."

    jump bad_end_02f

label bad_end_02f:

    scene bg overlay_merah with dissolve
    hide laras
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 02F - Kamu tidak tahu beban yang dia bawa."
    "Laras merasa kamu tidak memahami situasi keluarganya. Beban pikirannya bertambah, sekarang ada tekanan baru yang kamu taruh di pundaknya."
    "Pesan Edukatif: Selalu hargai otonomi helpee. Tanya dulu apa yang mereka butuhkan, jangan langsung tentukan solusinya."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 03":
            scene bg lorong_fasilkom_sore with dissolve
            $ safe_music("bgm_warm.mp3")
            show laras open at kiri
            jump pilihan_03_laras

        "Kembali ke pilihan skenario":
            jump start

label cabang_03b_laras:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_open.mp3")

    show laras relieved at kiri with dissolve
    k "Malam ini, mau aku temenin makan dulu, atau mau aku hubungi teman dekatmu buat nemenin di kosan biar kamu nggak sendirian?"
    "Laras terdiam. Matanya berkaca-kaca lagi, tapi kali ini bukan karena kesedihan. Karena lega."
    l "Makasih ya, Ran. Aku beneran takut sendirian malam ini."
    k "Yuk."
    "Mereka berjalan bersama ke kantin."

    jump good_end_02

label good_end_02:

    scene bg kantin_fasilkom with dissolve
    $ safe_music("bgm_open.mp3")

    "Good Ending 02 - Dia tidak sendirian malam itu."
    "Laras tidak langsung sembuh dari kedukaan. Tapi malam itu, dia punya seseorang yang menemaninya makan, dan itu cukup untuk membuat besok terasa sedikit lebih mungkin untuk dihadapi."
    "Pesan Edukatif: Dukungan sosial nyata, kehadiran fisik, dan pemenuhan kebutuhan dasar adalah bentuk stabilisasi emosi yang efektif sebagai langkah pertama."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Mainkan skenario lain":
            jump start

        "Selesai":
            return

# --- SKENARIO 3: MATIL ---

label scene_03_intro:

    scene bg kamar_kosan with dissolve
    $ safe_music("bgm_tense_night.mp3")

    "Malam ini kamu sedang mereview dokumen proyek kelompok di kamar kosan."
    "Tiba-tiba grup chat proyek kelompokmu mendadak ramai."
    "Ketua kelompok mengirim pesan panjang yang menuduh Geri 'matil' — main tinggal — karena menghilang sejak sore dan belum mengumpulkan bagian tugasnya."
    "Pesan pasif-agresif mulai bermunculan dari anggota lain."

    "\"Kalau emang niatnya matil dari awal bilang aja kali, biar gak bebanin sirkel.\""
    "\"Gue hapus aja ya namanya dari submission besok pagi? Gak usah dikasih ampun.\""

    "Kamu melihat tanda centang biru di semua pesan itu. Geri sudah membaca semuanya — tapi tidak membalas sepatah kata pun."

    show geri read_receipt at kiri with dissolve

    jump pilihan_01_geri

label pilihan_01_geri:

    "Kamu menatap layar HP-mu. Ketikan-ketikan baru terus bermunculan di grup."

    menu:
        "Apa yang kamu lakukan?"

        "Ketik di grup: ikut menyindir dan setuju namanya dihapus.":
            jump cabang_01a_geri

        "Ketik di grup: membela Geri secara frontal di grup.":
            jump cabang_01b_geri

        "Tetap diam di grup, lalu DM pribadi ke Geri.":
            jump cabang_01c_geri

label cabang_01a_geri:

    $ safe_music("bgm_melancholy.mp3")

    "Tak lama setelah kamu mengirim pesan itu, notifikasi muncul."
    "Geri keluar dari grup kelompok."
    "Kamu tersadar bahwa sirkelnya sendiri — termasuk kamu — telah menutup pintu bagi dirinya untuk menjelaskan."

    "Apa yang akan kamu lakukan?"

    menu:
        "DM Geri dan minta maaf, tanyakan kondisinya.":

            $ safe_sound("sfx_correct.mp3")
            $ safe_music("bgm_focus.mp3")
            k "Ger, maaf banget ya soal di grup tadi. Gue kebawa panik deadline sampai ikut nyindir lu. Lu gak apa-apa? Cerita ke gue dong."
            jump pilihan_02_geri

        "Biarkan saja — dia yang salah pakai matil.":

            jump bad_end_03a

label cabang_01b_geri:

    $ safe_sound("sfx_wrong.mp3")
    $ safe_music("bgm_conflict.mp3")

    "Grup sirkel malah pecah dan saling berantem antar anggota."
    "\"Kok lu malah belain dia sih? Lu mau ngerjain bagiannya?\""

    "Geri semakin merasa bersalah — kehadirannya memicu keributan besar di dalam sirkel."

    "Apa yang akan kamu lakukan?"

    menu:
        "Berhenti di grup, lalu DM Geri secara pribadi.":

            $ safe_sound("sfx_correct.mp3")
            $ safe_music("bgm_focus.mp3")
            "Kamu berhenti membalas di grup dan membuka chat pribadi dengan Geri."
            jump pilihan_02_geri

        "Terus berdebat di grup untuk membuktikan siapa yang paling solid.":

            jump neutral_end_03a

label cabang_01c_geri:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_focus.mp3")

    "Kamu membuka ruang obrolan pribadi dengan Geri dan mengirim pesan untuk menanyakan kabarnya."
    "Beberapa menit berlalu. Lalu Geri membalas."

    show geri sad at kiri with dissolve

    g "Gue beneran takut baca grup, Ran. Gue gak ada niat matil… Dari siang laptop gue mati total karena ketumpahan air dan semua data proyek ada di sana."
    g "Gue mau pinjem laptop kosan temen tapi gue malu banget karena dari tadi sore gue panik dan nangis sendirian di kosan. Gue takut didepak dan dapet nilai E dari dosen."

    jump pilihan_02_geri

label pilihan_02_geri:

    hide geri
    show geri sad at kiri

    "Geri baru saja bercerita. Kondisinya jauh berbeda dari yang diasumsikan di grup."

    menu:
        "Respons kamu?"

        "\"Ya lu lagian kenapa gak bilang dari sore? Cuekin aja ketikan anak-anak. Jangan nangis lagi, cowok harus kuat.\"":
            jump cabang_02a_geri

        "\"Astaga, musibah banget itu laptop mati pas mepet deadline. Wajar banget lu panik, Ger. Lu gak usah mikirin grup dulu ya.\"":
            jump cabang_02b_geri

        "\"Lu jangan panik! Sekarang juga pesen ojol, ke warnet, kerjain ulang dari nol malam ini!\"":
            jump cabang_02c_geri

label cabang_02a_geri:

    $ safe_sound("sfx_tricky.mp3")
    $ safe_music("bgm_melancholy.mp3")

    show geri closed_off at kiri with dissolve
    g "Gue males debat, Ran…"

    jump recovery_02_geri

label cabang_02c_geri:

    $ safe_sound("sfx_tricky.mp3")
    $ safe_music("bgm_melancholy.mp3")

    show geri closed_off at kiri with dissolve
    g "Gue beneran gak ada tenaga buat ke warnet malam-malam gini, kepala gue pusing banget…"

    jump recovery_02_geri

label recovery_02_geri:

    "Responsnya menunjukkan dia mulai menutup diri — merasa disalahkan atau dipaksa bergerak saat mentalnya sedang blank."

    "Apa yang akan kamu lakukan?"

    menu:
        "Maaf, fokus tenangkan Geri dulu dan tanyakan apa yang bisa dibantu.":

            $ safe_sound("sfx_correct.mp3")
            k "Eh maaf ya, Ger, gue gak maksud menggurui atau maksa lu malam-malam gini. Gue cuma khawatir sama lu. Sekarang lu tarik napas pelan-pelan dulu, ada yang bisa gue bantu buat bikin lu merasa lebih tenang?"
            jump geri_terdiam

        "Yaudah kalau emang gak bisa dipaksa, istirahat aja deh.":

            jump neutral_end_03b

label cabang_02b_geri:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_warm.mp3")

    k "Astaga, musibah banget itu laptop mati pas mepet deadline. Wajar banget lu panik sekarang, Ger. Lu gak usah mikirin grup dulu ya, yang penting lu tenangin diri dulu ya."

    jump geri_terdiam

label geri_terdiam:

    show geri cry at kiri with dissolve

    "Geri terdiam sejenak, lalu menghela napas panjang."
    g "Gue… gue udah nyoba cari solusi dari sore tapi buntu terus. Gue takut banget nama gue dicoret besok."
    "Baru kali ini dia mengakui kondisinya dengan jujur."

    jump pilihan_03_geri

label pilihan_03_geri:

    "Geri sudah jujur soal kondisinya. Sekarang dia butuh sesuatu yang konkret."

    menu:
        "Langkah berikutnya?"

        "\"Kecemasan lu udah parah banget. Besok pagi lu harus ikut gue ke konselor fakultas.\"":
            jump cabang_03a_geri

        "\"Malam ini lu tidur aja, jangan buka grup. Gue bantu ketik ulang data sebisanya, besok kita omongin ke anak-anak.\"":
            jump cabang_03b_geri

        "\"Gue bantu telepon ketua kelompok privat buat jelasin musibah laptop lu.\"":
            jump cabang_03c_geri

label cabang_03a_geri:

    $ safe_sound("sfx_wrong.mp3")
    $ safe_music("bgm_melancholy.mp3")

    show geri offended at kiri with dissolve
    "Geri merasa dianggap 'lemah mental' karena menangis akibat tekanan tugas. Dia tersinggung, mematikan ponselnya, dan memilih menerima nilai E serta menjauh dari sirkel pertemanan kalian sepenuhnya."

    jump bad_end_03a

label cabang_03b_geri:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_warm.mp3")

    k "Malam ini lu tidur aja, jangan buka grup kelompok dulu. Biar sebagian data lu yang ilang gue bantu ketik ulang malam ini sebisanya. Besok pagi kita omongin bareng-bareng ke anak-anak."

    show geri grateful at kiri with dissolve
    g "Ran.. lu serius? Makasih banget. Gue udah hopeless banget malam ini."
    "Geri menutup grup kelompok. Kamu mulai mengetik ulang bagian data sebisanya."

    jump good_end_03

label cabang_03c_geri:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_warm.mp3")

    k "Gimana kalau malam ini gue bantu telepon ketua kelompok kita secara privat buat jelasin musibah laptop lu? Biar dia paham kalau lu gak berniat matil dan nama lu gak dicoret."

    show geri surprised at kiri with dissolve
    "Geri sempat ragu karena takut merepotkan. Kamu meyakinkannya bahwa ini yang bisa kamu lakukan sekarang."

    show geri normal at kiri with dissolve
    g "...oke deh. Makasih ya, Ran."
    "Kamu menutup aplikasi chat dan menelepon ketua kelompok secara pribadi — menjelaskan musibah laptop Geri dengan kepala dingin."

    scene bg kamar_kosan_malam with dissolve

    jump good_end_03

label bad_end_03a:

    scene bg overlay_merah with dissolve
    hide geri
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 03A - Geri merasa sirkelnya sendiri sudah membuangnya."
    "Geri mengalami kecemasan sosial akut, mengurung diri di kosan, dan memutuskan untuk drop mata kuliah tersebut karena takut bertemu dengan sirkelnya di kampus."
    "Pesan Edukatif: Ikut menyudutkan helpee di kelompok terdekat akan meruntuhkan sistem dukungan sosialnya."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 01":
            scene bg kamar_kosan with dissolve
            $ safe_music("bgm_tense_night.mp3")
            show geri read_receipt at kiri
            jump pilihan_01_geri

        "Kembali ke pilihan skenario":
            jump start

label neutral_end_03a:

    scene bg overlay_kuning with dissolve
    hide geri
    $ safe_sound("sfx_neutralend.mp3")
    $ safe_music("bgm_melancholy.mp3")

    "Neutral Ending 03A - Suasana dingin. Geri tetap menarik diri."
    "Suasana grup menjadi dingin dan canggung. Geri tetap tidak mengumpulkan tugasnya karena merasa menjadi beban konflik, dan memilih menarik diri dari sirkel pertemanan."
    "Pesan Edukatif: Membela helpee secara frontal di ruang grup yang sedang emosional sering justru meningkatkan ketegangan."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 01":
            scene bg kamar_kosan with dissolve
            $ safe_music("bgm_tense_night.mp3")
            show geri read_receipt at kiri
            jump pilihan_01_geri

        "Kembali ke pilihan skenario":
            jump start

label neutral_end_03b:

    scene bg overlay_kuning with dissolve
    hide geri
    $ safe_sound("sfx_neutralend.mp3")
    $ safe_music("bgm_melancholy.mp3")

    "Neutral Ending 03B - Geri pasrah. Namanya dicoret dari submission."
    "Geri tidak membalas lagi pesanmu malam itu. Keesokan paginya, ketua kelompok benar-benar mencoret nama Geri dari submission."
    "Pesan Edukatif: Memaksakan solusi praktis saat helpee sedang terguncang emosinya membuat mereka menutup diri dari bantuan selanjutnya."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 02":
            scene bg kamar_kosan with dissolve
            $ safe_music("bgm_focus.mp3")
            show geri sad at kiri
            jump pilihan_02_geri

        "Kembali ke pilihan skenario":
            jump start

label good_end_03:

    scene bg kamar_kosan_malam with dissolve
    $ safe_music("bgm_warm.mp3")

    hide geri
    "Good Ending 03 - Kesalahpahaman berhasil diluruskan."
    "Melalui bantuanmu — baik dengan mengetik ulang data maupun mediasi privat dengan ketua kelompok — kesalahpahaman tentang 'matil' berhasil diluruskan."
    "Kelompok sepakat memberikan kelonggaran waktu. Nama Geri tidak dicoret. Hubungan sirkel pertemanan kalian tetap terjaga dengan baik."
    "Pesan Edukatif: Tahap Link pada konflik sirkel bertujuan mengembalikan rasa aman dan memulihkan fungsi sosial helpee."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Mainkan skenario lain":
            jump start

        "Selesai":
            return

# --- SKENARIO 4: DEMO DAY ---

label scene_04_intro:

    scene bg lorong_gedung_baru with dissolve
    $ safe_music("bgm_hectic_corridor.mp3")

    "Hari ini adalah jadwal giliranmu untuk mendemonstrasikan proyek akhir mata kuliah SDA ke asisten dosen."
    "Saat kamu menunggu giliran di lorong, kamu melihat dua temanmu yang satu slot waktu demo di lab sebelah."
    "Andi duduk bersandar di dinding lorong sambil memegang dadanya, napasnya pendek-pendek, dan wajahnya pucat."
    "Di sebelahnya, Laras duduk memeluk lutut sambil menangis sesenggukan karena berkas laporan kelompoknya mendadak corrupt."
    "Antrean asdos berjalan cepat, dan 10 menit lagi giliranmu masuk ke lab akan tiba."

    show andi panic at kiri
    show laras cry at kanan

    jump pilihan_01_demo

label pilihan_01_demo:

    "Kamu menatap keduanya. Waktu sangat terbatas."

    menu:
        "Apa yang kamu lakukan?"

        "Fokus pada proyek sendiri dan mengabaikan mereka.":
            jump cabang_01a_demo

        "Menangani Laras terlebih dahulu dan tanya kronologi berkas corrupt.":
            jump cabang_01b_demo

        "Amankan Andi dulu karena tanda-tanda serangan panik, sambil memantau Laras.":
            jump cabang_01c_demo

label cabang_01a_demo:

    $ safe_music("bgm_melancholy.mp3")

    "Kamu mengalihkan pandangan ke readme di repository GitHub-mu, berusaha fokus pada demo."
    "Andi tiba-tiba ambruk karena kekurangan oksigen akibat serangan panik."

    jump recovery_01_demo_fatal

label cabang_01b_demo:

    $ safe_music("bgm_melancholy.mp3")

    "Kamu langsung menghampiri Laras dan menanyakan kronologi berkas laporan yang corrupt secara detail."
    "Andi yang sedang kesulitan bernapas merasa semakin terabaikan, sementara Laras justru makin panik karena dicecar pertanyaan saat emosinya sedang penuh."

    jump recovery_01_demo_fatal

label recovery_01_demo_fatal:

    "Apa yang akan kamu lakukan?"

    menu:
        "Minta maaf dan lakukan triase fisik — bantu Andi menarik napas.":

            $ safe_sound("sfx_correct.mp3")
            $ safe_music("bgm_focus.mp3")
            k "Laras, bentar ya, tarik napas dulu pelan-pelan. Andi, liat gue, ikutin napas gue... tarik dari hidung, buang dari mulut..."
            "Kamu mengalihkan fokus ke penanganan fisik Andi yang paling darurat."
            jump cabang_01c_demo

        "Ikut panik dan berlari memanggil asdos di lab.":

            jump bad_end_04

label cabang_01c_demo:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_focus.mp3")

    hide andi
    hide laras

    "Kamu berhasil mengendalikan situasi dengan tenang. Kamu meminta Andi meluruskan kakinya dan menuntun Laras untuk ikut menarik napas dalam-dalam bersamamu."
    "Napas Andi mulai melambat dan membaik, namun dia bergumam:"

    show andi exhausted at kiri
    show laras sad at kanan

    a "Gue beneran blank, Ran... Program AVL Tree gue mendadak error pas gue tes run tadi di selasar. Gue takut gak lulus matkul ini."
    "Di sisi lain, Laras masih menangis karena selain laporan kelompoknya rusak, dia merasa bersalah karena Geri sempat dituduh 'matil' oleh anak-anak sirkel mereka semalam."

    jump pilihan_02_demo

label pilihan_02_demo:

    "Andi dan Laras sudah sedikit lebih stabil secara fisik. Tapi keduanya masih terbebani masalah yang berbeda."

    menu:
        "Respons kamu?"

        "Rebut laptop Andi untuk debugging dan suruh Laras ketik ulang laporan dari awal.":
            jump cabang_02a_demo

        "Grounding bersama dan validasi bahwa tekanan hari ini memang sangat berat.":
            jump cabang_02b_demo

        "\"Guys, gue juga 10 menit lagi demo dan asdos gue pelit nilai. Yuk tahan bentar!\"":
            jump cabang_02c_demo

label cabang_02a_demo:

    $ safe_sound("sfx_tricky.mp3")
    $ safe_music("bgm_melancholy.mp3")

    "Andi semakin blank karena logikanya diintervensi orang lain secara terburu-buru, sedangkan Laras merasa ketakutan sosialnya diremehkan."
    "Mereka berdua kembali gemetaran karena waktu sisa demo tinggal 5 menit lagi."

    jump recovery_02_demo

label cabang_02c_demo:

    $ safe_sound("sfx_tricky.mp3")
    $ safe_music("bgm_melancholy.mp3")

    show andi exhausted at kiri
    show laras sad at kanan

    k "Guys, plis, gue juga 10 menit lagi maju demo dan asdos penguji gue terkenal pelit nilai. Kita semua lagi pusing, yuk bisa yuk tahan bentar!"
    "Andi semakin blank karena logikanya diintervensi, sedangkan Laras merasa ketakutan sosialnya diremehkan."
    "Mereka berdua kembali gemetaran karena waktu sisa demo tinggal 5 menit lagi."

    jump recovery_02_demo

label recovery_02_demo:

    "Apa yang akan kamu lakukan?"

    menu:
        "Maaf, fokus ke penenangan — stop mikirin spek program, fokus napas.":

            $ safe_sound("sfx_correct.mp3")
            k "Maaf, gue malah bikin kalian makin pusing. Stop mikirin spek program dulu. Yuk merem bentar, lupain asdosnya dulu. Fokus ke napas kalian aja sekarang."
            jump cabang_02b_demo

        "Biarkan mereka karena jam demo kamu sudah masuk.":

            jump neutral_end_04

label cabang_02b_demo:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_warm.mp3")

    "Berkat ketenanganmu, Andi berhasil mendapatkan kembali fokus berpikirnya dan Laras sudah berhenti menangis."
    "Pintu lab terbuka, dan asdos memanggil nama kelompok mereka untuk masuk."
    "Mereka berdua sudah jauh lebih stabil, tetapi masih butuh penguat eksternal agar kecemasan tidak kambuh saat dicecar asdos."

    show andi normal at kiri
    show laras normal at kanan

    jump pilihan_03_demo

label pilihan_03_demo:

    "Pintu lab sudah terbuka. Andi dan Laras butuh satu langkah lagi sebelum masuk."

    menu:
        "Langkah berikutnya?"

        "Suruh mereka langsung masuk ke meja asdos dan berdoa semuanya lancar.":
            jump cabang_03a_demo

        "Berlari cari dosen koordinator untuk meminta pembatalan demo hari ini.":
            jump cabang_03b_demo

        "Hubungi PJ asdos, jelaskan situasi darurat, dan janji menunggu di luar lab.":
            jump cabang_03c_demo

label cabang_03a_demo:

    $ safe_music("bgm_melancholy.mp3")

    "Andi dan Laras masuk ke lab tanpa ada asdos yang diberi tahu untuk memantau kondisi mereka."
    "Serangan panik Andi berisiko kambuh di tengah-tengah demo."

    jump bad_end_04

label cabang_03b_demo:

    $ safe_music("bgm_melancholy.mp3")

    "Dosen koordinator merasa kamu terlalu mencampuri sistem penjadwalan tanpa prosedur resmi."
    "Andi dan Laras tetap masuk demo dalam kondisi pikiran yang kacau."

    jump neutral_end_04

label cabang_03c_demo:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_warm.mp3")

    "Kamu menghubungi PJ asdos di lab dan menjelaskan situasi darurat secara singkat agar mereka mendapat sedikit kelonggaran waktu persiapan."
    "Kamu berjanji kepada Andi dan Laras bahwa kamu akan menunggu di kursi luar lab sampai mereka selesai."
    "Giliran demomu sendiri berjalan lancar karena fokusmu terasah setelah mengelola situasi krisis."

    jump good_end_04

label bad_end_04:

    scene bg overlay_merah with dissolve
    hide andi
    hide laras
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 04 - Lorong lab menjadi gaduh."
    "Lorong lab menjadi gaduh dan mengganggu jalannya demo mahasiswa lain. Asdos menegurmu karena membuat keributan."
    "Andi dilarikan ke klinik dalam kondisi lemas, sementara Laras dinyatakan gagal demo hari itu."
    "Pesan Edukatif: Look pada situasi kompleks menuntut triase — dahulukan gejala fisik akut sebelum krisis emosional murni."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 01":
            scene bg lorong_gedung_baru with dissolve
            $ safe_music("bgm_hectic_corridor.mp3")
            show andi panic at kiri
            show laras cry at kanan
            jump pilihan_01_demo

        "Kembali ke pilihan skenario":
            jump start

label neutral_end_04:

    scene bg overlay_kuning with dissolve
    hide andi
    hide laras
    $ safe_sound("sfx_neutralend.mp3")
    $ safe_music("bgm_melancholy.mp3")

    "Neutral Ending 04 - Andi dan Laras masuk lab dalam kondisi kacau."
    "Mereka tidak bisa menjelaskan kompleksitas waktu dari struktur data mereka dengan lancar ke asdos. Nilai proyek mereka jatuh."
    "Pesan Edukatif: Listen dalam krisis kelompok bukan berarti menyelesaikan masalah teknis saat itu juga. Fokus pada stress management jangka pendek."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 02":
            scene bg lorong_gedung_baru with dissolve
            $ safe_music("bgm_focus.mp3")
            show andi exhausted at kiri
            show laras sad at kanan
            jump pilihan_02_demo

        "Kembali ke pilihan skenario":
            jump start

label good_end_04:

    scene bg selasar_gedung_baru with dissolve
    $ safe_music("bgm_warm.mp3")

    hide andi
    hide laras

    "Good Ending 04 - Kamu tidak hanya berhasil menyelamatkan nilai proyekmu sendiri."
    "Sore harinya, kalian bertiga berdiri di selasar Gedung Baru Fasilkom dengan perasaan lega."
    "Andi berhasil mendemonstrasikan fungsi insert dan delete pada programnya dengan lancar, dan Laras berhasil mendapat file cadangan laporannya melalui cloud backup."
    "Kamu berhasil menjadi lifesaver bagi teman-teman seangkatanmu di tahun kedua ini."
    "Pesan Edukatif: Link pada level integrasi melibatkan mobilisasi peer support dan perantara internal kampus secara bijak."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Mainkan skenario lain":
            jump start

        "Selesai":
            return

# --- SKENARIO 5: LELAH ---

label scene_05_intro:

    scene bg balkon_lt5_malam with dissolve
    $ safe_music("bgm_crisis_night.mp3")

    "Kamu baru saja selesai mengerjakan revisi tugas di kelas. Tas sudah di pundak, kamu melangkah menuju tangga."
    "Di balkon lantai 5, kamu melihat siluet seseorang berdiri di dekat pagar — tidak bergerak, menatap kosong ke bawah."
    "Kamu mengenali postur itu. Budi."
    "Teman yang biasanya paling keras tertawanya di angkatan. Sebulan terakhir dia menghilang dari grup, jarang masuk kelas, selalu menolak diajak ngumpul."
    "Lalu kamu ingat pesan di grup angkatan dari Budi sore tadi: \"Makasih buat semuanya ya, temen-temen. Keyboard mekanik gue ambil aja di loker, gue titip buat yang butuh.\""
    "Sesuatu di dadamu langsung mencelos."

    show budi blank_stare at kiri with dissolve

    jump pilihan_01_budi

label pilihan_01_budi:

    "Budi berdiri sangat dekat dengan pagar balkon. Kamu harus segera memutuskan."

    menu:
        "Apa yang kamu lakukan?"

        "Berteriak dari jauh: \"Budi! Ngapain di situ? Turun sekarang, bahaya!\"":
            jump cabang_01a_budi

        "Mendekat pelan dengan langkah tenang dan sapa dengan suara rendah.":
            jump cabang_01b_budi

        "Langsung turun cari satpam, meninggalkan Budi sendirian di balkon.":
            jump cabang_01c_budi

label cabang_01a_budi:

    $ safe_sound("sfx_wrong.mp3")

    show budi cornered at kiri with dissolve
    "Budi tersentak kaget. Tubuhnya refleks bergerak mundur satu langkah ke arah pagar."
    b "Jangan deket-deket! Gue cuma pengen tenang!"
    "Suaranya pecah. Kamu bisa melihat jelas sekarang, matanya merah, tangannya gemetar memegang pagar."

    jump recovery_01_budi

label cabang_01c_budi:

    $ safe_sound("sfx_wrong.mp3")

    show budi cornered at kiri with dissolve
    "Budi tersentak kaget. Tubuhnya refleks bergerak mundur satu langkah ke arah pagar."
    b "Jangan deket-deket! Gue cuma pengen tenang!"
    "Suaranya pecah. Kamu bisa melihat jelas sekarang, matanya merah, tangannya gemetar memegang pagar."

    jump recovery_01_budi

label recovery_01_budi:

    "Situasi masih bisa diselamatkan. Langkah berikutmu akan menentukan segalanya."

    menu:
        "Berhenti di tempat dan bicara pelan — cuma ingin nemenin.":

            $ safe_sound("sfx_correct.mp3")
            k "Maaf, Bud. Gue nggak bermaksud ngagetin. Gue diem di sini ya, gue cuma pengen nemenin lu."
            "Kamu tidak bergerak. Hanya berdiri di sana, di jarak yang aman."
            "Beberapa detik berlalu terasa sangat panjang. Tapi perlahan, tarikan napas Budi mulai melambat."
            jump pilihan_02_budi

        "Terus mendekat sambil berteriak: \"Bud, jangan gila! Turun!\"":
            jump bad_end_05a

label cabang_01b_budi:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_crisis_night.mp3")

    "Kamu memperlambat langkah. Satu langkah. Berhenti sejenak. Satu langkah lagi."
    "Nafasmu sendiri kamu atur agar terdengar tenang."

    show budi blank_stare at kiri with dissolve
    k "Bud..."
    "Hanya itu yang kamu ucapkan. Satu kata, suara rendah."
    "Budi perlahan menoleh. Matanya merah. Pipinya basah."

    jump pilihan_02_budi

label pilihan_02_budi:

    show budi breakdown at kiri with dissolve

    "Kamu berhasil ada di dekat Budi tanpa membuatnya semakin panik. Budi mulai menangis hebat, tubuhnya bergetar. Dia mulai bicara."
    b "Gue nggak punya masa depan lagi, Ran. Semuanya udah berakhir. IPK gue hancur, gue udah jadi beban orang tua. Gue capek pura-pura ceria terus."

    menu:
        "Respons kamu?"

        "\"Bud, inget Tuhan. Banyak orang yang lebih susah dari lu tapi tetap bertahan.\"":
            jump cabang_02a_budi

        "\"Gue dengerin, Bud. Gue di sini. Ceritain aja semuanya, lu nggak sendirian malam ini.\"":
            jump cabang_02b_budi

        "\"Eh, daripada sedih di sini, yuk ke resto baru deket Kutek, gue yang traktir!\"":
            jump cabang_02c_budi

label cabang_02a_budi:

    $ safe_sound("sfx_wrong.mp3")

    show budi bitter at kiri with dissolve
    k "Bud, inget Tuhan. Banyak orang yang lebih susah dari lu tapi tetap bertahan. Masa gara-gara IPK doang lu mau nyerah kayak gini?"
    "Budi berhenti menangis. Tapi bukan karena lebih baik."
    b "Lu pikir ini cuma soal IPK? Lu beneran nggak paham..."
    "Budi berbalik, kembali menghadap ke luar pagar balkon."

    jump recovery_02_budi

label cabang_02c_budi:

    $ safe_sound("sfx_wrong.mp3")

    show budi bitter at kiri with dissolve
    k "Eh, daripada sedih di sini, ada resto baru deket Kutek yang enak. Yuk kita ke sana sekarang, gue yang traktir!"
    "Budi berhenti menangis. Tapi bukan karena lebih baik."
    b "Lu pikir seblak atau makanan bisa nyelesaiin masalah gue? Lu beneran nggak paham..."
    "Budi berbalik, kembali menghadap ke luar pagar balkon."

    jump recovery_02_budi

label recovery_02_budi:

    "Masih ada satu kesempatan. Tapi ini yang terakhir."

    menu:
        "Maaf, minta kesempatan untuk benar-benar mendengarkan.":

            $ safe_sound("sfx_correct.mp3")
            k "Maaf banget, Bud. Omongan gue ngaco tadi. Gue bodoh, nggak bisa milih kata-kata. Tolong kasih gue kesempatan buat dengerin cerita lu yang sebenernya. Gue di sini fokus buat lu."
            "Budi tidak langsung menjawab. Tapi bahunya turun sedikit. Lalu, pelan-pelan, dia mulai bicara lagi."
            jump pilihan_03_budi_from_breakdown

        "Membela diri: \"Gue kan cuma ngasih tahu hal baik!\"":
            jump bad_end_05b

label cabang_02b_budi:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_gentle.mp3")

    show budi breakdown at kiri with dissolve
    k "Gue dengerin, Bud. Gue di sini. Ceritain aja semuanya, lu nggak sendirian malam ini."
    "Kamu tidak mencoba mengisi keheningan. Kamu hanya ada di sana."
    "Budi menangis sejadi-jadinya. Semuanya keluar — tekanan semester, rasa takut mengecewakan orang tua, kelelahan yang menumpuk bertahun-tahun."
    "Lama kelamaan, tangisnya mereda. Perlahan, dia melangkah mundur dari pagar. Lalu terduduk lemas di lantai balkon."

    jump pilihan_03_budi_from_breakdown

label pilihan_03_budi_from_breakdown:

    show budi exhausted at kiri with dissolve
    b "Gue takut pulang ke kosan, Ran. Gue takut sendirian malam ini."

    jump pilihan_03_budi

label pilihan_03_budi:

    "Budi sudah menjauh dari pagar. Tapi dia masih sangat rapuh. Kondisi ini gawat darurat — ada ancaman nyata terhadap nyawa."

    menu:
        "Langkah berikutnya?"

        "\"Yaudah kalau lu udah agak tenang, balik kosan ya. Besok kita ngobrol lagi.\"":
            jump cabang_03a_budi

        "Tetap menemani Budi dan hubungi Satgas PPKS / keamanan kampus untuk bantuan profesional.":
            jump cabang_03b_budi

        "\"Gue janji nggak bakal kasih tahu siapa-siapa. Yang penting lu janji jangan lakuin ini lagi.\"":
            jump cabang_03c_budi

label cabang_03a_budi:

    $ safe_sound("sfx_wrong.mp3")
    $ renpy.music.stop(channel="music", fadeout=1.0)

    k "Yaudah kalau lu udah agak tenang, lu balik kosan ya. Jangan lupa istirahat, besok kita ngobrol lagi."
    "Budi mengangguk pelan. Dia berdiri, mengambil tasnya, dan berjalan menuju tangga."
    "Kamu menonton punggungnya menghilang di balik pintu."
    "Kamu pulang dengan perasaan lega, merasa sudah melakukan yang terbaik."

    jump bad_end_05c

label cabang_03b_budi:

    $ safe_sound("sfx_correct.mp3")
    $ safe_music("bgm_gentle.mp3")

    "Kamu tidak beranjak dari sisi Budi."
    "Dengan satu tangan yang terus memegang bahunya, kamu perlahan mengeluarkan ponsel dan mengirim pesan ke teman di bawah: \"Lt 5 balkon. Sekarang. Tolong hubungi keamanan kampus.\""
    "Kamu tidak memberi tahu Budi dulu, karena kamu tahu dia butuh merasa aman dulu sebelum menerima bahwa bantuan sedang dalam perjalanan."
    k "Gue di sini, Bud. Gue nggak kemana-mana."

    "Dua puluh menit kemudian, tim dari Klinik Makara dan pihak keamanan kampus tiba."

    show budi held at kiri with dissolve
    "Budi sempat menolak. Tapi kamu tetap ada di sisinya, menjelaskan pelan-pelan bahwa ini bukan pengkhianatan — ini adalah cara kamu menjaganya."
    b "Lu nggak pergi?"
    k "Nggak. Gue nemenin sampai lu aman."
    "Malam itu, Budi mendapatkan penanganan intensif dari tenaga profesional."

    jump good_end_05

label cabang_03c_budi:

    $ safe_sound("sfx_wrong.mp3")
    $ safe_music("bgm_gentle.mp3")

    k "Gue janji nggak bakal kasih tahu siapa-siapa soal malam ini, termasuk orang tua atau dosen lu. Yang penting lu janji ya jangan lakuin ini lagi."
    "Budi mengangguk. Untuk pertama kalinya malam ini, ada sedikit rasa lega di wajahnya."
    "Kamu mengantar Budi pulang ke kosannya. Malam itu dia tidak sendirian."
    "Tapi penanganan profesional tidak pernah datang, karena kamu sudah berjanji untuk merahasiakannya."

    jump neutral_end_05

label bad_end_05a:

    scene bg overlay_hitam with dissolve
    hide budi
    $ safe_sound("sfx_badend.mp3")
    $ renpy.music.stop(channel="music", fadeout=0.5)

    "Bad Ending 05A - Terlalu keras. Terlalu cepat."
    "Budi yang emosinya sedang tidak stabil merasa semakin terancam. Dalam kepanikannya, dia mengambil satu langkah mundur yang fatal."
    "Ambulans kampus datang. Tapi semuanya sudah terlambat."
    "Pesan Edukatif: Pada situasi gawat darurat, tindakan agresif dapat memicu kepanikan instan. Penolong harus tenang, bicara pelan, dan menjaga jarak aman."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari recovery path":
            scene bg balkon_lt5_malam with dissolve
            $ safe_music("bgm_crisis_night.mp3")
            show budi cornered at kiri
            jump recovery_01_budi

        "Kembali ke pilihan skenario":
            jump start

label bad_end_05b:

    scene bg overlay_hitam with dissolve
    hide budi
    $ safe_sound("sfx_badend.mp3")
    $ renpy.music.stop(channel="music", fadeout=0.5)

    "Bad Ending 05B - Dia sudah tidak mau bicara."
    "Budi merasa benar-benar tidak dipahami. Dia menutup matanya."
    "Sebelum kamu sempat berbuat apapun, semuanya sudah berakhir."
    "Pesan Edukatif: Menceramahi atau mengalihkan topik saat krisis bunuh diri membuat mereka merasa semakin terisolasi. Yang dibutuhkan hanya didengar."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari recovery path":
            scene bg balkon_lt5_malam with dissolve
            $ safe_music("bgm_crisis_night.mp3")
            show budi bitter at kiri
            jump recovery_02_budi

        "Kembali ke pilihan skenario":
            jump start

label bad_end_05c:

    scene bg overlay_hitam with dissolve
    hide budi
    $ safe_sound("sfx_badend.mp3")
    $ safe_music("bgm_badend.mp3")

    "Bad Ending 05C - Kamu pikir itu sudah cukup."
    "Keesokan paginya, Fasilkom gempar."
    "Budi ditemukan tidak sadarkan diri di kamar kosnya. Kondisi yang stabil di balkon tadi malam ternyata hanya jeda, bukan akhir dari krisisnya."
    "Pesan Edukatif: Jangan pernah meninggalkan seseorang yang baru melewati krisis bunuh diri sendirian. 'Terlihat lebih tenang' bukan berarti sudah aman."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 03":
            scene bg balkon_lt5_malam with dissolve
            $ safe_music("bgm_gentle.mp3")
            show budi exhausted at kiri
            jump pilihan_03_budi

        "Kembali ke pilihan skenario":
            jump start

label neutral_end_05:

    "Neutral Ending 05 - Janjimu menunda bantuan yang dia butuhkan."
    "Dua hari kemudian, Budi tidak sengaja menenggak obat dosis tinggi dan harus dilarikan ke ICU."
    "Dia selamat, tapi kondisinya memburuk karena penanganan profesional terlambat karena janjimu untuk merahasiakan krisisnya."
    "Pesan Edukatif: Dalam kasus gawat darurat yang mengancam nyawa, prinsip kerahasiaan gugur demi keselamatan korban."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Coba lagi dari pilihan 03":
            scene bg balkon_lt5_malam with dissolve
            $ safe_music("bgm_gentle.mp3")
            show budi exhausted at kiri
            jump pilihan_03_budi

        "Kembali ke pilihan skenario":
            jump start

label good_end_05:

    $ safe_music("bgm_open.mp3")

    hide budi

    "Good Ending 05 - Kamu tidak pergi."
    "Budi tidak langsung sembuh. Pemulihan butuh waktu yang panjang."
    "Tapi malam ini, dia tidak sendirian di tempat yang paling gelap dalam hidupnya, dan itu sudah cukup untuk membuat ada malam esok yang bisa dihadapi."
    "Pesan Edukatif: Tahap Link pada kondisi gawat darurat psikiatri mewajibkan penolong segera merujuk ke fasilitas kesehatan. Menemani, tidak meninggalkan, dan menghubungkan dengan profesional menyelamatkan nyawa."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Mainkan skenario lain":
            jump start

        "Selesai":
            return
