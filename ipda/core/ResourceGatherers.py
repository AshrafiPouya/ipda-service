import re
import requests

base_url = 'https://yt.artemislena.eu'

key = ' <source src=(\"\/latest_version\?id.+?local=true\")'

txt = requests.get('https://yt.artemislena.eu/watch?v=bwEIqjU2qgk').text

result = re.search(key, txt).groups(0)[0][1:-1]

final = base_url+result
