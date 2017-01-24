# NLP - Formal and Geolocation Features Extraction
This is a Python 2 project about Natural Language Processing and specially about geolocation features extraction from a corpus. We use the known NLTK and some other python modules. We used an annotated corpus as input. Corpus has the same structure with the corpus in [this](https://github.com/sp1thas/thesis/tree/master/dev) project.
-  [geolocation.py](geolocation.py)

This scripts extract general features for Natural Language Processing. For example calculates chars per document or symbols per document etc. For more info check the script.

- [general.py](general.py)

This script extract geolocation features for english documents. Author's nationality is necessary.

- [both.py](both.py)

This script extract both general and geolocation features.

## Pre-requirements
* NLTK
* Dataset with correct annotations.

### Python 2 modules Installation
run as root:
```bash
pip install -r requirements.txt
```

## Author
Simakis Panagiotis (Initial Work)

## Licence
This project is licensed under the GNU General Public License version 3 - see the [LICENSE](LICENSE) file for details
