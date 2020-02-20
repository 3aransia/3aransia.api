# 3aransia.api

Languages and Dialects transliteration 3aransia API

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

## Usage

### Routes

#### Get Alphabet codes route

- ```/get_alphabets_codes_route/```: get alphabets codes route

##### Example

/get_alphabets_codes_route/

```json
{
  "alphabets_codes": [
    "ma", 
    "ar", 
    "la", 
    "ab", 
    "gr"
  ]
}
```

#### Get available languages

- ```/get_alphabets_route/```: get alphabets route

##### Example

/get_alphabets_route/

```json
{
  "alphabets": {
    "ab": "Abjadi Alphabet", 
    "ar": "Arabian Alphabet", 
    "gr": "Greek Alphabet", 
    "la": "Latin Alphabet", 
    "ma": "Moroccan Alphabet"
  }
}
```

#### Transliteration route

- ```/transliteration_route/```: transliteration route

##### Params

- ```text```: Text to translate
- ```source-language```: source language code
- ```target-language```: target language code

##### Example

/transliteration_route/?text=ktb+bl3rbya+hnaya&source-language=ma&target-language=ar

```json
{
  "transliteration": "كتب بلعربيا هنايا"
}
```

### Public API

#### API Link

[https://api3aransia.herokuapp.com/](https://api3aransia.herokuapp.com/)

#### Usage 

[https://api3aransia.herokuapp.com/get_alphabets_codes_route/](https://api3aransia.herokuapp.com/get_alphabets_codes_route/)

```json
{
  "alphabets_codes": [
    "ma", 
    "ar", 
    "la", 
    "ab", 
    "gr"
  ]
}
```
[https://api3aransia.herokuapp.com/get_alphabets_route](https://api3aransia.herokuapp.com/get_alphabets_route)

```json
{
  "alphabets": {
    "ab": "Abjadi Alphabet", 
    "ar": "Arabian Alphabet", 
    "gr": "Greek Alphabet", 
    "la": "Latin Alphabet", 
    "ma": "Moroccan Alphabet"
  }
}
```

[https://api3aransia.herokuapp.com/transliteration_route/?text=ktb+bl3rbya+hnaya&source-language=ma&target-language=ar](https://api3aransia.herokuapp.com/transliteration_route/?text=ktb+bl3rbya+hnaya&source-language=ma&target-language=ar)

```json
{
  "transliteration": "كتب بلعربيا هنايا"
}
```

## Other related projects

- [3aransia](https://pypi.org/project/aaransia/) The python library of 3aransia
- [3aransia.web](http://3aransia.com) The web application of 3aransia
