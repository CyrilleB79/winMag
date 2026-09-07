# Windows Büyüteç

* Yazar: Cyrille Bougot
* NVDA uyumluluğu: 2019.3 ve sonrası

Bu eklenti, Windows Büyüteç'in NVDA ile kullanımını geliştirir.


## Özellikler

* Bazı dahili Büyüteç ve renk filtreleme klavye komutlarının sonucunu duyurmaya izin verir.
* Tablo dolaşım komutlarının Büyüteç komutlarıyla çakıştığı durumları azaltmayı amaçlar.
* Büyüteç'in çeşitli yerel seçeneklerini değiştirmek için bazı klavye kısayolları ekler.
* Büyüteç yapılandırma parametrelerini kaydetmeye ve geri yüklemeye izin verir.
* Windows Büyüteç tarafından sağlanmayan bazı ek özellikler ekler (görüntülemek için fare, Büyüteç penceresi üstte değil)

## Ayarlar

Windows Büyüteç eklentisinin ayar paneli, NVDA'nın yerel Windows Büyüteç komutlarına nasıl tepki vereceğini yapılandırmanıza olanak tanır.
Görebildiklerinize bağlı olarak daha fazla veya daha az komutun bildirilmesini isteyebilirsiniz.
Panel ayrıca Windows Büyüteç kontrol penceresinin davranışını değiştirme seçeneğini de içerir.

Bu panel, NVDA menüsünde Tercihler -> Ayarlar seçilerek ve ardından Ayarlar penceresinde Windows Büyüteç kategorisi seçilerek açılabilir.
NVDA+Windows+O ve ardından O klavye kısayolu da bu ayarlar panelinin doğrudan açılmasına izin verir.

Panel aşağıdaki seçenekleri içerir:

* Görünüm hareketlerini bildir: Görünümü Control+Alt+Oklar komutlarıyla hareket ettirdiğinizde nelerin bildirildiğini kontrol eder. Üç seçenek şunlardır:
  
    * Kapalı: Hiçbir şey bildirilmez.
    * Konuşarak: bir konuşma mesajı, yakınlaştırılan görünümün, görünümün taşınmakta olduğu boyuttaki konumunu belirtir.
    * Bip sesi ile: bir ton çalınır, yükselip alçalan perdesi ile görünümün taşınmakta olduğu boyutta yakınlaştırılan görünümün konumunu belirtir.
  
  Bu seçenek, sabitlenmiş görünüm modunu etkilemez.

* Ekran kenarlarını bildir: Control+Alt+Ok tuşlarıyla görünümü hareket ettirirken ekranın kenarlarına ulaştığınızda neyin bildirileceğini kontrol eder. Üç seçenek vardır: Kapalı, Konuşma ile ve Ton ile. Bu seçenek sabitlenmiş görünüm modunu etkilemez.
  Üç seçenek şunlardır: Kapalı, Konuşma ile ve Sesli.
  Bu seçenek sabitlenmiş görünüm modunu etkilemez.
* Görünümün konumunu bildiren tonların ses seviyesi: görünüm hareketlerini veya ekran kenarlarını tonlarla bildirmeyi seçtiyseniz tonların ses seviyesini ayarlamayaa olanak tanır.
* Bildirimleri aç veya kapat:
  İşaretlendiğinde, Windows++ veya Windows+Escape komutlarını kullanarak Büyüteci açıp kapattığınızda Büyütecin durumu bildirilir.
* Yakınlaştırmayı Bildir:
  İşaretlendiğinde, Windows++ veya Windows+- yakınlaştırma komutlarını kullandığınızda Büyüteç'in yakınlaştırma seviyesi bildirilir.
* Rengi Ters çevirmeyi bildir:
  İşaretlendiğinde, Control+Alt+I tuşlarını kullanarak renk ters çevirme durumu bildirilir.
* Görünüm değişikliklerini Bildir:
  İşaretlendiğinde, görünüm türünü değiştiren bir komut kullandığınızda (Control+Alt+M, Control+Alt+F, Control+Alt+D, Control+Alt+L) görünüm türü bildirilir.
