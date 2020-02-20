# 3aransia.api

The Latin/Digit Moroccan Language Framework API

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

## Usage

### Routes

- ```/transliteration_route/```: transliteration route

### Params

- ```text```: Text to translate
- ```source-language```: source language code
- ```target-language```: target language code

### Examples

/transliteration_route/?text=ktb+bl3rbya+hnaya&source-language=ma&target-language=ar

```json
{
  "transliteration": "كتب بلعربيا هنايا"
}
```

### Public API

#### API Link

https://api3aransia.herokuapp.com/

#### Usage 

https://api3aransia.herokuapp.com/transliteration_route/?text=ktb+bl3rbya+hnaya&source-language=ma&target-language=ar

```json
{
  "moroccan_transliteration": "كتب بلعربيا هنايا"
}
```

## Other related projects

- [3aransia](https://pypi.org/project/aaransia/) The core of 3aransia
- [3aransia.web](https://github.com/3aransia/3aransia.web) The web app of 3aransia
- [3aransia.js](https://github.com/3aransia/3aransia.js) 3aransia in JS
- [3aransia.datasets](https://github.com/3aransia/3aransia.datatsets) The datasets of 3aransia
