import os
import sys
import csv
import json
import pandas as pd

def validate_jsonl(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            data=list(file)
            for line in data:
                row_data=json.loads(line)
            return True
    except:
        return False
    
def write_to_csv(input_file_path,csv_output_file_path):
    try:
        print('Writing to CSV file Started')
        with open(input_file_path, 'r') as file:
            data=list(file)
            csv_data=[]
            for line in data:
                line_data=json.loads(line)
                line_data_list=[]
                for message in line_data["messages"]:
                    line_data_list.append(message["content"])
                csv_data.append(line_data_list)
            with open(csv_output_file_path, 'w', newline='') as csvfile:  
                csvwriter = csv.writer(csvfile)  
                csvwriter.writerows(csv_data)
        print('Writing to CSV file Completed')
            
    except:
        print('Writing to CSV file Failed')

def write_to_xlsx(csv_output_file_path,xlsx_output_file_path):
    try:
        print('Writing to XLSX file Started')
        df = pd.read_csv(csv_output_file_path, header=None)
        excelWriter = pd.ExcelWriter(xlsx_output_file_path)
        df.to_excel(excelWriter, index=False, header=None)
        excelWriter._save()
        print('Writing to XLSX file Completed')
    except:
        print('Writing to XLSX file Failed')

n = len(sys.argv)
if n!=2:
    print("Invalid number of arguments\nCorrect Command Schema : python '.\Chat Completions - JSONL to CSV and XLSX.py' [Input Filename]")
    print('Aborting Execution...')
else:
    input_file_path=sys.argv[1].replace('.\\','')
    csv_output_file_path=input_file_path.replace('.jsonl','.csv')
    xlsx_output_file_path=input_file_path.replace('.jsonl','.xlsx')
    print("Input File Path : " + input_file_path)
    print("CSV Output File Path : " + csv_output_file_path)
    print("XLSX Output File Path : " + xlsx_output_file_path)

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
            write_to_csv(input_file_path, csv_output_file_path)
            write_to_xlsx(csv_output_file_path, xlsx_output_file_path)
        else:
            print('Validating JSONL file Completed - JSONL file is Invalid')
            print('Aborting Execution...')
    else:
        print("Only JSONL file is allowed as input")
        print('Aborting Execution...')
        exit()