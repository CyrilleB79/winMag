# Windows Büyüteç #

* Yazar: Cyrille Bougot
* NVDA uyumluluğu: 2018.3 ve sonrası
* [kararlı sürümü][1] indir
* [Geliştirme sürümünü][2] indir

Bu eklenti, Windows Büyüteç'in NVDA ile kullanımını geliştirir.


## Özellikler:

* Bazı Varsayılan Büyüteç klavye komutlarının sonucunu bildirmeye izin
  verir.
* Tablo gezinme komutlarının Büyüteç komutlarıyla çakıştığı durumları
  azaltmayı amaçlar.
* Adds some keyboard shortcuts to toggle various native options of the
  Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse
  to view, Magnifier window not on top)

## Ayarlar

Windows Büyüteç eklentisinin ayar paneli, NVDA'nın Varsayılan Windows Büyüteç komutlarına nasıl tepki vereceğini yapılandırmanıza olanak tanır.
Görme düzeğinizegöre daha fazla veya daha az komutun rapor edilmesini isteyebilirsiniz.
Bu panel, NVDA menüsünde Tercihler -> Ayarlar seçilerek ve ardından Ayarlar penceresinde Windows Büyüteç kategorisi seçilerek açılabilir.
NVDA+Windows+O ve ardından O klavye kısayolu da bu ayarlar panelini doğrudan açmaya izin verir.

Panel aşağıdaki seçenekleri içerir:

* görünüm hareketlerini raporla: Görünümü Control+Alt+Oklar komutlarıyla
  hareket ettirdiğinizde nelerin rapor edildiğini kontrol eder. Üç seçenek
  şunlardır:
  
    * Kapalı: Hiçbir şey bildirilmez.
    * Konuşma ile: bir konuşma mesajı, yakınlaştırılan görünümün, görünümün
      taşınmakta olduğu boyuttaki konumunu belirtir.
    * Tonlarla: bir ton çalınır, yükselip alçalan perdesi ile görünümün
      taşınmakta olduğu boyutta yakınlaştırılan görünümün konumunu belirtir.
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the view position: allows to define the
  volume of the tones if you have selected to report view moves or screen
  edges with tones.
* Açma veya Kapatmayı raporla: İşaretlenirse, açmak veya kapatmak için
  Windows++ veya Windows+Escape komutlarını kullandığınızda Büyüteç'in
  durumu bildirilir.
* Yakınlaştırmayı raporla: İşaretlenirse, Windows++ veya Windows+-
  yakınlaştırma komutlarını kullandığınızda Büyüteç'in yakınlaştırma düzeyi
  raporlanır.
* Rengi Ters çevirmeyi raporla: İşaretlenirse, kontrol+Alt+I geçiş komutunu
  kullandığınızda rengi tersine çevirme durumu raporlanır.
* Görünüm değişikliklerini raporla: İşaretlenirse, görünüm türünü değiştiren
  bir komut kullandığınızda görünüm türü raporlanır (Control+Alt+M,
  Control+Alt+F, Control+Alt+D, Control+Alt+L)
* Mercek vey Sabitlenmiş pencere yeniden boyutlandırıldığında raporla:
  İşaretlenirse, yeniden boyutlandırma komutlarını (Alt+Shift+Oklar)
  kullandığınızda bir mesaj bildirilir. Yerleştirilmiş pencere modunda,
  yükseklik veya genişlik bildirilir. Lens modunda, yeni boyut şimdilik
  raporlanamıyor. Bu yeniden boyutlandırma komutu, Windows'un tüm
  sürümlerinde mevcut değil gibi görünüyor; Windows sürümünüz bunları
  desteklemiyorsa, bu seçeneği işaretlememelisiniz.
* Belgelerde ve liste görünümlerinde, control+alt+ok kısayollarını Windows
  Büyüteç'e ilet: Üç kullanılabilir seçenek vardır:
  
    * Never: The command is not passed to Windows Magnifier and standard
      NVDA table navigation can operate.  When used in documents out of a
      table, the Control+Alt+Arrow command reports a "Not in a table" error
      message.  This is the standard behaviour of NVDA without this add-on.
      You can still use NVDA+Windows+O then arrows to move the magnified
      view.
    * Only when not in table: In table or in list views, Control+Alt+Arrow
      commands perform standard table navigation.  When used in documents
      out of a table, Control+Alt+Arrow commands perform standard Magnifier
      view move commands.  If you still want to move Windows Magnifier view
      while in table or in list view, you will need to press NVDA+F2 before
      using Control+Alt+Arrow commands or alternately use NVDA+Windows+O
      then arrows.  This option is the best compromise if you want to use
      Control+Alt+Arrow for both Magnifier and table navigation.
    * Daima: Control+Alt+Ok komutları, her durumda Büyüteç'in görünümünü
      hareket ettirir. Tabloda gezinmek için Control+Alt+Ok kullanmazsanız
      bu seçenek yararlı olabilir. Örneğin: NVDA'da tablo gezinme
      kısayollarını değiştirdiğiniz veya tablo gezinmesi için yalnızca [Easy
      table navigator][5] eklentisini kullandığınız zaman.


## Bu eklenti tarafından eklenen komutlar

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

* NVDA+Windows+O ardından C: İmleç izlemeyi açar veya kapatır.
* NVDA+Windows+O ardından F: Odak izlemeyi açar veya kapatır.
* NVDA+Windows+O ardından M: Fare izlemeyi açar veya kapatır.
* NVDA+Windows+O ardından T: Genel olarak izlemeyi açar veya kapatır.
* NVDA+Windows+O ardından S: yumuşatmayı açar veya kapatır.
* NVDA+Windows+O ardından R: Fare izleme modları arasında geçiş yapar
  (ekranın kenarında veya ekranın ortasında); bu özellik yalnızca Windows 10
  build 17643 veya üzeri sürümlerde mevcuttur.
