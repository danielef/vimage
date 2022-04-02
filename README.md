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

