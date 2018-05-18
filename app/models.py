from sklearn.externals import joblib
import pandas as pd


def pull_models():
	'''
	Load the pickled models for use.
	'''
	model_aware =  joblib.load(r'C:\Users\william.raikes\Programming\Python\Creative_Elements_App\model_building\pickled_models\rf_aware_resp.pkl') 
	model_cons =  joblib.load(r'C:\Users\william.raikes\Programming\Python\Creative_Elements_App\model_building\pickled_models\rf_cons_resp.pkl') 
	model_purch =  joblib.load(r'C:\Users\william.raikes\Programming\Python\Creative_Elements_App\model_building\pickled_models\rf_purch_resp.pkl') 

	return [model_aware, model_cons, model_purch]


def default_prediction():
	'''
	Return a default dataframe for the default prediction.
	'''
	return pd.DataFrame({

		#Product
	    'Product_Achat': [0], 
	    'Product_Android OS': [0], 
	    'Product_Android Pay': [0], 
	    'Product_Android Wear': [0], 
	    'Product_Chromebook': [0],  
	    'Product_Chromecast': [0], 
	    'Product_Chromecast Audio': [0],  
	    'Product_Daydream View': [0], 
	    'Product_Digital Skills': [0], 
	    'Product_Duo': [0],  
	    'Product_Ellen Show': [0], 
	    'Product_Feed': [0],  
	    'Product_G Suite': [0], 
	    'Product_GSA': [0], 
	    'Product_Google Activate': [0],  
	    'Product_Google Assistant': [0], 
	    'Product_Google Cloud': [0], 
	    'Product_Google Duo': [0], 
	    'Product_Google Express': [0], 
	    'Product_Google Home': [0], 
	    'Product_Google Home Max': [0], 
	    'Product_Google Home Mini': [0], 
	    'Product_Google Photos': [0], 
	    'Product_Google Play': [0], 
	    'Product_Google Store': [0], 
	    'Product_Google User Trust': [0], 
	    'Product_Nexus': [0], 
	    'Product_Pixel': [0], 
	    'Product_Pixel 2': [0], 
	    'Product_Pixelbook': [0], 
	    'Product_Project Fi': [0], 
	    'Product_Watercooler BCE': [0], 
	    'Product_YouTube Music': [0], 
	    'Product_YouTube Music/Emerging Artists': [0],  
	    'Product_YouTube Red': [0], 
	    'Product_YouTube TV': [0], 
	    
	    #Class Variables
	    'Region_APAC': [0], 
	    'Region_EMEA': [0], 
	    'Region_North_America': [0], 
	    'Platform_Mobile': [0], 
	    'Platform_Desktop': [0], 
	    'Video_Length_:06': [0], 
	    'Video_Length_:15': [0], 
	    'Video_Length_:30': [0], 
	  	
	  	#Creative Elements
	    'Real_World_animated': [0], 
	    'Real_World_both': [0], 
	    'Real_World_real world': [0], 
	    'Story_Driven_no': [0], 
	    'Story_Driven_yes': [0], 
	    'Event_no': [0], 
	    'Event_yes': [0], 
	    'Google_Logo_Upfront_Recode_1+': [0], 
	    'Google_Logo_Upfront_Recode_Zero': [0], 
	    'Product_Logo_Upfront_Recode_1+': [0], 
	    'Product_Logo_Upfront_Recode_Zero': [0], 
	    'Audio_Mention_Upfront_Recode_1+': [0], 
	    'Audio_Mention_Upfront_Recode_Zero': [0], 
	    'No_of_Visuals_Recode_One+': [0], 
	    'No_of_Visuals_Recode_Zero': [0], 
	    'Google_Logo_50_no': [0], 
	    'Google_Logo_50_yes': [0], 
	    'Product_Logo_50_no': [0], 
	    'Product_Logo_50_yes': [0], 
	    'Product_Shot_50_no': [0], 
	    'Product_Shot_50_yes': [0], 
	    'Text_on_End_Card_no': [0], 
	    'Text_on_End_Card_yes': [0], 
	    'Demo_no': [0], 
	    'Demo_yes': [0], 
	    'Front_Card_no': [0], 
	    'Front_Card_yes': [0], 
	    'Pop_Culture_no': [0], 
	    'Pop_Culture_yes': [0], 
	    'Music_no': [0], 
	    'Music_yes': [0], 
	    'Voiceover_no': [0], 
	    'Voiceover_yes': [0], 
	    'No_Product_Msgs_Recode_One': [0], 
	    'No_Product_Msgs_Recode_Two+': [0], 
	    'No_Product_Msgs_Recode_Zero': [0]

		})


