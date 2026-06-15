import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('../data/gmo_dataset_clean.csv')

app = dash.Dash(__name__)

country_counts = df.groupby('primary_country').size().reset_index(name='gmo_count')
country_risk = df.groupby('primary_country')['risk_score'].mean().reset_index()
country_data = country_counts.merge(country_risk, on='primary_country')

app.layout = html.Div([
    html.H1('GMO Safety Evidence Dashboard',
            style={'textAlign': 'center', 'color': '#2c3e50', 'padding': '20px'}),

    html.P('Approval status and risk assessments for GMO products worldwide',
           style={'textAlign': 'center', 'color': '#7f8c8d'}),

    html.Hr(),

    html.Div([
        html.Div([
            html.Label('Crop Type:'),
            dcc.Dropdown(
                id='crop-filter',
                options=[{'label': 'All', 'value': 'All'}] +
                        [{'label': i, 'value': i} for i in sorted(df['crop_type'].unique())],
                value='All', clearable=False
            )
        ], style={'width': '30%', 'display': 'inline-block', 'marginRight': '20px'}),

        html.Div([
            html.Label('Approval Status:'),
            dcc.Dropdown(
                id='status-filter',
                options=[{'label': 'All', 'value': 'All'}] +
                        [{'label': i, 'value': i} for i in sorted(df['approval_status'].unique())],
                value='All', clearable=False
            )
        ], style={'width': '30%', 'display': 'inline-block'}),
    ], style={'padding': '20px'}),

    html.Hr(),

    dcc.Graph(id='world-map'),
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='scatter-chart'),
])

@app.callback(
    Output('world-map', 'figure'),
    Output('bar-chart', 'figure'),
    Output('scatter-chart', 'figure'),
    Input('crop-filter', 'value'),
    Input('status-filter', 'value')
)
def update_charts(crop, status):
    filtered = df.copy()
    if crop != 'All':
        filtered = filtered[filtered['crop_type'] == crop]
    if status != 'All':
        filtered = filtered[filtered['approval_status'] == status]

    country_counts = filtered.groupby('primary_country').size().reset_index(name='gmo_count')
    country_risk = filtered.groupby('primary_country')['risk_score'].mean().reset_index()
    country_data = country_counts.merge(country_risk, on='primary_country')

    fig_map = px.choropleth(
        country_data,
        locations='primary_country',
        locationmode='country names',
        color='gmo_count',
        hover_name='primary_country',
        hover_data={'risk_score': ':.2f'},
        color_continuous_scale='Greens',
        title='GMO Products by Country'
    )

    fig_bar = px.bar(
        filtered,
        x='crop_type',
        y='risk_score',
        color='crop_type',
        title='Risk Score by Crop Type',
        labels={'crop_type': 'Crop Type', 'risk_score': 'Risk Score'}
    )

    fig_scatter = px.scatter(
        filtered,
        x='approval_year',
        y='risk_score',
        color='crop_type',
        hover_name='gmo_name',
        size='risk_score',
        title='Approval Year vs Risk Score',
        labels={'approval_year': 'Approval Year', 'risk_score': 'Risk Score'}
    )

    return fig_map, fig_bar, fig_scatter

if __name__ == '__main__':
    app.run(debug=True)