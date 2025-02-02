# DeepSeek-R1

## Gerekli Kütüphaneler
`pip install together`
`pip install Flask`

## API Key
DeepSeek R1 modelini kullanmak için together.ai sitesine kayıt olunmalı. analyze.py, roadmap.py ve main.py dosyalarında bulunan,
`client = Together(api_key="**********************************")`
kodundaki api_key bölümüne, together.ai sitesinden aldığınız API Key'i girmelisiniz. Eğer API Key almada sorun yaşarsanız, karaman.ahmet@std.izu.edu.tr adresine mail attığınız takdirde test sürecinde kullanmanız için kendi API Key'imi verebilirim.

## Dosyaların Görevleri:
### analyze.py
test klasörünün içerisindeki kodları inceler. Bu kodlar için güvenlik, mimari ve best practices açısından yorumlar yapar.

### roadmap.py
test klasörünün içerisindeki kodları inceler. Bu kodların görevlerinden yola çıkarak projenin amacını ve konusunu tahmin eder. Bu tahminler doğrultusunda tavsiyelerde bulunur ve roadmap önerileri verir.

### main.py
İsim ve yaş bilgilerini alıp report.txt dosyasına kaydeden basit bir koddur. Amacı, programın kullanımı esnasında kullanıcının karşılaştığı hatanın yapay zekaya yorumlatılabileceğini göstermektir. Yaş girişi esnasında doğal sayı yerine karakter girerek bunu test edebilirsiniz. main.py dosyasını çalıştırdığınız zaman http://127.0.0.1:5000 adresini açmanız gerekmektedir. Bu adresten programı başlattıktan sonra veri girişleri, dosyanın çalıştırıldığı terminal üzerinden yapılmalıdır. Bu adresi, müşteri temsilcisi veya geliştirici ekibin hataları gördüğü ve çözüm önerileri sunmakta kullandığı ara yüzün çok daha basit hali gibi düşünebilirsiniz.

## Önemli Not
together.ai sitesinin ücretsiz üyeliklere sunduğu kredi $1.00 ile sınırlıdır. Bu nedenle kodlarda yapay zekanın kullanabileceği maksimum token miktarını kısıtlı tutmam gerekti. Bu yüzden de yapay zekanın yaptığı yorumlar yarıda kesilebilir. Yarıda kesilmesine rağmen yaptığı tahmin ve yorumların doğru olduğunu görebilirsinz. Eğer daha tutarlı sonuçlar görmek isterseniz max_tokens değerlerini arttırabilirsiniz ancak together.ai sitesinde ücretsiz olarak kullanabileceğimiz kredi miktarının sınırlı olduğunu unutmayın.
