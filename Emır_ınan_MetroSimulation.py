from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:   #  bir fonksiyon tanımlamak için def anahtar kelimesi kullanılır.
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        queue = deque([(baslangic, [baslangic], baslangic.hat, 0)])   #bu komut satırında kuruk oluşturuldu. (collections.deque kullanarak bir kuyruk oluşturun)
        ziyaret_edildi = {baslangic.idx: 0}

        while queue: # queue = kuruk  # Kuyruk boş olmadığı sürece devam etmesi için döngü ekliyoruz.
            mevcut, yol, hat, aktarmalar = queue.popleft()

            if mevcut == hedef:
                return [ist.ad for ist in yol]

            for komsu, _ in mevcut.komsular:
                yeni_aktarma = aktarmalar + (1 if komsu.hat != hat else 0)

                if komsu.idx not in ziyaret_edildi or yeni_aktarma < ziyaret_edildi[komsu.idx]:
                    ziyaret_edildi[komsu.idx] = yeni_aktarma
                    queue.append((komsu, yol + [komsu], komsu.hat, yeni_aktarma))

        return None       

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = [(0, id(baslangic), baslangic, [])]
        min_sure = {baslangic.idx: 0}

        while pq:
            sure, _, mevcut, yol = heapq.heappop(pq)

            if mevcut == hedef:
                return ([ist.ad for ist in yol + [mevcut]], sure)

            for komsu, ek_sure in mevcut.komsular:
                yeni_sure = sure + ek_sure

                if komsu.idx not in min_sure or yeni_sure < min_sure[komsu.idx]:
                    min_sure[komsu.idx] = yeni_sure
                    heapq.heappush(pq, (yeni_sure, id(komsu), komsu, yol + [mevcut]))
        return None

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstanbul İstasyonlar ekleme METRO HATLARI
    # Kırmızı Hat Yenikapı-Atatürk Havalimanı Metro Hattı
    metro.istasyon_ekle("K1A", "Yenikapı", "Kırmızı Hat")
    metro.istasyon_ekle("K2A", "Aksaray", "Kırmızı Hat")
    metro.istasyon_ekle("K3A", "Fatih", "Kırmızı Hat")
    metro.istasyon_ekle("K4A", "Topkapı", "Kırmızı Hat")
    metro.istasyon_ekle("K5A", "Bayrampaşa", "Kırmızı Hat")
    metro.istasyon_ekle("K6A", "Sagmacılar", "Kırmızı Hat")
    metro.istasyon_ekle("K7A", "otogar", "Kırmızı Hat")
    metro.istasyon_ekle("K8A", "davutpaşa-YTÜ", "Kırmızı Hat")
    metro.istasyon_ekle("K9A", "Merter", "Kırmızı Hat")
    metro.istasyon_ekle("K10A", "Zeytinburnu", "Kırmızı Hat")
    metro.istasyon_ekle("K11A", "Bakırköy", "Kırmızı Hat")
    metro.istasyon_ekle("K12A", "Atatürk-hava-limanı", "Kırmızı Hat")

    # Mor Hat - Yenikapı-Kirazlı Metro Hattı
    metro.istasyon_ekle("K1B", "otogar", "Mor Hat") # AKTARMA NOKTASI K8A DAN K1B 
    metro.istasyon_ekle("K2B", "ESENLER", "Mor Hat")
    metro.istasyon_ekle("K3B", "Menderes", "Mor Hat")
    metro.istasyon_ekle("K4B", "Üçyüzlü", "Mor Hat")
    metro.istasyon_ekle("K5B", "bagcılar-meydan", "Mor Hat")
    metro.istasyon_ekle("K6B", "Kirazlı", "Mor Hat")
    
    # Yeşil Hat - Yenikapı-Seyrantepe-Hacıosman Metro Hattı
    metro.istasyon_ekle("Y1", "Yenikapı", "Yeşil Hat") # AKTARMA NOKTASI K1A DAN Y1
    metro.istasyon_ekle("Y2", "Vezneciler", "Yeşil Hat")
    metro.istasyon_ekle("Y3", "haliç", "Yeşil Hat")
    metro.istasyon_ekle("Y4", "şişhane", "Yeşil Hat")
    metro.istasyon_ekle("Y5", "taksim", "Yeşil Hat")
    metro.istasyon_ekle("Y6", "Levent", "Yeşil Hat")
    metro.istasyon_ekle("Y7", "4.levent", "Yeşil Hat")
    metro.istasyon_ekle("Y8", "seyrantepe", "Yeşil Hat")
    metro.istasyon_ekle("Y9", "İTÜ", "Yeşil Hat")
    metro.istasyon_ekle("Y10", "Atatürk-oto-sanayi", "Yeşil Hat")
    metro.istasyon_ekle("Y11", "Hacıosman", "Yeşil Hat")

    # Mavi Hat - Bakırköy-Kayaşehir Metro Hattı
    metro.istasyon_ekle("M1", "BakırköyY", "Mavi Hat") 
    metro.istasyon_ekle("M2", "Özgürlük-meydan", "Mavi Hat")
    metro.istasyon_ekle("M3", "İncirli", "Mavi Hat")
    metro.istasyon_ekle("M4", "ilkyuva", "Mavi Hat")
    metro.istasyon_ekle("M5", "kirazlı", "Mavi Hat") # AKTARMA NOKTASI K6B DAN M5
    metro.istasyon_ekle("M6", "Yenimahalle", "Mavi Hat")
    metro.istasyon_ekle("M7", "Mahmutbey", "Mavi Hat") 
    metro.istasyon_ekle("M8", "İstoç", "Mavi Hat")
    metro.istasyon_ekle("M9", "İkitelli-sanayi", "Mavi Hat")
    metro.istasyon_ekle("M10", "Şehir-hastanesi", "Mavi Hat")
    metro.istasyon_ekle("M11", "Kayaşehir", "Mavi Hat")
    
    # Pempe hat - Kadıköy-Sabiha Gökçen Havalimanı Metro Hattı
    metro.istasyon_ekle("P1", "Kadıköy", "Pempe Hat")
    metro.istasyon_ekle("P2", "Ayrılık-çeşmesi", "Pempe Hat")
    metro.istasyon_ekle("P3", "acıbadem", "Pempe Hat")
    metro.istasyon_ekle("P4", "bostacı", "Pempe Hat")
    metro.istasyon_ekle("P5", "Pendik", "Pempe Hat")
    metro.istasyon_ekle("P6", "Havalimanı", "Pempe Hat")
    
    # Turuncu hat- Bostancı-Parseller Metro Hattı
    metro.istasyon_ekle("M1A","Bostancı", "Turuncu Hat")  # AKTARMA NOKTASI P4 DEN M1A
    metro.istasyon_ekle("M2A","Kozyatagı", "Turuncu Hat")
    metro.istasyon_ekle("M3A","İçerenköy", "Turuncu Hat")
    metro.istasyon_ekle("M4A","Mevlana", "Turuncu Hat") 
    metro.istasyon_ekle("M5A","dudullu", "Turuncu Hat")
    metro.istasyon_ekle("M6A","Parseller", "Turuncu Hat")

    # İstanbul İstasyonlar ekleme TRAMVAY HATLARI
    # T1 TRAMVAY HATTI
    metro.istasyon_ekle("T1A","Kabataş", "T1")  
    metro.istasyon_ekle("T2A","Fındıklı", "T1")
    metro.istasyon_ekle("T3A","Tophane", "T1")
    metro.istasyon_ekle("T4A","Karaköy", "T1") 
    metro.istasyon_ekle("T5A","eminönü", "T1")
    metro.istasyon_ekle("T6A","Sirkeci", "T1")
    metro.istasyon_ekle("T7A","Sultanahmet", "T1")
    metro.istasyon_ekle("T8A","Aksaray", "T1")  # aktarma noktası K2A T4A
    metro.istasyon_ekle("T9A","Topkapı", "T1")  # aktarma noktası K4A T9A
    metro.istasyon_ekle("T10A","Zeytinburnu", "T1") # aktarma noktası K10A T10A
    metro.istasyon_ekle("T11A","bagcılar", "T1")  # aktarma noktası K5B T11A
     
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1A","K2A",4)    # Yenikapı -> Aksaray
    metro.baglanti_ekle("K2A","K3A",4)    # Aksaray -> Fatih
    metro.baglanti_ekle("K3A", "K4A",3)   # Fatih -> Topkapı
    metro.baglanti_ekle("K4A","K5A",5)    # Topkapı -> Bayrampaşa
    metro.baglanti_ekle("K5A","K6A",3)    # Bayrampaşa -> Sagmacılar
    metro.baglanti_ekle("K6A", "K7A",8)   # Sagmacılar -> otogar
    metro.baglanti_ekle("K7A","K8A",4)    # otogar -> davutpaşa-YTÜ
    metro.baglanti_ekle("K8A","K9A",5)    # davutpaşa -> merter
    metro.baglanti_ekle("K9A", "K10A",3)  #  merter -> zeytinburnu
    metro.baglanti_ekle("K10A","K11A",3)  # zeytinburnu -> bakırköy
    metro.baglanti_ekle("K11A","K12A",4)  # bakırköy -> atatürk-havalimanı

    # Mor Hat bağlantıları
    metro.baglanti_ekle("K1B","K2B",3)   # Otogar -> esenler
    metro.baglanti_ekle("K2B","K3B",3)   # esenler -> menderes
    metro.baglanti_ekle("K3B", "K4B",4)  # menderes -> üçyüzlü
    metro.baglanti_ekle("K4B","K5B",4)   # üçyüzlü -> bagcılar-meydan
    metro.baglanti_ekle("K5B","K6B",4)   # bagcılar-meydan -> kirazlı
    
    # Yeşil Hat bağlantıları
    metro.baglanti_ekle("Y1","Y2",5)    # yenikapı -> vezneciler
    metro.baglanti_ekle("Y2","Y3",5)    # vezneciler -> haliç
    metro.baglanti_ekle("Y3", "Y4",5)   # haliç -> şişhane
    metro.baglanti_ekle("Y4","Y5",3)    # şişhane -> taksim
    metro.baglanti_ekle("Y5","Y6",10)   # taksim -> levent
    metro.baglanti_ekle("Y6", "Y7",3)   # levent -> 4.levent
    metro.baglanti_ekle("Y7","Y8",6)    # 4.levent -> seyrantepe
    metro.baglanti_ekle("Y8","Y9",4)    # seyrantepe-> İTÜ
    metro.baglanti_ekle("Y9", "Y10",4)  # İTÜ-> ATATÜRK-OTO-SANAYİ
    metro.baglanti_ekle("Y10","Y11",4)  # ATATÜRK-OTO-SANAYİ-> Hacıosman

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1","M2",3)   # bakırköy-> özgürlük-meydan
    metro.baglanti_ekle("M2","M3",3)   # özgürlük-meydan-> incirli
    metro.baglanti_ekle("M3","M4",6)   # incirli-> ilkyuva
    metro.baglanti_ekle("M4","M5",3)   # ilkyuva-> kirazlı
    metro.baglanti_ekle("M5", "M6",4)  # kirazlı-> yenimahalle
    metro.baglanti_ekle("M6","M7",3)   # yenimahalle-> mahmutbey
    metro.baglanti_ekle("M7","M8",3)   # mahmutbey-> istoç
    metro.baglanti_ekle("M8", "M9",15) # istoç-> ikitelli-sanayi
    metro.baglanti_ekle("M9", "M10",6) # ikitelli-sanayi-> şehir hastanesi

    # Pempe Hat bağlantıları
    metro.baglanti_ekle("P1","P2",5)    # kadıköy-> ayrılık çeşmesi
    metro.baglanti_ekle("P2","P3",4)    # ayrılık çeşmesi-> acıbadem
    metro.baglanti_ekle("P3", "P4",10)  #  acıbadem-> bostancı
    metro.baglanti_ekle("P4","P5",18)   #  bostancı-> pendik
    metro.baglanti_ekle("P5","P6",9)    # pendik-> sabiha gökçen havalimanı

    # Turuncu hat bağlantıları
    metro.baglanti_ekle("M1A","M2A",6)  # bostancı-> kozyatagı
    metro.baglanti_ekle("M2A","M3A",5)  # kozyatagı-> içerenköy
    metro.baglanti_ekle("M3A", "M4A",4) # içerenköy-> mevlena
    metro.baglanti_ekle("M4A","M5A",5)  # mevlana -> dudullu
    metro.baglanti_ekle("M5A","M6A",4)  # dudullu -> parseller

    # TRAMVAY HATTI 
    # T1 hat bağlantıları
    metro.baglanti_ekle("T1A","T2A",3)  # kabataş-> fındıklı
    metro.baglanti_ekle("T2A","T3A",3)  # fındıklı-> tophane
    metro.baglanti_ekle("T3A", "T4A",4) # tophane-> karaköy
    metro.baglanti_ekle("T4A","T5A",4)  # karaköy -> eminönü
    metro.baglanti_ekle("T5A","T6A",3)  # eminönü -> sirkeci
    metro.baglanti_ekle("T6A","T7A",5)  # sirkeci-> sultanahmet
    metro.baglanti_ekle("T7A","T8A",15)  # sultanahmet-> aksaray
    metro.baglanti_ekle("T8A", "T9A",8) # aksaray-> topkapı
    metro.baglanti_ekle("T9A","T10A",10)  # topkapı -> zeytinburnu
    metro.baglanti_ekle("T10A","T11A",12)  # zeytinburnu -> bagcılar

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K7A", "K1B",2)  # OTAGAR AKTARMA
    metro.baglanti_ekle("K1A", "Y1",2)  # Yenikapı aktarma
    metro.baglanti_ekle("K6B", "M5",3)  # Kirazlı aktarma
    metro.baglanti_ekle("P4", "M1A",3)  # Bostancı aktarma
    metro.baglanti_ekle("K2A", "T4A",2 )  # Aksaray aktarma
    metro.baglanti_ekle("K4A", "T9A",4)  # Topkapı aktarma
    metro.baglanti_ekle("K10A", "T10A",2)  # Zeytinburnu aktarma
    metro.baglanti_ekle("K5B", "T11A",2)  # Bagcılar aktarma


    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: YENİKAPI DAN BAKIRKÖYE
    print("\n1. YENİKAPI'den BAKIRKÖY'ye:")
    rota = metro.en_az_aktarma_bul("K1A", "K11A")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(rota))
    
    sonuc = metro.en_hizli_rota_bul("K1A", "K11A")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))

    # Senaryo 2: YENİKAPI DAN SİRKECİ
    print("\n1. YENİKAPI'den SİRKECİ'ye:")
    rota = metro.en_az_aktarma_bul("K1A", "T6A")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(rota))
    
    sonuc = metro.en_hizli_rota_bul("K1A", "T6A")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))
    
    # Senaryo 3: FATİH DEN ÜÇYÜZLÜ
    print("\n1. FATİH'den ÜÇYÜZLÜ'ye:")
    rota = metro.en_az_aktarma_bul("K3A", "K4B")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(rota))
    
    sonuc = metro.en_hizli_rota_bul("K3A", "K4B")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))

    # Senaryo 4: YENİKAPI DEN İTÜ
    print("\n1. YENİKAPI'den İTÜ'ye:")
    rota = metro.en_az_aktarma_bul("K1A", "Y9")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(rota))
    
    sonuc = metro.en_hizli_rota_bul("K1A", "Y9")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))

    # Senaryo 5: ESENLER DEN KAYAŞEHİR
    print("\n1. ESENLER'den KAYAŞEHİR'ye:")
    rota = metro.en_az_aktarma_bul("K2B", "M11")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(rota))
    
    sonuc = metro.en_hizli_rota_bul("K2B", "M11")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))

    # Senaryo 6: KADIKÖY DEN DUDULLU
    print("\n1. KADIKÖY'den DUDULLU'ye:")
    rota = metro.en_az_aktarma_bul("P1", "M5A")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(rota))
    
    sonuc = metro.en_hizli_rota_bul("P1", "M5A")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))

    # Senaryo 7: FATİH DEN KABATAŞ
    print("\n1. FATİH'den KABATAŞ'ye:")
    rota = metro.en_az_aktarma_bul("K3A", "T1A")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(rota))
    
    sonuc = metro.en_hizli_rota_bul("K3A", "T1A")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))

    # Senaryo 8: MENDERES DEN TOPHANE
    print("\n1. MENDERES'den TOPHANE'ye:")
    rota = metro.en_az_aktarma_bul("K3B", "T3A")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(rota))
    
    sonuc = metro.en_hizli_rota_bul("K3B", "T3A")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))