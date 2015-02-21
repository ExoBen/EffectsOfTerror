import requests

r = requests.post('https://http-api.openbloomberg.com/', cert=('../../keys/stacshack_spring_2015_023.crt', '../../keys/stacshack_spring_2015_023.key'), verify=False)

r.text
