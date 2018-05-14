import pandas as pd, numpy as np
from models import pull_models

models =  pull_models()


def _response(df):
    y = models[0].predict(df)[0]
    #y = [str(round(x*100, 1)) + '%' for x in y]

    return y


# def _video_length(df, param):
#     if param == 'fifteen':
#         df['s15'] = 1
#     elif param == 'thirty':
#         df['s30'] = 1

#     return df


# def _platform(df, param):
#     if param == 'desktop':
#         df['desktop'] = 1

#     return df


# def _real_world(df, param):
#     if param == 'real':
#         df['Real_World_real world'] = 1
#     elif param == 'anim':
#         df['Real_World_animated'] = 1

#     return df


# def _music(df, param):
#     if param == 'no':
#         df['Music_no'] = 1
#     else:
#         df['Music_yes'] = 1

#     return df


# def _voiceover(df, param):
#     if param == 'no':
#         df['Voiceover_no'] = 1
#     else:
#         df['Voiceover_yes'] = 1

#     return df


# def _event(df, param):
#     if param == 'no':
#         df['Event_no'] = 1
#     else:
#         df['Event_yes'] = 1

#     return df


# def _story_driven(df, param):
#     if param == 'no':
#         df['Story_Driven_no'] = 1
#     else:
#         df['Story_Driven_yes'] = 1

#     return df


# def _pop_culture(df, param):
#     if param == 'no':
#         df['Pop_Culture_no'] = 1
#     else:
#         df['Pop_Culture_yes'] = 1

#     return df


# def _demo(df, param):
#     if param == 'no':
#         df['Demo_no'] = 1
#     else:
#         df['Demo_yes'] = 1

#     return df


# def _front_card(df, param):
#     if param == 'no':
#         df['Front_Card_no'] = 1
#     else:
#         df['Front_Card_yes'] = 1

#     return df


# def _text_end_card(df, param):
#     if param == 'no':
#         df['Text_on_End_Card_no'] = 1
#     else:
#         df['Text_on_End_Card_yes'] = 1

#     return df


# def _google_logo_50(df, param):
#     if param == 'no':
#         df['Google_Logo_50_no'] = 1
#     else:
#         df['Google_Logo_50_yes'] = 1

#     return df


# def _product_logo_50(df, param):
#     if param == 'no':
#         df['Product_Logo_50_no'] = 1
#     else:
#         df['Product_Logo_50_yes'] = 1

#     return df


# def _product_shot_50(df, param):
#     if param == 'no':
#         df['Product_Shot_50_no'] = 1
#     else:
#         df['Product_Shot_50_yes'] = 1

#     return df


