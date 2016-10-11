from Spider.facebook_crawler import FacebookSpider

# Instructions:
# Pass username and password through constructor
# set webdrive path
# set profile to scrape
# start!
# Download Chrome webdriver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads

fb_username = ''
fb_password = ''
path_to_webdriver = ''
profile_to_scrape = ''

if __name__ == '__main__':
    spider = FacebookSpider(fb_username, fb_password)
    spider.set_webdriver_path(path_to_webdriver)
    spider.set_scroll_count(10)
    #e.g 'zuck'
    spider.set_profile_to_scrape(profile_to_scrape)
    print(spider.start())
