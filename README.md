# enstack_backend_test

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)

## Features

- Solution for BE Test:
    1. test_a.py
    2. test_b.py

- Solution for App that collects accelerometer data:
    * test_c_a.md
    * test_c_b.md

- Solution for API Server Test built in Flask:
    * test_d.py

## Installation

Make sure Python 3.12 is installed on your system.

### Install Python 3.12

#### Ubuntu / Debian

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev
```

#### macOS (using Homebrew)
```bash
brew install python@3.12
brew link --overwrite python@3.12
```

#### Windows

```bash
Download the installer from the official Python website.

Run the installer and ensure "Add Python to PATH" is checked.

Choose "Customize installation" and ensure pip and venv are selected.
```

#### ✅ Verify the installation:
```bash
python3.12 --version
```

#### Create and Activate Virtual Environment
```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### ✅ To Run Test for BE Test & API Server:
```bash
python -v
```
