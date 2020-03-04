# 3aransia.api

Transliteration of languages and dialects 3aransia API

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
    "ar", 
    "af", 
    "sq", 
    "al", 
    "az", 
    "eu", 
    "bo", 
    "ca", 
    "co", 
    "hr", 
    "cs", 
    "da", 
    "nl", 
    "en", 
    "eo", 
    "et", 
    "tl", 
    "fi", 
    "fr", 
    "fs", 
    "gl", 
    "de", 
    "ht", 
    "ha", 
    "hw", 
    "hu", 
    "is", 
    "ig", 
    "id", 
    "ga", 
    "it", 
    "ki", 
    "ku", 
    "la", 
    "lv", 
    "li", 
    "lt", 
    "lu", 
    "ma", 
    "mg", 
    "ms", 
    "mt", 
    "mo", 
    "no", 
    "pl", 
    "pt", 
    "ro", 
    "sa", 
    "gc", 
    "el", 
    "ss", 
    "sh", 
    "sk", 
    "sl", 
    "so", 
    "es", 
    "su", 
    "sw", 
    "sv", 
    "tn", 
    "tr", 
    "tu", 
    "uz", 
    "vi", 
    "cy", 
    "xh", 
    "yo", 
    "zu", 
    "fa", 
    "ur"
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
    "af": "Afrikaans Alphabet", 
    "al": "Algerian Alphabet", 
    "ar": "Arabic Alphabet", 
    "az": "Azerbaijani Alphabet", 
    "bo": "Bosnian Alphabet", 
    "ca": "Catalan Alphabet", 
    "co": "Corsican Alphabet", 
    "cs": "Czech Alphabet", 
    "cy": "Welsh Alphabet", 
    "da": "Danish Alphabet", 
    "de": "German Alphabet", 
    "el": "Greek Alphabet", 
    "en": "English Alphabet", 
    "eo": "Esperanto Alphabet", 
    "es": "Spanish Alphabet", 
    "et": "Estonian Alphabet", 
    "eu": "Basque Alphabet", 
    "fa": "Persian Alphabet", 
    "fi": "Finnish Alphabet", 
    "fr": "French Alphabet", 
    "fs": "Frisian Alphabet", 
    "ga": "Irish Alphabet", 
    "gc": "Gaelic Alphabet", 
    "gl": "Galician Alphabet", 
    "ha": "Hausa Alphabet", 
    "hr": "Croatian Alphabet", 
    "ht": "Creole Alphabet", 
    "hu": "Hungarian Alphabet", 
    "hw": "Hawaiian Alphabet", 
    "id": "Indonesian Alphabet", 
    "ig": "Igbo Alphabet", 
    "is": "Icelandic Alphabet", 
    "it": "Italian Alphabet", 
    "ki": "Kinyarwanda Alphabet", 
    "ku": "Kurdish Alphabet", 
    "la": "Latin Alphabet", 
    "li": "Libyan Alphabet", 
    "lt": "Lithuanian Alphabet", 
    "lu": "Luxembourgish Alphabet", 
    "lv": "Latvian Alphabet", 
    "ma": "Moroccan Alphabet", 
    "mg": "Malagasy Alphabet", 
    "mo": "Maori Alphabet", 
    "ms": "Malay Alphabet", 
    "mt": "Maltese Alphabet", 
    "nl": "Dutch Alphabet", 
    "no": "Norwegian Alphabet", 
    "pl": "Polish Alphabet", 
    "pt": "Portuguese Alphabet", 
    "ro": "Romanian Alphabet", 
    "sa": "Samoan Alphabet", 
    "sh": "Shona Alphabet", 
    "sk": "Slovak Alphabet", 
    "sl": "Slovenian Alphabet", 
    "so": "Somali Alphabet", 
    "sq": "Albanian Alphabet", 
    "ss": "Sesotho Alphabet", 
    "su": "Sundanese Alphabet", 
    "sv": "Swedish Alphabet", 
    "sw": "Swahili Alphabet", 
    "tl": "Filipino Alphabet", 
    "tn": "Tunisian Alphabet", 
    "tr": "Turkish Alphabet", 
    "tu": "Turkmen Alphabet", 
    "ur": "Urdu Alphabet", 
    "uz": "Uzbek Alphabet", 
    "vi": "Vietnamese Alphabet", 
    "xh": "Xhosa Alphabet", 
    "yo": "Yoruba Alphabet", 
    "zu": "Zulu Alphabet"
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
    "ar", 
    "af", 
    "sq", 
    "al", 
    "az", 
    "eu", 
    "bo", 
    "ca", 
    "co", 
    "hr", 
    "cs", 
    "da", 
    "nl", 
    "en", 
    "eo", 
    "et", 
    "tl", 
    "fi", 
    "fr", 
    "fs", 
    "gl", 
    "de", 
    "ht", 
    "ha", 
    "hw", 
    "hu", 
    "is", 
    "ig", 
    "id", 
    "ga", 
    "it", 
    "ki", 
    "ku", 
    "la", 
    "lv", 
    "li", 
    "lt", 
    "lu", 
    "ma", 
    "mg", 
    "ms", 
    "mt", 
    "mo", 
    "no", 
    "pl", 
    "pt", 
    "ro", 
    "sa", 
    "gc", 
    "el", 
    "ss", 
    "sh", 
    "sk", 
    "sl", 
    "so", 
    "es", 
    "su", 
    "sw", 
    "sv", 
    "tn", 
    "tr", 
    "tu", 
    "uz", 
    "vi", 
    "cy", 
    "xh", 
    "yo", 
    "zu", 
    "fa", 
    "ur"
  ]
}
```
[https://api3aransia.herokuapp.com/get_alphabets_route](https://api3aransia.herokuapp.com/get_alphabets_route)

```json
{
  "alphabets": {
    "af": "Afrikaans Alphabet", 
    "al": "Algerian Alphabet", 
    "ar": "Arabic Alphabet", 
    "az": "Azerbaijani Alphabet", 
    "bo": "Bosnian Alphabet", 
    "ca": "Catalan Alphabet", 
    "co": "Corsican Alphabet", 
    "cs": "Czech Alphabet", 
    "cy": "Welsh Alphabet", 
    "da": "Danish Alphabet", 
    "de": "German Alphabet", 
    "el": "Greek Alphabet", 
    "en": "English Alphabet", 
    "eo": "Esperanto Alphabet", 
    "es": "Spanish Alphabet", 
    "et": "Estonian Alphabet", 
    "eu": "Basque Alphabet", 
    "fa": "Persian Alphabet", 
    "fi": "Finnish Alphabet", 
    "fr": "French Alphabet", 
    "fs": "Frisian Alphabet", 
    "ga": "Irish Alphabet", 
    "gc": "Gaelic Alphabet", 
    "gl": "Galician Alphabet", 
    "ha": "Hausa Alphabet", 
    "hr": "Croatian Alphabet", 
    "ht": "Creole Alphabet", 
    "hu": "Hungarian Alphabet", 
    "hw": "Hawaiian Alphabet", 
    "id": "Indonesian Alphabet", 
    "ig": "Igbo Alphabet", 
    "is": "Icelandic Alphabet", 
    "it": "Italian Alphabet", 
    "ki": "Kinyarwanda Alphabet", 
    "ku": "Kurdish Alphabet", 
    "la": "Latin Alphabet", 
    "li": "Libyan Alphabet", 
    "lt": "Lithuanian Alphabet", 
    "lu": "Luxembourgish Alphabet", 
    "lv": "Latvian Alphabet", 
    "ma": "Moroccan Alphabet", 
    "mg": "Malagasy Alphabet", 
    "mo": "Maori Alphabet", 
    "ms": "Malay Alphabet", 
    "mt": "Maltese Alphabet", 
    "nl": "Dutch Alphabet", 
    "no": "Norwegian Alphabet", 
    "pl": "Polish Alphabet", 
    "pt": "Portuguese Alphabet", 
    "ro": "Romanian Alphabet", 
    "sa": "Samoan Alphabet", 
    "sh": "Shona Alphabet", 
    "sk": "Slovak Alphabet", 
    "sl": "Slovenian Alphabet", 
    "so": "Somali Alphabet", 
    "sq": "Albanian Alphabet", 
    "ss": "Sesotho Alphabet", 
    "su": "Sundanese Alphabet", 
    "sv": "Swedish Alphabet", 
    "sw": "Swahili Alphabet", 
    "tl": "Filipino Alphabet", 
    "tn": "Tunisian Alphabet", 
    "tr": "Turkish Alphabet", 
    "tu": "Turkmen Alphabet", 
    "ur": "Urdu Alphabet", 
    "uz": "Uzbek Alphabet", 
    "vi": "Vietnamese Alphabet", 
    "xh": "Xhosa Alphabet", 
    "yo": "Yoruba Alphabet", 
    "zu": "Zulu Alphabet"
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
