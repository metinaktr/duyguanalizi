# 🚗 Tesla Yorum Analizi - LDA ile Konu Modelleme

Bu proje, **Tesla ile ilgili yorumları** analiz etmek için **Latent Dirichlet Allocation (LDA)** yöntemini kullanır. Türkçe yorumlardan temaları çıkarır ve her tema için en sık geçen kelimeleri görselleştirir.

## 📌 Özellikler
- Excel dosyasından yorumları okur.
- Türkçe stop-word'leri filtreler.
- **CountVectorizer** ile metinleri vektörleştirir.
- **LDA** ile 5 tema oluşturur.
- Her tema için en sık geçen 10 kelimeyi çubuk grafik olarak görselleştirir.

## 🛠 Kullanılan Teknolojiler
- **Python 3.x**
- **pandas**
- **scikit-learn**
- **nltk**
- **matplotlib**

## 📂 Dosya Yapısı
```
├── tesla_lda.py        # Ana Python kodu
├── tesla_100_x.xlsx    # Yorumların bulunduğu Excel dosyası
├── tema_1.png          # Tema 1 görselleştirmesi
├── tema_2.png          # Tema 2 görselleştirmesi
...
└── README.md           # Proje açıklaması
```

## ⚙️ Kurulum
1. Gerekli kütüphaneleri yükleyin:
```bash
pip install pandas scikit-learn nltk matplotlib openpyxl
```

2. NLTK stop-word'lerini indirin:
```python
import nltk
nltk.download('stopwords')
```

3. Excel dosyasını `C:/Users/PC/Desktop/makine_ogrenme/tesla_100_x.xlsx` yoluna yerleştirin.

## ▶️ Çalıştırma
```bash
python tesla_lda.py
```

## 📊 Çıktılar
- Konsolda her tema için en sık geçen kelimeler listelenir.
- `tema_1.png`, `tema_2.png` ... dosyaları oluşturulur.

## 🔍 Örnek Tema Çıktısı
```
Topic 1:
araba elektrik motor performans hız şarj batarya yol sürüş
```
