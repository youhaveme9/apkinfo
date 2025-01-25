# Android Info
Scan apk bundles or AndroidManifest.xml to extract formatted useful information

Get an high level overview of AndroidManifest.xml file of an android apk while reversing the apk such as `exported or non-exported activities` , `package information`, `permissions`, `services`, etc and the list of potential vulnerabilities

## Installation

- Download and install jadx from [here](https://github.com/skylot/jadx?tab=readme-ov-file#download)

#### Fork the repo
```bash
git clone https://github.com/youhaveme9/ctfinfo
```
#### Install the dependencies
```bash
pip install -r requirements.txt
```

## Usage

#### Windows

```bash
python apkinfo.py --xml <path_to_AndroidManifest.xml>
python apkinfo.py --apk <path_to_target.apk>
```
#### Linux/mac

```bash
python3 apkinfo.py --xml <path_to_AndroidManifest.xml>
python3 apkinfo.py --apk <path_to_target.apk>
```

