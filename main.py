import requests

with open('sources/links.txt', 'r') as file:
    links = file.read().splitlines()

print('Downloading files...')

for link in links:
    name = link[link.rfind('/')+1:]
    response = requests.get(link)
    with open(f'downloads/{name}', 'wb') as file:
        file.write(response.content)

print('Download complete!\n').upper()