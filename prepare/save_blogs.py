import re
import urllib2


def save_blogs(blog_urls_path, data_base_path):
    stop_words = []
    blog_index = 0
    data_type = blog_urls_path.split('_')[2]

    for blog_url_and_label in open(blog_urls_path, 'r'):
        try:
            url = blog_url_and_label.split(',')[0].strip()
            label = blog_url_and_label.split(',')[1].strip()

            blog_web_page = urllib2.urlopen(url)
            print "Downloaded " + blog_web_page

            blog_file = open(data_base_path + '/' + label + '/' + data_type + '/' + str(blog_index) + '.txt', 'w')

            for line in blog_web_page:
                line = line.strip()
                words = re.split(r'\W+', line)
                for word in words:
                    if word not in stop_words:
                        blog_file.write(word + " ")

            blog_file.close()
            blog_index += 1

        except:
            print "Failed downloading " + url
            # if there was an error downloading the file just move to the next one
            continue


def get_stop_words():
    return []