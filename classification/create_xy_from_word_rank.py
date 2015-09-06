import os
import re


def create_xy_from_word_rank(sample_type, labels, word_rank, base_path='blogs'):
    x, y = [], []

    for label in labels:
        blog_files_names = os.listdir(base_path + '/' + label + '/' + sample_type)

        for blog_file_name in blog_files_names:
            blog_file_path = base_path + '/' + label + '/' + sample_type + '/' + blog_file_name
            print "creating feature vector from " + blog_file_path

            blog_file = open(blog_file_path, 'r')
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