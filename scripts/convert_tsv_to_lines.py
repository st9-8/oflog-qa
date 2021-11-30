#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: st9_8

"""
    Utility command line script used to convert tsv annotated file to txt lines file format.
    Usage:
        python convert_tsv_line.py [filename]
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
    output_file = file_path.parent / 'questions_annoted_ner_data.txt'
    
    if len(sys.argv) == 4:
        if sys.argv[2] == '-o':
            output_file = sys.argv[3]
        else:
            print(f'Error: Unrecogized option "{sys.argv[2]}"')
            sys.exit(1)
            
    with open(file_path) as tsv_file:
        with open(output_file, 'w') as lines:
            tsv_reader = csv.reader(tsv_file, delimiter='\t')
            
            line_text = []
            ner_text = []
            for row in tsv_reader:
                if row:
                    line_text.append(row[0].strip())
                    if len(row[1]) > 1:
                        for word in row[0].split():
                            ner_text.append(row[1])
                    else:
                        ner_text.append(row[1].strip())
                else:
                    if 'question' in file_path.name:
                        lines.write(' '.join(line_text) + ' ?')
                        lines.write('\n')
                        lines.write(' '.join(ner_text))
                        lines.write('\n')
                        lines.write('\n')
                    else:
                        lines.write(' '.join(line_text))
                        lines.write('\n')
                        lines.write(' '.join(ner_text))
                        lines.write('\n')
                    
                    line_text = []
                    ner_text = []

    print('Successfully converted tsv data to line files file')
    print(f'New file saved at: {output_file}')
    
    # python convert_tsv_to_lines.py ../ner/sentences_ner_training_data.tsv -o ../data/CRF_training/sentences_annotated_ner_data.txt
    # python convert_tsv_to_lines.py ../ner/questions_ner_data.tsv -o ../data/CRF_training/questions_annotated_ner_data.txt