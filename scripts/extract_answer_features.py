#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: st9_8
from nltk import word_tokenize, pos_tag

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

    raise NotImplemented


def extract_pos(question):
    """
        Function used to extract POS tags from question sentence
    """

    raise NotImplemented


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
