from bs4 import BeautifulSoup as BS
import requests as req
import time
import re
import os

speakers = ['russell-m-nelson', 'dallin-h-oaks', 'henry-b-eyring',
            'm-russel-ballard', 'jeffrey-r-holland', 'dieter-f-uchtdorf',
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

"""This creates a directory that will contain all the files generated from this 
script. The top directory folder will be nix_semester_project and under that 
will be 100_speaker_data and under that will contain the individual folders of 
each speaker and inside of each of those folders will be a folder called 
source_data that will hold the .html file and the .txt file."""
if not os.path.exists(r'nix_semester_project'):
    for i in speakers:
        os.makedirs(r'nix_semester_project\100_speaker_data\{}\source_data'.format(i))


# speakers = ['russell-m-nelson', 'reyna-i-aburto']
gen_conf_dictionary = {}  # This may not be used but is here if needed

lds_website = r'https://www.lds.org'


"""Generate a header"""
def header():
    my_header = {'user-agent': 'Michael Nix (nix.byu@gmail.com)'}
    return my_header


"""Extracts all the html from lds.org main page and returns a soup object used
by the next function lds_gen_conf_link"""
def lds_website_soup(website=lds_website):
    lds_website_response = req.get(website, headers=header())
    lds_website_html_code = lds_website_response.text
    lds_webs_soup = BS(lds_website_html_code, 'html.parser')
    return lds_webs_soup


"""Extracts the link for the general conference page from lds_web_soup and
returns the full path to the LDS General Conference page"""
def lds_gen_conf_link(lds_webs_soup=lds_website_soup()):
    links = [all_links for all_links in lds_webs_soup.find_all('a')]
    wanted_links = [link.get('href') for link in links]
    for gen_conf_link in wanted_links:
        gen_conf_regex = re.match(r'\S+HP16GC\S+', gen_conf_link)
        if gen_conf_regex is not None:
            return gen_conf_regex.group()


"""lds_gen_conf_website contains the general conference web page link"""
lds_gen_conf_website = lds_gen_conf_link()


"""Extracts all the html from the general conference web page and returns a
soup object used by the next function all_speakers_link"""
def lds_gen_conf_soup(lds_gen_conf_site=lds_gen_conf_website):
    lds_gen_conf_response = req.get(lds_gen_conf_site, headers=header())
    lds_gen_conf_html_code = lds_gen_conf_response.text
    lds_gen_conf_page_soup = BS(lds_gen_conf_html_code, 'html.parser')
    return lds_gen_conf_page_soup


"""Extracts and returns the partial link that will go to "All Speakers" page"""
def all_speakers_link(lds_gen_conf_page_soup=lds_gen_conf_soup()):
    links = [all_links for all_links in lds_gen_conf_page_soup.find_all('a')]
    wanted_links = [link.get('href') for link in links]
    for speaker_link in wanted_links:
        if speaker_link is not None:
            speaker_link_regex = re.match(r'\S+/speakers\?lang=eng',
                                          speaker_link)
            if speaker_link_regex is not None:
                return speaker_link_regex.group()


"""gen_conf_speaker_page contains the direct path to the 'All Speakers' page"""
gen_conf_speaker_page = lds_website + all_speakers_link()


"""Extracts all the html from the 'All Speakers' page and returns a soup
object used by the next function speaker_main_page"""
def lds_gen_conf_speaker_soup(gen_conf_speaker_site=gen_conf_speaker_page):
    lds_gen_conf_speaker_response = req.get(gen_conf_speaker_site,
                                            headers=header())
    lds_gen_conf_speaker_html_code = lds_gen_conf_speaker_response.text
    lds_gen_conf_speaker_page_soup = BS(lds_gen_conf_speaker_html_code,
                                        'html.parser')
    return lds_gen_conf_speaker_page_soup


"""Extracts the partial link that points to the main page of each individual
speaker. Each partial link is appended to a list containing all the extracted
partial links."""
def speaker_main_page_link(lds_gen_conf_speaker_page_soup=lds_gen_conf_speaker_soup()):
    links = [all_links for all_links in lds_gen_conf_speaker_page_soup.find_all('a')]
    wanted_links = [link.get('href') for link in links]
    speaker_links = []
    for page_one_link in wanted_links:
        if page_one_link is not None:
            for speaker in speakers:
                page_one_regex = re.match(r'\S+{}\S+'.format(speaker), page_one_link)
                if page_one_regex is not None:
                    wanted_link = page_one_regex.group()
                    main_page_link = lds_website + wanted_link
                    speaker_links.append(main_page_link)
    return set(speaker_links)


"""Accesses each speaker's main page and extracts all the html from each
speaker's main page. The returned soup is used by the next function
speaker_main_page_talk_links()"""
def speaker_main_page_soup(speaker_link):
    speaker_main_page_response = req.get(speaker_link, headers=header())
    speaker_main_page_html = speaker_main_page_response.text
    speaker_main_page_soup = BS(speaker_main_page_html, 'html.parser')
    return speaker_main_page_soup


"""Extracts all the links for each talk on the speaker's main page"""
def speaker_main_page_talk_links(main_page_soup):
    speaker_talk_pointers_list = []
    main_page_links = [all_links for all_links in main_page_soup.find_all('a')]
    main_page_wanted_links = [link.get('href') for link in main_page_links]
    for speaker_main_page_talk_link in main_page_wanted_links:
        if speaker_main_page_talk_link is not None:
            speaker_talk_link_regex = re.match(r'\S+/\d+/\d+/.*', speaker_main_page_talk_link)
            if speaker_talk_link_regex is not None:
                speaker_talk_pointers_list.append(lds_website + speaker_talk_link_regex.group())
    return speaker_talk_pointers_list


"""This code block fills in the gen_conf_dictionary with each key being the
name of the speaker and the values as a list of links to the talks those people
have given. The links point to pages housing the individual talks. These pages
will have their html scraped and this will be saved locally. The scrapped html
code will have the actual talk text in it that will be parsed in another
script."""
for speaker in speakers:
    for speaker_link in speaker_main_page_link():
        if speaker in speaker_link:
            talk = speaker_main_page_talk_links(speaker_main_page_soup(speaker_link))
    gen_conf_dictionary[speaker] = talk


def html_code_for_each_talk_page(talk_links):

    talk_page_count = 0

    for talk_page in talk_links:
        talk_page_count += 1

    for i in speakers:
        with open(r'C:\Users\manua\Desktop\semester_project_article_spinner\nix_semester_project\100_speaker_data\{}\source_data\{}_talk_0'.format(i, i) + str(talk_page_count) + '.html', 'w', encoding='utf-8') as file_out:
            time.sleep(3)
            talk_page_response = req.get(talk_page, headers=header())
            talk_page_html_code = talk_page_response.text
            talk_page_soup = BS(talk_page_html_code, 'html.parser')
            print(talk_page_soup, file=file_out)
    print(speaker, talk_page_count)


for speaker, talk_links in gen_conf_dictionary.items():
    for talk in talk_links:
        html_code_for_each_talk_page(talk)

# for speaker, talk_links in gen_conf_dictionary.items():
#     print(talk_links)