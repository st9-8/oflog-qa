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
output = ''

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Error: Please provide the file to be converted')
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if len(sys.argv) == 3:
        if sys.argv[1] == '-with_punc':
            file_path = Path(sys.argv[2])
            output = file_path.parent / 'sentences_pos_tagged.txt'
        else:
            print(f'Error: Unrecognized argument \'{sys.argv[1]}\'')
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[2] == '-o':
            output = sys.argv[3]
        else:
            print(f'Error: Unrecogized option "{sys.argv[2]}"')
            sys.exit(1)

    count = 1

    with open(file_path) as datafile:
        with open(output, 'w') as pos_file:
            print('Processing...')
            for line in datafile.readlines():
                line_text = []
                pos_text = []
                if len(line) > 1:
                    if not with_punc:
                        line = line.replace('(', ' (')
                        table = str.maketrans('', '', string.punctuation)
                        line = line.translate(table)

                    tokens = word_tokenize(line)
                    for word, pos in pos_tag(tokens):
                        line_text.append(word)
                        pos_text.append(pos)

                    if 'question' in file_path.name:
                        pos_file.write(' '.join(line_text) + ' ?')
                    else:
                        pos_file.write(' '.join(line_text))
                    pos_file.write('\n')
                    pos_file.write(' '.join(pos_text))
                    pos_file.write('\n')
                    pos_file.write('\n')

                    count += 1

    print('Successfully tagged input data with POS class')
    print(f'{count} lines tagged')
    print(f'New file saved at: {output}')

# python pos_tagger.py ../data/full_training/sentences.txt -o ../data/CRF_training/sentences_annotated_pos_data.txt
# python pos_tagger.py ../data/full_training/questions.txt -o ../data/CRF_training/questions_annotated_pos_data.txt
