import lxml.html
import csv
import os

# '''打开相对路径的文件'''
# html_path = os.path.expanduser('69GM2046C00x04-node6.htm')

'''将所有要爬取的文件名写入数组'''
files = ['69GM2046C00x04-node6.htm', '69GM2047C00x01-node7.htm', '69GM2048C00x04-2-node8.htm', '69GM2049C00x01-node9.htm']

'''打开htm格式文件'''
for file in range(len(files)):
    with open(files[file], encoding = 'utf-8') as f:
        html_code = f.read()

    '''初始化数组'''
    EmergencyErrorCode = []
    Group = []
    Event = []
    Description = []
    Event_ID = []
    data = []

    '''初始化selector'''
    selector = lxml.html.fromstring(html_code)
    Events_Error_Code = selector.xpath('//*[@id="TableOfEvents"]/tr[@id="TableContentBkg"]')


    '''获取故障代码信息'''
    for i in range(len(Events_Error_Code)):

        # 获取紧急错误代码（Emergency Error Cpde）
        EmergencyErrorCode_list = Events_Error_Code[i].xpath('td[2]/text()')
        if len(EmergencyErrorCode_list) != 0:
        #     # EmergencyErrorCode.append('')
        # else:
            EmergencyErrorCode.append(EmergencyErrorCode_list[0])

            # 获取故障所在组名
            Group.append(Events_Error_Code[i].xpath('td[@id="EventGroup"]/text()')[0])
            # 获取故障
            Event.append(Events_Error_Code[i].xpath('td[@id="EventName"]/text()')[0])
            # 获取故障描述以及何时发生
            Description_all = Events_Error_Code[i].xpath('td[@id="EventDescription"]')[0]
            Description.append(Description_all.xpath('string(.)'))
            # 获取故障代码
            Event_ID.append(Events_Error_Code[i].xpath('td[6]/text()')[0])


    '''将每组数据组成字典添加到数组中'''
    for i in range(len(Event_ID)):
        dict = {'EmergencyErrorCode': EmergencyErrorCode[i], 'Group': Group[i], 'Event': Event[i],
                'Description': Description[i], 'Event_ID': Event_ID[i]}
        data.append(dict)

    '''将获取的数据写入csv格式文件'''
    titles = ['EmergencyErrorCode', 'Group', 'Event', 'Description', 'Event_ID']
    file_name = 'C80D-Error_Event_node' + str(file + 6) + '-filterde.csv'
    with open(file_name, 'w', newline = '', encoding = 'UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames = titles)
        writer.writeheader()
        writer.writerows(data)