import requests
import lxml.html
import csv

html_code = ''
selector = lxml.html.fromstring(hml_code)
EventEmcyCode = sellector.xpath('//*[@id="TableContentBkg"]/td[2]')
Group = sellector.xpath('//*[@id="EventGroup"]')
Event = sellector.xpath('//*[@id="EventName"]')
Description = sellector.xpath('//*[@id="EventDescription"]')
Event_ID = sellector.xpath('//*[@id="event-100u"]')


data = [{}]
titles = ['EventEmcyCode', 'Group', 'Event', 'Description', 'Event_ID']
with open('C80D-Error_Event.csv', encoding = 'utf-8') as f:
    writer = csv.DictWriter(f, filename = titles)
    writer.writeheader()
    writer.writerows(data)
    
