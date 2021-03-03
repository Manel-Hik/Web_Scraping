# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class InfoUdemySpider(CrawlSpider):
    name = 'info__udemy'
    allowed_domains = ['www.udemy.com']
    start_urls = ['https://www.udemy.com/courses/personal-development']

    #user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    #print("hihihihih;;;;")
    #def start_requests(self):
     #   yield scrapy.Request(url='https://www.udemy.com/courses/personal-development', headers={
      #      'User-Agent': self.user_agent
       # })
    
    rules = (

        Rule(LinkExtractor(restrict_xpaths="//div[@class='course-list--container--3zXPS']/div[@class='popper--popper--19faV popper--popper-hover--4YJ5J']/a"), callback='parse_item', follow=True),#,process_request='set_user_agent'),
        #Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )

    #def set_user_agent(self,request):
     #   request.headers['User-Agent'] = self.user_agent
      #  return request


    def parse_item(self, response):
        yield{
            'course_title': response.xpath("//h1[@class='udlite-heading-xl clp-lead__title clp-lead__title--small']/text()").get(),

            'duration': response.xpath("//div[@class='udlite-text-sm']/span/span/span/text()").get(),

            'Description': response.xpath("//div[@class='udlite-text-md clp-lead__headline']/text()").get(),

            'Rating': response.xpath("(//span[@class='udlite-heading-sm star-rating--rating-number--3lVe8'])[2]/text()").get(), 

            'Nb_subscribed': response.xpath("(//div[@data-purpose='enrollment'])[2]/text()").get(),

            'Language': response.xpath("(//div[@class='clp-lead__element-item clp-lead__locale']/text())[2]").get(),

            'instructor_name': response.xpath("(//div[@class='udlite-heading-lg instructor--instructor__title--34ItB']/a)[1]/text()").get(),

            'instructor_presentation':response.xpath("(//div[@class='show-more--content--isg5c show-more--with-gradient--2abmN'])[2]/text()").extract(),

            'course_reviews':response.xpath("//div[@class='udlite-text-sm individual-review--individual-review__comment--2o94n']/text()").extract(),


            'course_url': response.url,
            #'user_agent': response.request.headers['User-Agent']

        }