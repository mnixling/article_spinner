import os
import glob
import re
from string import punctuation as punct

import nltk
from nltk.tokenize import sent_tokenize

speakers = ['russell-m-nelson', 'dallin-h-oaks', 'henry-b-eyring',
            'm-russell-ballard', 'jeffrey-r-holland', 'dieter-f-uchtdorf',
            'david-a-bednar', 'quentin-l-cook', 'd-todd-christofferson',
            'neil-l-andersen', 'ronald-a-rasband', 'gary-e-stevenson',
            'dale-g-renlund', 'gerrit-w-gong', 'ulisses-soares',
            'angel-abrea', 'reyna-i-aburto', 'marcos-a-aidukaitis',
            'silvia-h-allred', 'jose-l-alonso', 'carlos-h-amado',
            'wilford-w-andersen', 'koichi-aoyagi', 'ian-s-ardern',
            'mervyn-b-arnold', 'carlos-e-asay', 'brian-k-ashton',
            'marvin-j-ashton', 'eduardo-ayala', 'robert-l-backman',
            'steven-r-bangerter', 'ben-b-banks', 'w-mark-bassett',
            'merrill-j-bateman', 'david-s-baxter', 'david-l-beck',
            'julie-b-beck', 'randall-k-bennett', 'ezra-taft-benson',
            'jean-b-bingham', 'shayne-m-bowen', 'william-r-bradford',
            'mark-a-bragg', 'ted-e-brewerton', 'm-joseph-brough',
            'monte-j-brough', 'l-edward-brown', 'dean-r-burgess',
            'h-david-burton', 'linda-k-burton', 'f-enzio-busche',
            'douglas-l-callister', 'tad-r-callister', 'helio-r-camargo',
            'george-i-cannon', 'robert-w-cantwell', 'craig-a-cardon',
            'bruce-a-carlson', 'matthew-l-carpenter', 'gerald-j-causse',
            'sheldon-f-child', 'yoon-h-choi', 'albert-choules-jr',
            'craig-o-christensen', 'shirley-d-christensen',
            'darwin-b-christenson', 'kim-b-clark', 'don-r-clark',
            'j-richard-clarke', 'l-whitney-clayton', 'weatherford-t-clayton',
            'gayle-m-clegg', 'gary-j-coleman', 'spencer-j-condie',
            'carl-b-cook', 'gene-r-cook', 'mary-n-cook', 'richard-e-cook',
            'lawrence-e-corbridge', 'bonnie-h-cordon', 'valeri-v-cordon',
            'j-devn-cornish', 'claudio-r-m-costa', 'joaquin-e-costa',
            'michelle-d-craig', 'rulon-g-craven', 'legrand-r-curtis',
            'derek-a-cuthbert', 'charles-w-dahlquist-ii', 'elaine-s-dalton',
            'adhemar-damiani', 'dean-myron-davies', 'massimo-de-feo',
            'benjamin-de-hoyos', 'robert-k-dellenbach', 'royden-g-derrick',
            'gordon-b-hinckley', 'thomas-s-monson', 'james-e-faust',
            'richard-g-scott']

def all_files():
    all_files_list = []
    spun_data_rel_path = r'data\spun_data'

    for i in speakers:
        source_data_rel_path = r'data\100_speaker_data\{}\source_data'.format(i)

        for filename in sorted(glob.glob(os.path.join(source_data_rel_path, '*.txt'))):
            all_files_list.append(filename)

    for file_name in glob.glob(os.path.join(spun_data_rel_path, '*.txt')):
        all_files_list.append(file_name)
    return all_files_list

def register():
    for i in speakers:




def ttr(in_Text):
    return len(set(in_Text)) / len(in_Text)


feature_names = ['ttr', 'REGISTER']
with open('mc_feat_names.txt', 'w') as name_file:
    name_file.write('\t'.join(feature_names))

with open('mc_features.csv', 'w') as output_file:
    for file in all_files():
        print('.', end='', flush=True)
        with open(file, encoding='utf-8') as current_file:
            text = current_file.read()
        # sent_text = sent_tokenize(text)    THIS MAY BE USED LATER???????
        tok_text = nltk.word_tokenize(text)
        # tag_text = nltk.pos_tag(tok_text)  THIS MAY BE USED LATER???????
        print(ttr(tok_text), sep=',', file=output_file)

    print()
