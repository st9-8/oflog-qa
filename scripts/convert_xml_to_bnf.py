def extract_pos_from_candidate(text, pos, word_index):
    """
        Utility function used to extract chunking pos for a word
    """
    
    if len(text) != len(pos):
        return
    
    index, word = word_index[0], word_index[1]
    
    if index == 0:
        return f'pos[0]={pos[0]}\tpos[0]|pos[1]={pos[0]}|{pos[1]}\tpos[0]|pos[1]|pos[2]={pos[0]}|{pos[1]}|{pos[2]}'
    elif  index == 1:
        return f'pos[-1]={pos[index-1]}\tpos[-1]|pos[0]={pos[index-1]}|{pos[index]}\tpos[-1]|pos[0]|pos[1]={pos[index-1]}|{pos[index]}|{pos[index+1]}'
    elif index == len(text) - 1:
        return f'pos[-2]={pos[index-2]}\tpos[-2]|pos[-1]={pos[index-2]}|{pos[index-1]}\tpos[-2]|pos[-1]|pos[0]={pos[index-2]}|{pos[index-1]}|{pos[index]}'
    elif index == len(text) - 2:
        return f'pos[-2]={pos[index-2]}\tpos[-2]|pos[-1]={pos[index-2]}|{pos[index-1]}\tpos[-2]|pos[-1]|pos[0]={pos[index-2]}|{pos[index-1]}|{pos[index]}\tpos[0]={pos[index]}\tpos[0]|pos[1]={pos[index]}|{pos[index+1]}'
    else:
        return f'pos[-2]={pos[index-2]}\tpos[-2]|pos[-1]={pos[index-2]}|{pos[index-1]}\tpos[-2]|pos[-1]|pos[0]={pos[index-2]}|{pos[index-1]}|{pos[index]}\tpos[0]={pos[index]}\tpos[0]|pos[1]={pos[index]}|{pos[index+1]}\tpos[0]|pos[1]|pos[2]={pos[index]}|{pos[index+1]}|{pos[index+2]}'


def extract_ner_from_candidate(text, ner, word_index):
    """
        Utility function used to extract chunking ner for a word
    """
    
    if len(text) != len(ner):
        return
    
    index, word = word_index[0], word_index[1]
    
    if index == 0:
        return f'ner[0]={ner[0]}\tner[0]|ner[1]={ner[0]}|{ner[1]}\tner[0]|ner[1]|ner[2]={ner[0]}|{ner[1]}|{ner[2]}'
    elif  index == 1:
        return f'ner[-1]={ner[index-1]}\tner[-1]|ner[0]={ner[index-1]}|{ner[index]}\tner[-1]|ner[0]|ner[1]={ner[index-1]}|{ner[index]}|{ner[index+1]}'
    elif index == len(text) - 1:
        return f'ner[-2]={ner[index-2]}\tner[-2]|ner[-1]={ner[index-2]}|{ner[index-1]}\tner[-2]|ner[-1]|ner[0]={ner[index-2]}|{ner[index-1]}|{ner[index]}'
    elif index == len(text) - 2:
        return f'ner[-2]={ner[index-2]}\tner[-2]|ner[-1]={ner[index-2]}|{ner[index-1]}\tner[-2]|ner[-1]|ner[0]={ner[index-2]}|{ner[index-1]}|{ner[index]}\tner[0]={ner[index]}\tner[0]|ner[1]={ner[index]}|{ner[index+1]}'
    else:
        return f'ner[-2]={ner[index-2]}\tner[-2]|ner[-1]={ner[index-2]}|{ner[index-1]}\tner[-2]|ner[-1]|ner[0]={ner[index-2]}|{ner[index-1]}|{ner[index]}\tpos[0]={ner[index]}\tner[0]|ner[1]={ner[index]}|{ner[index+1]}\tner[0]|ner[1]|ner[2]={ner[index]}|{ner[index+1]}|{ner[index+2]}'
    
    
