import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import html2text as HtT
from googletrans import Translator, constants
from selenium.common.exceptions import WebDriverException

data = pd.read_csv('test.csv')
df = pd.DataFrame(data, columns=['Country (mentioned)', 'Claim', 'Source', 'Fact-checked Article'])
cols_as_np = df[df.columns[0]].to_numpy()

#selenium + translation setup
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = wd.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=chrome_options)
translator = Translator()

# driver.get("https://www.asu.edu/")  if you want an example of the text outputted, uncomment this section
# html = driver.page_source
# text = HtT.html2text(html)
# print(text)

# Country keys
countriesZero = ["Africa",
                 "Albania",
                 "Algeria",
                 "Almeria",
                 "Bangladesh",
                 "Barbados",
                 "Belarus",
                 "Bolivia",
                 "Bulgaria",
                 "Burundi",
                 "CÃ´te d'Ivoire",
                 "California",
                 "Cameroon",
                 "Costa Rica",
                 "Democratic Republic of Congo",
                 "Democratic Republic of the Congo",
                 "Ecuador",
                 "El Salvador",
                 "Ethiopia",
                 "European",
                 "Georgia",
                 "Ghana",
                 "Gibraltar",
                 "Guinea",
                 "Haiti",
                 "Honduras",
                 "Iran",
                 "Jakarta",
                 "Jamaica",
                 "Korea",
                 "Laos",
                 "Liberia",
                 "Madagascar",
                 "Malawi",
                 "Martinique",
                 "Morocco",
                 "Myanmar",
                 "Nepal",
                 "Palestinian Territory",
                 "Paraguay",
                 "Puerto Rico",
                 "Rwanda",
                 "Saudi Arabia",
                 "Senegal",
                 "Slovakia",
                 "South African",
                 "South Sudan",
                 "Syria",
                 "Tunisia",
                 "Uganda",
                 "United Arab Emirates",
                 "United Statets",
                 "Uruguay",
                 "Vaccine",
                 "Vatican City",
                 "world wide",
                 "World wide",
                 "worldwide",
                 "Worldwide",
                 "Zimbabwe"]
countriesOne = ["Bosina",
                "Lebanon",
                "Qatar",
                "Scotland",
                "Seychelles",
                "United KIngdom"]
countriesTwo = ["Antarctica"]
countriesThree = ["Guinea-Bissau"]
sourceZero = ["audio recording",
              "bernie sanders",
              "daily expose",
              "email",
              "emmanuel macron",
              "facbook",
              "fake document",
              "flÃ¡vio bolsonaro",
              "flavio bolsonaro",
              "Harry Roque",
              "health department",
              "Jair Bolsonaro",
              "joÃ£o doria",
              "lord sumption",
              "michaÅ‚ dworczyk",
              "michael yeedon",
              "multiple persons",
              "Multiple sources",
              "multiplie sources",
              "multple sources",
              "mutliple sources",
              "news website",
              "nick donnelly",
              "scam",
              "social networks",
              "sophia dorinskaya",
              "steven hotze",
              "tayyip erdogan",
              "telegram",
              "telegraph",
              "various authors",
              "viral image",
              "websites",
              "whataspp"]
sourceOne = ["andrÃ©s manuel lÃ³pez obrador",
             "carlos bolsonaro",
             "government source",
             "ione belarra",
             "michael \"mike\" defensor",
             "narendra modi",
             "Several sources",
             "Social Networking Media Users"]
sourceTwo = ["government party",
             "pereson"]
sourceThree = ["anthony fauci",
               "doctors for life",
               "reddit"]
