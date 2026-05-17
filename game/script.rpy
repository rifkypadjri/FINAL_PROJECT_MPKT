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
image bg overlay_merah = Solid("#5a1010")

image andi sad = Text("Andi - sad", size=44, color="#ffffff")
image andi defensive = Text("Andi - defensive", size=44, color="#ffffff")
image andi cry = Text("Andi - cry", size=44, color="#ffffff")
image andi surprised = Text("Andi - surprised", size=44, color="#ffffff")
image andi normal = Text("Andi - normal", size=44, color="#ffffff")

image laras sad = Text("Laras - sad", size=44, color="#ffffff")
image laras shocked = Text("Laras - shocked", size=44, color="#ffffff")
image laras tense = Text("Laras - tense", size=44, color="#ffffff")
image laras open = Text("Laras - open", size=44, color="#ffffff")
image laras relieved = Text("Laras - relieved", size=44, color="#ffffff")
image laras alarmed = Text("Laras - alarmed", size=44, color="#ffffff")
image laras guilty = Text("Laras - guilty", size=44, color="#ffffff")
image laras flat = Text("Laras - flat", size=44, color="#ffffff")

transform kiri:
    xalign 0.2
    yalign 0.8

define k = Character("Kiran", color="#9ad7ff")
define a = Character("Andi", color="#ffd08a")
define l = Character("Laras", color="#d6b2ff")

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
