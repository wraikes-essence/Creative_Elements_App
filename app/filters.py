import pandas as pd, numpy as np
from models import pull_models

models =  pull_models()

def _response(df, param):
    if param == 'abs':
        y = models[1].predict(df)[0]
        y = [str(round(x*100, 1)) + '%' for x in y]

    elif param == 'head':
        y = models[2].predict(df)[0]
        y = [str(round(x*100, 1)) + '%' for x in y]        

    else:
        y = models[0].predict_proba(df)
        y = [str(round(x[0][1] * 100, 1)) + '%' for x in y]

    return y

def _video_length(df, param):
    if param == 'six':
        df['Video_Length_:06'] = 1
    elif param == 'fifteen':
        df['Video_Length_:15'] = 1
    else:
        df['Video_Length_:30'] = 1

    return df


def _platform(df, param):
    if param == 'mobile':
        df['Platform_Mobile'] = 1
    else:
        df['Platform_Desktop'] = 1

    return df


def _product(df, param):
    if param == 'chromebook':
        df['Product_Chromebook'] = 1
    elif param == 'chromecast':
        df['Product_Chromecast'] = 1    
    elif param == 'chromecast_audio':
        df['Product_Chromecast Audio'] = 1
    elif param == 'gsa':
        df['Product_GSA'] = 1
    elif param == 'g_home':
        df['Product_Google Home'] = 1
    elif param == 'g_home_max':
        df['Product_Google Home Max'] = 1
    elif param == 'g_home_mini':
        df['Product_Google Home Mini'] = 1
    elif param == 'g_play':
        df['Product_Google Play'] = 1
    elif param == 'nexus':
        df['Product_Nexus'] = 1
    elif param == 'pixel':
        df['Product_Pixel'] = 1
    elif param == 'pixel2':
        df['Product_Pixel 2'] = 1
    elif param == 'pixelbook':
        df['Product_Pixelbook'] = 1   
    elif param == 'project_fi':
        df['Product_Project Fi'] = 1
    else:
        df['Product_YouTube Red'] = 1   

    return df


def _real_world(df, param):
    if param == 'real':
        df['Real_World_real world'] = 1
    elif param == 'anim':
        df['Real_World_animated'] = 1
    else:
        df['Real_World_both'] = 1

    return df


def _music(df, param):
    if param == 'no':
        df['Music_no'] = 1
    else:
        df['Music_yes'] = 1

    return df


def _voiceover(df, param):
    if param == 'no':
        df['Voiceover_no'] = 1
    else:
        df['Voiceover_yes'] = 1

    return df


def _event(df, param):
    if param == 'no':
        df['Event_no'] = 1
    else:
        df['Event_yes'] = 1

    return df


def _story_driven(df, param):
    if param == 'no':
        df['Story_Driven_no'] = 1
    else:
        df['Story_Driven_yes'] = 1

    return df


def _pop_culture(df, param):
    if param == 'no':
        df['Pop_Culture_no'] = 1
    else:
        df['Pop_Culture_yes'] = 1

    return df


def _demo(df, param):
    if param == 'no':
        df['Demo_no'] = 1
    else:
        df['Demo_yes'] = 1

    return df


def _front_card(df, param):
    if param == 'no':
        df['Front_Card_no'] = 1
    else:
        df['Front_Card_yes'] = 1

    return df


def _text_end_card(df, param):
    if param == 'no':
        df['Text_on_End_Card_no'] = 1
    else:
        df['Text_on_End_Card_yes'] = 1

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


