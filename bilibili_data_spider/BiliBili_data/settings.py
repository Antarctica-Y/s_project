# Scrapy settings for BiliBili_data project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'BiliBili_data'

SPIDER_MODULES = ['BiliBili_data.spiders']
NEWSPIDER_MODULE = 'BiliBili_data.spiders'


custom_settings = { 'DOWNLOAD_DELAY': 1, 'CONCURRENT_REQUESTS_PER_IP': 4, 'DOWNLOADER_MIDDLEWARES': {},}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BiliBili_data (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55',
   'Host' : 'api.bilibili.com',
   'cookie': '''buvid3=D76FB979-2CAE-FEAD-54DE-246F636EF84742626infoc; i-wanna-go-back=-1; b_lsid=DF2E10110B_17FE9520E89; _uuid=9F81BD10B-1E4F-C38F-DCEB-21010310CD1CD8E43383infoc; buvid4=E7260CB2-BA1F-F951-CF29-4E7A9791709B07583-022022611-sY8l0EfnQAU7CEcUQivvHg%3D%3D; sid=bh3py6c1; fingerprint=17bdc3ea41f31b5c4b2b9342243de1e2; buvid_fp_plain=undefined; DedeUserID=22682736; DedeUserID__ckMd5=b73512ca36f38918; SESSDATA=aeb4631b%2C1664438966%2C8ccb8*41; bili_jct=35647abfeddde74cb136e5ab3776ab5b; buvid_fp=17bdc3ea41f31b5c4b2b9342243de1e2; CURRENT_FNVAL=4048; bsource=search_bing; blackside_state=1; rpdid=|(J|Y||uJR~J0J'uYR)))~|uu; hit-dyn-v2=1; innersign=0; b_ut=5'''
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'BiliBili_data.middlewares.BilibiliDataSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'BiliBili_data.middlewares.BilibiliDataDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'BiliBili_data.pipelines.BilibiliDataPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