* Mercek veya sabitlenmiş pencere yeniden boyutlandırmayı bildirir:
  İşaretlendiğinde, yeniden boyutlandırma komutlarını (Alt+Shift+Ok tuşları) kullandığınızda bir mesaj görüntülenir.
  Sabitlenmiş pencere modunda, yükseklik veya genişlik bildirilir.
  Lens modunda, yeni boyut şimdilik bildirilemez.
  Bu yeniden boyutlandırma komutları tüm Windows sürümlerinde mevcut görünmüyor; Windows sürümünüz bunları desteklemiyorsa, bu seçeneği işaretlememelisiniz.
* Belgelerde ve liste görünümlerinde, Ctrl+Alt+Ok tuşları kısayollarını Windows Büyüteç'e ilet:
  There are three possible choices:
  
    * Asla: Komut, Windows Büyüteç'e iletilmez ve standart NVDA tablo Dolaşımı çalışabilir.
      Tablo dışındaki belgelerde kullanıldığında, Control+Alt+Ok tuşları “Tablo içinde değil” hata mesajını bildirir.
      Bu, NVDA'nın bu eklenti olmadan standart davranışıdır.
      NVDA+Windows+O tuşlarını ve ok tuşlarını kullanarak büyütülmüş görüntüyü hareket ettirebilirsiniz.
    * Yalnızca tabloda olmadığında: Tablo veya liste görünümlerinde, Control+Alt+Ok tuşları standart tabloda dolaşma gerçekleştirir.
      Tablo dışındaki belgelerde kullanıldığında, Control+Alt+Ok tuşları standart Büyüteç görünümü hareket komutlarını gerçekleştirir.
      Tablo veya liste görünümündeyken Windows Büyüteç görünümünü hala taşımak istiyorsanız, Control+Alt+Ok tuşlarını kullanmadan önce NVDA+F2 tuşlarına basmanız veya dönüşümlü olarak NVDA+Windows+O ve ardından okları kullanmanız gerekecektir.
      Hem Büyüteç hem de tabloda dolaşım için Control+Alt+Ok tuşlarını kullanmak istiyorsanız bu seçenek en iyi uzlaşmadır.
    * Daima: Control+Alt+Ok tuşları, her durumda Büyüteç'in görünümünü hareket ettirir.
      Bu seçenek, tablo içinde dolaşım için Control+Alt+Ok tuşlarını kullanmıyorsanız yararlı olabilir. Örneğin, NVDA'da tablo dolaşım kısayollarını değiştirdiyseniz veya tablo dolaşımı için yalnızca [Easy table navigator][5] eklentisini kullanıyorsanız.

* Windows Büyüteç komut penceresini her zaman üstte tut:
  İşaretlenmezse, Büyüteç'in kontrol penceresi diğer pencerelerin üzerinde her zaman üstte kalmaz.
* Renk filtresini bildir
  İşaretlendiğinde, `Windows+Control+C` geçiş komutunu kullandığınızda kullanılan renk filtresi bildirilir.

## Bu eklenti tarafından eklenen komutlar

Bu eklenti, yerel Büyüteç komutlarına ek olarak ek komutlar sağlar:

* Yapılandırma sayfasını açmadan Büyüteç'in seçeneklerini kontrol etmeyi sağlayan komutlar.
* Bu eklentiye özel ek komutlar.

Tüm bu ek komutlara Büyüteç katmanı komutu NVDA+Windows+O aracılığıyla erişilebilir:

* NVDA+Windows+O ardından C: İmleç izlemeyi açar veya kapatır.
* NVDA+Windows+O ardından F: Odak izlemeyi açar veya kapatır.
* NVDA+Windows+O ardından M: Fare izlemeyi açar veya kapatır.
* NVDA+Windows+O sonra T: Genel olarak izlemeyi açar veya kapatır. İzleme tekrar açıldığında, izleme kapatılmadan önceki son etkin izleme yapılandırmasına ayarlanır.
  İzleme tekrar açıldığında, izleme kapatılmadan önceki son aktif izleme yapılandırmasına ayarlanır.
