# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 11:00:33 2025

@author: Akademik
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nltk
from nltk.corpus import stopwords

# Excel dosyasını yükle
df = pd.read_excel('C:/Users/PC/Desktop/makine_ogrenme/tesla_100_x.xlsx', engine='openpyxl')

# Yorum sütununu al
comments = df['Yorum']

# Türkçe stop-word'leri indir (ilk kullanımda gerekli)
nltk.download('stopwords')
turkish_stopwords = stopwords.words('turkish')

# Yorumları vektörleştir
vectorizer = CountVectorizer(stop_words=turkish_stopwords)
comments_vectorized = vectorizer.fit_transform(comments)

# LDA modeli oluştur
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(comments_vectorized)

# Temaları ve en sık geçen kelimeleri yazdır
words = vectorizer.get_feature_names_out()
topics = lda.components_

for topic_idx, topic in enumerate(topics):
    print(f"Topic {topic_idx + 1}:")
    print(" ".join([words[i] for i in topic.argsort()[:-11:-1]]))
    print("\n")
    
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Excel dosyasını yükle
df = pd.read_excel('C:/Users/PC/Desktop/makine_ogrenme/tesla_100_x.xlsx', engine='openpyxl')

# Yorum sütununu al
comments = df['Yorum']

# Türkçe stop-word'leri indir (ilk kullanımda gerekli)
nltk.download('stopwords')
turkish_stopwords = stopwords.words('turkish')

# Yorumları vektörleştir
vectorizer = CountVectorizer(stop_words=turkish_stopwords)
comments_vectorized = vectorizer.fit_transform(comments)

# LDA modeli oluştur
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(comments_vectorized)

# Temaları ve en sık geçen kelimeleri yazdır
words = vectorizer.get_feature_names_out()
topics = lda.components_

# Her tema için çubuk grafik oluştur
for topic_idx, topic in enumerate(topics):
    plt.figure(figsize=(10, 6))
    plt.barh([words[i] for i in topic.argsort()[:-11:-1]], topic[topic.argsort()[:-11:-1]])
    plt.xlabel('Frekans')
    plt.ylabel('Kelime')
    plt.title(f'Tema {topic_idx + 1}: En Sık Geçen Kelimeler')
    plt.gca().invert_yaxis()
    plt.savefig(f'tema_{topic_idx + 1}.png')
    plt.show()