import yaml

new_data = {
    "age": 26,
    "city": "Warsaw"

}

with open('data.yml', "r") as file: #Read from a yaml file
    data = yaml.safe_load(file)
    data['name'] = "Wasiq"


with open('data.yml', "a") as file:
    yaml.dump(new_data, file, default_flow_style=False)

