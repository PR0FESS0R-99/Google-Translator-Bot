from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 

LANGUAGE = InlineKeyboardMarkup(
 [[
 InlineKeyboardButton("Afrikaans", callback_data='lang af')
 ],[
 InlineKeyboardButton("Albanian", callback_data='lang sq')
 ],[
 InlineKeyboardButton("Amharic",callback_data ='lang am')
 ],[  
 InlineKeyboardButton("Arabic", callback_data='lang ar')
 ],[
 InlineKeyboardButton("Armenian", callback_data='lang hy') 
 ],[
 InlineKeyboardButton("Azerbaijani",callback_data = 'lang az')       
 ],[
 InlineKeyboardButton("Basque",callback_data ="lang eu")
 ],[
 InlineKeyboardButton("Belarusian",callback_data ="lang be")
 ],[
 InlineKeyboardButton("Bengali",callback_data="lang bn")
 ],[
 InlineKeyboardButton("Bosnian",callback_data = "lang bs")
 ],[
 InlineKeyboardButton("Bulgarian",callback_data ="lang bg")
 ],[
 InlineKeyboardButton("Catalan",callback_data = "lang ca")
 ],[ 
 InlineKeyboardButton("Corsican",callback_data ="lang co")
 ],[
 InlineKeyboardButton("Croatian",callback_data = "lang hr")
 ],[
 InlineKeyboardButton("Czech", callback_data = "lang cs")
 ],[
 InlineKeyboardButton("Danish",callback_data = "lang da")
 ],[
 InlineKeyboardButton("Dutch",callback_data = "lang nl")
 ],[
 InlineKeyboardButton("Esperanto",callback_data = "lang eo")
 ],[
 InlineKeyboardButton("English",callback_data = "lang en")
 ],[
 InlineKeyboardButton("Estonian",callback_data = "lang et")
 ],[
 InlineKeyboardButton("Finnish",callback_data = "lang fi")
 ],[
 InlineKeyboardButton("French",callback_data = "lang fr")
 ],[
 InlineKeyboardButton("Frisian",callback_data = "lang fy")
 ],[
 InlineKeyboardButton("Galician",callback_data = "lang gl")
 ],[
 InlineKeyboardButton("Georgian",callback_data = "lang ka")
 ],[
 InlineKeyboardButton("German",callback_data = "lang de")
 ],[
 InlineKeyboardButton("Greek",callback_data = "lang el")
 ],[
 InlineKeyboardButton("Gujarati",callback_data = "lang gu")
 ],[
 InlineKeyboardButton("Haitian Creole",callback_data = "lang ht")
 ],[
 InlineKeyboardButton("Hausa",callback_data ="lang ha")
 ],[
 InlineKeyboardButton("Hindi",callback_data = "lang hi")
 ],[
 InlineKeyboardButton("Hungarian",callback_data = "lang hu")
 ],[
 InlineKeyboardButton("Icelandic",callback_data = "lang is")
 ],[
 InlineKeyboardButton("Igbo",callback_data = "lang ig")
 ],[
 InlineKeyboardButton("Indonesian",callback_data = "lang id")
 ],[
 InlineKeyboardButton("Irish",callback_data = "lang ga")
 ],[
 InlineKeyboardButton("Italian",callback_data = "lang it")
 ],[
 InlineKeyboardButton("Japanese",callback_data = "lang ja")
 ],[
 InlineKeyboardButton("Javanese",callback_data = "lang jv")
 ],[
 InlineKeyboardButton("Kannada",callback_data = "lang kn")
 ],[
 InlineKeyboardButton("Kazakh",callback_data = "lang kk")
 ],[
 InlineKeyboardButton("Khmer",callback_data = "lang km")
 ],[
 InlineKeyboardButton("Kinyarwanda",callback_data = "lang rw")
 ],[
 InlineKeyboardButton("Korean",callback_data ="lang ko")
 ],[
 InlineKeyboardButton("Kurdish",callback_data = "lang ku")
 ],[
 InlineKeyboardButton("Kyrgyz",callback_data ="lang ky")
 ],[
 InlineKeyboardButton("Lao",callback_data = "lang lo")
 ],[
 InlineKeyboardButton("Latin",callback_data = "lang la")
 ],[
 InlineKeyboardButton("Latvian",callback_data = "lang lv")
 ],[
 InlineKeyboardButton('Lithuanian',callback_data ="lang lt")
 ],[
 InlineKeyboardButton("Luxembourgish",callback_data = "lang lb")
 ],[
 InlineKeyboardButton("Macedonian",callback_data = "lang mk")
 ],[
 InlineKeyboardButton("Malagasy",callback_data ="lang mg")
 ],[
 InlineKeyboardButton("Malay",callback_data ="lang ms")
 ],[
 InlineKeyboardButton("Malayalam",callback_data = "lang ml")
 ],[
 InlineKeyboardButton("Maltese",callback_data = "lang mt")
 ],[
 InlineKeyboardButton("Maori",callback_data = "lang mi")
 ],[
 InlineKeyboardButton("Marathi",callback_data = "lang mr")
 ],[
 InlineKeyboardButton("Mongolian",callback_data = "lang mn")
 ],[
 InlineKeyboardButton("Myanmar (Burmese)",callback_data = "lang my")
 ],[
 InlineKeyboardButton("Nepali",callback_data ="lang ne")
 ],[
 InlineKeyboardButton("Norwegian",callback_data = "lang no")
 ],[
 InlineKeyboardButton("Nyanja (Chichewa)",callback_data = "lang ny")
 ],[
 InlineKeyboardButton("Odia",callback_data = "lang or")
 ],[
 InlineKeyboardButton("Pashto",callback_data = "lang ps")
 ],[
 InlineKeyboardButton("Persian",callback_data = "lang fa")
 ],[
 InlineKeyboardButton("Polish",callback_data = "lang pl")
 ],[
 InlineKeyboardButton("Portuguese",callback_data = "lang pt")
 ],[
 InlineKeyboardButton("Punjabi",callback_data = "lang pa")
 ],[
 InlineKeyboardButton("Romanian",callback_data = "lang ro")
 ],[
 InlineKeyboardButton("Russian",callback_data = "lang ru")
 ],[
 InlineKeyboardButton("Samoan",callback_data= "lang sm")
 ],[
 InlineKeyboardButton("Scots Gaelic",callback_data = "lang gd")
 ],[
 InlineKeyboardButton("Serbian",callback_data = "lang sr")
 ],[
 InlineKeyboardButton("Sesotho",callback_data = "lang st")
 ],[
 InlineKeyboardButton("Shona",callback_data ="lang sn")
 ],[
 InlineKeyboardButton("Sindhi",callback_data ="lang sd")
 ],[
 InlineKeyboardButton("Sinhala (Sinhalese)",callback_data = "lang si")
 ],[
 InlineKeyboardButton("Slovak",callback_data = "lang sk")
 ],[
 InlineKeyboardButton("Slovenian",callback_data = "lang sl")
 ],[
 InlineKeyboardButton("Somali",callback_data = "lang so")
 ],[
 InlineKeyboardButton("Spanish",callback_data = "lang es")
 ],[
 InlineKeyboardButton("Sundanese",callback_data ="lang su")
 ],[
 InlineKeyboardButton("Swahili",callback_data ="lang sw")
 ],[
 InlineKeyboardButton("Swedish",callback_data = "lang sv")
 ],[
 InlineKeyboardButton("Tagalog (Filipino)",callback_data ='lang tl')
 ],[
 InlineKeyboardButton("Tajik",callback_data = "lang tg")
 ],[
 InlineKeyboardButton("Tamil",callback_data = "lang ta")
 ],[
 InlineKeyboardButton("Tatar",callback_data = "lang tt")
 ],[
 InlineKeyboardButton("Telugu",callback_data = "lang te")
 ],[
 InlineKeyboardButton("Thai",callback_data = "lang th"),
 ],[
 InlineKeyboardButton("Turkish",callback_data = "lang tr")
 ],[
 InlineKeyboardButton("Turkmen",callback_data ="lang tk")    
 ],[
 InlineKeyboardButton("Ukrainian",callback_data = "lang uk")
 ],[
 InlineKeyboardButton("Urdu",callback_data = "lang ur")
 ],[    
 InlineKeyboardButton("Uyghur",callback_data ="lang ug")
 ],[     
 InlineKeyboardButton("Uzbek",callback_data = "lang uz")
 ],[  
 InlineKeyboardButton("Vietnamese",callback_data ="lang vi")
 ],[   
 InlineKeyboardButton("Welsh",callback_data = "lang cy")
 ],[    
 InlineKeyboardButton("Xhosa",callback_data = "lang xh")
 ],[   
 InlineKeyboardButton("Yiddish",callback_data = "lang yi")
 ],[     
 InlineKeyboardButton("Yoruba",callback_data = "lang yo")
 ]]
 )
