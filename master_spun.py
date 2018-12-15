import os
import glob


def glob_file_spun_data():
    glob_file_spun_list = []
    spun_data_rel_path = r'data\spun_data'

    for file_name in glob.glob(os.path.join(spun_data_rel_path, '*.txt')):
        glob_file_spun_list.append(file_name)
    return glob_file_spun_list


def create_spun_master_txt():
    for filename in glob_file_spun_data():
        with open(filename, 'r', encoding='utf-8') as input_txt:
            with open('data\spun_master_text.txt', 'a', encoding='utf-8') as output_txt:
                text = input_txt.read()
                print(text, file=output_txt)


create_spun_master_txt()
