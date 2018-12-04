import glob
import os

speakers = ['russell-m-nelson', 'dallin-h-oaks']

def glob_file():
    glob_file_list = []
    for i in speakers:
        partial_path = r'nix_semester_project\100_speaker_data\{}\source_data'.format(i)

        for filename in sorted(glob.glob(os.path.join(partial_path, '*.txt'))):
            glob_file_list.append(filename)
    return glob_file_list

def create_master_txt():
    for filename in glob_file():
        with open(filename, 'r', encoding='utf-8') as input_txt:
            with open('master_txt.txt', 'a', encoding='utf-8') as output_txt:
                text = input_txt.read()
                print(text, file=output_txt)


create_master_txt()
