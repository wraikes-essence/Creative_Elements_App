import pandas as pd, numpy as np
from models import pull_models


def _response(df, models):
    ##predictions = predict_proba(df)

    y_lift = [round(x.predict(df)[0] * 100.0, 2) for x in models[:3]]

    return y_lift


def _product(df, param):
    _dict = {
        #'achat': 'Product_Achat',
        'android_os': 'pro_android_os',
        'android_pay': 'pro_android_pay',
        'android_wear': 'pro_android_wear',
        'chromebook': 'pro_chromebook',
        'chromecast': 'pro_chromecast',
        'chromecast_audio': 'pro_chromecast_aud',
        'daydream': 'pro_daydream',
        'digital': 'pro_digital_skills',
        'duo': 'pro_duo',
        'ellen': 'pro_ellen',
        'feed': 'pro_feed',
        'g_suite': 'pro_g_suite',
        'gsa': 'pro_gsa',
        #'google_activate': 'Product_Google Activate',
        'google_assistant': 'pro_google_assist',
        'google_cloud': 'pro_google_cloud',
        'google_duo': 'pro_google_duo',
        'google_express': 'pro_google_express',
        'google_home': 'pro_google_home',
        'google_home_max': 'pro_google_home_max',
        'google_home_mini': 'pro_google_home_mini',
        'google_photos': 'pro_google_photos',
        'google_play': 'pro_google_play',
        #'google_store': 'Product_Google Store',
        'user_trust': 'pro_google_user',
        'nexus': 'pro_nexus',
        'pixel': 'pro_pixel',
        'pixel_2': 'pro_pixel_2',
        'pixelbook': 'pro_pixelbook',        
        'fi': 'pro_fi',
        'water': 'pro_watercooler',
        'youtube': 'pro_youtube',
        'youtube_music': 'pro_youtube_music',        
        'youtube_ea': 'pro_youtube_music', 
        'youtube_red': 'pro_youtube_red',
        'youtube_tv': 'pro_youtube_tv'
    }

    df[_dict[param]] = 1

    return df


def _region(df, param):

    _dict = {
        'apac': 'apac',
        'emea': 'emea',
        'north_america': 'north_america'
    }

    df[_dict[param]] = 1

    return df


def _platform(df, param):

    if param == 'desktop': 
        df['desktop'] = 1
    elif param == 'mobile':
        df['mobile'] = 1
    else:
        df['desktop'] = 1
        df['mobile'] = 1

    return df


def _video_length(df, param):

    if param == 'fifteen':
        df['s15'] = 1
    elif param == 'thirty':
        df['s30'] = 1
    else:
        df['s06'] = 1

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

    _dict = {
        'zero': 'No_Product_Msgs_Recode_Zero',
        'one': 'No_Product_Msgs_Recode_One',
        'two': 'No_Product_Msgs_Recode_Two+'
    }

    df[_dict[param]] = 1

    return df





















