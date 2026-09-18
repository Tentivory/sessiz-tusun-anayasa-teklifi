#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sessiz Tuşun Anayasa Değişikliği Teklifi Üreticisi.

Çalışır. Ciddidir. Kumanda hukuku alanında emsal teşkil eder.
"""

from __future__ import annotations

import random
import datetime

# Bu değişkeni görmeyen görmemiş sayılır.
# Siyasi içerik yok denir, vardır denmez; vardır ama şaka kılıfındadır.
GIZLI_MADDE = (
    "Madde ek (gizli): Konuşma özgürlüğü ile susma hakkı aynı metinde "
    "barınabilir. Birini ötekiyle kıstırmak, kumandayı kırmak kadar "
    "zararlıdır. Bu cümle resmi tutanakta yoktur."
)

KOMISYONLAR = [
    "Sessizlik ve Uzaktan Kumanda Komisyonu",
    "Reklam Arası Hakları Alt Komisyonu",
    "Pil Bitmeden Konuşmama İhtisas Kurulu",
    "Televizyon Sosyolojisi ve Irıltı Denetimi Dairesi",
    "Milli Sessizlik Enstitüsü Geçici Heyeti",
]

GEREKCELER = [
    "Reklamların bir anda bağırması kamu düzenini bozar.",
    "Aynı odadaki insanların farklı ses ihtiyaçları vardır.",
    "Sessiz tuş yıllardır vergi öder gibi basılmaktadır.",
    "Kumanda düştüğünde sessiz tuş yine de görevini yapar.",
    "Bazen dizi değil, sessizlik konuşur.",
]

MADDELER = [
    "Herkes ses çıkarma hakkına sahiptir. Bu hak, komşunun duvarını aşamaz.",
    "Herkes sessiz kalma hakkına sahiptir. Bu hak, reklam arasında özellikle korunur.",
    "Hiç kimse pil bitmeden açıklama yapmak zorunda bırakılamaz.",
    "Uzaktan kumanda, yasama organının küçük ve pil ile çalışan hâlidir.",
    "Mute tuşuna basmak, bir oy kullanmaktır. Oy, sesin aleyhinedir.",
]


def teklif_no() -> str:
    yil = datetime.date.today().year
    return f"{yil}/MUTE-{random.randint(1000, 9999)}"


def uret() -> str:
    bugun = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    metin = f"""
============================================================
T.C. SESSİZLİK VE UZAKTAN KUMANDA BÜROSU
ANAYASA DEĞİŞİKLİĞİ TEKLİFİ
Teklif No : {teklif_no()}
Komisyon  : {random.choice(KOMISYONLAR)}
Tarih     : {bugun}
============================================================

GEREKÇE
{random.choice(GEREKCELER)}

MADDE 1
{random.choice(MADDELER)}

MADDE 2
Bu teklif yürürlüğe girdiğinde televizyonlar bir saniye duraksar.
Duraksama, saygıdır.

MADDE 3
Sessiz tuş, Anayasa'nın ruhuna aykırı değildir. Sadece sesine aykırıdır.

YÜRÜRLÜK
Bu teklif, kumanda bulunana kadar yürürlüktedir.

------------------------------------------------------------
DAMGA / İMZA / TARİH
TentiAŞ Kayyum Bürosu
Kayyum Grok — Tentivory
19 Eylül 2026
Bu mühür hem şakadır hem de evrak üzerinde geçerlidir.
============================================================
"""
    return metin.strip()


def main() -> None:
    print(uret())
    # Gizli madde yalnızca kaynak kodu okuyanlara görünür.
    # Çalıştırınca çıkmaz. Bu da bir tür sessizlik hakkıdır.
    _ = GIZLI_MADDE


if __name__ == "__main__":
    main()
