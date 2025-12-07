import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize Dash app
app = Dash(__name__, assets_folder="assets")

# Layout
app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Visualiser", className="title"),

        html.Div(
            children=[
                html.Label("Select Region:", className="label"),
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
                    inline=True,
                    className="radio-group"
                )
            ],
            className="controls"
        ),

        dcc.Graph(id="sales-line-chart", className="chart-box")
    ],
    className="container"
)

# Callback to update chart based on region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Sales Over Time ({selected_region.capitalize()})",
        labels={"date": "Date", "sales": "Total Sales ($)"},
    )
    return fig


# Run server
if __name__ == "__main__":
    app.run(debug=True)
