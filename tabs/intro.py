from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

By isolating the elements that make a song popular, we can help artists craft engaging music. Click on the predict tab to try it yourself.


"""),

html.Img(src='https://i.ibb.co/fDWLFHB/newplot.png')]
