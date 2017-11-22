# Frequency Analysis of Words
The script looks in the specified text file ten most frequent words
# How to ise
The script requires the installed Python interpreter version 3.5 To call the help, run the script with the -h or --help option.
```bash
~$python lang_frequency.py -h
usage: lang_frequency.py [-h] file_path
positional arguments:
  file_path   file path to find top 10 words
optional arguments:
  -h, --help  show this help message and exit
```
To start searching for most frequent words in a text file, you must specify the path to the text file using the space after the script is called.
```bash
~$python lang_frequency.py war.txt
Ten most repetitive words in the text and the number of their repetitions:
"и" = 10649
"в" = 5308
"не" = 4404
"что" = 3954
"он" = 3825
"на" = 3383
"с" = 3108
"как" = 2151
"я" = 1959
"его" = 1937
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
