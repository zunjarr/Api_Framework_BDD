import requests
import json
import jsonpath

url = 'https://integrichain.zendesk.com/api/v2/tickets.json'
zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
print("The content/Body is ", zen_auth_respo.content)
json_response = json.loads(zen_auth_respo.text)
# data = json_response['tickets']
# print('type of data is ')
# print(type(data))

for i in json_response['tickets']:
    print('All tags values are ', i['tags'])
    list_of_tags = i['tags']
    print('list_of_tags', list_of_tags)
    print(type(i['tags']))
    for j in i['tags']:
        print('value of j is ', j)
        # if j == 'chargebacks':
        #     print('value of j is ', j)

print('All stars ***************************************************************************')

for dictionary in json_response['tickets']:
    # print('All dicts are ', dictionary)
    # print('Tags value will be ', dictionary['tags'])

    for key in dictionary:
        # print(key, 'and value is ', dictionary[key])
        if key == 'tags':
            count = 0
            print(f'Final Value of {key} is', dictionary[key])
            count = count + 1
            print('Count is ', count)
            print(type(dictionary[key]))
            for val in dictionary[key]:
                if val == 'chargebacks':
                    print(val)


# for x in data:
#     keys_tkt = x.keys()
#     item_tkt = x.
#     print(type(keys_tkt))
#     print("keys_tkt are  ", keys_tkt)
#     for k,v in keys_tkt.iteritems:
#         print('value of k is ', k)
#         if k == 'tags':
#             print('inside if loop')
#             print('Specific tag value is  ', k.values)
#   # values_tkt = x.values()
# print(type(values_tkt))
# print("values_tkt are  ", values_tkt)
# for v in values_tkt:
#     print('value of v is ', v)


# id_of_ticket = zen_auth_respo.json()['tickets'][0]

# print('All values in id_of_ticket are ', id_of_ticket)
# print('id_of_ticket is ', id_of_ticket['tags'])
# print(type(id_of_ticket))
# print("Before for loop")

# specific_key = 'tags'
# for key, di in json.loads(zen_auth_respo.text).items():  # items on Py 3k
#     print('values of key are', key, 'values of di are', di[1]['id'])
#     for val in di:
#         if val == 'url':
#             print('Fetched url is ', val)
# if di.startswith(specific_key):
#     if di['tags']:
#         print(k, v)
#         break


# tag_name_list = ['new_client', 'datatype_852', 'issuecat_line_count']
# for k in id_of_ticket.items:
#     print('All keys are ', k)
#
# for id_t in id_of_ticket:
#     if 'new_client' == 360030348131:
#         print("inside if loop")
#         print('id_of_ticket are ', id_t)
