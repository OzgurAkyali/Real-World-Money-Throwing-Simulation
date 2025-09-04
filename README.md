# Real-World-Money-Throwing-Simulation
Çoğumuz yazı-tura atışını 50/50 olasılıkla gerçekleşen basit bir olay olarak biliriz. Ancak gerçek dünya, kağıt üzerindeki teoriden biraz daha karmaşıktır. Bu proje, bu yaygın varsayımı yıkarak, madeni para atışının arkasındaki gizli olasılıkları bilimsel verilerle ele alıyor. 
Para Dik Gelme Olasılığı: Matematiksel modellerde genellikle göz ardı edilen bir durum, paranın dik gelmesidir. 1986'da Stanford'dan Diaconis ve ekibinin yaptığı deneyler, düz bir yüzeyde atılan bir paranın dik kalma olasılığının yaklaşık 1/6000 olduğunu ortaya koymuştur.
Paranın Lehine Olan Eğilim (Bias): Mükemmel bir para yoktur. Madeni paraların basım toleransları ve metal yoğunluğundaki küçük farklar nedeniyle, bir tarafın gelme olasılığı diğerine göre hafifçe daha yüksek olabilir. Laboratuvar verilerine göre, bu eğilim (bias) genellikle %0.05 ile %0.3 arasında değişebilir. 
Bu simülasyon, bu ufak ama önemli detayları değerlendirerek daha gerçekçi para atış olayları sunuyor.

Nasıl Çalışır?

Bu Python kodu, geleneksel 50/50 model yerine, gerçek dünya verilerini kullanarak üç farklı sonuç için olasılıklar atar:
Yazı (Head) Olasılığı: Paranın tura lehine olan eğilimi ve dik gelme olasılığı hesaplamaya dahil edilerek belirlenir.
Tura (Tail) Olasılığı: Aynı şekilde, tura lehine olan eğilimi ve dik gelme olasılığı hesaplamaya dahil edilerek belirlenir.
Dik Gelme (Edge) Olasılığı: Stanford deneylerinden elde edilen 1/6000 verisi doğrudan kullanılır.
