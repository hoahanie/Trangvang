import scrapy
from scrapy.crawler import CrawlerProcess

class dich_vu_bds(scrapy.Spider):
    name = 'dich_vu_bds'

    start_urls = ['https://trangvangvietnam.com/categories/486679/bat-dong-san-dich-vu-bat-dong-san.html?']

    headers = {
        'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    def parse(self,response):
        number_page = response.xpath('//*[@id="paging"]/a[last()-1]/text()').get()
        self.log(number_page)

        for i in range(1,int(number_page)+1):
            yield scrapy.Request(
                url=self.start_urls[0] + "page=" + str(i),
                headers= self.headers,
                callback=self.parse_page
            )
    def parse_page(self,response):
        urls = response.xpath('.//h2[@class="company_name"]//a/@href').extract()
        yield {
            "url": urls
        }