* NVDA+Windows+O ardından X: Metin imleci izleme modları arasında geçiş
  yapar (ekranın kenarında veya ekranın ortasında); bu özellik yalnızca
  Windows 10 build 18894 veya üzeri sürümlerde mevcuttur.
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command not available in docked view mode).
* NVDA+Windows+O then W: Switches on or off the mode keeping Windows
  Magnifier's control window always on top of the other ones.  This feature
  is only available for installed versions of NVDA.
* NVDA+Windows+O ardından O: Windows Büyüteç eklenti ayarlarını açar.
* NVDA+Windows+O ardından H: Büyüteç katmanı komutlarıyla ilgili yardımı
  görüntüler.

Her komut için varsayılan bir doğrudan hareket yoktur, ancak isterseniz
girdi hareketi iletişim kutusunda normal olarak bir tane
atayabilirsiniz. Aynı şekilde, Büyüteç katmanı erişim hareketini de
değiştirebilir veya silebilirsiniz (NVDA+Windows+O). Ancak Büyüteç katmanı
alt komutlarının kısayol tuşlarını değiştiremezsiniz.


## Büyüteç'in Varsayılan komutları

Aşağıdaki Büyüteç Varsayılan komutlarının sonucu, yapılandırmasına göre bu
eklenti tarafından bildirilebilir:

* Büyüteç'i Başlat: Windows++ (alfa sayısal klavyede veya sayısal tuş
  takımında)
* Büyüteçten Çık: Windows+Escape
* Yakınlaştır: Windows++ (alfa sayısal klavyede veya sayısal tuş takımında)
* Uzaklaştır: Windows+- (alfa sayısal klavyede veya sayısal tuş takımında)
* Rengi ters çevirmeyi aç/kapat: Control+Alt+I
* Sabitlenmiş görünümü seçin: Control+Alt+D
* Tam ekran görünümünü seçin: Control+Alt+F
* Mercek görünümünü seçin: Control+Alt+L
* Üç görünüm türü arasında geçiş yapın: Control+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

Burada ayrıca yalnızca bilgi için diğer Büyüteç varsayılan komutlarının bir
listesi bulunmaktadır:

* Control+Alt+fareKaydırma Tekerleği: Fare kaydırma tekerleğini kullanarak
  yakınlaştırır ve uzaklaştırır.
* Control+Windows+M: Büyüteç ayarları penceresini açar.
* Control+Alt+R: Merceği fare ile yeniden boyutlandırır.
* Control+Alt+Boşluk çubuğu: Tam ekran görünümü kullanılırken tüm masaüstünü
  hızlı bir şekilde gösterir.

Büyüteç Varsayılankomutlarının hiçbiri değiştirilemez.


## Notlar:

* Intel grafik kartı bulunan bilgisayarlar için, kontrol+alt+ok
  (sol/sağ/yukarı/aşağı) da ekranın yönünü değiştirmek için
  kısayollardır. Bu kısayollar varsayılan olarak etkindir ve görünümü
  taşımak için Windows Büyüteç kısayollarıyla çakışır. Bunları Büyüteç ile
  kullanabilmek için devre dışı bırakmanız gerekecek. Intel kontrol
  panelinden veya sistem tepsisinde bulunan Intel menüsünden devre dışı
  bırakılabilirler.
* Windows sürümünüze bağlı olarak Alt+Shift+Ok, büyütülmüş görünümü (mercek
  veya sabitlenmiş) yeniden boyutlandırmak için kullanılan Windows Büyüteç
  kısayollarıdır. Büyüteç etkinken (tam ekran modunda bile), bu kısayollar
  Büyüteç tarafından yakalanır ve daha önce NVDA+F2'ye bassanız bile
  uygulamaya aktarılamaz. Mevcut uygulamada bu kısayolları kullanmak için
  Büyüteç'ten (Windows+Escape) çıkmanız ve sonra (Windows++) yeniden açmanız
  gerekir. Örneğin, MS word'de başlık seviyesini azaltmak için:
  
    * Büyüteç'ten çıkmak için Windows+Escape tuşlarına basın.
    * Mevcut başlık düzeyini azaltmak için Alt+Shift+Sağ Ok tuşlarına basın.
    * Büyüteç'i yeniden açmak için Windows++ tuşuna basın.

* Windows Büyüteç'in özellikleri ve kısayolları hakkında daha fazla bilgi
  için aşağıdaki sayfalara bakmak isteyebilirsiniz:

    * [Ekrandaki ögelerin daha kolay görülmesini sağlamak için Büyüteç'i
      kullanın](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Erişilebilirlik için Windows klavye kısayolları][4]

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## Sürüm Geçmişi:

### Version 2.0

* The view can be moved with arrows while in Windows Magnifier layer.
* Capability to keep the Magnifier commands Window always on top or not.
* Added "Report screen edges" feature.
* Volume setting of tones when using move view commands.
* Reporting view moves and mouse to view commands are now supported in Lens
  mode.
* Compatibility with NVDA 2022.1.
* Fixed a bug that sometimes incorrectly reported that the Magnifier was not
  working upon script call.
* The release is now performed thanks to a GitHub action instead of
  appVeyor.
* Updated localizations.

### Version 1.1

* Added localizations.

### Sürüm 1.0

* İlk sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html