def extract_question_features(qword, qtext, qtype, qpos, qner, qheadwords, qcomps, qdels):
    """
        Utility function used to extract question related feature
    """
    
    features = []
    headwords = ''
    headwords_pos = ''
    headwords_ner = ''
    
    comparisons = ''
    comparisons_pos = ''
    comparisons_ner = ''
    
    delimiters = ''
    delimiters_pos = ''
    delimiters_ner = ''
    
    qword_pos = qpos[qtext.index(qword)]
    qword_ner = qner[qtext.index(qword)]
    qwords = f'qword|qword_pos|qword_ner={qword}|{qword_pos}|{qword_ner}'
    
    names = []
    values = []
    names_pos = []
    values_pos = []
    names_ner = []
    values_ner =[]
    
    features.append(qwords)
    features.append(f'qtype={qtype}')
    
    h_pos = ''
    h_ner = ''
    
    for index, headword in enumerate(qheadwords):
        names.append(f'qheadword[{index}]')
        values.append(f'{headword}')
        headwords = f'{"|".join(names)}={"|".join(values)}'
        
        names_pos.append(f'qheadword_pos[{index}]')
        if len(headword.split()) > 1:
            h_pos = ' '.join([qpos[qtext.index(h)] for h in headword.split()])
        values_pos.append(f'{h_pos}')
        headwords_pos = f'{"|".join(names_pos)}={"|".join(values_pos)}'
        
        names_ner.append(f'qheadword_ner[{index}]')
        if len(headword.split()) > 1:
            h_ner = ' '.join([qner[qtext.index(h)] for h in headword.split()])
        values_ner.append(f'{h_ner}')
        headwords_ner = f'{"|".join(names_ner)}={"|".join(values_ner)}'
    
    features.append(headwords)
    features.append(headwords_pos)
    features.append(headwords_ner)
    
    names = []
    values = []
    names_pos = []
    values_pos = []
    names_ner = []
    values_ner = []
    
    if '-' not in qcomps:
        for index, comp in enumerate(qcomps):
            names.append(f'qcomp[{index}]')
            values.append(f'{comp}')
            comparisons = f'{"|".join(names)}={"|".join(values)}'

            names_pos.append(f'qcomp_pos[{index}]')
            values_pos.append(f'{qpos[qtext.index(comp)]}')
            comparisons_pos = f'{"|".join(names_pos)}={"|".join(values_pos)}'

            names_ner.append(f'qcomp_ner[{index}]')
            values_ner.append(f'{qner[qtext.index(comp)]}')
            comparisons_ner = f'{"|".join(names_ner)}={"|".join(values_ner)}'

        features.append(comparisons)
        features.append(comparisons_pos)
        features.append(comparisons_ner)

        names = []
        values = []
        names_pos = []
        values_pos = []
        names_ner = []
        values_ner = []
    
    if '-' not in qdels:
        for index, delimiter in enumerate(qdels):
            names.append(f'qdelimiter[{index}]')
            values.append(f'{delimiter}')
            delimiters = f'{"|".join(names)}={"|".join(values)}'

            names_pos.append(f'qdelimiter_pos[{index}]')
            values_pos.append(f'{qpos[qtext.index(delimiter)]}')
            delimiters_pos = f'{"|".join(names_pos)}={"|".join(values_pos)}'

            names_ner.append(f'qdelimiter_ner[{index}]')
            values_ner.append(f'{qner[qtext.index(delimiter)]}')
            delimiters_ner = f'{"|".join(names_ner)}={"|".join(values_ner)}'

        features.append(delimiters)
        features.append(delimiters_pos)
        features.append(delimiters_ner)

        names = []
        values = []
        names_pos = []
        values_pos = []
        names_ner = []
        values_ner = []
    
    return '\t'.join(features)

def write_to_disk(crf_lines, output):
    """
        Utility function used to write to disk the formatted data
    """
    
    with open(output, 'w') as bnf_file:
        for line in crf_lines:
            bnf_file.write('\t'.join(line))
            bnf_file.write('\n')
    
    print('Successfully converting XML file format to BNF file format.')
    print(f'New file saved at: {output}')

