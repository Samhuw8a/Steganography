# Steganography
![test](https://github.com/Samhuw8a/Steganography/actions/workflows/test.yml/badge.svg) 
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

![release](https://img.shields.io/github/v/release/Samhuw8a/Steganography)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FSamhuw8a%2FSteganography%2Fmaster%2Fpyproject.toml&color=d8634c)


Eine Python Implementation von LSB-Steganographie mit AES-encryption und compression für unkomprimierte Bildformate.
## CLI
Das Programm bietet ein CLI mit welchem man Dateien *extracten* und *embeden* kann.

Weiter Parameter findet man unter: [Usage](docs/main_usage.md).


## Instalation
Clone the repo onto your computer
```sh
git clone https://github.com/Samhuw8a/Steganography
cd Steganography
```

install the Programm using pip
```sh
python -m pip install .
```

Now you can run the Programm by calling
```sh
steganography -h
```
