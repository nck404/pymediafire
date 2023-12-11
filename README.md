<h1 align="center">
  mediafire-dl
</h1>

## Description

**mediafire-dl** is a script written in Python to automate the download of files from [mediafire.com](https://mediafire.com) with a simple command-line interface.


## Prerequisites

It is necessary to have **python3** and **pip3**


## Installation

```bash
pip3 install git+https://github.com/nck404/pymediafire
```

## Usage

### From Command Line

```bash
$ # mediafire-dl mediafire_link_1 

$ # mediafire-dl mediafire_link_1 mediafire_link_2 mediafire_link_3
```

### From Python

```python
import mediafire_dl

url = 'https://mediafire.com/xx/xx/file.zip'
output = 'file.zip'
mediafire_dl.download(url, output, quiet=False)
```

