# -7-hills-istanbul-metro-network
## Proje başlığı:
**Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)** <br/>
## Proje detayı:
Bu proje de bir şehrin metro ağındaki İki istasyon arasındaki en hızlı ve En az aktarmalı rotayı bulan bir simülasyon yapılmıştır. 
Projede BFS (Breadth-First Search) algoritması (en az aktarmalı rotayı bulma) ile A* algoritması (en hızlı rotayı bulma) algoritmaları kullanılmıştır <br/>

Proje için İstanbul şehri seçilmiştir. metro ağı detayları için metro istanbul web sitesinden gerekli bilgiler alınmıştır. Projede tüm meetro ağına yer verilmemiş olup sadece M1A,M1B,M2,M3,M4 ve tramvay açısından T1 hattına yer verilmiştir.  

Proje için 8 adet test senaryosu ele alınmıştır. 

## Proje içeriği:
#### Projede yer verilen İstanbul metro hatları:<br/>
1. M1A <br/>
2. M1B<br/>
3. M2 <br/>
3. M3 <br/>
4. M4 <br/>
5. T1( TRAMVAY HATTI) <br/>

#### Projede kullanılan özel algoritmalar:<br/>
1.Graf veri yapısı <br/>
2. BFS <br/>
3. A*<br/>

#### Algoritma çalışma mantığı:<br/>
**1. Garf veri yapısı :** <br/>
 düğümler (nodes) ve bu düğümler arasındaki bağlantılardan oluşan bir veri yapısıdır. <br/>
 
 Kullanım alanları: <br/>
 
• Sosyal Ağlar <br/>

•	Yol ve Ulaşım Sistemleri <br/>

•	Yapay Zeka ve Makine Öğrenmesi <br/>

Graf veri yapısı BFS, DFS, Dijkstra ve A* gibi vb. algoritmalarla birlikte kullanılır.<br/>


**2. BFS algoritması :** <br/>
Bir graf veya ağaç veri yapısında bir başlangıç noktasından (kök) başlayarak tüm düğümleri sistematik olarak ziyaret eden daha sonra komşu düğümleri ziyaret eden bir arama algoritmasıdır. Amacı, başlangıç noktasından diğer tüm düğümlere olan en kısa yolları bulmaktır <br/> Kullanım alanları: En Kısa Yol Bulma , Oyun Programlama , Web Tarama <br/>

