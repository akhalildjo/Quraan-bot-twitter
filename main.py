############################################################
# This code displays random verse from the Quran both in   #
# French                                   #
# -------------------------------------------------------- #
# API from http://api.alquran.cloud                        #
# Author: Khalil (s/o Abdul Baqi & Aymen)                  #
# Date: 2022                                               #
# ##########################################################

# This function takes a random number
# between 1 and 6237 (which are the total number of verses in the Quran
# and returns:
# verse_fr: verse in French 
# sura: Name of surah in french, then number of sura and after : the number of verse
import random
import requests
import shutil
from pyuploadcare import File, conf
from pyuploadcare import Uploadcare

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
HCTI_API_USER_ID = '61cadc9f-a8f0-4ae9-bdd5-55bdc7665e12'
HCTI_API_KEY = '10bf943e-b62b-4d0d-85d5-2fc55b9a78f3'

uploadcare = Uploadcare(public_key='2d4e43fc3c8a34c42899', secret_key='feafd32694f41f3d88ed')


def bring_verse(verse):
    url = 'http://api.alquran.cloud/ayah/'+str(verse)+'/editions/quran-uthmani,fr.hamidullah'
    json_data = requests.get(url).json()
    verse_a = json_data['data'][0]['text']
    verse_en = json_data['data'][1]['text']
    sura = json_data['data'][0]['surah']['englishName']+\
           '('+str(json_data['data'][0]['surah']['number'])+'):'+\
           str(json_data['data'][0]['numberInSurah'])
    return [verse_en,sura]

aya = random.randint(1,6237)
link = bring_verse(aya)

concat = '﴾'+link[0]+'۝'+'﴿'+'<br/><br/>-'+link[1]

response=concat
response2=link[1]

data = {'html': f"<div class='wrapper text-center d-block p-4'><h1 class='text-white p-4 m-4'>{response}</h1>,</div> <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' integrity='sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z' crossorigin='anonymous'>",
'css': "@import url('https://fonts.googleapis.com/css2?family=Fanwood+Text:ital@0;1&display=swap');.wrapper {font-family: 'Fanwood Text', serif;background-color: #000000;background-position: center;background-repeat: no-repeat;background-size: cover;height: 100%;width: 800px;background-image: url('https://cdn.discordapp.com/attachments/977531626584145920/993164648633352322/fond.svg');}h1 {font-size: 4rem !important;}.highlight {color: #c72b4e;}"}

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

#print("Your image URL is: %s"%image.json()['url'])

download = image.json()['url']
print (download)

"""res = requests.get(download, stream = True)
file_name = 'ayah.png'
if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')
"""

ucare_file: File = uploadcare.upload(download)
