# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:00:37 2025

@author: Akademik
"""

import pandas as pd
from transformers import pipeline
from tensorflow.keras.models import Model

# Excel dosyasını oku
df = pd.read_excel('C:/Users/Pc/Desktop/makine_ogrenme/tesla_100_x.xlsx', engine='openpyxl')

# Duygu analizi yapılacak sütun adını belirtin (ör: 'yorum')
text_column = "Yorum"

# Türkçe BERT modelini yükle
classifier = pipeline("sentiment-analysis", model="savasy/bert-base-turkish-sentiment-cased")

# Sonuçları bir listeye ekle
results = []
for text in df[text_column]:
    if pd.isna(text):
        results.append(None)
        continue
    prediction = classifier(str(text))[0]
    results.append(prediction['label'])

# Sonuçları yeni bir sütun olarak ekle
df["duygu"] = results

# Sonuçları yeni bir Excel dosyasına kaydet
df.to_excel("C:/Users/Pc/Desktop/makine_ogrenme/duygu_analiz_sonuclari.xlsx", index=False)
print("Duygu analizi tamamlandı ve sonuçlar duygu_analiz_sonuclari.xlsx dosyasına kaydedildi.")
