import yaml

text = "Input a key value to find in dict.\n \
To search value in nested dictionary, input \n \
values in order, separate by space. \n\
To exit, enter blank line.\n\n"


with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)

keys = input(text)
if not(keys):
    print("booba")
    exit
keys = keys.split()
value = data

key = None
try:
    for key in keys:
            value = value[key]
except KeyError:
    raise Exception(f"Error in confguraton: no such key {key}") from None

print(value)
