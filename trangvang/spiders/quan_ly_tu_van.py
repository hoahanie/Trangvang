import scrapy
from scrapy.crawler import CrawlerProcess

class quan_ly_tu_van(scrapy.Spider):
    name = 'quan_ly_tu_van'

    start_urls = 'https://trangvangvietnam.com/categories/197660/bat-dong-san-quan-ly-va-tu-van-bat-dong-san.html?'

    headers = {
        'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    def parse(self,response):
        number_page = response.xpath('//*[@id="paging"]/a[last()-1]/text()').get()
        self.log(number_page)

        for i in range(1,int(number_page)+1):
            yield scrapy.Request(
                url=self.start_urls + "page=" + str(i),
                headers= self.headers,
                callback=self.parse_page
            )
    def parse_page(self,response):
        urls = response.xpath('.//h2[@class="company_name"]//a/@href').extract()
        for url in urls:
            yield scrapy.Request(
                url=url,
                headers = self.headers,
                callback = self.parse_detail
            )

    def parse_detail(self,response):
        name = response.xpath('//div[@class="tencongty"]/h1/text()').get()
        email = response.xpath('//div[@class="text_email"]/p/a/text()').get()
        website = response.xpath('//div[@class="text_website"]/p/a/text()').get()
        address = response.xpath('//div[@class="diachi_chitiet_li2dc"]/p/text()').get()
        phone = response.xpath('//div[@class="diachi_chitiet_li2"]/span/text()').get()
        thitruong = response.xpath('//div[@class="thitruong_loaidn_text"]/p/text()').get()
        loaihinh = response.xpath('//*[@id="listing_basic_info"]/div[5]/div[2]/div[2]/p/text()').get()

        yield {
            "name": name,
            "email": email,
            "website": website,
            "address": address,
            "phone": phone,
            "thitruong": thitruong,
            "loaihinh": loaihinh
        }