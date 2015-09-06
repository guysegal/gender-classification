import os
from steps.create_xy_from_rank import create_xy_from_rank
from steps.get_blog_words_ranks import get_blog_words_ranks
from steps.save_blogs import save_blogs
from steps.svc_predict import svc_predict

genders = os.listdir("blogs")
save_blogs("raw/blog_urls_train")
save_blogs("raw/blog_urls_test")

#train

train_words_rank = get_blog_words_ranks("train", genders, 2000)

x_train, y_train = create_xy_from_rank("train", genders, train_words_rank)

#test

x_test, y_test = create_xy_from_rank("test", genders, train_words_rank)

#execute

svc_predict(x_train, y_train, x_test, y_test)


print "done"