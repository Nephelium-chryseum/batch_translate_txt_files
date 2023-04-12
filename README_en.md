# Batch Text File Translator

This Python script uses the googletrans library to batch translate all .txt files in a specified folder from one language to another. It leverages the Google Translate service to perform the translations.

## Requirements

- Python 3.6 or later
- googletrans library (version 4.0.0-rc1)

## Installation

1. Make sure you have Python 3.6 or later installed on your system. You can check the Python version by running `python --version` or `python3 --version`.

2. Install the required library using pip:

pip install -r requirements.txt


## Usage

1. Open the script in a text editor and replace 'path/to/input/folder' with the path to the folder containing the .txt files you want to translate. Similarly, replace 'path/to/output/folder' with the path to the folder where you want to save the translated files.

2. Set the `source_language` and `destination_language` variables to the appropriate language codes (e.g., 'en' for English, 'es' for Spanish, 'zh-CN' for Simplified Chinese).

3. Run the script using the command:

python batch_translate_txt_files.py


The script will process each .txt file in the input folder, translate its content, and save the translated text to a new file with the same name in the output folder.

## Language Codes

You can find the supported language codes for Google Translate here:

[https://cloud.google.com/translate/docs/languages](https://cloud.google.com/translate/docs/languages)

---

**Author:** Nephelium & GPT4
**Date:** April 4, 2023