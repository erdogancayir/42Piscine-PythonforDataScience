import time
from datetime import datetime

# Saniye cinsinden Unix zamanını alırız
# Unix zamanını (yani 1970 yılının 1 Ocak tarihinden itibaren geçen süreyi saniye cinsinden) hesaplar,
#   ve bu değeri hem normal ondalıklı formatında hem de bilimsel gösterim formatında çıktı olarak verir. 
seconds_since_epoch = time.time()
print("Seconds since January 1, 1970: {:.4f} or {:.2e} in scientific notation".format(seconds_since_epoch, seconds_since_epoch))

# Şimdiki zamanı alırız ve belirtilen formatta çıktıyı veririz
now = datetime.now()
formatted_date = now.strftime("%b %d %Y")
print(formatted_date)
