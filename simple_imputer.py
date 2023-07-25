import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# Rastgele bir veri seti oluşturuyoruz. Burada bazı değerler eksik (NaN).
veriler = pd.DataFrame({
    'yas': [25, np.nan, 30, 35, 40],
    'gelir': [50000, 60000, np.nan, 80000, 90000],
    'cinsiyet': ['E', 'K', np.nan, 'E', 'K']
})

print("Orjinal Veri Seti:\n")
print(veriler)

# SimpleImputer'ı oluşturuyoruz. 'mean' (ortalama) stratejisini kullanıyoruz.
# Bu strateji, her sütundaki eksik değerleri o sütunun ortalaması ile doldurur.
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# 'yas' ve 'gelir' sütunlarındaki değerleri bir numpy dizisine çeviriyoruz.
# Cinsiyet sütunu kategorik olduğu için burada 'mean' stratejisi uygulanamaz, bu yüzden atlıyoruz.
yas_gelir = veriler.iloc[:, 0:2].values

# Imputer'ı yas_gelir verilerine uyduruyoruz ve ardından bu verileri dönüştürüyoruz.
# Bu işlem, eksik değerleri her sütunun ortalaması ile doldurur.
yas_gelir = imputer.fit_transform(yas_gelir)

print("\nEksik Veriler Doldurulduktan Sonra:\n")
print(yas_gelir)




"""
SimpleImputer, Scikit-learn kütüphanesinde bulunan bir sınıftır ve eksik veri noktalarını doldurmak için kullanılır. Yani, veri setinizde herhangi bir sütunda eksik değerler (genellikle NaN olarak temsil edilir) olduğunda, SimpleImputer'ı kullanarak bu eksik değerleri doldurabilirsiniz.

SimpleImputer'ın nasıl dolduracağını belirlemek için çeşitli stratejiler kullanabilirsiniz:

    "mean": Eksik değerler, sütundaki mevcut değerlerin ortalamasıyla doldurulur (yalnızca sayısal veriler için).
    "median": Eksik değerler, sütundaki mevcut değerlerin medyanıyla doldurulur (yalnızca sayısal veriler için).
    "most_frequent": Eksik değerler, sütundaki en sık rastlanan değerle doldurulur. Bu, sayısal ve kategorik verilerde kullanılabilir.
    "constant": Eksik değerler, önceden belirlenmiş bir sabit değerle doldurulur. Bu, fill_value parametresi ile belirlenir ve sayısal ve kategorik verilerde kullanılabilir.

Kullanımı genellikle aşağıdaki adımları içerir:

    SimpleImputer sınıfından bir nesne oluşturulur ve doldurma stratejisi belirlenir.
    fit metodu, verilere uygulanır. Bu adımda, SimpleImputer verileri analiz eder ve doldurma için gereken bilgileri (örneğin, her sütunun ortalaması veya en sık rastlanan değeri) öğrenir.
    transform metodu, verilere uygulanır. Bu adımda, SimpleImputer eksik değerleri doldurur.

fit ve transform adımlarını tek bir adımda gerçekleştiren fit_transform metodu da mevcuttur.
"""
