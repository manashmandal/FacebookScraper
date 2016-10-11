from Spider.facebook_crawler import FacebookSpider

# Instructions:
# Pass username and password through constructor
# set webdrive path
# set profile to scrape
# start!
# Download Chrome webdriver from here:

fb_username = 'username or email'
fb_password = 'pass'
path_to_webdriver = 'D:\chromedriver_win32\chromedriver.exe'
prof = 'DonaldTrump'

if __name__ == '__main__':
    spider = FacebookSpider(fb_username, fb_password)
    spider.set_webdriver_path(path_to_webdriver)
    spider.set_profile_to_scrape(prof)
    spider.set_delay_between_scroll(1)
    spider.set_scroll_count(2000)
    urls = spider.extract_post_urls()
    print(urls)
    txt = spider.extract_text(urls)
    print(txt)

    # print(spider.start())

    # print(spider.start())