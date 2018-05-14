import dash, pandas as pd, numpy as np
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from models import default_prediction
from functions import *
                    # (_response, _video_length, _pop_culture, _real_world, 
                    #  _music, _voiceover, _story_driven, _front_card, 
                    #  _demo, _product_shot_50, 
                    #  _google_logo_50, _product_logo_50, _event, _platform,
                    #  _text_end_card)

X = default_prediction()

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Creative Rate Predictions App: Prototype'),

    html.Div(children='''
        Welcome to the prototype web app for making pre-test 
        rate predictions based on creative elements.
    '''),

    html.Div([
        dcc.Graph(
            id='main_graph', 
            figure={
                'data': [go.Bar(
                    x=1,
                    y=0.5,
                    text=0.5,
                    textposition='auto',
                    name='Predictions',
                    marker=dict(
                        color='rgb(58,200,225)'
                    )
                )],
                'layout': go.Layout(
                    title= 'Creative Analysis: Rate Predictions',
                    showlegend=False,
                    yaxis=dict(
                       range=[-1, 1]
                    )
                )
            }
        )
    ])
])

    # html.Div([

    #     html.Div([

            # html.Label('Video Length'),
            # dcc.Dropdown(
            #     id='video_length',
            #     options=[
            #         {'label': '6 Seconds', 'value': 'six'},
            #         {'label': '15 Seconds', 'value': 'fifteen'},
            #         {'label': '30 Seconds', 'value': 'thirty'}
            #     ],
            #     value='six'
            # ),

            # html.Label('Platform'),
            # dcc.Dropdown(
            #     id='platform',
            #     options=[
            #         {'label': 'Mobile', 'value': 'mobile'},
            #         {'label': 'Desktop', 'value': 'desktop'}
            #     ],
            #     value='mobile'
            # ),

            # html.Label('Real World vs. Animated'),
            # dcc.Dropdown(
            #     id='real_world',
            #     options=[
            #         {'label': 'Real World', 'value': 'real'},
            #         {'label': 'Animated', 'value': 'anim'},
            #         {'label': 'Both', 'value': 'both'}
            #     ],
            #     value='real'
            # ),

            # html.Label('Presence of Music'),
            # dcc.Dropdown(
            #     id='music',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Presence of Voiceover'),
            # dcc.Dropdown(
            #     id='voice',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Event or Holiday Themed'),
            # dcc.Dropdown(
            #     id='event',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Story Driven'),
            # dcc.Dropdown(
            #     id='story',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Pop Culture Reference'),
            # dcc.Dropdown(
            #     id='pop_culture',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),  

            # html.Label('Demo or Functionality Shown'),
            # dcc.Dropdown(
            #     id='demo',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Presence of Front Card'),
            # dcc.Dropdown(
            #     id='front',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Text on End Card'),
            # dcc.Dropdown(
            #     id='text_end_card',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Google Logo: 50% Presence'),
            # dcc.Dropdown(
            #     id='google_logo_50',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Product Logo: 50% Presence'),
            # dcc.Dropdown(
            #     id='product_logo_50',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # ),

            # html.Label('Product Shot: 50% Presence'),
            # dcc.Dropdown(
            #     id='product_shot_50',
            #     options=[
            #         {'label': 'Yes', 'value': 'yes'},
            #         {'label': 'No', 'value': 'no'}
            #     ],
            #     value='no'
            # )
    #     ], style={'width': '40%'})
    # ])#, style={'columnCount': 4})



# @app.callback(
#     dash.dependencies.Output('main_graph', 'figure')
#     #[#dash.dependencies.Input('video_length', 'value'),
#      #dash.dependencies.Input('platform', 'value'),
#      #dash.dependencies.Input('product', 'value'),
#      #dash.dependencies.Input('real_world', 'value'),
#      #dash.dependencies.Input('music', 'value'),
#      #dash.dependencies.Input('voice', 'value'),
#      #dash.dependencies.Input('event', 'value'),
#      #dash.dependencies.Input('story', 'value'),
#      #dash.dependencies.Input('pop_culture', 'value'),
#      #dash.dependencies.Input('demo', 'value'),
#      #dash.dependencies.Input('front', 'value'),
#      #dash.dependencies.Input('text_end_card', 'value'),
#      #dash.dependencies.Input('google_logo_50', 'value'),
#      #dash.dependencies.Input('product_logo_50', 'value'),
#      #dash.dependencies.Input('product_shot_50', 'value')
# #])
# )
# def update_graph(): #response):#video_length, platform, 
#     #real_world): #, music, voice, event, story, pop_culture,
#     #demo, front, text_end_card, google_logo_50,
#     #product_logo_50, product_shot_50):
    
#     #X_pred = X.copy()
#     #X_pred = _video_length(X_pred, video_length)
#     #X_pred = _platform(X_pred, platform)
#     #X_pred = _product(X_pred, product)  
#     #X_pred = _real_world(X_pred, real_world)
#     #X_pred = _music(X_pred, music)
#     #X_pred = _voiceover(X_pred, voice)
#     #X_pred = _event(X_pred, event)  
#     #X_pred = _story_driven(X_pred, story)
#     #X_pred = _pop_culture(X_pred, pop_culture)
#     #X_pred = _demo(X_pred, demo)
#     #X_pred = _front_card(X_pred, front)
#     #X_pred = _text_end_card(X_pred, text_end_card)
#     #X_pred = _google_logo_50(X_pred, google_logo_50)   
#     #X_pred = _product_logo_50(X_pred, product_logo_50)   
#     #X_pred = _product_shot_50(X_pred, product_shot_50)


#     #y_pred = [round(x[0][1], 3) for x in model.predict_proba(X_pred)]
#     y = _response(X)
    

#     return {
#             'data': [go.Bar(
#                 x=1,
#                 y=y,
#                 text=y,
#                 textposition='auto',
#                 name='Predictions',
#                 marker=dict(
#                     color='rgb(58,200,225)'
#                 )
#             )],
#             'layout': go.Layout(
#                 title= 'Creative Analysis: Rate Predictions',
#                 showlegend=False,
#                 yaxis=dict(
#                    range=[-1, 1]
#                 )
#             )
#     }
    

if __name__ == '__main__':
    app.run_server(debug=True)
