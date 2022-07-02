############################################################
# This code displays random verse from the Quran both in   #
# French (Pickthall)                                       #
# -------------------------------------------------------- #
# API from http://api.alquran.cloud                        #
# Author: Khalil (s/o Abdul Baqi)                          #
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
'css': "@import url('https://fonts.googleapis.com/css2?family=Fanwood+Text:ital@0;1&display=swap');.wrapper {font-family: 'Fanwood Text', serif;background-color: #000000;background-position: center;background-repeat: no-repeat;background-size: cover;height: 100%;width: 800px;background-image: url('data:image/svg+xml,%3C%3Fxml version='1.0' encoding='utf-8'%3F%3E%3C!-- Generator: Adobe Illustrator 26.0.0  SVG Export Plug-In . SVG Version: 6.00 Build 0) --%3E%3Csvg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='50 10 400 700' style='enable-background:new 0 0 508 768%3B' xml:space='preserve'%3E%3Cstyle type='text/css'%3E.st0%7Bfill:%231B1615%3B%7D.st1%7Bfill:%23606060%3B%7D.st2%7Bfill:%234E4B4C%3B%7D.st3%7Bfont-family:'AthelasArabic-Book'%3B%7D.st4%7Bfont-size:26.2068px%3B%7D.st5%7Bfill:%23B6996F%3B%7D.st6%7Bfill:%23FFFFFF%3B%7D.st7%7Bfill:%23606060%3Bstroke:%231D1D1B%3Bstroke-miterlimit:10%3B%7D%3C/style%3E%3Cg id='Calque_1'%3E%3Crect x='-1' y='-3' class='st0' width='250' height='30'/%3E%3Cg%3E%3Cg%3E%3Cg%3E%3Cpath class='st1' d='M278.6 439.57c5.3-8.83 11.56-18.96 14.27-26.99c2.33-6.92 2.55-8.39 5.13-16.17c3.23-9.73 3.92-20.04 2.82-30.24c-0.08-0.75-0.13-1.5-0.17-2.26c-0.17-3.26-0.87-6.49-2.18-9.48c-7.32-16.76-18.83-31.43-26.65-47.66c-8.73-18.12-15.73-33.57-9.79-52.92c0.83-2.45 0.75-4.57-2.04-5.72c-7.06 11.68-12.01 24.28-16.23 37.22c-5.45 16.7-3.42 32.22 6.56 46.82c6.44 9.42 12.61 19.05 18.46 28.84c11.32 18.95 16.87 39.15 12.12 61.34c-0.65 2.38-2.08 8.11-3.41 11.62c-0.02 0.05-0.04 0.09-0.05 0.14c-0.76 1.97-1.87 3.8-3.18 5.46l0 0c-4.71 5.21-8.35 11.7-16.12 15c1.71-21.8-2.83-41.22-14.5-58.63c-5.38-8.03-11.32-15.72-17.3-23.33c-14.88-18.9-19.44-40.21-16.14-63.79c1.96-13.97 5.9-27.51 7.84-41.5c-21.62 29.14-28.03 62.47-25.89 97.8c1.24 20.39 13.33 36.04 25.76 51.02c15.89 19.16 23.92 40.78 22.41 65.78c-0.08 1.29-0.62 2.97 1.73 4.01c6.83-4.24 12.11-10.43 17.27-16.72c7.11-8.68 13.03-18.15 18.37-28'/%3E%3Cpath class='st1' d='M262.04 253.85c-0.68-1.91-1.36-3.81-2.04-5.72c4.08-11.34 5.64-19.13 14.64-29.13C271.42 231.98 267.3 241.91 262.04 253.85z'/%3E%3C/g%3E%3Cg%3E%3Cpath class='st1' d='M317.45 198.74c-0.16 31.74 12.11 60.42 21.89 89.72c1.38 4.13 2.38 8.39 3.55 12.58c1.21 1.79 0.52 3.69 0.34 5.56c-0.39 1.11-1.16 2.04-1.54 3.16c-4.3 12.79-10.54 15.32-23.03 9.32c-14.34-33.75-25.36-68.11-19.52-105.61C300.89 205.49 308.04 199.73 317.45 198.74z'/%3E%3Cpath class='st1' d='M318.67 319.09c4.57-0.08 9.24-0.8 13.68-0.08c5.61 0.91 5.33-3.07 6.17-6.16c0.71-2.61-0.44-6.17 3.95-6.48c4.76 5.64 2.52 11.49 0.47 17.3c-0.75 2.12-2.46 3.04-4.66 3.42c-8.72 1.5-8.72 1.53-4.68 10.25c4.41-4.78 9.93-6.31 16.08-5.75c7.81 38.18-4.86 94.3-25.51 108.88c3.01-10.47 5.19-20.11 6.35-29.92c3.29-27.85-0.55-54.91-9.19-81.42C320.27 325.84 319.55 322.44 318.67 319.09z'/%3E%3Cpath class='st1' d='M308.95 162.28c6.43-27.22 17.26-52.44 33.78-75.15c-13.45 30.64-19.01 63.16-24.3 95.76c-1.77 1.5-3.51 3.08-5.87 3.59c-4.61 1-7.37-0.39-7.23-5.62C305.52 174.46 308.2 168.56 308.95 162.28z'/%3E%3Cpath class='st1' d='M308.95 162.28c0.09 4.32-0.24 8.49-1.86 12.65c-1.11 2.85-1.85 6.35 0.37 9.08c2.82 3.46 4.97-0.94 7.54-1.06c1.14-0.05 2.29-0.04 3.43-0.06c-0.33 5.29-0.66 10.57-0.99 15.86c-6.05 4.97-14.92 6.43-18.29 14.74C300.29 196 303.35 178.9 308.95 162.28z'/%3E%3Cpath class='st1' d='M349.69 331.59c-2.07 1.01-4.29 3.08-6.2 2.82c-6.1-0.83-7.44 3.01-8.2 8.74c-5.14-4.7-6.44-10.05-7.88-15.12c-0.89-3.16 0.99-5.02 4.48-4.46c2.96 0.48 6.81 4.08 8.63 0.43c1.82-3.65 3.62-7.99 3.08-12.52c-0.21-1.73-0.74-3.41-1.13-5.12c0.14-1.77 0.28-3.55 0.42-5.32C346.8 310.86 348.87 321.09 349.69 331.59z'/%3E%3C/g%3E%3Cpath class='st1' d='M186.7 215.15l-0.23 25.14c0 0.36 0.2 0.69 0.53 0.84l23.69 11.16c0.56 0.26 1.22-0.09 1.31-0.7l2.48-16.87c0.08-0.52 0.58-0.88 1.1-0.77l17.31 3.52c0.55 0.11 1.07-0.29 1.11-0.85l1.02-17.69c0.03-0.57 0.57-0.97 1.12-0.85l16.69 3.67c0.6 0.13 1.17-0.35 1.12-0.97l0.05-26.84c-0.02-0.34-0.24-0.64-0.55-0.78l-23.88-9.56c-0.63-0.28-1.33 0.21-1.29 0.9l1.16 19.39c0.04 0.64-0.56 1.12-1.18 0.94l-20.64-5.87c-0.59-0.17-1.18 0.28-1.18 0.89l0.01 17.85c0 0.6-0.56 1.04-1.15 0.9l-17.44-4.32C187.27 214.12 186.71 214.55 186.7 215.15z'/%3E%3Cg%3E%3Cpath class='st1' d='M170.07 395.58c4.46 31.42 20.77 58.02 34.71 85.58c1.96 3.88 3.57 7.95 5.34 11.93c1.45 1.59 1.05 3.57 1.15 5.45c-0.22 1.16-0.85 2.19-1.06 3.35c-2.39 13.28-8.19 16.69-21.43 12.57c-19.1-31.3-35-63.69-34.67-101.64C154.67 404.66 160.91 397.92 170.07 395.58z'/%3E%3Cpath class='st1' d='M188.79 514.46c4.51-0.75 9.03-2.14 13.52-2.07c5.68 0.08 4.82-3.81 5.21-6.99c0.33-2.68-1.33-6.05 2.97-6.98c5.53 4.88 4.17 11 2.98 17.04c-0.43 2.21-1.99 3.37-4.11 4.06c-8.41 2.75-8.4 2.79-3.14 10.82c3.67-5.37 8.9-7.69 15.08-8.02c13.28 36.64 8.91 94.01-9.4 111.43c1.45-10.8 2.21-20.66 1.93-30.53c-0.8-28.03-8.53-54.24-20.94-79.22C191.35 520.91 190.15 517.65 188.79 514.46z'/%3E%3Cpath class='st1' d='M156.36 360.74c2.4-27.87 9.45-54.39 22.49-79.26c-8.85 32.27-9.62 65.26-10.11 98.27c-1.54 1.74-3.03 3.56-5.28 4.41c-4.41 1.66-7.35 0.68-7.97-4.51C154.73 373.29 156.52 367.06 156.36 360.74z'/%3E%3Cpath class='st1' d='M156.36 360.74c0.71 4.26 0.99 8.44 0 12.79c-0.68 2.98-0.91 6.55 1.69 8.92c3.29 3.01 4.78-1.65 7.3-2.15c1.12-0.22 2.26-0.37 3.38-0.55c0.44 5.28 0.89 10.55 1.33 15.83c-5.26 5.8-13.82 8.53-15.95 17.24C152.69 395.36 153.24 377.99 156.36 360.74z'/%3E%3Cpath class='st1' d='M221.3 522.32c-1.91 1.3-3.8 3.68-5.72 3.69c-6.15 0.06-6.92 4.06-6.84 9.84c-5.77-3.9-7.84-9.01-10-13.81c-1.34-2.99 0.24-5.11 3.78-5.06c3 0.04 7.33 3.04 8.6-0.83c1.27-3.87 2.42-8.43 1.22-12.83c-0.46-1.68-1.23-3.27-1.86-4.9c-0.12-1.77-0.24-3.55-0.36-5.32C215.42 502.23 218.96 512.05 221.3 522.32z'/%3E%3C/g%3E%3Cpolygon class='st1' points='265.64 233 257.14 253.11 261.64 249 '/%3E%3Cpolygon class='st1' points='265.35 246.21 260.6 259.33 260.6 253.11 '/%3E%3Cpolygon class='st1' points='261.37 257.22 260.1 261.95 260.64 258 '/%3E%3Cpolygon class='st1' points='267.32 229.26 249.41 269.69 257.74 259.59 '/%3E%3Cg%3E%3Cpath class='st1' d='M299.13 355.5c-1.81-6.17-4.38-12.18-7.78-18.06c-4.76-8.24-10.11-16.19-15.51-24.08c-13.44-19.59-16.17-40.52-10.67-62.86c3.26-13.24 8.5-25.88 11.74-39.14c-24.65 25.94-35.25 57.49-36.26 91.65c-0.55 18.71 11.35 33.15 22 48L299.13 355.5z'/%3E%3C/g%3E%3C/g%3E%3C/g%3E%3Cg%3E%3Ctext transform='matrix(1 0 0 1 149.5017 708.9355)' class='st2 st3 st4'%3E%40_SaintCoranSVG%3C/text%3E%3C/g%3E%3C/g%3E%3Cg id='Calque_2'%3E%3C/g%3E%3Cg id='Calque_3'%3E%3C/g%3E%3C/svg%3E');}h1 {font-size: 4rem !important;}.highlight {color: #c72b4e;}"}

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))
#image = open("image.svg", "w")
#image.write(data)
#image.close()