from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd

from app import app

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to plug in the featues of your song and find the predicted popularity of the track. 
        Try to make a song with 90 popularity or more!

    """),

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### danceability'),
        dcc.Slider(
            id='danceability',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### energy'),
        dcc.Slider(
            id='energy',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### key'),
        dcc.Slider(
            id='key',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),


        html.Div([
        dcc.Markdown('###### loudness'),
        dcc.Slider(
            id='loudness',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### mode'),
        dcc.Slider(
            id='mode',
            min=0,
            max=1,
            step=1,
            value=1,
            marks={n: str(n) for n in range(0, 3, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### speechiness'),
        dcc.Slider(
            id='speechiness',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### acousticness'),
        dcc.Slider(
            id='acousticness',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### instrumentalness'),
        dcc.Slider(
            id='instrumentalness',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### liveness'),
        dcc.Slider(
            id='liveness',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### valence'),
        dcc.Slider(
            id='valence',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### tempo'),
        dcc.Slider(
            id='tempo',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 11, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### duration_ms'),
        dcc.Slider(
            id='duration_ms',
            min=0,
            max=5,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 7, 1)}
        ),
    ], style=style),

        html.Div([
        dcc.Markdown('###### time_signature'),
        dcc.Slider(
            id='time_signature',
            min=0,
            max=5,
            step=1,
            value=5,
            marks={n: str(n) for n in range(1, 6, 1)}
              ),
    ], style=style),
])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('danceability', 'value'),
     Input('energy', 'value'),
     Input('key', 'value'),
     Input('loudness', 'value'),
     Input('mode', 'value'),
     Input('speechiness', 'value'),
     Input('acousticness', 'value'),
     Input('instrumentalness', 'value'),
     Input('liveness', 'value'),
     Input('valence', 'value'),
     Input('tempo', 'value'),
     Input('duration_ms', 'value'),
     Input('time_signature', 'value')])
def predict(danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,
liveness,valence,tempo,duration_ms,time_signature
):

    df = pd.DataFrame(
        columns=['danceability', 'energy', 'key','loudness','mode','speechiness'
,'acousticness','instrumentalness','liveness', 'valence', 'tempo', 'duration_ms',
 'time_signature',],
        data=[[danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,
liveness,valence,tempo,duration_ms,time_signature]]
    )

    pipeline = load('model/pipeline.joblib')
    y_pred_log = pipeline.predict(df)
    y_pred = y_pred_log[0]
    results = f'The predicted popularity of the song is {y_pred:,.0f}/100'

    return results


