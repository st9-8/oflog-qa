#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: st9_8

"""
    Utility command line script used to convert doccano annotated file to tsv file format.
    Usage:
        python convert_doccano_to_tsv.py [filename]
"""


from pathlib import Path

import sys
import csv
import json


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Error: Please provide the file to be converted')
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    output_file = file_path.parent / 'questions_annoted_ner_data.tsv'
    
    with open(file_path) as doccano_file:
        doccano_data = json.load(doccano_file)
        with open(output_file, 'w') as ner:
            ner_writer = csv.writer(ner, delimiter='\t')
            for data_item in doccano_data:
                for label in data_item['label']:
                    word = data_item['data'][label[0]:label[1]+1]
                    label_tag = label[2]
                    ner_writer.writerow([word, label_tag])

    print('Successfully converted doccano data to tsv file')
    print(f'New file saved at: {output_file}')