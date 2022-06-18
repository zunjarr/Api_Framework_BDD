import requests
import json
import pandas as pd
from csv import writer
from csv import reader
from bs4 import BeautifulSoup
import re
import ast

# url = 'https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm'
# data = requests.get(url)
# soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())
# moviesTable = soup.find('table', {'class': 'findList'})
# print(moviesTable.prettify())
# tbody = moviesTable.findAll('tbody')
# print('tbody is ', tbody)
# rows = moviesTable.findAll('tr')
# print('rows are ', rows)
# for row in rows:
#     print('Value of row ', row)
#     if row.findall('td'):
#         print('td is present')
#         row_data = row.findall('td')
#         print(row_data)


# url = 'https://integrichain.zendesk.com/proxy/v2/apps/secure/https://jiraplugin.zendesk.com/integrations/jira/account/integrichain/links/for_ticket?ticket_id=79846'
# zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
# print("The content/Body is ", zen_auth_respo.content)
# json_response = json.loads(zen_auth_respo.text)

# for dictionary in json_response['results']:
#     # print('All dicts are ', dictionary)
#     print('id of ticket is ', dictionary['id'])

# str1 = 'Client DIR name is DIR'
# word = 'DIR'
# count = str1.count(word)
# print('count is ', count)
# if word in str1.split():
#     print(word)
#     print('Ticket having DIR word')

# ----------------------------------------------
# description = "Open/Closed: Open\\nDate of Discovery: 2022-06-01\\nTrade Partner: Cardinal Health\\nIssue Type: Missing File\\nData Type: 852\\nAction Taken: Reached out to TP\\nEmail Subject Line: Gilead - Missing Cardinal Health 852 File [2022-06-01]\\nContacts: johndoe@cardinalhealth.com\\nInvestigative Notes: IntegriChain discovered we have not received 852 files for Cardinal Health for transaction date 05/31.\\nContact Attempts: 1"
# b = description.replace('\\n', ' ').split()
# print('output is ', b)
# print(type(b))

# description = "Open/Closed: Open\\nDate of Discovery: 2022-06-01\\nTrade Partner: Cardinal Health\\nIssue Type: Missing File\\nData Type: 852\\nAction Taken: Reached out to TP\\nEmail Subject Line: Gilead - Missing Cardinal Health 852 File [2022-06-01]\\nContacts: johndoe@cardinalhealth.com\\nInvestigative Notes: IntegriChain discovered we have not received 852 files for Cardinal Health for transaction date 05/31.\\nContact Attempts: 1"
# data1 = json.loads(description)
# print(data1)
# print(type(data1))


# desc1 = description.split('\\')
# print(desc1)
# # emp_dict = {}
# for each_value in desc1:
#     print(each_value)
# if 'Trade Partner' in each_value:
#     print('yes')
#     res_dict = ast.literal_eval(each_value)
#     print(res_dict)

# print(len(i))
#     # k_v = i.split(':')
#     # print(k_v)

# list1 = description.split()
# dic = {}
# for entry in list1:
#     print(entry)
#     key, val = entry.split(':')
#     dic[key] = int(val)

# s = "tkt_"
# key_list = ['subject', 'description', 'status', 'client_name', 'transaction_date', 'trade_partner', 'discovery_date' 'data_type', 'issue_category', 'outreach_attempt', 'email_subject_line', 'contact_cc', 'data_issue_resolution']
# for k_l in key_list:
#     i = k_l
#     print(f"{s}{i}")

url = 'https://integrichain.zendesk.com/api/v2/search/incremental?per_page=30&include=highlights&page=1&type=ticket&query=DIR'
zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
json_response = json.loads(zen_auth_respo.text)

for dictionary in json_response['results']:
    print('All dicts are ', dictionary)

    tkt_status = dictionary['status']
    key_list = dictionary.keys()
    print('keys are', key_list)

    col_list = ['subject', 'description', 'status', 'client_name', 'transaction_date', 'trade_partner',
                'discovery_date' 'data_type', 'issue_category', 'outreach_attempt', 'email_subject_line', 'contact_cc',
                'data_issue_resolution']
    df = pd.DataFrame()
    emp_k_l_list = []
    for k_l in col_list:
        if k_l in dictionary.keys():
            print(k_l + ' key is present')
            # tkt_+ {k_l} = dictionary[k_l]
            print('And its value is ', dictionary[k_l])
            s = "tkt_"
            i = k_l
            col_name = f"{s}{i}"
            print('col_name value is ', col_name)
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
                    print('k_l is ', k_l)
                    emp_k_l_list = emp_k_l_list.append(k_l)
                    print('dictionary[k_l] is ', dictionary[k_l])

                    # df = pd.DataFrame(data=[dictionary[k_l]],
                    #                   columns=([f'{k_l}']))
                    df = pd.DataFrame({f'{k_l}': [dictionary[k_l]]})
                    print(df)
                    # emp_k_l_list = emp_k_l_list.append(k_l)
                    # print('Updated emp_k_l_list is ', emp_k_l_list)
            # emp_dict.update(f'k_l, dictionary[k_l])

        else:
            print(k_l + ' key is not present')


    df_final_excel = df.to_excel(f'C:/Users/dorugzu/PycharmProjects/pythonProject/pythonProject/Zendesk_API_Auto/utilities/output_excel.xlsx')
    print('Final Excel data is', df_final_excel)
    print('Excel printed successfully')

# df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 6, 9], "E": [4, 4, 4]})
# df.assign(C=df.A + df.B)
# print(df)

# Added lines for testing purpose
