# 图片EXIF

- 参考
    - https://feei.cn/exif
    - EXIF指可交换图片文件格式（Exchangeable Image file Format），可以在图片中记录数码相机的相关数据，比如拍摄的设备、拍摄的参数以及地理位置等。

- pip install exifread

- 用法
    - EXIF.py /Users/play/Downloads/IMG_20190501_170544.jpg
EXIF.py /Users/play/Downloads/IMG_20190501_163737.jpg

```
import exifread

fp='IMG_20190501_165148.jpg'
with open(fp,'rb') as f:
    tags = exifread.process_file(f)

tags
tags.keys()
tags['GPS GPSAltitude']
type(_)
t=tags['GPS GPSAltitude']
t.values
t.values[0]
type(_)
convert = lambda ratio: float(ratio.num)/float(ratio.den)
alt=[convert(c) for c in t.values]

```
