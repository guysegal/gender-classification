import os
import re


def get_word_rank(sample_type, labels, max_words, base_path):
    counts = {}
    for label in labels:
        files_names = os.listdir(base_path + '/' + label + '/'+sample_type)
        for file_name in files_names:
            file_path = base_path + '/' + label + '/'+sample_type+'/' + file_name
            print "adding words from ["+file_path+"] to words rank "

            opened_file = open(file_path, 'r')
            file_text = opened_file.read()
            opened_file.close()

            words_in_file = re.split(r'\W+', file_text)
            for word in words_in_file:
                word = word.strip()
                if len(word) > 0:
                    counts[word] = counts.get(word, 0) + 1

    word_rank = {}
    n = 0
    for word in sorted(counts, key=counts.get, reverse=True):
        word_rank[word] = n
        n += 1
        if n == max_words:
            break

    return word_rank