import pandas as pd, numpy as np
from models import pull_models


def _response(df, models):
    ##predictions = predict_proba(df)

    y = [round(x.predict_proba(df)[0][1] * 100.0, 2) for x in models]

    return y


def _product(df, param):
    _dict = {
        'achat': 'Product_Achat',
        'android_os': 'Product_Android OS',
        'android_pay': 'Product_Android Pay',
        'android_wear': 'Product_Android Wear',
        'chromebook': 'Product_Chromebook',
        'chromecast': 'Product_Chromecast',
        'chromecast_audio': 'Product_Chromecast Audio',
        'daydream': 'Product_Daydream View',
        'digital': 'Product_Digital Skills',
        'duo': 'Product_Duo',
        'ellen': 'Product_Ellen Show',
        'feed': 'Product_Feed',
        'g_suite': 'Product_G Suite',
        'gsa': 'Product_GSA',
        'google_activate': 'Product_Google Activate',
        'google_assistant': 'Product_Google Assistant',
        'google_cloud': 'Product_Google Cloud',
        'google_duo': 'Product_Google Duo',
        'google_express': 'Product_Google Express',
        'google_home': 'Product_Google Home',
        'google_home_max': 'Product_Google Home Max',
        'google_home_mini': 'Product_Google Home Mini',
        'google_photos': 'Product_Google Photos',
        'google_play': 'Product_Google Play',
        'google_store': 'Product_Google Store',
        'user_trust': 'Product_Google User Trust',
        'nexus': 'Product_Nexus',
        'pixel': 'Product_Pixel',
        'pixel_2': 'Product_Pixel 2',
        'pixelbook': 'Product_Pixelbook',        
        'fi': 'Product_Project Fi',
        'water': 'Product_Watercooler BCE',
        'youtube_music': 'Product_YouTube Music',        
        'youtube_ea': 'Product_YouTube Music/Emerging Artists', 
        'youtube_red': 'Product_YouTube Red',
        'youtube_tv': 'Product_YouTube TV'
    }

    df[_dict[param]] = 1

    return df


def _region(df, param):
    if param == 'apac':
        df['Region_APAC'] = 1
    elif param == 'emea':
        df['Region_EMEA'] = 1
    else:
        df['Region_North_America'] = 1

    return df


def _platform(df, param):
    if param == 'desktop': 
        df['Platform_Desktop'] = 1
    elif param == 'mobile':
        df['Platform_Mobile'] = 1
    else:
        df['Platform_Desktop'] = 1
        df['Platform_Mobile'] = 1

    return df


def _video_length(df, param):
    if param == 'fifteen':
        df['Video_Length_:15'] = 1
    elif param == 'thirty':
        df['Video_Length_:30'] = 1
    else:
        df['Video_Length_:06'] = 1

    return df


def _real_world(df, param):
    if param == 'real':
        df['Real_World_real world'] = 1
    elif param == 'both':
        df['Real_World_both'] = 1
    else:
        df['Real_World_animated'] = 1

    return df


def _story(df, param):
    if param == 'no':
        df['Story_Driven_no'] = 1
    else:
        df['Story_Driven_yes'] = 1

    return df


def _event(df, param):
    if param == 'no':
        df['Event_no'] = 1
    else:
        df['Event_yes'] = 1

    return df


def _google_upfront(df, param):
    if param == 'no':
        df['Google_Logo_Upfront_Recode_Zero'] = 1
    else:
        df['Google_Logo_Upfront_Recode_1+'] = 1

    return df


def _product_upfront(df, param):
    if param == 'no':
        df['Product_Logo_Upfront_Recode_Zero'] = 1
    else:
        df['Product_Logo_Upfront_Recode_1+'] = 1

    return df


def _audio_upfront(df, param):
    if param == 'no':
        df['Audio_Mention_Upfront_Recode_Zero'] = 1
    else:
        df['Audio_Mention_Upfront_Recode_1+'] = 1

    return df


def _no_of_visuals(df, param):
    if param == 'no':
        df['No_of_Visuals_Recode_Zero'] = 1
    else:
        df['No_of_Visuals_Recode_One+'] = 1

    return df


def _google_logo_50(df, param):
    if param == 'no':
        df['Google_Logo_50_no'] = 1
    else:
        df['Google_Logo_50_yes'] = 1

    return df


def _product_logo_50(df, param):
    if param == 'no':
        df['Product_Logo_50_no'] = 1
    else:
        df['Product_Logo_50_yes'] = 1

    return df


def _product_shot_50(df, param):
    if param == 'no':
        df['Product_Shot_50_no'] = 1
    else:
        df['Product_Shot_50_yes'] = 1

    return df


def _text_end_card(df, param):
    if param == 'no':
        df['Text_on_End_Card_no'] = 1
    else:
        df['Text_on_End_Card_yes'] = 1

    return df


def _demo(df, param):
    if param == 'no':
        df['Demo_no'] = 1
    else:
        df['Demo_yes'] = 1

    return df


def _front(df, param):
    if param == 'no':
        df['Front_Card_no'] = 1
    else:
        df['Front_Card_yes'] = 1

    return df


def _pop_culture(df, param):
    if param == 'no':
        df['Pop_Culture_no'] = 1
    else:
        df['Pop_Culture_yes'] = 1

    return df


def _music(df, param):
    if param == 'no':
        df['Music_no'] = 1
    else:
        df['Music_yes'] = 1

    return df


def _voice(df, param):
    if param == 'no':
        df['Voiceover_no'] = 1
    else:
        df['Voiceover_yes'] = 1

    return df


def _product_msgs(df, param):
    if param == 'zero':
        df['No_Product_Msgs_Recode_Zero'] = 1
    elif param == 'one':
        df['No_Product_Msgs_Recode_One'] = 1
    else:
        df['No_Product_Msgs_Recode_Two+'] = 1

    return df





















