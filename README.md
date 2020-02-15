# 3aransia.api

The Latin/Digit Moroccan Language Framework API

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

## Usage

### Routes

> '/transliterate_moroccan_route/<string:moroccan_entry>' 
> '/transliterate_arabic_moroccan_route/<string:moroccan_arabic_entry>' 

### Examples

> /transliterate_moroccan_route/ktb+bl3rbya+hnaya 

```json
{
  "moroccan_transliteration": "كتب بلعربيا هنايا"
}
```

> /transliterate_moroccan_arabic_route/كتب+بلربيا+هنايا 
```json
{
  "moroccan_arabic_transliteration": "ktb blrbia hnaya"
}
```

### Public API

#### CORS Anywhere with heroku

> https://cors-anywhere.herokuapp.com/ 

#### API Link

> https://api3aransia.herokuapp.com/ 

#### Public Usage 

> https://cors-anywhere.herokuapp.com/https://api3aransia.herokuapp.com/transliterate_moroccan_route/ktb+bl3rbya+hnaya 

```json
{
  "moroccan_transliteration": "كتب بلعربيا هنايا"
}
```

> https://cors-anywhere.herokuapp.com/https://api3aransia.herokuapp.com/transliterate_moroccan_arabic_route/كتب+بلربيا+هنايا 

```json
{
  "moroccan_arabic_transliteration": "ktb blrbia hnaya"
}
```

## Other related projects

- [3aransia](https://github.com/3aransia/3aransia) The core of 3aransia
- [3aransia.web](https://github.com/3aransia/3aransia.web) The web app of 3aransia
- [3aransia.js](https://github.com/3aransia/3aransia.js) 3aransia in JS
- [3aransia.datasets](https://github.com/3aransia/3aransia.datatsets) The datasets of 3aransia
