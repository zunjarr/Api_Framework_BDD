import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

# url = 'https://integrichain.zendesk.com/api/v2/tickets.json'
# url = 'https://integrichain.zendesk.com/api/v2/search/incremental?per_page=30&include=highlights&page=1&type=ticket&query=tags:chargebacks'
# url = 'https://integrichain.zendesk.com/api/v2/search/incremental?per_page=30&include=highlights&page=1&type=ticket&query=status:open'
# zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# print("status_code is ", zen_auth_respo.status_code)
# print("The content/Body is ", zen_auth_respo.content)
# print("Type is ", type(zen_auth_respo))
# json_response = json.loads(zen_auth_respo.text)
# print('json_response is ', json_response)
# print("Type is ", type(json_response))
# print('results is ', json_response['results'])
# print('results 0 is ', json_response['results'][0])
# tags
# for dictionary in json_response['tickets']:
#     print('dictionary is ', dictionary)
#     print("Type is ", type(dictionary))
#     print('dictionary tags is ', dictionary['tags'])

# tags_list = dictionary['tags']
# print('tags_list is ', tags_list)
# for tag in tags_list:
#     if tag == 'chargebacks' and len(tags_list) == 1:
#         print('id of tag is ', dictionary['id'])

# status


# # ticket_type= incident
# url = 'https://integrichain.zendesk.com/api/v2/search/incremental?&type=ticket&query=ticket_type:incident'
# zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# print("The content/Body is ", zen_auth_respo.content)
# json_response = json.loads(zen_auth_respo.text)
#
# for dictionary in json_response['results']:
#     # print('All dicts are ', dictionary)
#     print('For ticket_type=incident, id of ticket is ', dictionary['id'])
#
# # tags= chargeback
# url = 'https://integrichain.zendesk.com/api/v2/search/incremental?per_page=30&include=highlights&page=1&type=ticket&query=tags:chargebacks'
# zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# # print("The content/Body is ", zen_auth_respo.content)
# json_response = json.loads(zen_auth_respo.text)
#
# for dictionary in json_response['results']:
#     # print('All dicts are ', dictionary)
#     print('For tags=chargeback,id of ticket is ', dictionary['id'])
#
# # assignee= Anthony J. Del Signore
# url = 'https://integrichain.zendesk.com/api/v2/search/incremental?per_page=30&include=highlights&page=1&type=ticket&query=assignee:ajd@integrichain.com'
# zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# # print("The content/Body is ", zen_auth_respo.content)
# json_response = json.loads(zen_auth_respo.text)
#
# for dictionary in json_response['results']:
#     # print('All dicts are ', dictionary)
#     print('For assignee= Anthony J. Del Signore,id of ticket is ', dictionary['id'])
#
# # updated date= Past month
# url = 'https://integrichain.zendesk.com/api/v2/search/incremental?per_page=30&include=highlights&page=1&type=ticket&query=updated>1month'
# zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# # print("The content/Body is ", zen_auth_respo.content)
# json_response = json.loads(zen_auth_respo.text)
#
# for dictionary in json_response['results']:
#     # print('All dicts are ', dictionary)
#     print('For updated date= Past month,id of ticket is ', dictionary['id'])
#
# # status = open
# url = 'https://integrichain.zendesk.com/api/v2/search/incremental/?&type=ticket&query=status:open&size=200'
# zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# print("The content/Body is ", zen_auth_respo.content)
# print("status code is ", zen_auth_respo.status_code)
# json_response = json.loads(zen_auth_respo.text)
#
# for dictionary in json_response['results']:
#     # print('All dicts are ', dictionary)
#     print('For status=open,id of ticket is ', dictionary['id'])

# GIR
# url1 = 'https://integrichain.zendesk.com/api/v2/tickets.json'
url = 'https://integrichain.zendesk.com/api/v2/search/incremental?per_page=30&include=highlights&page=1&type=ticket&query=DIR'
zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# print("The content/Body is ", zen_auth_respo.content)
# print("status code is ", zen_auth_respo.status_code)
json_response = json.loads(zen_auth_respo.text)

