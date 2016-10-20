import json
from translate import Translator

def translateSentence(text):
	languages = [
		{ 'lang_id':	'hu',	'language':	'Hungarian'	}
		,{ 'lang_id':	'fr',	'language':	'French'	}
		,{ 'lang_id':	'de',	'language':	'German'	}
		,{ 'lang_id':	'es',	'language':	'Spanish'	}
		,{ 'lang_id':	'it',	'language':	'Italian'	}
	]

	sentence_eng = text
	sentence_lan = "\n"

	for i in range(0,len(languages)):
		links = []
		lang_id = languages[i]['lang_id']
		language = languages[i]['language']

		translator= Translator(to_lang=lang_id)
		translation = translator.translate(sentence_eng)
		
		sentence_lan=sentence_lan+language+" : "+translation+"\n"

	return sentence_lan