if __name__ == '__main__':
    from pathlib import Path

    import sys
    import xml.etree.ElementTree as ET
    
    if len(sys.argv) <= 1:
        print('Error: Please provide the file to be converted')
        sys.exit(1)

    file_path = Path(sys.argv[1])
    output = file_path.parent / file_path.name.replace('xml', 'bnf')

    if len(sys.argv) == 4:
        if sys.argv[2] == '-o':
            output = sys.argv[3]
        else:
            print(f'Error: Unrecogized option "{sys.argv[2]}"')
            sys.exit(1)
            
    qa = ET.parse(file_path)
    root = qa.getroot()
    
    pair = []
    B, I, O = 'B-ANS', 'I-ANS', 'O-ANS'

    crf_lines = []
    
    count_qa = 1
    count_cand = 1
    for qa_pair in root:
        question = qa_pair.find('question')
        question_text = question.text.split('\n')[1].strip().split()
        question_pos = question.text.split('\n')[2].strip().split()
        question_ner = question.text.split('\n')[3].strip().split()
        question_qword = question.text.split('\n')[4].strip()
        question_qtype = question.text.split('\n')[5].strip()
        question_comparisons = question.text.split('\n')[6].strip().split(',')
        question_comparisons = list(map(lambda item: item.strip(), question_comparisons))
        question_delimiters = question.text.split('\n')[7].strip().split(',')
        question_delimiters = list(map(lambda item: item.strip(), question_delimiters))
        question_headwords = question.text.split('\n')[8].strip().split(',')
        question_headwords = list(map(lambda item: item.strip(), question_headwords))
        
        # print(question.text.split('\n')[1].strip())
        
        # For candidate
        # pos[-2], pos[-2]|pos[-1], pos[-2]|pos[-1]|pos[0], pos[0], pos[0]|pos[1], pos[0]|pos[1]|pos[2]
        # ner[-2], ner[-2]|ner[-1], ner[-2]|ner[-1]|ner[0], ner[0], ner[0]|ner[1], ner[0]|ner[1]|ner[2]
        # qword
        # atype
        # qcomp[1], qcomp[2]
        # qdel[1], qdel[0]
        # WMD
        # qheadword
        # B-ANS, I-ANS, O-ANS
        
        for candidate in qa_pair.findall('candidate'):
            text = candidate.text.split('\n')[1].strip().split()
            pos = candidate.text.split('\n')[2].strip().split()
            ner = candidate.text.split('\n')[3].strip().split()
            distance = candidate.text.split('\n')[4].strip()
            answers = candidate.text.split('\n')[5].strip().split(',')
            answers = list(map(lambda item: item.strip(), answers))
            
            # Extract token for answer
            answer_tagged = []
            for answer in answers:
                if answer != '-':
                    answer_tokens = answer.split()
                    answer_tagged = [(answer_tokens[0], B)]
                    answer_tagged.extend([(token, I) for token in answer_tokens[1:]])
            
            # print(f'QAPair {count_qa}')
            # print(f'\tCandidate {count_cand}: {answer_tagged}')
            
            dict_tagged = dict(answer_tagged)
            for index, text_token in enumerate(text):
                if answer_tagged:
                    if text_token in dict_tagged.keys():
                        crf_lines.append([dict_tagged[text_token], extract_pos_from_candidate(text, pos, (index, text_token)), 
                                        extract_ner_from_candidate(text, ner, (index, text_token)), f'wdm={distance}', extract_question_features(question_qword, question_text, question_qtype, question_pos, question_ner, question_headwords, question_comparisons, question_delimiters)])
                    else:
                        crf_lines.append([O, extract_pos_from_candidate(text, pos, (index, text_token)),
                                        extract_ner_from_candidate(text, ner, (index, text_token)), f'wdm={distance}', extract_question_features(question_qword, question_text, question_qtype, question_pos, question_ner, question_headwords, question_comparisons, question_delimiters)])
                        
                else:
                    crf_lines.append([O, extract_pos_from_candidate(text, pos, (index, text_token)),
                                    extract_ner_from_candidate(text, ner, (index, text_token)), f'wdm={distance}', extract_question_features(question_qword, question_text, question_qtype, question_pos, question_ner, question_headwords, question_comparisons, question_delimiters)])
                    
            
            
            # print(f'\tCandidate {count_cand}: {crf_lines}')
            count_cand += 1
        count_qa += 1

    write_to_disk(crf_lines, output)