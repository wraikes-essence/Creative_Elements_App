import dash, pandas as pd, numpy as np
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from models import default_prediction, pull_models
from functions import (_response, _product, _region, 
                      _platform, _video_length, _real_world,
                      _story, _event, _google_upfront,
                      _product_upfront, _audio_upfront, 
                      _no_of_visuals, _google_logo_50, _product_logo_50,
                      _product_shot_50, _text_end_card, _demo,
                      _front, _pop_culture, _music, _voice,
                      _product_msgs)


#Initial Variables
models = pull_models()
X = default_prediction()
app = dash.Dash()


app.layout = html.Div([
    

    html.Div([
        html.H1('Creative Rate Predictions App: Prototype'),
        html.P('''Welcome to the prototype web app for making pre-test 
        rate predictions based on creative elements.'''),
        dcc.Graph(
            id='main_graph'
        )
    ], style={'float': 'left', 'width': '70%', 'position': 'fixed'}
    ),


    html.Div([

        html.H1('Global Variables'),
        html.Label('Product'),
        dcc.Dropdown(
            id='product',
            options=[
                {'label': 'Achat', 'value': 'achat'},
                {'label': 'Android OS', 'value': 'android_os'},
                {'label': 'Android Pay', 'value': 'android_pay'},
                {'label': 'Android Wear', 'value': 'android_wear'},
                {'label': 'Chromebook', 'value': 'chromebook'},
                {'label': 'Chromecast', 'value': 'chromecast'},
                {'label': 'Chromecast Audio', 'value': 'chromecast_audio'},
                {'label': 'Daydream View', 'value': 'daydream'},
                {'label': 'Digital Skills', 'value': 'digital'},
                {'label': 'Duo', 'value': 'duo'},
                {'label': 'Ellen Show', 'value': 'ellen'},
                {'label': 'Feed', 'value': 'feed'},
                {'label': 'G Suite', 'value': 'g_suite'},
                {'label': 'GSA', 'value': 'gsa'},
                {'label': 'Google Activate', 'value': 'google_activate'},
                {'label': 'Google Assistant', 'value': 'google_assistant'},
                {'label': 'Google Cloud', 'value': 'google_cloud'},
                {'label': 'Google Duo', 'value': 'google_duo'},
                {'label': 'Google Express', 'value': 'google_express'},
                {'label': 'Google Home', 'value': 'google_home'},
                {'label': 'Google Home Max', 'value': 'google_home_max'},
                {'label': 'Google Home Mini', 'value': 'google_home_mini'},
                {'label': 'Google Photos', 'value': 'google_photos'},
                {'label': 'Google Play', 'value': 'google_play'},
                {'label': 'Google Store', 'value': 'google_store'},
                {'label': 'Google User Trust', 'value': 'user_trust'},
                {'label': 'Nexus', 'value': 'nexus'},
                {'label': 'Pixel', 'value': 'pixel'},
                {'label': 'Pixel 2', 'value': 'pixel_2'},
                {'label': 'Pixelbook', 'value': 'pixelbook'},
                {'label': 'Project Fi', 'value': 'fi'},
                {'label': 'Watercooler BCE', 'value': 'water'},
                {'label': 'YouTube Music', 'value': 'youtube_music'},
                {'label': 'YouTube Music/Emerging Artists', 'value': 'youtube_ea'},
                {'label': 'YouTube Red', 'value': 'youtube_red'},
                {'label': 'YouTube TV', 'value': 'youtube_tv'}
            ],
            value='google_home'
        ),
        

        html.Label('Region'),  ## Checkbox
        dcc.Dropdown(
            id='region',
            options=[
                {'label': 'North America', 'value': 'north_america'},
                {'label': 'EMEA', 'value': 'emea'},
                {'label': 'APAC', 'value': 'apac'}
            ],
            value='north_america'
        ),


        html.Label('Platform'),
        dcc.Dropdown(
            id='platform',
            options=[
                {'label': 'Both', 'value': 'both'},
                {'label': 'Mobile', 'value': 'mobile'},
                {'label': 'Desktop', 'value': 'desktop'}
            ],
            value='both'
        ),


        html.Label('Video Length'),
        dcc.Dropdown(
            id='video_length',
            options=[
                {'label': '6 Seconds', 'value': 'six'},
                {'label': '15 Seconds', 'value': 'fifteen'},
                {'label': '30 Seconds', 'value': 'thirty'}
            ],
            value='six'
        ),

        html.Br(),
        html.H1('Creative Elements'),
        html.Label('Real World vs. Animated'),
        dcc.Dropdown(
            id='real_world',
            options=[
                {'label': 'Real World', 'value': 'real'},
                {'label': 'Animated', 'value': 'anim'},
                {'label': 'Both', 'value': 'both'}
            ],
            value='real'
        ),


        html.Label('Story Driven'),
        dcc.Dropdown(
            id='story',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Event or Holiday Themed'),
        dcc.Dropdown(
            id='event',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Upfront Google Logo'),
        dcc.Dropdown(
            id='google_upfront',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Upfront Product Logo'),
        dcc.Dropdown(
            id='product_upfront',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Upfront Audio Mention'),
        dcc.Dropdown(
            id='audio_upfront',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('non-Google or Product Logos'),
        dcc.Dropdown(
            id='no_of_visuals',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Google Logo: 50% Presence'),
        dcc.Dropdown(
            id='google_logo_50',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Product Logo: 50% Presence'),
        dcc.Dropdown(
            id='product_logo_50',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Product Shot: 50% Presence'),
        dcc.Dropdown(
            id='product_shot_50',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Text on End Card'),
        dcc.Dropdown(
            id='text_end_card',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Demo or Functionality Shown'),
        dcc.Dropdown(
            id='demo',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Presence of Front Card'),
        dcc.Dropdown(
            id='front',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Pop Culture Reference'),
        dcc.Dropdown(
            id='pop_culture',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),  


        html.Label('Presence of Music'),
        dcc.Dropdown(
            id='music',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('Presence of Voiceover'),
        dcc.Dropdown(
            id='voice',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no'
        ),


        html.Label('No. of Product Messages'),
        dcc.Dropdown(
            id='product_msgs',
            options=[
                {'label': 'Zero', 'value': 'zero'},
                {'label': 'One', 'value': 'one'},
                {'label': 'Two+', 'value': 'two'}
            ],
            value='zero'
        )
    ], style={'float': 'right', 'width': '20%', 'lineHeight': '30px'})
])


@app.callback(
    dash.dependencies.Output('main_graph', 'figure'),
    [
        dash.dependencies.Input('product', 'value'),
        dash.dependencies.Input('region', 'value'),
        dash.dependencies.Input('platform', 'value'),
        dash.dependencies.Input('video_length', 'value'),
        dash.dependencies.Input('real_world', 'value'),
        dash.dependencies.Input('story', 'value'),
        dash.dependencies.Input('event', 'value'),
        dash.dependencies.Input('google_upfront', 'value'),
        dash.dependencies.Input('product_upfront', 'value'),
        dash.dependencies.Input('audio_upfront', 'value'),
        dash.dependencies.Input('no_of_visuals', 'value'),
        dash.dependencies.Input('google_logo_50', 'value'),
        dash.dependencies.Input('product_logo_50', 'value'),
        dash.dependencies.Input('product_shot_50', 'value'),
        dash.dependencies.Input('text_end_card', 'value'),
        dash.dependencies.Input('demo', 'value'),
        dash.dependencies.Input('front', 'value'),
        dash.dependencies.Input('pop_culture', 'value'),                
        dash.dependencies.Input('music', 'value'),
        dash.dependencies.Input('voice', 'value'),
        dash.dependencies.Input('product_msgs', 'value')
    ]
)
def update_graph(product, region, platform,
                 video_length, real_world, story,
                 event, google_upfront, product_upfront,
                 audio_upfront, no_of_visuals, google_logo_50,
                 product_logo_50, product_shot_50, 
                 text_end_card, demo, front, pop_culture,
                 music, voice, product_msgs):
    
    X_pred = X.copy()
    X_pred = _product(X_pred, product)
    X_pred = _region(X_pred, region)
    X_pred = _platform(X_pred, platform)
    X_pred = _video_length(X_pred, video_length)
    X_pred = _real_world(X_pred, real_world)
    X_pred = _story(X_pred, story)
    X_pred = _event(X_pred, event) 
    X_pred = _google_upfront(X_pred, google_upfront) 
    X_pred = _product_upfront(X_pred, product_upfront) 
    X_pred = _audio_upfront(X_pred, audio_upfront) 
    X_pred = _no_of_visuals(X_pred, no_of_visuals) 
    X_pred = _google_logo_50(X_pred, google_logo_50) 
    X_pred = _product_logo_50(X_pred, product_logo_50) 
    X_pred = _product_shot_50(X_pred, product_shot_50)               
    X_pred = _text_end_card(X_pred, text_end_card)
    X_pred = _demo(X_pred, demo)    
    X_pred = _front(X_pred, front)
    X_pred = _pop_culture(X_pred, pop_culture)
    X_pred = _music(X_pred, music)
    X_pred = _voice(X_pred, voice)
    X_pred = _product_msgs(X_pred, product_msgs)
  
    y = _response(X_pred, models)
    
    return {
            'data': [go.Bar(
                x=['Awareness', 'Consideration', 'Purchase'],
                y=y,
                text=y,
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
                   range=[-100, 100]
                )
            )
    }
    

if __name__ == '__main__':
    app.run_server(debug=True)


    #[#dash.dependencies.Input('video_length', 'value'),

#])