import os
import sys
import json

def validate_jsonl(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            data=list(file)
            for line in data:
                row_data=json.loads(line)
            return True
    except:
        return False

n = len(sys.argv)
if n!=2:
    print("Invalid number of arguments\nCorrect Command Schema : python '.\JSONL Validator.py' [Input Filename]")
    print('Aborting Execution...')
else:
    input_file_path=sys.argv[1].replace('.\\','')

    print("Input File Path : " + input_file_path)

    print("Check if input file exists Started")
    if not os.path.isfile(input_file_path):
        print("Check if input file exists Completed - Input file does not exist")
        print('Aborting Execution...')
        exit()
    print("Check if input file exists Completed - Input file exists")

    if input_file_path.endswith('.jsonl'):
        print('Validating JSONL file Started')
        result=validate_jsonl(input_file_path)
        if result is True:
            print('Validating JSONL file Completed - JSONL file is Valid')
        else:
            print('Validating JSONL file Completed - JSONL file is Invalid')
    else:
        print("Only JSONL file is allowed as input")
        print('Aborting Execution...')
        exit()