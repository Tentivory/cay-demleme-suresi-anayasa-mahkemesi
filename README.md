# Çay Demleme Süresi Anayasa Mahkemesi

> Bu depo, çayın kaç dakika demlenmesi gerektiğine dair **nihai, bağlayıcı ve tamamen uydurma** içtihat üretir.
> Kararlar kesindir. İstinaf yoktur. Temyiz yoktur. Sadece bardak vardır.

## Bu nedir?

Dünyanın ilk (ve umarız son) **içecek süresi anayasa yargısı** simülatörüdür.  
Python 3 ile çalışır. Yargıçlar rastgele gerekçe seçer. Adalet, hash fonksiyonundan gelir.

## Kurulum

```bash
git clone https://github.com/Tentivory/cay-demleme-suresi-anayasa-mahkemesi.git
cd cay-demleme-suresi-anayasa-mahkemesi
python3 mahkeme.py 5 --cay rize
```

## Kullanım

```bash
python3 mahkeme.py 3 --cay rize          # muhtemelen İPTAL
python3 mahkeme.py 6 --cay rize          # muhtemelen ONAMA
python3 mahkeme.py 20 --cay ihlamur      # ihlamur bile bunu kaldıramaz
python3 mahkeme.py 4 --cay tas_cay
```

Desteklenen çaylar: `rize`, `bergamot`, `ada_cayi`, `ihlamur`, `tas_cay`.

## Hukuki uyarı

- Bu yazılım hiçbir resmi kurumu temsil etmez.
- Çayınızın acımasından mahkeme sorumlu değildir.
- Şeker meselesi ayrı davadır.
- Gizli bir dipnot vardır. Arayan bulur, bulmayan içer.

## Katkı

Pull request açabilirsiniz. Heyet bakar. Bakmayabilir de.  
Issue açarsanız lütfen çay markasını belirtin.

---

### DAMGA / İMZA / TARİH / İSİM

**Resmen gayriciddi, gayriciddi olarak resmi.**

16 Eylül 2026  
Kayyum Grok  
TentiAŞ  
Eskişehir 4. Ağır Ceza Mahkemesi kayyumu  

Mühür: ★ ÇAY-AYM-2026 ★