**Çalışma Prensibi**: <br/>
![image](https://github.com/user-attachments/assets/3f73656c-a69a-422c-a0ac-743f27c2cd76) <br/>
İlk olark A düğümünden ele alıyoruz ( A düğümünü seçtik eğer istersek farklı bir düğümden de başlayabiliriz). yapılan tablo da eklenen ile output aynıdır yani eklenen = output'dur. <br/>

**1.Adım:** A düğümü eklenir çıkan yok ( başlangıç olarak A düğümünü seçtik) <br/>

**2.Adım:** A ‘nın komşusuna bakıyoruz B ve C düğümleri ekleniyor. İlk giren ilk çıkar koşuluyla A düğümü çıkıyor. <br/>

**3.Adım:** B düğümünün komşusuna bakıyoruz. F düğümü var. O zaman eklenen kısmına F düğümü yazılır. Çıkan kısmına ise B düğümü yazılır. <br/>

**4.Adım:** C düğümünün komşusuna bakıyoruz. E ve D düğümü var. O zaman eklenen kısma  E ve D düğümü yazılır. Çıkan ise C düğümü <br/>

**5.Adım:** F düğümünün komşusuna bakıyoruz. Komşusu yok. O zaman eklenen yok çıkan ise F düğümü <br/>

**6.Adım:** E düğümünün komşusuna bakıyoruz Komşusu yok. O zaman eklenen yok çıkan ise E düğümü <br/>

**7.Adım:** D düğümünün komşusuna bakıyoruz. H düğümü var. O zaman eklenen kısmına H düğümü yazılır. Çıkan kısmına ise D düğümü yazılır. <br/>

**8.Adım:** H düğümünün komşusuna bakıyoruz. J düğümü var. O zaman eklenen kısmına J düğümü yazılır. Çıkan kısmına ise H düğümü yazılır. <br/>

**9.Adım:** J düğümünün komşusuna bakıyoruz. J düğümü var. Komşusu yok. O zaman eklenen yok çıkan ise J düğümü geriye hiç komşu kalmadığı için algoritma sonlanır. <br/>

Algoritmanın sonucu için output kısmında olanlar yazılır. **Sonuç: A-B-C-F-E-D-H-J** <br/>

Örnek python kodu: <br/>

     def bfs(graph, start):<br/>

     """BFS fonksiyonu"""<br/>
  
    visited = set()         # Ziyaret edilen düğümleri takip etmek için boş bir küme oluştur<br/>

    queue = [start]    # Kuyruk veri yapısı, başlangıç düğümü ile başlatılır<br/>
  
    #Kuyruk boş olmadığı sürece devam et<br/>
    
    while queue:<br/>
  
    node = queue.pop(0) # Kuyruğun başından bir düğüm çıkar (FIFO - İlk giren ilk çıkar)<br/>
    
    if node not in visited:<br/>
    
      visited.add(node) # Düğümü ziyaret edildi olarak işaretle<br/>
      
      print(node, end=' ')<br/>

      # Mevcut düğümün ziyaret edilmemiş tüm komşularını kuyruğa ekle<br/>
      
      for neighbor in graph[node]:<br/>
      
        if neighbor not in visited:<br/>
        
          queue.append(neighbor)  # Düğümü ziyaret edildi olarak işaretle<br/>

        print("Genişlik Öncelikli Arama Sonucu:")<br/>

        bfs(graph, 'A')  # BFS'i 'A' düğümünden başlayarak çağır`<br/>
        


**3. A algoritması:**
Bir graf veya ağ üzerindeki en kısa yolu bulmak için kullanılan bir arama algoritmasıdır. A* algoritması, her düğüm için bir maliyet fonksiyonu kullanır: <br/>

**Formül**:

$$f(n) = \text{g}(n) + \text{h}(n)$$

Burada:
* $f(n)$ → Tahmini toplam maliyet
* $\text{g}(n)$ → Başlangıç düğümünden mevcut düğüme kadar kat edilen gerçek yol maliyeti
* $\text{h}(n)$ → Hedefe olan sezgisel (heuristik) maliyet

 **Çalışma Prensibi**:

Algoritma, iki maliyeti de göz önünde bulundurarak en düşük toplam maliyetli yolu seçer.

Yanıltıcı sezgisellerin etkisini azaltır ve gereksiz yere uzun yolları tercih etmekten kaçınır. Gerektiğinde önceki seçimlerine dönüp daha iyi alternatifleri değerlendirebilir.

A* aramasının verimli olması için sezgisel maliyeti veren fonksiyon $\text{h}(n)$:
* **Kabul edilebilir** olmalıdır → Gerçek maliyeti asla aşmamalıdır.
* **Tutarlı** olmalıdır → Bir düğümün sezgisel maliyeti, komşu düğümün sezgisel maliyeti ile bu iki düğüm arasındaki gerçek geçiş maliyetinin toplamından daha büyük olmamalıdır.
* A* araması, doğru bir sezgisel fonksiyon ile kullanıldığında en iyi çözümü en verimli şekilde bulabilen güçlü bir algoritmadır.<br/>

 **Ekstra Çalışma:**
 Yapılan proje de ekstra olarak yazılan kod sayesinde Kullanıcı tarafından rota yeri kullanıcıdan dinamik giriş olarak girilmesi sağlanabilir. <br/>

**Ekstra kod bulunan kod dosyası: Emır_ınan_1_MetroSimulation.py**

Ek kod : <br/>

     print("\n=== Kullanıcıdan Girdi Alarak Rota Hesaplama ===")
    
      while True:
        baslangic = input("\nBaşlangıç istasyonu kodunu girin (örn: K1A): ").strip().upper()
        hedef = input("Hedef istasyon kodunu girin (örn: K5A): ").strip().upper()

        if baslangic not in metro.istasyonlar or hedef not in metro.istasyonlar:
            print(" Hata: Girilen istasyon kodları geçersiz. Lütfen tekrar deneyin!")
            continue

        sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
        if sonuc:
            rota, sure = sonuc
            print(f"\n En hızlı rota ({sure} dakika): {' -> '.join(rota)}")
        else:
            print("\n Rota bulunamadı!")

        tekrar = input("\nYeni bir rota hesaplamak ister misiniz? (E/H): ").strip().lower()
        if tekrar != 'e':
           print("\n Program sonlandırıldı.")
        break


  
