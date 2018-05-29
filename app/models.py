from sklearn.externals import joblib
import pandas as pd


def pull_models():
	'''
	Load the pickled models for use.
	'''
	#KPI Lift
	aware_lift =  joblib.load(r'C:\Users\william.raikes\Programming\Python\Creative_Elements_App\model_building\pickled_models\rf_aware_creative_lift.pkl') 
	cons_lift =  joblib.load(r'C:\Users\william.raikes\Programming\Python\Creative_Elements_App\model_building\pickled_models\rf_cons_creative_lift.pkl') 
	purch_lift =  joblib.load(r'C:\Users\william.raikes\Programming\Python\Creative_Elements_App\model_building\pickled_models\rf_purch_creative_lift.pkl')

	return [aware_lift, cons_lift, purch_lift]


def default_prediction():
	'''
	Return a default dataframe for the default prediction.
	'''
	return pd.DataFrame({

		'north_america': [0], 
	    'emea': [0], 
	    'apac': [0], 
	    'mobile': [0], 
	    'desktop': [0], 
	    's06': [0],
	    's15': [0], 
	    's30': [0],
	       
	    'pro_nexus': [0], 
	    'pro_android_os': [0], 
	    'pro_chromebook': [0], 
	    'pro_chromecast_aud': [0],
	    'pro_chromecast': [0], 
	    'pro_google_play': [0], 
	    'pro_youtube_red': [0],
	    'pro_youtube_music': [0], 
	    'pro_google_user': [0], 
	    'pro_google_photos': [0],
	    'pro_g_suite': [0], 
	    'pro_pixel': [0], 
	    'pro_daydream': [0], 
	    'pro_android_pay': [0],
	    'pro_google_home': [0], 
	    'pro_gsa': [0], 
	    'pro_google_assist': [0], 
	    'pro_youtube_tv': [0],
	    'pro_android_wear': [0], 
	    'pro_fi': [0], 
	    'pro_youtube': [0], 
	    'pro_google_cloud': [0],
	    'pro_google_express': [0], 
	    'pro_digital_skills': [0], 
	    'pro_feed': [0],
	    'pro_google_home_mini': [0],
	    'pro_duo': [0], 
	    'pro_ellen': [0], 
	    'pro_pixelbook': [0],
	    'pro_google_duo': [0], 
	    'pro_pixel_2': [0], 
	    'pro_watercooler': [0],
	    'pro_google_home_max': [0], 
	  	
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


