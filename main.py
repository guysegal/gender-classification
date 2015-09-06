import os

from classification.create_xy_from_word_rank import create_xy_from_word_rank
from classification.get_word_rank import get_word_rank
from classification.classify_with_svm import classify_with_svm


train_words_rank = get_word_rank("train", ["female", "male", "unknown"], 2000, "data/blogs")

x_train, y_train = create_xy_from_word_rank("train", ["female", "male", "unknown"], train_words_rank, "data/blogs")

x_test, y_test = create_xy_from_word_rank("test", ["female", "male", "unknown"], train_words_rank, "data/blogs")

accuracy = classify_with_svm(x_train, y_train, x_test, y_test)


print "done"