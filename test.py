import lxml.html
import csv
import os

html_path = os.path.expanduser('69GM2046C00x04-node6.htm')

with open('69GM2046C00x04-node6.htm', encoding = 'utf-8') as f:
    html_code = f.read()

selector = lxml.html.fromstring(html_code)
Events_Error_Code = selector.xpath('//*[@id="TableOfEvents"]/tr[@id="TableContentBkg"]')
print(Events_Error_Code)

for i in range(len(Events_Error_Code)):
    print(Events_Error_Code[i])
    EventEmcyCode = (Events_Error_Code[i]).xpath('td[2]/text()')
    print(EventEmcyCode)
    break