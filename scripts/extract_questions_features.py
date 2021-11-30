#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: st9_8

from os import getenv
from pathlib import Path
from nltk import word_tokenize, pos_tag
from nltk.tag import StanfordNERTagger

import sys


"""
    Utility script used to extract all features from questions
    1. Question word
    2. NER
    3. POS
    4. Question type: type of output needed by this question
    5. Comparison keywords, identified as RB(*)
    6. Delimiters: Some word find in a predefined set (in, by, during, on)
    7. Triples from question
"""


def extract_qword(question):
    """
        Function used to extract question word in question sentence

        Question words: who | which
    """
    if 'who' in question.lower():
        return 'who'
    elif 'which' in question.lower():
        return 'which'

    return None


def extract_ner(question):
    """
        Function used to extract NER tags from question sentence
    """
    model = StanfordNERTagger(
        getenv('OFLOG_NER_QUESTIONS_TAGGER'), getenv('STANFORD_NER'))
    question_tokens = word_tokenize(question)

    ner_tagged_question = ' '.join(
        [f'{word}/{ner}' for word, ner in model.tag(question_tokens)])

    return ner_tagged_question


def extract_pos(question):
    """
        Function used to extract POS tags from question sentence
    """

    tokens = word_tokenize(question)
    pos_tagged_question = ' '.join(
        [f'{word}/{pos}' for word, pos in pos_tag(tokens)])

    return pos_tagged_question


def extract_question_type(question):
    """
        Function used to extract question type from question

        The process for now it is purely deterministic
            - Who: LogUser
            - Which: LogResource
    """

    qword = extract_qword(question)
    if qword == 'who':
        return 'LogUser'
    elif qword == 'which':
        return 'LogResource'

    return None


def extract_comparison_words(question):
    """
        Function used to extract comparison words in question
    """

    tokens = word_tokenize(question.lower())
    pos_tags = pos_tag(tokens)
    comp_words = [word for word, pos in pos_tags if 'RB' in pos or 'JJ' in pos]

    return ', '.join(comp_words) or None


def extract_delimiters(question):
    """
        Function used to extract delimiter word in question
    """

    delimiters = ['by', 'during', 'in', 'on']

    present_delimiters = []
    tokens = word_tokenize(question)

    for delm in delimiters:
        if delm in tokens:
            present_delimiters.append(delm)

    return ', '.join(present_delimiters) or None


def extract_triples(question):
    """
        Function used to extract triples from question sentence
    """

    raise NotImplemented


def extract_headword(question):
    """
        Function used to extract headword
    """

    raise NotImplemented


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Error: Please provide the file to be converted')
        sys.exit(1)

    file_path = Path(sys.argv[1])
    output = file_path.parent / 'questions_extra_features.txt'

    if len(sys.argv) == 4:
        if sys.argv[2] == '-o':
            output = sys.argv[3]
        else:
            print(f'Error: Unrecogized option "{sys.argv[2]}"')
            sys.exit(1)

    with open(file_path) as data_file:
        with open(output, 'w') as extra_features_file:
            for line in data_file.readlines():
                qword = extract_qword(line)
                # pos = extract_ner(line)
                # ner = extract_pos(line)
                qtype = extract_question_type(line)
                comparison_words = extract_comparison_words(line)
                delimiters = extract_delimiters(line)

                extra_features_file.write(line)
                if qword:
                    extra_features_file.write(qword)
                    extra_features_file.write('\n')
                else:
                    extra_features_file.write('-')
                    extra_features_file.write('\n')
                if qtype:
                    extra_features_file.write(qtype)
                    extra_features_file.write('\n')
                else:
                    extra_features_file.write('-')
                    extra_features_file.write('\n')
                if comparison_words:
                    extra_features_file.write(comparison_words)
                    extra_features_file.write('\n')
                else:
                    extra_features_file.write('-')
                    extra_features_file.write('\n')
                if delimiters:
                    extra_features_file.write(delimiters)
                    extra_features_file.write('\n')
                else:
                    extra_features_file.write('-')
                    extra_features_file.write('\n')
                extra_features_file.write('\n')

    print('Successfully extracted features file')
    print(f'New file saved at: {output}')

# python extract_questions_features.py ../data/full_training/questions.txt -o ../data/CRF_training/questions_extra_features.txt