* NVDA+Windows+O ardından S: yumuşatmayı açar veya kapatır.
* NVDA+Windows+O ardından R: Fare işaretçisi izleme modları arasında geçiş yapar (ekranın kenarı içinde veya ekranın ortasında); bu özellik yalnızca Windows 10 derleme 17643 veya üzeri sürümlerde mevcuttur.
* NVDA+Windows+O ardından X: Metin imleci izleme modları arasında geçiş yapar (ekranın kenarında veya ekranın ortasında); bu özellik yalnızca Windows 10 build 18894 veya üzeri sürümlerde mevcuttur.
* NVDA+Windows+O ve ardından shift+P: Büyüteçteki geçerli yapılandırma parametrelerini NVDA'nın yapılandırmasına kaydeder.
* NVDA+Windows+O ardından P: Büyütecin geçerli yapılandırma parametrelerini NVDA'nın yapılandırmasından geri yükler.
  NVDA'nın yapılandırmasına önceden hiçbir yapılandırma parametresi kaydedilmemişse, bunun yerine Windows Büyüteç'in varsayılan yapılandırma parametreleri geri yüklenir.
* NVDA+Windows+O ve ardından Oklar: Büyütülmüş görünümü hareket ettirir.
* NVDA+Windows+O ardından V: Fare imlecini büyütülmüş görünümün ortasına taşır (komut yalnızca tam ekran görünümünde kullanılabilir).
* NVDA+Windows+O ve W: Windows Büyüteç'in kontrol penceresinin her zaman diğer pencerelerin üstünde tutulmasına izin veren modu açar veya kapatır. Bu özellik yalnızca kurulu NVDA sürümleri için mevcuttur.
  Bu özellik yalnızca NVDA'nın yüklü sürümlerinde kullanılabilir.
* NVDA+Windows+O ardından O: Windows Büyüteç eklenti ayarlarını açar.
* NVDA+Windows+O ardından H: Büyüteç katmanı komutlarıyla ilgili yardımı görüntüler.

Her komut için varsayılan bir doğrudan hareket yoktur, ancak isterseniz girdi hareketi iletişim kutusunda normal olarak bir tane atayabilirsiniz.Her komut için varsayılan bir doğrudan hareket yoktur, ancak isterseniz girdi hareketi iletişim kutusunda normal bir hareket belirleyebilirsiniz.
Aynı şekilde, Büyüteç katmanı erişim hareketini (NVDA+Windows+O) de değiştirebilir veya silebilirsiniz.
Ancak, Büyüteç katmanı alt komutlarının kısayol tuşunu değiştiremezsiniz.


## Büyüteç'in yerel komutları

Aşağıdaki Büyüteç yerel komutlarının veya diğer Erişilebilirlik komutlarının sonucu, yapılandırmasına göre bu eklenti tarafından bildirilebilir:

