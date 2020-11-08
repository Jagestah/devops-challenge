import requests
import yaml
import time

# save an empty list to house the data that will be written to the json file that will result from this app
output = []

# call to the swapi url of a given list of urls returned as the value of a key in my original request
def fetch_swapi_object(url):
    # films do not seem to have a key of name and therefore must have their own logic, all other objects I've tested with do
    # if future objects are discovered to have some other identifier in their keys that would be logical to add, it can be added here
    # always check for an object where name will work first to slightly increase the speed of building the final list to write to the file
    if "films" not in url:
        return requests.get(url=url).json()['name']
    else:
        return requests.get(url=url).json()['title']

#open the input.yaml file, read from it, call to the swapi api, filter for only desired keys listed in infoRequest and build the list
with open(r'input.yaml') as file:
    documents = yaml.full_load(file)

    for _, v in documents.items():
        for info_request in v:
            response = requests.get(url=f"https://swapi.dev/api/{info_request['type']}/{info_request['id']}").json()
            output_item = {}
            
            for input_yaml_inforequest_key in info_request['infoRequest']:
                if type(response[input_yaml_inforequest_key]) is list:
                    sub_list = []
                    for value in response[input_yaml_inforequest_key]:
                        sub_list.append(fetch_swapi_object(value))
                    output_item[input_yaml_inforequest_key] = sub_list
                else:
                    output_item[input_yaml_inforequest_key] = response[input_yaml_inforequest_key]
            output.append(output_item)

# create the new file with arg "x", then write my list to it
with open('swapi-output.json', 'x') as output_file:
        output_file.write(f'{output}')

time.sleep(10000)