urlZero = ["http://aosfatos.org",
           "http://checkyourfact.com",
           "https://aajtak.intoday.in",
           "https://annielab.org",
           "https://aosfatos.org",
           "https://az.teyit.org",
           "https://cinjenice.afp.com",
           "https://efectococuyo.com",
           "https://fit.thequint.com",
           "https://ghanafact.com",
           "https://hindi.asianetnews.com",
           "https://hindi.boomlive.in",
           "https://hindi.thequint.com",
           "https://kalimasada.turnbackhoax.id",
           "https://kannada.asianetnews.com",
           "https://malayalam.samayam.com",
           "https://maldita.es",
           "https://namibiafactcheck.org.na",
           "https://navbharattimes.indiatimes.com",
           "https://observador.pt",
           "https://observers.france24.com",
           "https://oglobo.globo.com",
           "https://proveri.afp.com",
           "https://rappler.com",
           "https://sciencefeedback.co",
           "https://scroll.in",
           "https://srilanka.factcrescendo.com",
           "https://tamil.factcrescendo.com",
           "https://telugu.newsmeter.in",
           "https://tfc-taiwan.org.tw",
           "https://timesofindia.indiatimes.com",
           "https://verifica.efe.com",
           "https://verificado.com.mx",
           "https://verificat.afp.com",
           "https://www.aajtak.in",
           "https://www.abc.net.au",
           "https://www.altnews.in",
           "https://www.animalpolitico.com",
           "https://www.aosfatos.org",
           "https://www.asianetnews.com",
           "https://www.bbc.com",
           "https://www.boatos.org",
           "https://www.boombd.com",
           "https://www.boomlive.in",
           "https://www.cbsnews.com",
           "https://www.dogrulukpayi.com",
           "https://www.efe.com",
           "https://www.ellinikahoaxes.gr",
           "https://www.factchecker.in",
           "https://www.factcrescendo.com",
           "https://www.factrakers.org",
           "https://www.faktisk.no",
           "https://www.fastcheck.cl",
           "https://www.malumatfurus.org",
           "https://www.mygopen.com",
           "https://www.newsstate.com",
           "https://www.noz.de",
           "https://www.oneindia.com",
           "https://www.thequint.com",
           "https://www.thip.media",
           "https://www.tjekdet.dk",
           "https://www.voachinese.com",
           "https://youturn.in",
           "https://zimfact.org"]
urlOne = ["https://comprovem.afp.com",
          "https://evrimagaci.org",
          "https://www.eltiempo.com",
          "https://www.nytimes.com"]
urlTwo = ["https://www.faitscovid19.ca",
          "https://www.poynter.org"]


def checkURL(urlArray, url):
    temp = 0
    for full in urlArray:
        if url.find(full) != -1:
            temp = 1
    return temp

Id = 0
numZeros = 0
numOnes = 0
numTwos = 0
numThree = 0
submission = pd.DataFrame()

for index, row in df.iterrows():
    print("claim number is ")
    print(Id)
    Id += 1
    if row['Country (mentioned)'] in countriesZero:
        print("country", 0)
        submission.append({'Id': Id, "Category": 0})
    elif row['Country (mentioned)'] in countriesOne:
        print("country", 1)
        submission.append({'Id': Id, "Category": 1})
    elif row['Country (mentioned)'] in countriesTwo:
        print("country", 2)
        submission.append({'Id': Id, "Category": 2})
    elif row['Country (mentioned)'] in countriesThree:
        print("country", 3)
        submission.append({'Id': Id, "Category": 3})
    elif row['Source'] in sourceZero:
        print("Source", 0)
        submission.append({'Id': Id, "Category": 0})
    elif row['Source'] in sourceOne:
        print("Source", 1)
        submission.append({'Id': Id, "Category": 1})
    elif row['Source'] in sourceTwo:
        print("Source", 2)
        submission.append({'Id': Id, "Category": 2})
    elif row['Source'] in sourceThree:
        print("Source", 3)
        submission.append({'Id': Id, "Category": 3})
    elif checkURL(urlZero, row['Fact-checked Article']) == 1:
        print("URL", 0)
        submission.append({'Id': Id, "Category": 0})
    elif checkURL(urlOne, row['Fact-checked Article']) == 1:
        print("URL", 1)
        submission.append({'Id': Id, "Category": 1})
    elif checkURL(urlTwo, row['Fact-checked Article']) == 1:
        print("URL", 2)
        submission.append({'Id': Id, "Category": 2})
    else:
    #selenium open/save text of article
        checkedURL = row['Fact-checked Article']
        try:
            driver.get(checkedURL)
            html = driver.page_source
            text = HtT.html2text(html) # this gives us all the text from the body of the website + a lil more that 
            englishText = translator.translate(text) # translates to english automatically, can then search englishText
            TranslatedText = englishText.text
            score = -1

            if("false" in TranslatedText):
                score = 0
                numZeros += 1
            elif("misleading" in TranslatedText):
                score = 1
                numOnes += 1
            elif("true" in TranslatedText):
                score = 2
                numTwos += 1
            elif("unproven" in TranslatedText):
                score = 3
                numThree += 1
            submission.append({'Id': Id, "Category": score})
        except WebDriverException:
            print() # website is down
            score = 0
            submission.append({'Id': Id, "Category": score})

print("Number of 0's from scraping")
print(numZeros)
print("Number of 1's from scraping")
print(numOnes)
print("Number of 2's from scraping")
print(numTwos)
print("Number of 3's from scraping")
print(numThree)
submission.to_csv('submission.csv')
