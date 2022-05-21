############################################################
# This code displays random verse from the Quran both in   #
# Arabic original and English translation (Pickthall)      #
# -------------------------------------------------------- #
# API from http://api.alquran.cloud                        #
# Author: Abdul Baqi                                       #
# Date: Oct 2018                                           #
# ##########################################################

import random
import requests

# This function takes a random number
# between 1 and 6237 (which are the total number of verses in the Quran
# and returns:
# verse_fr: verse in French (Pickthall translation)
# sura: Name of surah in english, then number of sura and after : the number of verse
# example: Taa-Haa(20):108
HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
HCTI_API_USER_ID = '294236c3-0e9f-48d7-999e-4ff5c0db9e9e'
HCTI_API_KEY = '6c47f721-4ed9-4b7b-87ad-369abea0f105'

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

concat = '﴾'+link[0]+'﴿'+'<br/><br/>-'+link[1]
#print(concat)
#print(link[0])
#print(link[1])
#output = {'response':link[0], 'response2':link[1]}
#output = {'response':concat, 'response2':link[1]}

response=concat
response2=link[1]

data = {'html': f"<div class='wrapper text-center d-block p-4'><h1 class='text-white p-4 m-4'>{response}</h1>,</div> <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' integrity='sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z' crossorigin='anonymous'>",
'css': ".wrapper {width: 800px;background-color: #000000;background-image: url(/fond.svg);} h1{font-size: 4rem !important;}.highlight {color: #c72b4e;}"}

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))
print("Your image URL is: %s"%image.json()['url'])