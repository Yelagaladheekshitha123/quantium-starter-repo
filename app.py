import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
data = pd.read_csv("formatted_data.csv")

# Convert date
data["date"] = pd.to_datetime(data["date"])

# Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f7",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.Div([
            html.Label(
                "Select Region:",
                style={"fontWeight": "bold", "fontSize": "18px"}
            ),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                labelStyle={
                    "display": "inline-block",
                    "marginRight": "15px"
                }
            ),
        ],
        style={
            "textAlign": "center",
            "marginBottom": "30px"
        }),

        dcc.Graph(id="sales-chart")
    ]
)

# Callback to update graph
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == selected_region]

    grouped = filtered_data.groupby("date")["sales"].sum().reset_index()

    fig = px.line(
        grouped,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "sales": "Sales"}
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)