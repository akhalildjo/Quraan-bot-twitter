import random
import requests
import tweepy

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
HCTI_API_USER_ID = '1f4eb7e2-46c8-471c-b6d4-86cfad39a1e0'
HCTI_API_KEY = '4411ee60-4bbd-42e8-a751-045c12ee61bb'

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAMqZeQEAAAAA2MEKDzeejFu6HdCxgbZ0na7Ug5M%3DPbkKQYsyZjrduHXvhhNwPbaaL8ocRaAXEm0e5Vy0j9qXSbaVAQ")
api = tweepy.API(auth)

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

response=concat
response2=link[1]

data = {'html': f"<div class='wrapper text-center d-block p-4'><h1 class='text-white p-4 m-4'>{response}</h1>,</div> <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' integrity='sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z' crossorigin='anonymous'>",
'css': "@import url('https://fonts.googleapis.com/css2?family=Fanwood+Text:ital@0;1&display=swap');.wrapper {font-family: 'Fanwood Text', serif;background-color: #000000;background-position: center;background-repeat: no-repeat;background-size: cover;height: 100%;width: 800px;background-image: url('https://cdn.discordapp.com/attachments/658453312492011576/992920940482666667/fond.svg');}h1 {font-size: 4rem !important;}.highlight {color: #c72b4e;}"}

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

