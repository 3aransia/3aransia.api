# 3aransia.api

Languages and Dialects transliteration 3aransia API

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

## Usage

### Routes

- /transliterate_moroccan_route/<string:moroccan_entry>
- /transliterate_arabic_moroccan_route/<string:moroccan_arabic_entry>

### Examples

/transliterate_moroccan_route/ktb+bl3rbya+hnaya

```json
{
  "moroccan_arabic_transliteration": "كتب بلعربيا هنايا"
}
```

/transliterate_moroccan_arabic_route/كتب+بلربيا+هنايا

```json
{
  "moroccan_transliteration": "ktb blrbia hnaya"
}
```

### Public API

#### API Link

https://api3aransia.herokuapp.com/

#### Usage 

https://api3aransia.herokuapp.com/transliterate_moroccan_route/ktb+bl3rbya+hnaya

```json
{
  "moroccan_arabic_transliteration": "كتب بلعربيا هنايا"
}
```

https://api3aransia.herokuapp.com/transliterate_moroccan_arabic_route/كتب+بلعربيا+هنايا

```json
{
  "moroccan_transliteration": "ktb bl3rbya hnaya"
}
```

## Other related projects

- [3aransia](https://pypi.org/project/aaransia/) The python library of 3aransia
- [3aransia.web](http://3aransia.com) The web application of 3aransia
