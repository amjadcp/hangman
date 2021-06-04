import random

def Fruits():
  fruits=[
  "Abiu",
  "Açaí",
  "Acerola",
  "Ackee",
  "Africancucumber",
  "Apricot",
  "Avocado",
  "Banana",
  "Bilberry",
  "Blackberry",
  "Blackcurrant",
  "Blacksapote",
  "Blueberry",
  "Boysenberry",
  "Breadfruit"
   ]
  word = random.choice(fruits)
  return word
   

def Countries():
    countries=[
    "afghanistan",
    "albania",
    "Argentina",
    "america",
    "brazil",
    "Australia",
    "india",
    "pakistan",
    "chaina"
    ]
    word = random.choice(countries)
    return word


def Currencies():
    currencies = [
    "afghani",
    "euro",
    "colon",
    "crown",
    "rupee",
    "doller",
    "dalasi",
    "dinar",
    "kina",
    "kuna"
    ]
    word = random.choice(currencies)
    return word


def States():
    states =[
    "bihar",
    "kerala",
    "karnadaka",
    "thamizhndu",
    "manipur",
    "mizoram"
    ]
    word = random.choice(states)
    return word
