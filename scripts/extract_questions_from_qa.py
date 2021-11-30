from pathlib import Path

import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Error: Please provide the file to be converted')
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    output_file = '../data/test_questions.txt'
    
    with open(file_path, 'r') as qa_file:
        with open(output_file, 'w') as questions:
            for line in qa_file.readlines():
                if '?' in line:
                    question = line.split('?')[0]
                    question += '?\n'
                    questions.write(question)

    print('Successfully converted extracted questions from qa data file.')
    print(f'New file saved at: {output_file}')