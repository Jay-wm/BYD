import lxml.html
import csv
import os

html_path = os.path.expanduser('69GM2046C00x04-node6.htm')
with open('69GM2046C00x04-node6.htm', encoding = 'utf-8') as f:
    html_code = f.read()

# html = requests.get('file:///D:/69GM2046C00x04-node6.htm').content.decode()
selector = lxml.html.fromstring(html_code)
# EventEmcyCode = selector.xpath('//tbody[@id="TableOfEvents"]/tr[@id="TableContentBkg"]/td[2]/text()')
Group = selector.xpath('//*[@id="EventGroup"]/text()')
Event = selector.xpath('//*[@id="EventName"]/text()')

# Description_all = selector.xpath('//*[@id="EventDescription"]')
# for a in Description_all:
#     Description = a.xpath('string(.)')
Event_ID = selector.xpath('//tbody[@id="TableOfEvents"]/tr[@id="TableContentBkg"]/td[6]/text()')
data = []
for i in range(131):
    dict = {'Group': Group[i], 'Event': Event[i], 'Event_ID': Event_ID[i]}
    data.append(dict)
# titles = ['EventEmcyCode', 'Group', 'Event', 'Description', 'Event_ID']
titles = ['Group', 'Even
