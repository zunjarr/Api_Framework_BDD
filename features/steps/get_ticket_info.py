import requests
import json
import jsonpath

# url = 'https://integrichain.zendesk.com/agent/tickets/45763'
# url = 'https://integrichain.zendesk.com/agent/tickets/45763.json'

# url = 'https://integrichain.zendesk.com/api/v2/tickets/45763.json'
url = "https://integrichain.zendesk.com/api/v2/tickets/45763.json"
# url = 'https://integrichain.zendesk.com/api/v2/tickets.json'


zen_auth_respo = requests.get(url, auth=('zdorugadde@integrichain.com', 'Zendesk@7'))
print('zen_auth_respo is ', zen_auth_respo)

# response = requests.get(url)
print("response code is ", zen_auth_respo.status_code)
assert zen_auth_respo.status_code == 200, "Wrong status_code"
print("The content/Body is ", zen_auth_respo.content)
print(type(zen_auth_respo.content))

# print("Headers are ", zen_auth_respo.headers)
# print(type(zen_auth_respo.headers))
# print("response.json is ", zen_auth_respo.json())
json_response = json.loads(zen_auth_respo.text)

# print("json dumps is ", json.dumps(zen_auth_respo.json(), indent=4))

# print(type(zen_auth_respo.content))

# Fetch value using JSON path
id_of_ticket = jsonpath.jsonpath(json_response, "id")

id_of_ticket = zen_auth_respo.json()['ticket']['id']
print("Fetched id_of_ticket is ", id_of_ticket)

subject = zen_auth_respo.json()['ticket']['subject']
print("Fetched subject is ", subject)

description = zen_auth_respo.json()['ticket']['description']
print("Fetched description is ", description)
print(type(description))

priority = zen_auth_respo.json()['ticket']['priority']
print("Fetched priority is ", priority)

tags = zen_auth_respo.json()['ticket']['tags']
print("Fetched tags is ", tags)

trade_partner = zen_auth_respo.json()['ticket']['description'][30:63]
print("Fetched trade_partner is ", trade_partner)

assignee_id = zen_auth_respo.json()['ticket']['description']['assignee_id']
print("Fetched trade_partner is ", assignee_id)




# new_client = 360030348131
# SMITH DRUG COMPANY = 1900002207527
# datatype_852 = 360048136872
# issuecat_line_count = 360044982192
# ticket_form_id = 360003260872
# brand_id = 360003716372


# print(type(id_of_ticket))
# print("Fetched id_of_ticket is ", id_of_ticket)
# data = json.dumps(ticket)
# print('Data is ', data)

# Difference between json.loads(), load and dumps
# zunjar dorugade
# Zendesk@7
# zdorugadde@integrichain.com
