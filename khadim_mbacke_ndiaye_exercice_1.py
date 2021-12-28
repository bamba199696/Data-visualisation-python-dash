#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:12:11 2021

@author: khadim Mbacke Ndiaye
"""

from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd



data = pd.read_csv('/Users/macbookpro/Documents/airline (1).csv')

load_figure_template("flatly")
app=dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
app.layout=dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
                html.H2("Dashboard des retards de vols US Airline par Khadim Mbacké Ndiaye",style={'fontWeight':'bold','textAlign':'center'})
            ]
                
            ))
    ]),dbc.Col([
             dcc.Dropdown(id='Annee',
                     options=[{'label': x, 'value': x}
                              for x in sorted(data['Year'].unique())],
                     
                     placeholder='Selectionner une annee',
                     style={'width': '250px','textAlign':'center'}
                     )
            ], width={'size':4,'textAlign':'center'}),
    
       
  
        dbc.Row([
        
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_1",figure={})
        ], width={'size':6}
        ),
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_2",figure={})
        ], width={'size':6}
        )       
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_3",figure={})         
        ], width={'size':6}
        ),
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_4",figure={})
        ], width={'size':6}
        )       
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            dcc.Graph(id="fig_5",figure={})         
        ], width={'size':12}
        ),
        
    ]),
    
    
          
]) 


@app.callback(
[
Output('fig_1', 'figure'),
Output('fig_2', 'figure'),
Output('fig_3', 'figure'),
Output('fig_4', 'figure'),
Output('fig_5', 'figure')
],

Input('Annee','value')
)
def update_graphique(Annee):
    if  Annee:
       
    
       
        Moy_sec = data.groupby('Month')['SecurityDelay'].mean().reset_index()
        fig_1=px.bar(Moy_sec, x='Month', y='SecurityDelay', title='Moyenne mensuelle des retards de sécurité par compagnie',color='Month')
        Moy_trans =data.groupby('Month')['CarrierDelay'].mean().reset_index()
        fig_2=px.pie(Moy_trans, values='Month', names='CarrierDelay', title='Moyenne mensuelle des retards des transporteurs',color='Month')
        Moy_av =data.groupby('Month')['LateAircraftDelay'].mean().reset_index()
        fig_3=px.bar(Moy_av ,x='Month',y='LateAircraftDelay',title='moyenne mensuelle des retards des avions par compagnies ',color='Month')
        Moy_meteo = data.groupby('Month')['WeatherDelay'].mean().reset_index()
        fig_4=px.line(Moy_meteo,x='Month',y='WeatherDelay',markers=True,title="moyenne mensuelle des retards meteorologique: ")
        Moy_sys = data.groupby('Month')['NASDelay'].mean().reset_index()
        fig_5=px.line(Moy_sys,x='Month',y='NASDelay',markers=True,title='Moyenne mensuelle des retards des avions par compagnie aérienne ')

       
       
        return fig_3,fig_2,fig_4,fig_5,fig_1
    else:
        
        
        fig_1={}
        fig_2={}
        fig_3={}
        fig_4={}
        fig_5={}
        
        return fig_3,fig_2,fig_4,fig_1,fig_5

app.run_server(debug=True)
