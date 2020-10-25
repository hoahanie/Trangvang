import scrapy

class crawl_detail(scrapy.Spider):
    name = "crawl_detail"

    
    start_urls = ['https://trangvangvietnam.com/listings/1187889882/bat-dong-san-imuabanbds-cong-ty-cp-imuabanbds.html']

    def parse(self,response):
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