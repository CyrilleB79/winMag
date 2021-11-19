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
* Çeşitli Büyüteç seçenekleri arasında geçiş yapmak için bazı klavye
  kısayolları ekler.


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
  
Bu seçenek yalnızca tam görünüm modunu etkiler.
  
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
  
    * Asla: Komut Windows Büyüteç'e iletilmez ve standart NVDA tablo
      navigasyonu çalışabilir. Bir tablonun dışındaki belgelerde
      kullanıldığında, Control+Alt+Ok komutu bir "Tabloda değil" hata mesajı
      verir. Bu, eklenti olmadan NVDA'nın standart davranışıdır.
    * Yalnızca tabloda olmadığında: Tablo veya liste görünümlerinde,
      Control+Alt+Ok komutları standart tabloda gezinme gerçekleştirir. Bir
      tablonun dışındaki belgelerde kullanıldığında, Control+Alt+Ok
      komutları standart Büyüteç görünümü taşıma komutlarını
      gerçekleştirir. Tablo veya liste görünümündeyken Windows Büyüteç
      görünümünü yine de taşımak istiyorsanız, Control+Alt+Ok komutlarını
      kullanmadan önce NVDA+F2 tuşlarına basmanız gerekir. Hem Büyüteç hem
      de tabloda gezinme için Control+Alt+Ok kullanmak istiyorsanız bu
      seçenek en iyi yoldur.
    * Daima: Control+Alt+Ok komutları, her durumda Büyüteç'in görünümünü
      hareket ettirir. Tabloda gezinmek için Control+Alt+Ok kullanmazsanız
      bu seçenek yararlı olabilir. Örneğin: NVDA'da tablo gezinme
      kısayollarını değiştirdiğiniz veya tablo gezinmesi için yalnızca [Easy
      table navigator][5] eklentisini kullandığınız zaman.


## Bu eklenti tarafından eklenen komutlar

Varsayılan Büyüteç komutlarına ek olarak, bu eklenti, Büyüteç'in
seçeneklerini yapılandırma sayfasını açmadan kontrol etmeye olanak tanıyan
ek komutlar sağlar. Büyüteç seçeneklerini kontrol etmek için eklenen tüm
komutlara Büyüteç katman komutu olan NVDA+Windows+O aracılığıyla
erişilebilir:

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
* NVDA+Windows+O ardından V: Fare imlecini büyütülmüş görünümün ortasına
  taşır (komut yalnızca tam ekran görünümünde kullanılabilir).
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
* Merceği klavyeyle yeniden boyutlandırın: Shift+Alt+Sol/Sağ/Yukarı/Aşağı
  Ok. Not: Bu belgelenmiş gibi görünmese de, bu kısayol, Windows 2004 gibi
  son Windows sürümlerinde geri çekilmiş gibi görünüyor.
* Büyütülmüş görünümü hareket ettirin: Control+Alt+Oklar (raporlama yalnızca
  tam ekran modunu etkiler)

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


## Sürüm Geçmişi:

### Sürüm 1.0

* İlk sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html
