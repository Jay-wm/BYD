import requests
import lxml.html

html_code= ''
selector = lxml.html.fromstring(hml_code)
EventEmcyCode = sellector.xpath('//*[@id="TableContentBkg"]/td[2]')
Group = sellector.xpath('//*[@id="EventGroup"]')
Event = sellector.xpath('//*[@id="EventName"]')
Description = sellector.xpath('//*[@id="EventDescription"]')
Event_ID = sellector.xpath('//*[@id="event-100u"]')