* Büyüteç'i Başlat: Windows++ (alfa sayısal klavyede veya sayısal tuş takımında)
* Büyüteç'ten çık: Windows+Escape
* Yakınlaştır: Windows++ (alfa-sayısal klavyede veya sayısal tuş takımında)
* Uzaklaştır: Windows+- (alfa sayısal klavyede veya sayısal tuş takımında)
* Ayarlanan büyütme seviyesi ile 1x büyütme arasında geçiş yapın: `control+alt+-' (alfa sayısal klavyede veya sayısal tuş takımında)
* Renkleri Ters Çevir açık/kapalı: Ctrl+Alt+I
* Sabitlenmiş görünümü seçin: Control+Alt+D
* Tam ekran görünümünü seçin: Control+Alt+F
* Mercek görünümünü seçin: Control+Alt+L
* Üç görünüm türü arasında geçiş yapar: Control+Alt+M
* Merceği klavyeyle yeniden boyutlandırın: Shift+Alt+Sol/Sağ/Yukarı/AşağıOk
  Not: Bu durum belgelenmiş gibi görünmese de, bu kısayol Windows 10 2004 gibi son Windows sürümlerinde kaldırılmış gibi görünüyor.
* Büyütülmüş görünümü taşıma: Control+Alt+Oklar
* Renk filtrelerini değiştir: "Windows+Kontrol+C" (bu kısayolu [Windows Erişilebilirlik ayarları, Renk Filtreleri] [9]'de etkinleştirmiş olmanız şartıyla)

Bilgi amaçlı olarak diğer Büyüteç yerel komutlarının bir listesini de burada bulabilirsiniz:

* Kontrol+Alt+fareKaydırma Tekerleği: Fare kaydırma tekerleğini kullanarak yakınlaştırır ve uzaklaştırır.
* Kontrol+Windows+M: Büyüteç ayarları penceresini açar.
* Kontrol+Alt+R: Merceği fare ile yeniden boyutlandırır.
* Kontrol+Alt+Aralık: Tam ekran görünümü kullanılırken tüm masaüstünü hızlı bir şekilde gösterir.

Büyüteç yerel komutlarının hiçbiri değiştirilemez.


## Notlar

* Intel grafik kartına sahip bilgisayarlar için, kontrol+alt+ok (sol/sağ/yukarı/aşağı) aynı zamanda ekranın yönünü değiştirmeye yönelik kısayollardır.
  Bu kısayollar varsayılan olarak etkindir ve görünümü taşımak için Windows Büyüteç kısayollarıyla çakışır.
  Büyüteçte kullanabilmek için bunları devre dışı bırakmanız gerekecektir.
  Bunlar Intel kontrol panelinden veya sistem tepsisinde bulunan Intel menüsünden devre dışı bırakılabilir.
* Windows sürümünüze bağlı olarak, Alt+Shift+Ok tuşları, büyütülmüş görünümü (mercek veya kenara sabitlenmiş) yeniden boyutlandırmak için kullanılan Windows Büyüteç kısayollarıdır.
  Büyüteç etkin olduğunda (tam ekran modunda bile), bu kısayollar Büyüteç tarafından yakalanır ve önceden NVDA+F2 tuşlarına basmış olsanız bile uygulamaya aktarılamaz.
  Bu kısayolları mevcut uygulamada kullanmak için, Büyüteç'i kapatmanız (Windows+Escape) ve ardından yeniden açmanız (Windows++) gerekir.
  Örneğin MS Word'de başlık seviyesini düşürmek için:
  
    * Büyüteç'ten çıkmak için Windows+Escape tuşlarına basın.
    * Mevcut başlık seviyesini azaltmak için Alt+Shift+Sağ Ok tuşlarına basın.
    * Büyüteç'i yeniden açmak için Windows++ tuşuna basın.

* Windows Büyüteç'in özellikleri ve kısayolları hakkında daha fazla bilgi için aşağıdaki sayfalara bakmak isteyebilirsiniz:

    * [Ekrandaki ögelerin daha kolay görülmesini sağlamak için Büyüteç'i kullanın](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Erişilebilirlik için Windows klavye kısayolları][4]

* Bu eklenti çoklu ekran ortamında test edilmemiştir ve bazı özelliklerin bu ortamda çalışmama ihtimali vardır.
  Çoklu ekran ortamı kullanıyorsanız ve bunun desteklenmesini istiyorsanız, lütfen benimle iletişime geçin.
* Daha genel olarak, bu eklentinin [GitHub sayfası] [3] üzerinden veya doğrudan e-posta yoluyla benimle iletişime geçmekten çekinmeyin.


## Sürüm Geçmişi

### Sürüm 4.4

* Eklenti artık NVDA 2026.1 ile uyumlu.
* Eklenti artık NVDA 2019.2.1 ile uyumlu değil: Yalnızca NVDA 2019.3 ve sonraki sürümlerle uyumlu.
  NVDA 2019.2.1 ile uyumlu son sürüm [4.3][10]'dur.

### Sürüm 4.3

* Ayarlanan büyütme seviyesi ile 1x büyütme arasında geçiş yapmayı sağlayan yeni büyüteç komutu destekleniyor.
* NVDA 2026.1 ile uyumluluğu hazırlar.

### Sürüm 4.2

* Büyüteç veya Renk filtreleme komutları, bu eklenti çalışırken ilk kez kullanıldığında artık başarısız olmayacaktır.

### Sürüm 4.0

* Renk filtresini değiştir komutu (`Windows+Control+C`) tarafından etkinleştirilen filtre artık duyurulabilir; bu değiştirme komutunun daha önce Windows Erişilebilirlik ayarlarında etkinleştirilmiş olması gerekir.
* NVDA 2025.1 ile uyumlu.

### Sürüm 3.7

* NVDA 2024.1 ile uyumlu.

### Sürüm 3.6

* Hatalı uyumluluk aralığı düzeltildi.

### Sürüm 3.5

* NVDA 2024.1 ile uyumluluğu hazırlar.
* Eklentiyi NVDA'nın eski sürümleriyle kullanırken [GHSA-xg6w-23rw-39r8][8] ile ilgili olası güvenlik sorunlarını giderir. Ancak NVDA 2023.3.3 veya üzerini kullanmanız tavsiye edilir.
* Not: Artık çeviri güncellemeleri değişiklik günlüğünde görünmeyecek.

### Sürüm 3.4

* "Görüntülemek için fareyi hareket ettirin" komutu yeniden çalışıyor
* Yerelleştirmeler güncellendi.

### Sürüm 3.3

* Uyumluluk NVDA 2019.2.1 ve sonraki sürümlere düşürüldü.
  NVDA 2018.3 ile son uyumlu sürümler [3.2] [7] (kısmen uyumlu) ve [1.1] [6] (tamamen uyumlu)
* NVDA 2019.2.1'in ayarlar panelindeki bir hata düzeltildi.

### Sürüm 3.2

* Geliştirici kanalı kaldırıldı.
* Yerelleştirmeler güncellendi.

### Sürüm 3.1

* Büyüteç'in komut penceresinin en üste geri yüklenmesini engelleyen bir sorun düzeltildi.
* Eklentinin NVDA 2019.2.1'de çalışmasını engelleyen sorun düzeltildi.
* Yerelleştirmeler güncellendi.

### Sürüm 3.0

* Büyüteç penceresinde (klavye ile) yakınlaştırma düğmelerine basmak artık yeni yakınlaştırma seviyesini bildiriyor.
* Büyüteç kontrol penceresinin her zaman üstte kalıp kalmayacağını kontrol eden parametre artık yapılandırmada saklanıyor;Büyüteç kontrol penceresinin her zaman üstte kalıp kalmayacağını kontrol eden parametre artık yapılandırmada saklanıyor;
  Bu, NVDA yeniden başlatıldığında bu parametrenin hatırlandığı ve etkin profile bağlı olarak etkinleştirilebileceği veya etkinleştirilemeyeceği anlamına gelir.
* Görünüme taşı veya görünümü taşı komutlarını kullanırken ekran perdesinin beklenmedik şekilde devre dışı bırakılmasına neden olan bir hata düzeltildi.
* Her zaman Üstte seçeneği ayarı artık büyütme modu değiştirilirken de dikkate alınacaktır.
* Windows Büyüteç'in yapılandırmasını NVDA'nın yapılandırmasına kaydetme ve geri yükleme yeteneği eklendi.
* NVDA 2023.1 ile uyumlu.
* İzleme tekrar açıldığında hangi izleme türünün yeniden etkinleştirileceğini netleştirin.
* Yerelleştirmeler güncellendi.

### Sürüm 2.0

* Görünüm, Windows Büyüteç katmanındayken oklarla taşınabilir.
* Büyüteç komutları Penceresini her zaman üstte tutma veya tutmama özelliği.
* "Ekran kenarlarını bildir" özelliği eklendi.
* Hareketli görünüm komutlarını kullanırken tonların ses seviyesi ayarı.
* Görünüm hareketlerini bildirmek ve görüntülemek için fare komutları artık Mercek modunda desteklenmektedir.
* NVDA 2022.1 ile uyumlu.
* Kod çağrıldığında Büyüteç'in çalışmadığını bazen yanlış bildiren bir hata düzeltildi.
* Sürüm artık appVeyor yerine bir GitHub eylemi sayesinde gerçekleştiriliyor.
* Yerelleştirmeler güncellendi.

### Sürüm 1.1

* Yerelleştirmeler eklendi.

### Sürüm 1.0

* İlk sürüm.

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/en-us/help/13810

[6]: https://github.com/CyrilleB79/winMag/releases/download/V1.1/winMag-1.1.nvda-addon

[7]: https://github.com/CyrilleB79/winMag/releases/download/V3.2/winMag-3.2.nvda-addon

[8]: https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994

[9]: https://support.microsoft.com/en-us/windows/make-windows-easier-to-see-c97c2b0d-cadb-93f0-5fd1-59ccfe19345d

[10]: https://github.com/CyrilleB79/winMag/releases/download/V4.3/winMag-4.3.nvda-addon
