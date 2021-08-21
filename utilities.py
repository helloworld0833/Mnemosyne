def parser(file_input):
    try:
        file_input = file_input.decode('utf-8')
    except UnicodeDecodeError:
        file_input = file_input.decode('gbk')

    lines = []
    for line in file_input.split('\r'):
        if line.strip():
            lines.append(line.strip()+'\n')

    return lines

def read_words_from_file(file_name):
    with open(file_name, 'a+b') as f:
        f.seek(0)
        return parser(f.read())

def write_word_to_file(word, meaning, file_name):
    with open(file_name, 'a') as f:
        f.write('{} {} 100\n'.format(word, meaning))

def update_file(data_list, file_name):
    with open(file_name, 'w') as f:
        for data_line in data_list:
            f.write(data_line)
