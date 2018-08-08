from PIL import ImageGrab, Image, ImageFilter
import pytesseract as itt
import os
import requests as req
import urllib3 as urlib
from urllib.parse import quote
import time

google_custom_search_api = 'HERE GOES YOUR GOOGLE CUSTOM SEARCH API'
google_custom_search_id = 'HERE GOES YOUR GGOLE CUSTOM SEARCH ID'

#Starts function evrything when enter is pressed
def start11 ():
	os.system('cls')
	print ('HQ Hawks')
	print()
	input11 = input('Press enter to start: ')
	if input11 == '':
		evrything()
		
		
		
		
#Function evrything
def evrything ():
	#Clears screen
	os.system('cls')
	#Takes screenshoot of question
	qimage = ImageGrab.grab(bbox=(22, 148, 352, 306))
	qimage.save('D:\Screenshoots\qscrn.png', 'PNG')
	#Takes image of first answer
	image1 = ImageGrab.grab(bbox=(53, 345, 350, 370))
	image1.save('D:\Screenshoots\scrn1.png', 'PNG')
	#Takes image of second answer
	image2 = ImageGrab.grab(bbox=(48, 398, 335, 431))
	image2.save('D:\Screenshoots\scrn2.png', 'PNG')
	#Takes image of third answer
	image3 = ImageGrab.grab(bbox=(49, 457, 333, 493))
	image3.save('D:\Screenshoots\scrn3.png', 'PNG')
	
	
	#Ignore this
	"""
	qimage = ImageGrab.grab(bbox=(29, 175, 358, 334))
	qimage.save('E:\HQHck\Screenshoots\qscrn.png', 'PNG')
	
	image1 = ImageGrab.grab(bbox=(55, 370, 327, 402))
	image1.save('E:\HQHck\Screenshoots\scrn1.png', 'PNG')
	
	image2 = ImageGrab.grab(bbox=(55, 432, 328, 469))
	image2.save('E:\HQHck\Screenshoots\scrn2.png', 'PNG')
	
	image3 = ImageGrab.grab(bbox=(55, 494, 324, 534))
	image3.save('E:\HQHck\Screenshoots\scrn3.png', 'PNG')
	"""
	
	#Opens image and turns it into text
	q0 = itt.image_to_string(Image.open("D:\Screenshoots\qscrn.png"))
	a1 = itt.image_to_string(Image.open("D:\Screenshoots\scrn1.png"))
	a2 = itt.image_to_string(Image.open("D:\Screenshoots\scrn2.png"))
	a3 = itt.image_to_string(Image.open("D:\Screenshoots\scrn3.png"))
	
	#Removes \n from text
	q01 = q0.replace("\r"," ")
	q01 = q0.replace("\n"," ")
	
	a12 = a1.replace("\r"," ")
	a12 = a1.replace("\n"," ")

	a23 = a2.replace("\r"," ")
	a23 = a2.replace("\n"," ")
	
	a34 = a3.replace("\r"," ")
	a34 = a3.replace("\n"," ")
	
	
	#Turn normal text into url format text or smthing like that...
	q01 = quote(q0)
	a12 = quote(a1)
	a23 = quote(a2)
	a34 = quote(a3)
	#Gets answers from google custom search
	url1 = ('https://www.googleapis.com/customsearch/v1?key=' + google_custom_search_api + '&cx=' + google_custom_search_id + '&q=' + q01 + '%20' + a12)
	url2 = ('https://www.googleapis.com/customsearch/v1?key=' + google_custom_search_api + '&cx=' + google_custom_search_id + '&q=' + q01 + '%20' + a23)
	url3 = ('https://www.googleapis.com/customsearch/v1?key=' + google_custom_search_api + '&cx=' + google_custom_search_id + '&q=' + q01 + '%20' + a34)
	
	url1r = req.get(url1)
	data1 = url1r.json()
	
	#Set results into a1r variable
	a1r = data1['searchInformation']['formattedTotalResults']
	
	url2r = req.get(url2)
	data2 = url2r.json()
	
	a2r = data2['searchInformation']['formattedTotalResults']
	
	url3r = req.get(url3)
	data3 = url3r.json()
	
	a3r = data3['searchInformation']['formattedTotalResults']
	
	
	
	
	#Prints results
	print('First - ' + a1r)
	print('Second - ' + a2r)
	print('Third - ' + a3r)
	time.sleep(7)
	start11()
	
	
	
#Starts program
start11()





