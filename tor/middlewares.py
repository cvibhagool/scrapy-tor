from scrapy.conf import settings

class ProxyMiddleware(object):
    #Overide the request process by making it go through Tor
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.['HTTP_PROXY']