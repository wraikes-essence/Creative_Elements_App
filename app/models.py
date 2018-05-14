from sklearn.externals import joblib
import pandas as pd

def pull_models():
	'''
	Load the pickled models for use.
	'''
	model_aware =  joblib.load(r'C:\Users\william.raikes\Programming\Python\Creative_Elements_App\model_building\pickled_models\rf_aware.pkl') 

	return model_aware

def default_prediction():
	'''
	
	'''
	return pd.DataFrame({

		'emea': [0],
		'apac': [0],
		'desktop' [0],
		's15': [0],
		's30': [0],

		'Real_World_both': [0],
		'Real_World_real world': [0],
		'Story_Driven_yes': [0],
		'Event_yes': [0],
		'Google_Logo_Upfront_Recode_Zero': [0],
		'Product_Logo_Upfront_Recode_Zero': [0],
		'Audio_Mention_Upfront_Recode_Zero': [0],
		'No_of_Visuals_Recode_Zero': [0],
		'Google_Logo_50_yes': [0],
		'Product_Logo_50_yes': [0],
		'Product_Shot_50_yes': [0],
		'Text_on_End_Card_yes': [0],
		'Demo_yes': [0],
		'Front_Card_yes': [0],
		'End_Card_yes': [0],
		'Pop_Culture_yes': [0],
		'Visually_Text_Only_No': [0],
		'Music_yes': [0],
		'Voiceover_yes': [0],
		'No_Product_Msgs_Recode_Zero': [0],
		'No_Product_Msgs_Recode_Two': [0]



		'Video_Length_:06': [0], 
		'Video_Length_:15': [0],
		'Video_Length_:30': [0],
		    
		'Platform_Mobile': [0],
		'Platform_Desktop': [0],

		'Product_Google Home': [0], 
		'Product_Google Home Max': [0],
		'Product_Google Home Mini': [0], 
		'Product_Google Play': [0], 
		'Product_Pixel': [0],
		'Product_Pixel 2': [0],
		'Product_Pixelbook': [0],
		'Product_Chromebook': [0],
		'Product_Chromecast': [0],
		'Product_Chromecast Audio': [0],
		'Product_GSA': [0],
		'Product_Nexus': [0],
		'Product_Project Fi': [0],
		'Product_YouTube Red': [0],
		    
		'Real_World_animated': [0],


		'Music_no': [0],
		'Music_yes': [0],

		'Voiceover_no': [0], 
		'Voiceover_yes': [0],

		"Event_no": [0],
		"Event_yes": [0],

		'Story_Driven_no': [0], 


		'Pop_Culture_no': [0],
		'Pop_Culture_yes': [0],

		'Demo_no': [0],
		'Demo_yes': [0], 
		    
		'Front_Card_no': [0],
		'Front_Card_yes': [0], 

		'Text_on_End_Card_no': [0],
		'Text_on_End_Card_yes': [0],
		    
		'Google_Logo_50_no': [0], 
		'Google_Logo_50_yes': [0],

		'Product_Logo_50_no': [0],
		'Product_Logo_50_yes': [0],

		'Product_Shot_50_no': [0], 
		'Product_Shot_50_yes': [0],


		'Google_Logo': [0.0],
		'Product_Logo': [0.0],
		'Audio_Mention': [0.0],
		'No_of_Visuals': [0.0],
		'Visually_Text_Only': [0.0],
		'No_Product_Msgs': [0.0]
		})

