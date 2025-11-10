import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

data = {
    'Year': [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017],
    'Urbana': [39831, 39455, 39266, 38681, 41724, 42190, 42525, 42803],
    'Bloomington': [79986, 80262, 80379, 79968, 85603, 85610, 85228, 84945],
    'Iowa City': [76710, 76111, 75867, 74596, 76608, 76052, 75978, 75900],
    'College Park': [34667, 34434, 34374, 35110, 32173, 32228, 32235, 32247],
    'Ann Arbor': [122925, 122645, 121274, 121536, 119280, 120111, 121701, 121716],
    'East Lansing': [48964, 49160, 47702, 46854, 47641, 48028, 47825, 49025],
    'Evanston': [76006, 75614, 75618, 77517, 72683, 73409, 73980, 74603],
    'Eugene': [178786, 178686, 182053, 175096, 173236, 172553, 170777, 169575],
    'State College': [41228, 41267, 40757, 39525, 41366, 41673, 42398, 42515],
    'West Lafayette': [46338, 45193, 45097, 44672, 51605, 50836, 48997, 47531],
    'New Brunswick': [57487, 56567, 56143, 55708, 56182, 55653, 55859, 56106],
}

df = pd.DataFrame(data)

fig = px.bar(df,
             x='Year',
             y=df.columns[1:],
             title="Annual Crimes Comparison by City (2017-2024)",
             labels={"value": "Total Crimes", "variable": "City"},
             barmode='group'
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Total Crimes",
    xaxis_tickangle=-45,
    barmode='group',
    xaxis={'categoryorder':'array', 'categoryarray': df['Year'].tolist()}
)

# Show the plot
fig.show()