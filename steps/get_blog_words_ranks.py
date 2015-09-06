import os
import re


def get_blog_words_ranks(sample_type, labels, max_words):
    counts = {}
    for label in labels:
        blog_files_names = os.listdir('blogs/' + label + '/'+sample_type)
        for blog_file_name in blog_files_names:
            blog_file = open('blogs/' + label + '/'+sample_type+'/' + blog_file_name, 'r')
            blog_text = blog_file.read()
            blog_file.close()

            blog_words = re.split(r'\W+', blog_text)
            for word in blog_words:
                word = word.strip()
                if len(word) > 0:
                    counts[word] = counts.get(word, 0) + 1

    blog_words_rank = {}
    n = 0
    for word in sorted(counts, key=counts.get, reverse=True):
        blog_words_rank[word] = n
        n += 1
        if n == max_words:
            break

    return blog_words_rank