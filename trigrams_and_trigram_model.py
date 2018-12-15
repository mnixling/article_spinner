import nltk

master_txt_file = open('data\master_text.txt', 'r', encoding='utf-8').read()
master_txt_file = master_txt_file.splitlines()

"""Builds all the trigrams in master.txt. The structure of the trigram is:
{(Wn-2, Wn-1): Wn}"""
def build_trigrams():
    all_trigrams = {}
    for words in master_txt_file:
        word = words.lower()
        tokens = nltk.tokenize.word_tokenize(word)

        for i in range(len(tokens) - 2):
            dict_key = (tokens[i], tokens[i+1])
            dict_value = tokens[i+2]
            if dict not in all_trigrams:
                all_trigrams[dict_key] = dict_value
    return all_trigrams

with open('trigrams.txt', 'a', encoding='utf-8') as output_txt:
    for key, value in build_trigrams().items():
        print(key, value, file=output_txt)


"""Builds the trigram model. The structure of the trigram model is: 
{(W n-2, W n-1): [Wn, Wn, Wn,..., Wn],...,(W n-2, W n-1): [Wn,..., Wn]} where 
the key is a tuple of the two proceeding words and the value is the list of all
the words that may follow that tuple pair."""
def trigram_model():
    trigrams = {}
    for words in master_txt_file:
        word = words.lower()
        tokens = nltk.tokenize.word_tokenize(word)
        for i in range(len(tokens) - 2):
            dict_key = (tokens[i], tokens[i+1])
            if dict_key not in trigrams:
                trigrams[dict_key] = []
            trigrams[dict_key].append(tokens[i+2])
    return trigrams


"""Builds the trigram probabilities."""
trigram_probability = {}
for key, value in trigram_model().items():
    if len(set(value)) > 1:
        probability_dict = {}
        num = 0
        for word in value:
            if word not in probability_dict:
                probability_dict[word] = 0
            probability_dict[word] += 1
            num += 1
        for word, count in probability_dict.items():
            probability_dict[word] = float(count) / num
        trigram_probability[key] = probability_dict
with open('trigram_probabilities.txt', 'a', encoding='utf-8') as out_txt:
    for key, value in trigram_probability.items():
        print(key, value, file=out_txt)
