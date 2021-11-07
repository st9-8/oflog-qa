#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: st9_8

"""
    Utility command line script used to tag input file with POS class.
    Usage:
        python pos_tag.py [filename]
        python pos_tag.py -with_punc [filename]
        
        -with_punc: argument used to include punctiation in file tagging, default to False
"""


from pathlib import Path
from nltk import word_tokenize, pos_tag

import sys
import string

with_punc = False
file_position = 1

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Error: Please provide the file to be converted')
        sys.exit(1)

    if len(sys.argv) == 3:
        if sys.argv[1] != '-with_punc':
            print(f'Error: Unrecognized argument \'{sys.argv[1]}\'')
            sys.exit(1)
        with_punc = True
        file_position = 2
    
    
    file_path = Path(sys.argv[file_position])
    output = file_path.parent / 'sentences_pos_tagged.txt'
    count = 1
    

    with open(file_path) as datafile:
        with open(output, 'w') as posfile:
            print('Processing...')
            for line in datafile.readlines():
                if len(line) > 1:
                    if not with_punc:
                        line = line.replace('(', ' (')
                        table = str.maketrans('', '', string.punctuation)
                        line = line.translate(table)
                        
                    tokens = word_tokenize(line)
                    pos_line = ' '.join(
                        [f'{word}/{pos}' for word, pos in pos_tag(tokens)])

                    posfile.write(pos_line + '\n\n')
                    count += 1

    print('Successfully tagged input data with POS class')
    print(f'{count} lines tagged')
    print(f'New file saved at: {output}')
