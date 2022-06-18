# class ApiResources:
#     get_ticket_id = '/agent/tickets'

import requests
import json
import pandas as pd
from openpyxl import load_workbook

# type= incident
url = 'https://integrichain.zendesk.com/api/v2/search/incremental?per_page=30&include=highlights&page=1&type=ticket&query=ticket_type:incident'
zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# print("The content/Body is ", zen_auth_respo.content)
json_response = json.loads(zen_auth_respo.text)

emp_list_of_tag_and_id = []

for dictionary in json_response['results']:
    # print('type of json_response[tickets]')
    # print(type(json_response['tickets']))
    # print('All dicts are ', dictionary)
    # print(type(dictionary))               # <class 'dict'>
    # print('Tags value will be ', dictionary['tags'])
    # print(type(dictionary['tags']))         # <class 'list'>
    print('id of ticket is ', dictionary['id'])
    # print('tags value is ', dictionary['tags'])
    # tags_list = dictionary['tags']
    # print('tags_list is ', tags_list)
    print('url of ticket is ', dictionary['url'])
    # for tag in tags_list:
    #     if tag == 'chargebacks':
    #         print('id of tag is ', dictionary['id'])

    # tkt_id = dictionary['id']
    # print('New tkt_id is', tkt_id)
    # tkt_external_id = dictionary['external_id']
    # tkt_created_at = dictionary['created_at']
    # tkt_subject = dictionary['subject']
    # tkt_description = dictionary['description']
    # tkt_tags = dictionary['tags']
    # tkt_url = dictionary['url']

    # for item in dictionary.items():
    #     print('item is', item)
    # empty_list_id = []
    # empty_list_url = []
    # empty_list_tags = []
    # empty_list_created_at = []
    # empty_list_subject = []
    # empty_list_description = []

    # for k1 in dictionary:
    #     # print('key is ', k1)
    #     if k1 == 'id':
    #         print('id is ', dictionary[k1])
    #         empty_list_id = empty_list_id.append(dictionary[k1])
    #         df_sheet1 = pd.DataFrame({'id': [empty_list_id],
    #                                   'url': [empty_list_url],
    #                                   'tags': [empty_list_tags],
    #                                   'created_at': [empty_list_created_at],
    #                                   'subject': [empty_list_subject],
    #                                   'description': [empty_list_description]})
    #     elif k1 == 'url':
    #         print('url is ', dictionary[k1])
    #         empty_list_url.append(dictionary[k1])
    #     elif k1 == 'tags':
    #         print('tags is ', dictionary[k1])
    #         empty_list_tags.append(dictionary[k1])
    #     elif k1 == 'created_at':
    #         print('created_at is ', dictionary[k1])
    #         empty_list_created_at.append(dictionary[k1])
    #     elif k1 == 'subject':
    #         print('subject is ', dictionary[k1])
    #         empty_list_subject.append(dictionary[k1])
    #     elif k1 == 'description':
    #         print('description is ', dictionary[k1])
    #         empty_list_description.append(dictionary[k1])

# print('df_sheet1 is ', df_sheet1)
# print('1empty_list_id is ', empty_list_id)
# print('2empty_list_url is ', empty_list_url)
# print('3empty_list_tags is ', empty_list_tags)
# print('4empty_list_created_at is ', empty_list_created_at)
# print('5empty_list_subject is ', empty_list_subject)
# print('6empty_list_description is ', empty_list_description)

# create dataframe
# df_sheet1 = pd.DataFrame({'id': [empty_list_id, empty_list_id, '3', '4', '5', '6'],
#                           'url': [empty_list_url, empty_list_url, 'c', 'a', 'c', 'a'],
#                           'tags': [empty_list_tags, empty_list_tags, 'b', 'b', 'c', 'd'],
#                           'created_at': [empty_list_created_at, empty_list_created_at, 'w', 'a', 'q', 'a'],
#                           'subject': [empty_list_subject, empty_list_subject, 'm', 'n', 'v', 't'],
#                           'description': [empty_list_description, empty_list_description, 82, 87, 77, 61]})

# create excel writer object
# writer = pd.ExcelWriter(
#     'C:/Users/dorugzu/PycharmProjects/pythonProject/pythonProject/Zendesk_API_Auto/utilities/output_excel.xlsx')
# # write dataframe to excel sheet
# df_sheet1.to_excel(writer, 'sheet1')
#
# writer.save()
# print('DataFrame is written successfully to Excel')
# print(df_sheet1)

# file_name = f'C:/Users/dorugzu/PycharmProjects/pythonProject/pythonProject/Zendesk_API_Auto/utilities/output_excel.xlsx'
# df = pd.read_excel(file_name)  # Read Excel file as a DataFrame
# print('After reading Excel data ', df)

# ----------------------------------------------------------------------------
# Working properly
# df = pd.DataFrame(data=[['a', 'b', 'c', 'a', 'c', 'a'], ['1', '2', '3', '4', '5', '6']],
#                   columns=(['id', 'url', 'tags', 'created_at', 'subject', 'description']))
# df_final_excel = df[['id', 'url', 'tags', 'created_at', 'subject', 'description']].to_excel(
#     f'C:/Users/dorugzu/PycharmProjects/pythonProject/pythonProject/Zendesk_API_Auto/utilities/output_excel.xlsx')
# print('Final Excel data is', df_final_excel)
# ----------------------------------------------------------------------------

#     for key in dictionary['tags']:
#         print('key of dictionary is ', key)
#         print(type(key))
#         list_of_chargebacks = dictionary['tags']
#         print('list_of_chargebacks is ', list_of_chargebacks)
#         if 'chargebacks' in list_of_chargebacks and int(len(list_of_chargebacks)) == 1:
#             print('Final values are ', dictionary['tags'])
#             emp_list_of_tag_and_id.append(dictionary)
# print('emp_list_of_tag_and_id is ', emp_list_of_tag_and_id)

# writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
# wb = writer.book
# df = pd.DataFrame({'Col_A': [1, 2, 3, 4],
#                    'Col_B': [5, 6, 7, 8],
#                    'Col_C': [0, 0, 0, 0],
#                    'Col_D': [13, 14, 15, 16]})
#
# df.to_excel(writer, index=False)
# wb.save('test.xlsx')

# if key == 'tags':
#     list_of_chargebacks = dictionary[key]
#             if 'chargebacks' in list_of_chargebacks and int(len(list_of_chargebacks)) == 1:
#                 emp_list_of_tag_and_id.append(dictionary)
#
#
# print(emp_list_of_tag_and_id)

# for dict1 in emp_list_of_tag_and_id:
#     for k1 in dict1.items():
#         print(k1)
#         print(type(k1))

# print(dict(k1))
# print(dict((x, y) for x, y in k1))


# count += 1
# # print(key, 'and value is ', dictionary[key])
# ticket2 = dict(json_response['tickets'])
# print(type(ticket2))
# if key == 'tags':
#     for k, v in ticket2:
#         if k == 'id':
#             print(f'Final Value of {key} is', dictionary[key], v)
#             list_of_chargebacks = dictionary[key]
#     if 'chargebacks' in list_of_chargebacks and int(len(list_of_chargebacks)) == 1:
#         print('id of tkt is ', json_response['tickets'][0]['id'], list_of_chargebacks)
# count = count + 1
# print('Count is ', count)
# print(type(dictionary[key]))
# for val in dictionary[key]:
#     if val == 'chargebacks':
#         print('abc')

# Added lines for testing purpose
