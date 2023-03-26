# Görüntü İşleme ile Top Tespiti
## Proje İçeriği
Bu proje, bir video akışında video akışının sol yarısında ki kırmızı topları tespit eder ve tespit edilen kırmızı topların sayısı 3'ten büyük olduğunda API'ye uyarı gönderir ve uyarı gönderdiği resim karesini 'warning_frames' klasörüne kaydeder. Kod, görüntü işleme için OpenCV kütüphanesini ve POST isteklerini göndermek için requests kütüphanesini kullanır.Ve ayrıca diğer işlemler için NumPy, PIL, Base64 gibi kütüphaneleride içerir.
## Kullanım
Bu kodu kullanmak için, bir video dosyası adını ve yolunu değiştirerek veya kameranızı cv2.VideoCapture işlevine geçmeniz gerekecektir. Ayrıca, url değişkenini, uyarıları göndereceğiniz sunucunun adresiyle değiştirmeniz gerekecektir. Kodun çalışması için, Python3, OpenCV, NumPy, PIL, Base64 ve Requests kütüphanelerinin yüklü olması gerekmekte ve uyarıların gönderileceği sunucunun çalışır durumda ve bağlantılı olması da gerekmektedir. Ayrıca extract_images_from_video.py uzantılı python dosyasını çalıştırarak da videodan veya kameranızdan anlık olarak kareler alarak 'frames' dosyasına kaydedebilirsiniz.
## Örnek
![frame367](https://user-images.githubusercontent.com/95315841/227765675-62109576-5075-45db-9e32-ae1e86b643b8.jpeg)

![frame294](https://user-images.githubusercontent.com/95315841/227765680-1468e753-0a0b-4c2c-bfe3-70d76659c3ce.jpeg)

![Ekran görüntüsü 2023-03-26 115920](https://user-images.githubusercontent.com/95315841/227765815-73ddede0-f74f-43ff-afd9-15d7fc6b5fad.png)
