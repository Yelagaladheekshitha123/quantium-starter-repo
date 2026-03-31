import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load data
data = pd.read_csv("formatted_data.csv")

# Convert date
data["date"] = pd.to_datetime(data["date"])

# Group by date
data = data.groupby("date")["sales"].sum().reset_index()

# Create chart
fig = px.line(
    data,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales"}
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)