for dictionary in json_response['results']:
    print('All dicts are ', dictionary)
    # print('For subject,id of ticket is ', dictionary['id'])
    tkt_status = dictionary['status']
    keyss = dictionary.keys()
    print('keys are', keyss)
    # for key in dictionary.keys():
    key_list = ['subject', 'description', 'status', 'client_name', 'transaction_date', 'trade_partner',
                'discovery_date' 'data_type', 'issue_category', 'outreach_attempt', 'email_subject_line', 'contact_cc',
                'data_issue_resolution']


    for k_l in key_list:
        if k_l in dictionary.keys():
            print(k_l + ' key is present')
            print('Imp value is ', dictionary[k_l])
            s = "tkt_"
            i = k_l
            col_name = f"{s}{i}"
            # print('Value of final2 is ', col_name)
            emp_dict = {}

            # emp_dict = emp_dict[col_name]
            # print('1st ele added ', emp_dict)
            # print('First final key is ', col_name)
            emp_dict[col_name] = dictionary[k_l]
            # print('type is ')
            # print(type(emp_dict))
            key3 = emp_dict[col_name]
            # print('key3 is ', key3)
            final = dictionary[k_l]
            # print('final result is ', final)

            # emp_dict = emp_dict.append(final)
            # print('2nd ele added ', emp_dict)
            tkt_subject = dictionary['subject'].split()
            # print('Client name is ', tkt_subject[0])
            client_name = tkt_subject[0]

            word = 'DIR'
            count = dictionary['subject'].count(word)
            # print('count is ', count)
            if count > 0:
                # print('Ticket title with DIR ', dictionary['subject'])
                if word in dictionary['subject'].split():
                    print('Ticket has DIR word')
                    df = pd.DataFrame(data=[[dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l], dictionary[k_l]]],
                                      columns=(
                                          ['subject', 'description', 'status', 'client_name', 'transaction_date',
                                           'trade_partner',
                                           'discovery_date', 'data_type', 'issue_category', 'outreach_attempt',
                                           'email_subject_line',
                                           'contact_cc', 'data_issue_resolution']))
                    df_final_excel = df[
                        ['subject', 'description', 'status', 'client_name', 'transaction_date', 'trade_partner',
                         'discovery_date', 'data_type', 'issue_category', 'outreach_attempt', 'email_subject_line',
                         'contact_cc', 'data_issue_resolution']].to_excel(
                        f'C:/Users/dorugzu/PycharmProjects/pythonProject/pythonProject/Zendesk_API_Auto/utilities/output_excel.xlsx')
                    print('Final Excel data is', df_final_excel)
            # emp_dict.update(f'k_l, dictionary[k_l])
        else:
            print(k_l + ' key is not present')
    print('Excel printed successfully')
    # print('Before id loop')
    # print('tkt_status is ', tkt_status)
    # if 'id' in json_response['results']:
    #     tkt_id = dictionary['id']
    #     print('tkt_id is ', tkt_id)
    # print('After id loop')
    # print('Ticket title is ', dictionary['subject'])
    # ------------unskip from here to below----------------
    # tkt_subject = dictionary['subject']
    # print('tkt_subject is ', tkt_subject)
    # tkt_description = dictionary['description']
    # print('tkt_description is ', tkt_description)
    # print(type(dictionary['description']))
    # tkt_subject = dictionary['subject'].split()
    # print('Client name is ', tkt_subject[0])
    # client_name = tkt_subject[0]
    #
    # word = 'DIR'
    # count = dictionary['subject'].count(word)
    # # print('count is ', count)
    # if count > 0:
    #     # print('Ticket title with DIR ', dictionary['subject'])
    #     if word in dictionary['subject'].split():
    #         print('Ticket having DIR word')
    #         trade_part = 'Trade Partner'
    #         # if trade_part in dictionary['description'].split():
    #         #     print('Ticket having Trade Partner')                 # tkt_trade_partner, tkt_transaction_date
    #         df = pd.DataFrame(
    #             data=[[tkt_subject, tkt_description, tkt_status, client_name, tkt_discovery_date, tkt_data_type,
    #                    tkt_issue_category, tkt_outreach_attempt, tkt_email_subject_line, tkt_contact_cc,
    #                    tkt_data_issue_resolution, ]],
    #             columns=(['subject', 'description', 'status', 'client_name', 'transaction_date', 'trade_partner',
    #                       'discovery_date' 'data_type', 'issue_category', 'outreach_attempt', 'email_subject_line',
    #                       'contact_cc', 'data_issue_resolution']))
    #         df_final_excel = df[['subject', 'description', 'status', 'client_name', 'transaction_date', 'trade_partner',
    #                              'discovery_date' 'data_type', 'issue_category', 'outreach_attempt',
    #                              'email_subject_line', 'contact_cc', 'data_issue_resolution']].to_excel(
    #             f'C:/Users/dorugzu/PycharmProjects/pythonProject/pythonProject/Zendesk_API_Auto/utilities/output_excel.xlsx')
    #         print('Final Excel data is', df_final_excel)

    # else:
    #     print('There is no such ticket title having word DIR')

# 'https://integrichain.zendesk.com/api/v2/users/4578807155981/tickets/requested.json?include=comment_count,first_comment,last_comment,users&per_page=10&sort_order=desc&sort_by=id&exclude_count=true&exclude_archived=true'
