# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(
                                    id='site-dropdown',
                                    options=[{'label': 'All Sites', 'value': 'ALL'},
                                                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                                    value='ALL',
                                    placeholder="Select a launch site here",
                                    searchable="True"
                                    ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id="payload-slider",
                                                min=0,
                                                max=10000,
                                                step=1000,
                                                marks={0:"0", 1000:"1000", 2000:"2000", 3000:"3000", 
                                                        4000:"4000", 5000:"5000",6000:"6000", 7000:"7000", 8000:"8000", 
                                                        9000:"9000", 10000:"10000"},
                                                value=[min_payload,max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id="success-pie-chart",component_property="figure"),
            Input(component_id="site-dropdown",component_property="value"))

def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == "ALL":
        fig=px.pie(filtered_df, values="class",
        names="Launch Site",
        title="SpaceX Launch Site Success Distribution")
        return fig
    else:
        filtered_df = spacex_df[spacex_df["Launch Site"]==entered_site]
        filtered_df = filtered_df.groupby(["Launch Site", 'class']).size().reset_index(name="class_count")
        # Create foot chart with breakdown of successes and failures (class = 1 for success, 0 for failure)
        fig=px.pie(filtered_df, values="class_count",
                    names=filtered_df['class'].map({1: "Success", 0: "Failure"}),
                    title=f"Total success vs Failure for {entered_site}")
        fig.update_traces(marker = dict(colors=["red","blue"]))
        return fig
        
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [Input(component_id="site-dropdown", component_property="value"), 
     Input(component_id="payload-slider", component_property="value")]
)
def get_scatter_chart(entered_site, payload_mass):
    # Desempaquetar el rango de masa del payload
    low, high = payload_mass
    
    # Filtrar el DataFrame basado en el rango de payload
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    
    # Si se seleccionan todos los sitios
    if entered_site == "ALL":
        # Crear el scatter plot con la versión del booster como color
        fig = px.scatter(filtered_df, 
                         x="Payload Mass (kg)", 
                         y="class", 
                         color="Booster Version Category",
                         title="Payload vs Launch Outcome for All Sites",
                         labels={"class": "Launch Outcome"})
        fig.update_traces(marker=dict(size=8))
        fig.update_yaxes(tickvals=[0, 1], ticktext=["Failure", "Success"])
        return fig
    else:
        # Filtrar el DataFrame por el sitio seleccionado
        filtered_site_df = filtered_df[filtered_df["Launch Site"] == entered_site]
        
        
        # Crear el scatter plot para el sitio seleccionado
        fig = px.scatter(filtered_site_df, 
                         x="Payload Mass (kg)", 
                         y="class", 
                         color="Booster Version Category",
                         title=f"Payload vs Launch Outcome for {entered_site}",
                         labels={"class": "Launch Outcome"})
        fig.update_traces(marker=dict(size=8))
        fig.update_yaxes(tickvals=[0, 1], ticktext=["Failure", "Success"])
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
