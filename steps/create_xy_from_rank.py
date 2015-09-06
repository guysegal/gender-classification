import os
import re


def create_xy_from_rank(sample_type, labels, word_rank):
    x, y = [], []

    for label in labels:
        blog_files_names = os.listdir('blogs/' + label + '/'+sample_type)

        for blog_file_name in blog_files_names:
            blog_file = open('blogs/' + label + '/'+sample_type+'/' + blog_file_name, 'r')
            blog_text = blog_file.read()
            blog_words = re.split(r'\W+', blog_text)
            blog_file.close()

            number_of_unique_words_in_rank = len(word_rank.keys())
            feature_vector = [0 for i in range(number_of_unique_words_in_rank)]
            for word in blog_words:
                if word in word_rank:
                    feature_vector[word_rank[word]] += 1

            x.append(feature_vector)
            y.append(label)

    return x, y