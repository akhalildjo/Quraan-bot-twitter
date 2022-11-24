############################################################
# This code displays random verse from the Quran both in   #
# French                                   #
# -------------------------------------------------------- #
# API from http://api.alquran.cloud                        #
# Author: Ahmed Khalil (with help from AbdulBaqi, Abderrahman & Aymene)                  #
# Date: 2022                                               #
# ##########################################################

# This function takes a random number
# between 1 and 6237 (which are the total number of verses in the Quran)
# and returns:
# verse_fr: verse in French 
# sura: Name of surah in french, then number of sura and after : the number of verse
import random
import requests
import shutil
from pyuploadcare import File, conf
from pyuploadcare import Uploadcare
import os 

#Define HCTI API keys and link (don't forget to set config vars on Heroku)
HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
HCTI_API_USER_ID = os.getenv("HCTI_API_USER_ID")
HCTI_API_KEY = os.getenv("HCTI_API_KEY")

#Define uploadcare API keys ans save them into variable "uploadcare"
#uploadcare = os.getenv("Uploadcare") 
uploadcare = Uploadcare(public_key=os.getenv("public_key"), secret_key=os.getenv("secret_key"))

#The function that will parse a verse in french from the api alquran, we will call that function later
def bring_verse(verse):
    url = 'http://api.alquran.cloud/ayah/'+str(verse)+'/editions/quran-uthmani,fr.hamidullah'
    json_data = requests.get(url).json()
    verse_a = json_data['data'][0]['text']
    verse_en = json_data['data'][1]['text']
    sura = json_data['data'][0]['surah']['englishName']+\
           '('+str(json_data['data'][0]['surah']['number'])+'):'+\
           str(json_data['data'][0]['numberInSurah'])
    return [verse_en,sura]

#Bellow we will "randomize" a verse with random fucntion, then call it to generate new one with parser function we've defined earlier , then save it into a variable
aya = random.randint(1,6237)
link = bring_verse(aya)

#Formatting the response 
concat = '﴾'+link[0]+'۝'+'﴿'+'<br/><br/>-'+link[1]

#Insert the verse into html and css code, then as background use "background-image: url" css tag to use your background image saved in your local repository or elsewhere
data = {'html': f"<div class='wrapper text-center d-block p-4'><h1 class='text-white p-4 m-4'>{concat}</h1>,</div> <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' integrity='sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z' crossorigin='anonymous'>",
'css': "@import url('https://fonts.googleapis.com/css2?family=Fanwood+Text:ital@0;1&display=swap');.wrapper {font-family: 'Fanwood Text', serif;background-color: #000000;background-position: center;background-repeat: no-repeat;background-size: cover;height: 100%;width: 800px;background-image: url('{background_link}');}h1 {font-size: 4rem !important;}.highlight {color: #c72b4e;}"}

#Send the code above to HCTI APi, it will be converted to image
image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

#Display the link of generated image from HCTI
download = image.json()['url']
print (download)

#Send it to Uploadcare cloud hosting
ucare_file: File = uploadcare.upload(download)

#After what, a trigger will launch on Zapier.com, and post the image from Uploadcare to Twitter

