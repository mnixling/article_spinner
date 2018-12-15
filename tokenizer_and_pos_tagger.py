from nltk import word_tokenize
from nltk import pos_tag

with open(r'data\spun_master_text.txt', 'r', encoding='utf-8') as input_file:
    text = input_file.read()
    tok_text = word_tokenize(text)
    pos_text = pos_tag(tok_text)

    with open(r'data\spun_master_pos.txt', 'w', encoding='utf-8') as output_file:
        print(pos_text, file=output_file)
