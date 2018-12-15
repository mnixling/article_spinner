"""
Only run this script once.
This script creates a master text file that contains all the parsed text data.
"""
import glob
import os

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


"""Globs all the files and places them into a list"""
def glob_file_source_data():
    glob_file_source_list = []
    for i in speakers:
        partial_path = r'data\100_speaker_data\{}\source_data'.format(i)

        for filename in sorted(glob.glob(os.path.join(partial_path, '*.txt'))):
            glob_file_source_list.append(filename)
    return glob_file_source_list


def create_master_txt():
    for filename in glob_file_source_data():
        with open(filename, 'r', encoding='utf-8') as input_txt:
            with open('data\master_text.txt', 'a', encoding='utf-8') as output_txt:
                text = input_txt.read()
                print(text, file=output_txt)





create_master_txt()
