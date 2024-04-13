HELP_1 = """<b><u>ADMİN KOMUTLARI :</b></u>

Kanal için kullanmak üzere komutların başına <b>/c</b> eklemeniz yeterlidir.


/pause : Çalan akışı duraklatır.

/resume : Duraklatılmış akışı devam ettirir.

/skip : Şu anda çalan akışı atlar ve sıradaki parçayı çalmaya başlar.

/end veya /stop : Kuyruğu temizler ve şu anda çalan akışı sonlandırır.

/player : Etkileşimli bir çalıcı paneli alırsınız.

/queue : Kuyrukta bekleyen parçaların listesini gösterir.
"""

HELP_2 = """
<b><u>YETKİLİ KULLANICILAR :</b></u>

Yetkili kullanıcılar, sohbette yönetici hakları olmadan botu kullanabilirler.

/auth [kullanıcı adı/kullanıcı ID] : Botun yetkilendirme listesine bir kullanıcı ekler.

/unauth [kullanıcı adı/kullanıcı ID] : Bir kullanıcıyı yetkilendirme listesinden kaldırır.

/authusers : Grubun yetkili kullanıcılarının listesini gösterir.
"""

HELP_3 = """
<u><b>YAYIN KOMUTLARI</b></u> [Herkes Kullanamaz] :

/broadcast [mesaj veya bir mesaja cevap] : Botun sunucu sohbetlerine bir mesajı yayınlamasını sağlar.

<u>BROADCASTING MODES:</u>
<b>-pin</b> : Yayınlanan mesajlarınızı sunucu sohbetlerinde sabitler.
<b>-pinloud</b> : Yayınlanan mesajınızı sunucu sohbetlerinde sabitler ve üyelere bildirim gönderir.
<b>-user</b> : Mesajı botunuzu başlatan kullanıcılara yayınlar.
<b>-assistant</b> : Mesajınızı botun asistan hesabından yayınlar.
<b>-nobot</b> : Botun mesajı yayınlamamasını zorlar.

<b>ÖRNEK:</b> <code>/broadcast -user -assistant -pin test ediliyor yayını</code>
"""

HELP_4 = """<u><b>GRUBU KARALİSTEYE ALMAK:</b></u> [Herkes Kullanamaz]

Değerli botumuzu kullanarak saçma sohbetleri sınırlayın.

/blacklistchat [sohbet ID] : Bot kullanarak bir sohbeti engeller.
/whitelistchat [sohbet ID] : Engellenen sohbeti beyaz listeye alır.
/blacklistedchat : Engellenen sohbetlerin listesini gösterir.
"""

HELP_5 = """
<u><b>KULLANICI ENGELLEME:</b></u> [Herkes Kullanamaz]

Engellenen kullanıcıları yok sayarak bot komutlarını kullanmalarını engeller.

/block [kullanıcı adı veya bir kullanıcıya cevap] : Kullanıcıyı botumuzdan engeller.
/unblock [kullanıcı adı veya bir kullanıcıya cevap] : Engellenen kullanıcının engelini kaldırır.
/blockedusers : Engellenen kullanıcıların listesini gösterir.
"""

HELP_6 = """
<u><b>KANAL OYNATMA KOMUTLARI:</b></u>

Kanalda ses/video akışı yapabilirsiniz.

/cplay : Kanalın video sohbetinde istenen ses parçasını çalmaya başlar.
/cvplay : Kanalın video sohbetinde istenen video parçasını çalmaya başlar.
/cplayforce veya /cvplayforce : Devam eden akışı durdurur ve istenen parçayı çalmaya başlar.

/channelplay [sohbet kullanıcı adı veya ID] veya [disable] : Kanalı bir gruba bağlar ve grup tarafından gönderilen komutlarla parçaları çalmaya başlar.
"""

HELP_7 = """
<u><b>GLOBAL BAN ÖZELLİĞİ</b></u> [Herkes Kullanamaz] :

/gban [kullanıcı adı veya bir kullanıcıya cevap] : Küfürbazı tüm sunucu sohbetlerinden ve botu kullanarak onu engeller.
/ungban [kullanıcı adı veya bir kullanıcıya cevap] : Küfürbazın global olarak engelini kaldırır.
/gbannedusers : Global olarak engellenen kullanıcıların listesini gösterir.
"""

HELP_8 = """
<b><u>LOOP STREAM :</b></u>

<b>Aktif parçayı/şarkıyı veya yayını döngüde başlatır</b>

/loop [enable/disable] : Devam eden akışı döngüye alır/devre dışı bırakır.
/loop [1, 2, 3, ...] : Belirtilen değer için döngüyü etkinleştirir.
"""

HELP_9 = """
<u><b>BAKIM MODU</b></u> [Yalnızca sudoerlar için] :

/logs : Botun günlüklerini alır.

/logger [enable/disable] : Botun etkinliklerini günlüğe kaydetmeye başlar/devre dışı bırakır.

/maintenance [enable/disable] : Botun bakım modunu etkinleştirir/devre dışı bırakır.
"""

HELP_10 = """
<b><u>PING & STATSLAR :</b></u>

/start : Müzik botunu başlatır.
/help : Komutların açıklamalarıyla bir yardım menüsü alırsınız.

/ping : Botun pingini ve sistem istatistiklerini gösterir.

/stats : Botun genel istatistiklerini gösterir.
"""

HELP_11 = """
<u><b>PLAY KOMUTLARI :</b></u>

<b>v :</b> Video oynatma için kullanılır.
<b>force :</b> Zorla oynatma için kullanılır.

/play veya /vplay : Video sohbetinde istenen parçayı çalmaya başlar.

/playforce veya /vplayforce : Devam eden akışı durdurur ve istenen parçayı çalmaya başlar.
"""

```python
HELP_12 = """
<b><u>KARIŞTIRMA KUYRUK :</b></u>

/shuffle : Kuyruğu karıştırır.
/queue : Karıştırılmış kuyruğu gösterir.
"""

HELP_13 = """
<b><u>AKIŞI İLERİ SARMAYA YARAYAN KOMUTLAR :</b></u>

/seek [saniye cinsinden süre] : Akışı verilen süreye ileri sarmak için kullanılır.
/seekback [saniye cinsinden süre] : Akışı verilen süreye geri sarmak için kullanılır.
"""

HELP_14 = """
<b><u>ŞARKI İNDİRME</b></u>

/song [şarkı adı/yt url] : YouTube'dan herhangi bir parçayı MP3 veya MP4 formatında indirir.
"""

HELP_15 = """
<b><u>HIZ KOMUTLARI :</b></u>

Devam eden akışın oynatma hızını kontrol edebilirsiniz. [Yalnızca yöneticiler için]

/speed veya /playback : Grubun sesli oynatma hızını ayarlamak için.
/cspeed veya /cplayback : Kanalın sesli oynatma hızını ayarlamak için.
"""
