import os
import glob
from bs4 import BeautifulSoup as BS

"""
1. Glob each speaker's individual folder's content into a list
2. Iterate over the list to extract the talk
3. Save the talk in the source_data folder as <speaker>_talk_0<(#)#>.txt
"""


speakers = ['russell-m-nelson', 'dallin-h-oaks']

def glob_file():
    glob_file_list = []
    for i in speakers:
        partial_path = r'nix_semester_project\100_speaker_data\{}\source_data'.format(i)

        for filename in sorted(glob.glob(os.path.join(partial_path, '*.html'))):
            glob_file_list.append(filename)
    return glob_file_list


for filename in glob_file():
    with open(filename, 'r', encoding='utf-8') as input_file:
        html_code = input_file.read()
        html_soup = BS(html_code, 'html.parser')


        with open(filename.replace('html', '.txt'), 'w', encoding='utf-8') as txt_file:
            if html_soup is not None:
                for talk_title in html_soup.find_all('html'):
                    print(talk_title.title.string, file=txt_file)
                    for p in html_soup.find_all('p'):
                        text = p.get_text()
                        print(text, file=txt_file)

