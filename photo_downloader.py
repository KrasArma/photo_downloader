import pandas
import requests

df = pandas.read_excel("file_links.xlsx")

def downloader(url=''):
    try:
        responce = requests.get(url=url)
        z = df.at[i, 'Line']
        with open(f'photo{z} {j}', 'wb') as file:
            file.write(responce.content)
        return 'Ok'
    except:
        if url.find('http') >= 0:
            with open('bug_tracking.txt', 'a') as file:
                z = df.at[i, "Line"]
                file.write(f'Line: {z} Column: {j} not downloaded')

for i, row in df.iterrows():
    for j, value in row.items():
        if pandas.notna(value):
            if __name__ == '__main__':
                print(downloader_photo(url=f'{value}'))