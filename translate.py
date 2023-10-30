import googletrans

def trans(text):
    trans = googletrans.Translator()
    result = trans.translate(text, dest='en')
    return(result.text)