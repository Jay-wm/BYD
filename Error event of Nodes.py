import lxml.html
import csv
import os

html_path = os.path.expanduser('69GM2046C00x04-node6.htm')

with open('69GM2046C00x04-node6.htm', encoding = 'utf-8') as f:
    html_code = f.read()

selector = lxml.html.fromstring(html_code)

Group = selector.xpath('//*[@id="EventGroup"]/text()')
Event = selector.xpath('//*[@id="EventName"]/text()')

Event_ID = selector.xpath('//tbody[@id="TableOfEvents"]/tr[@id="TableContentBkg"]/td[6]/text()')
print(len(Group))

data = []
for i in range(131):
    dict = {'Group': Group[i], 'Event': Event[i], 'Event_ID': Event_ID[i]}
    data.append(dict)

titles = ['Group', 'Event', 'Event_ID']
with open('C80D-Error_Event.csv', 'w', encoding = 'UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames = titles)
    writer.writeheader()
    writer.writerows(data)
