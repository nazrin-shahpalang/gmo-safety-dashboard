import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('../data/gmo_dataset_clean.csv')

app = dash.Dash(__name__)

fig_bar = px.bar(
    df,
    x='crop_type',
    y='risk_score',
    color='crop_type',
    title='Risk Score by Crop Type',
    labels={'crop_type': 'Crop Type', 'risk_score': 'Risk Score'}
)

fig_scatter = px.scatter(
    df,
    x='approval_year',
    y='risk_score',
    color='crop_type',
    hover_name='gmo_name',
    title='Approval Year vs Risk Score',
    labels={'approval_year': 'Approval Year', 'risk_score': 'Risk Score'}
)

app.layout = html.Div([
    html.H1('GMO Safety Evidence Dashboard',
            style={'textAlign': 'center', 'color': '#2c3e50'}),

    html.P('Approval status and risk assessments for GMO products worldwide',
           style={'textAlign': 'center', 'color': '#7f8c8d'}),

    html.Hr(),

    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_scatter),

    html.Hr(),

    html.H3('All Records', style={'textAlign': 'center'}),
    html.Table([
        html.Thead(html.Tr([html.Th(col) for col in df.columns])),
        html.Tbody([
            html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
            for i in range(len(df))
        ])
    ], style={'margin': 'auto', 'borderCollapse': 'collapse'})
])

if __name__ == '__main__':
    app.run(debug=True)
