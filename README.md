# vimage
Extracts relevant scenes from a video using Locality Sensitive Hashing (LSH)

## Download

```
git clone https://github.com/danielef/vimage.git
```

## Setup
```
cd vimage
virtualenv -p python3.7 env
source env/bin/activate
pip install -r requirements.txt
```

## Running
By default prints a short usage:
```
python app.py
Loading logging configuration from: log.conf
usage: app.py [-h] -v VIDEO [-d DELAY] [-r RESIZE]
app.py: error: the following arguments are required: -v/--video
```

Real example:
```
python app.py --video=../../../Downloads/20220328_BX2_30AN5D_3.mp4
Loading logging configuration from: log.conf
2022-04-02 01:53:18,759 INFO     62471 root params: {'video': '../../../Downloads/20220328_BX2_30AN5D_3.mp4', 'delay': 15.0, 'resize': None}
f_skip: 91
2022-04-02 01:53:19,622 DEBUG    62471 root hash: 1f803ffc71bfe38c3f1c61c71f0e07fa7670f3be071c7038
2022-04-02 01:53:19,622 INFO     62471 root Writing: ../../../Downloads/20220328_BX2_30AN5D_3.mp4_vimage/91.jpg - 0.0
2022-04-02 01:53:20,359 DEBUG    62471 root hash: 1f803ffc71bfe38c3f1c61c71f4e07fa7670f3b6071c7038
2022-04-02 01:53:21,037 DEBUG    62471 root hash: 1f8037fc713fe38c3f1c61c71f4e07fa7670d3a0c71c723c
2022-04-02 01:53:21,734 DEBUG    62471 root hash: 1f8037fc71bfe38c3f1c61c71f0e07fa7670d39c471c7238
2022-04-02 01:53:22,425 DEBUG    62471 root hash: 1f803ffc71bfe38c3f1c61c71f0e07fa7670f3be071c7038
2022-04-02 01:53:23,161 DEBUG    62471 root hash: 000e47047e3fe38c3f0061f0030e381e0e38f86fc780763e
2022-04-02 01:53:23,162 INFO     62471 root Writing: ../../../Downloads/20220328_BX2_30AN5D_3.mp4_vimage/546.jpg - -0.046875
2022-04-02 01:53:23,971 DEBUG    62471 root hash: 000e3f0071f8e39e0700e2381f4fc0ff7e0ffb803ffc05ff
2022-04-02 01:53:23,971 INFO     62471 root Writing: ../../../Downloads/20220328_BX2_30AN5D_3.mp4_vimage/637.jpg - -0.15625
2022-04-02 01:53:24,765 DEBUG    62471 root hash: 0300f71c8f80e03c0701e03f0701f87a01c7f38e3f1c71fc
2022-04-02 01:53:24,765 INFO     62471 root Writing: ../../../Downloads/20220328_BX2_30AN5D_3.mp4_vimage/728.jpg - -0.046875
2022-04-02 01:53:25,527 DEBUG    62471 root hash: 040077f80f83c03c3e01e1f0070f803a7607f3803f1c31f8
2022-04-02 01:53:25,527 INFO     62471 root Writing: ../../../Downloads/20220328_BX2_30AN5D_3.mp4_vimage/819.jpg - 0.3125
2022-04-02 01:53:26,314 DEBUG    62471 root hash: 040067f80f87c03c3e01e1f0070f803a7607f3803f1c31f8
2022-04-02 01:53:26,969 DEBUG    62471 root hash: 040067f80787c03c3e01e1f0070f807a7607e3803f1c31f8
2022-04-02 01:53:27,631 DEBUG    62471 root hash: 040067f80f87c03c3e01e1f0070f807a7607f3803f1c31f8
2022-04-02 01:53:27,645 DEBUG    62471 root {'capture': <VideoCapture 0x7feb704516b0>, 'fps': 6.0, 'length': 1094, 'path': '../../../Downloads/20220328_BX2_30AN5D_3.mp4', 'last': array([ 32,   3, 191, 192, 124,  30,   1, 225, 240,  15,  15, 128,  56,
       124,   1, 211, 176,  63, 156,   1, 248, 225, 143, 192], dtype=uint8), 'saved': 5, 'readed': 1094}
```


## TODO
- Add params
  - LSH hashsize
  - LSH similarity threshold
