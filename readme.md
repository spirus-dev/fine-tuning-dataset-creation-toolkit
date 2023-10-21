# Introduction
This `Fine Tuning Dataset Creation Toolkit` will help you in creation of JSONL dataset files that are needed for fine tuning `Completions` models like `babbage-002` or `davinci-002` and `Chat completions` model like `gpt-35-turbo-0613` from XLSX and CSV files. These JSONL dataset files can be used to fine tune models in OpenAI or Azure OpenAI.

# Prerequisites
1. `Python 3.10+` installed
2. `virtualenv` package installed in Python

# Initial Setup
1. Create and activate a virtual environment
2. Install dependencies
3. Create a dataset in XLSX or CSV file

## 1. Create virtual environment
1. To create a virtual environment, open terminal in your working directory and execute this command  :

        python -m venv .venv
2. To activate virtual environment, execute this command in the terminal :
        
        ./.venv/Scripts/activate

## 2. Install dependencies
1. To install the dependencies needed to run this kit, execute this command in terminal :

        pip install -r requirements.txt

## 3. Create a dataset in XLSX or CSV file
1. To create a dataset, create a XLSX or CSV file. You can take reference from XLSX or CSV files inside `Sample` folder.
2. This XLSX or CSV file needs to be in your working directory. `[IMPORTANT]`

# How to use?

1. Convert XLSX/CSV dataset file to JSONL dataset file
2. Validate JSONL dataset file
3. Analyze JSONL dataset file `[FOR COMPLETIONS JSONL DATASET ONLY]`
4. Convert JSONL dataset files to XLSX and CSV files `[EXTRA]`

## 1. Convert XLSX/CSV to JSONL
1. Based on the model your JSONL dataset file will be targetting for fine tuning, there are different scripts that you can use
2. If you are creating dataset for `Completions` models like `babbage-002` or `davinci-002`, the script you should be using is `Completions Dataset Formatter.py`. This is how you should execute the script : 

        python 'Completions Dataset Formatter.py' [XLSX/CSV Filename]
3. If you are creating dataset for `Chat Completions` model like `gpt-35-turbo-0613`, the script you should be using is `Chat Completions Dataset Formatter.py`. This is how you should execute the script : 

        python 'Chat Completions Dataset Formatter.py' [XLSX/CSV Filename]
4. Both of them will create a JSONL dataset file in your working directory with name same as input XLSX/CSV file.

## 2. Validate JSONL dataset file
1. To validate JSONL files, you can make use of `JSONL Validator.py` script
2. This script will return output as `Valid` or `Invalid` based on the input file.
3. This is how you should execute the script : 

        python 'JSON Validator.py' [JSONL Filename]
4. This script can validate JSONL dataset files created for both `Completions` and `Chat Completions` models.

## 3. Analyze JSONL dataset file
1. This is only applicable to the datasets created for `Completions` models like `babbage-002` or `davinci-002`.
2. To analyze the JSONL dataset files, execute this command in your terminal :

        openai tools fine_tunes.prepare_data -f [JSON Filename]
3. More details can be found [[here]](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/fine-tuning?tabs=completionfinetuning&pivots=programming-language-studio#openai-cli-data-preparation-tool)

## 4. Convert JSONL dataset files to XLSX and CSV files
1. Based on the model your JSONL dataset file will be targetting for fine tuning, there are different scripts that you can use
2. To create XLSX and CSV files from JSONL file that was created for fine tuning of `Completions` models like `babbage-002` or `davinci-002`, the script you should be using is `Completions - JSONL to CSV and XLSX.py`. This is how you should execute the script : 

        python 'Completions - JSONL to CSV and XLSX.py' [JSONL Filename]
3. To create XLSX and CSV files from JSONL file that was created for fine tuning of `Chat Completions` model like `gpt-35-turbo-0613`, the script you should be using is `Chat Completions - JSONL to CSV and XLSX.py`. This is how you should execute the script : 

        python 'Chat Completions - JSONL to CSV and XLSX.py' [JSONL Filename]
4. Both of them will create a XLSX and CSV file in your working directory with name same as input JSON file.

# Thank you!
This toolkit saved me a lot of time in creating dataset files for fine tuning jobs. If it also helps you to save your time, then please share this with your friends and colleagues. Please don't forget to give it a ⭐. Feel free to raise an issue or send a PR for improvements.