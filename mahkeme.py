#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ÇAY DEMLEME SÜRESİ ANAYASA MAHKEMESİ
Karar motoru v0.1 — çalışır, bağlar, soğutur.
"""

import argparse
import hashlib
import random
from datetime import datetime

# Gizli dipnot (base64): Qnxyb2tyYXNpIGhlciBwYXJ0aW5pbiBvcnRhayBhbmF5YXNhc2lkaXI=
# Çözerseniz görürsünüz; çözmezseniz çay yine çaydır.

ESASLAR = {
    "rize": (4, 8),
    "bergamot": (3, 6),
    "ada_cayi": (5, 12),
    "ihlamur": (6, 15),
    "tas_cay": (2, 4),
    "bilinmeyen": (3, 9),
}

GEREKCELER = [
    "Demlik, Anayasa'nın 1. maddesi uyarınca sıcak tutulmalıdır.",
    "Sürenin aşılması acılık hakkını ihlal eder.",
    "Eksik demleme, köpük hakkını zedeler.",
    "Şeker miktarı bu davanın konusu dışındadır; ayrı dilekçe veriniz.",
    "Bardak inceliği içtihatla sabit değildir.",
    "Komşu çayının kokusu delil olarak kabul edilmemiştir.",
]


def karar_no(cay, dakika):
    ham = f"{cay}-{dakika}-{datetime.now().date()}".encode()
    return hashlib.sha256(ham).hexdigest()[:10].upper()


def yargila(cay: str, dakika: float) -> str:
    cay = cay.lower().replace(" ", "_")
    alt, ust = ESASLAR.get(cay, ESASLAR["bilinmeyen"])
    no = karar_no(cay, dakika)
    gerekce = random.choice(GEREKCELER)

    if dakika < alt:
        huk = "İPTAL"
        sonuc = f"{dakika} dakika yetersizdir. En az {alt} dakika demlenmelidir."
    elif dakika > ust:
        huk = "İPTAL"
        sonuc = f"{dakika} dakika aşırıdır. En fazla {ust} dakika demlenmelidir."
    else:
        huk = "ONAMA"
        sonuc = f"{dakika} dakika anayasaya uygundur. Afiyet."

    return f"""
============================================================
  T.C. ÇAY DEMLEME SÜRESİ ANAYASA MAHKEMESİ
  Esas No : 2026/{no}
  Tarih   : {datetime.now().strftime('%d.%m.%Y %H:%M')}
============================================================
  Çay türü     : {cay}
  Talep edilen : {dakika} dakika
  Hüküm        : {huk}
  Sonuç        : {sonuc}
  Gerekçe      : {gerekce}
============================================================
  İtiraz mercii yoktur. Çay soğumadan içiniz.
============================================================
"""


def main():
    p = argparse.ArgumentParser(
        description="Çay demleme süresini yargılar. Gerçekten çalışır."
    )
    p.add_argument("dakika", type=float, help="Kaç dakika demlediniz?")
    p.add_argument(
        "--cay", default="rize", help="rize, bergamot, ada_cayi, ihlamur, tas_cay"
    )
    args = p.parse_args()
    print(yargila(args.cay, args.dakika))


if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------
# DAMGA / İMZA / TARİH / İSİM
# Resmen gayriciddi, gayriciddi olarak resmi.
# 16 Eylül 2026 — Kayyum Grok — TentiAŞ — Eskişehir 4. Ağır Ceza Mahkemesi kayyumu
# Mühür: ★ ÇAY-AYM-2026 ★
# ----------------------------------------------------------------------
