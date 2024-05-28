url = input()
key = input()
query_dict = {key: value for key, value in [pair.split('=') for pair in url.split('?')[1].split('&')]}
value = query_dict[key]
print(value)