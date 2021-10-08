import plotly.express as px
import pandas as pd
 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
from datetime import date
 
from app import app #change this line
 
# Data Preprocessing
df = pd.read_csv('supermarket_sales.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format="%H:%M").dt.time


first_card = dbc.Card(
    dbc.ListGroup(
        [
            dbc.ListGroupItem([
                dbc.Col(
                    html.Div(style={'width':'100%', 'height':'100%','float':'left'},
                    children=[
                    html.Label('Date'),
                    dcc.DatePickerRange(
                    id = "date-check",
                    min_date_allowed=df['Date'].min(),
                    max_date_allowed=df['Date'].max(),
                    start_date= date(2019,1,1),
                    end_date=date(2019,3,30),
                    style ={'float': 'left'}
                )
                ])
                )
            ]),
               dbc.ListGroupItem([
                dbc.Col(
                    html.Div(style={'width':'50%', 'height':'100%','float':'left'},
                    children=[
                    html.Label('City'),
                    dcc.RadioItems(id='city-check',
                    options=[
                        {'label': ' Yangon', 'value': 'Yangon'},
                        {'label': ' Naypyitaw', 'value': 'Naypyitaw'},
                        {'label': ' Mandalay', 'value': 'Mandalay'}
                    ]
                    )
                ])
                )
            ]),
            dbc.ListGroupItem([
                dbc.Col(
                    html.Div(style={'float':'left'},
                    children=[
                    html.Label('Product Line'),
                    dcc.RadioItems(id='product-check',
                    options=[
                        {'label': ' Health and beauty', 'value': 'Health and beauty'},
                        {'label': ' Electronic accessories', 'value': 'Electronic accessories'},
                        {'label': ' Home and lifestyle', 'value': 'Home and lifestyle'},
                        {'label': ' Sports and travel', 'value': 'Sports and travel'},
                        {'label': ' Food and beverages', 'value': 'Food and beverages'},
                        {'label': ' Fashion accessories', 'value': 'Fashion accessories'}
                    ]
                    )
                ])
                )
            ]),
            dbc.ListGroupItem([
                dbc.Col(
                    html.Div(style={'width':'65%', 'height':'100%','float':'left'},
                    children=[
                    html.Label('Customer Type'),
                    dcc.RadioItems(id='customer-check',
                    options=[
                        {'label': ' Normal', 'value': 'Normal'},
                        {'label': ' Member', 'value': 'Member'}
                    ]
                    )
                ])
                )
            ]),
            dbc.ListGroupItem([
                dbc.Col(
                    html.Div(style={'width':'45%', 'height':'100%','float':'left'},
                    children=[
                    html.Label('Gender'),
                    dcc.RadioItems(id='gender-check',
                    options=[
                        {'label': ' Male', 'value': 'Male'},
                        {'label': ' Female', 'value': 'Female'}
                    ]
                    )
                ])
                )
            ]),
            dbc.ListGroupItem([
                dbc.Col(
                    html.Div(style={'width':'65%', 'height':'100%','float':'left'},
                    children=[
                    html.Label('Payment'),
                    dcc.RadioItems(id='payment-check',
                    options=[
                        {'label': ' Ewallet', 'value': 'Ewallet'},
                        {'label': ' Credit Card', 'value': 'Credit card'},
                        {'label': ' Cash', 'value': 'Cash'}
                    ]
                    )
                ])
                )
            ])
        ])
        )

second_card = dbc.Row([
            html.Div([
                dbc.Card([
                dbc.CardBody([
                    html.H1(id='invoice-data'),
                    html.H6('Invoice')
                    ]),
            ])
            ],  style={'width': '14.5%','textAlign': 'center'}),
            html.Div([
                dbc.Card([
                dbc.CardBody([
                    html.H1(id='total-sales'),
                    html.H6('Sales')
                    ]),
            ])
            ],  style={'width': '23.3%','textAlign': 'center'}),
            html.Div([
                dbc.Card([
                dbc.CardBody([
                    html.H1(id='income-per-purchase'),
                    html.H6('Income per Purchase')
                    ]),
            ])
            ],  style={'width': '21.4%','textAlign': 'center'}),
            html.Div([
                dbc.Card([
                dbc.CardBody([
                    html.H1(id='quantity'),
                    html.H6('Units In K')
                    ]),
            ])
            ],  style={'width': '14.55%','textAlign': 'center'}),
            html.Div([
                dbc.Card([
                dbc.CardBody([
                    html.H1(id='quantity-inv'),
                    html.H6('Units per Sell')
                    ]),
            ])
            ],  style={'width': '15.25%','textAlign': 'center'}),
            html.Div([
                dbc.Card([
                dbc.CardBody([
                    html.H1(id='rate-sales'),
                    html.H6('Rating')
                    ]),
            ])
            ],  style={'width': '11%','textAlign': 'center'})
]), dbc.Row([
html.Div([
            dcc.Graph(id='sales-by-date')
    ], style={'width': '55%','display': 'inline-block', 'vertical-align': 'middle'}),
html.Div([
            dcc.Graph(id='sales-by-category')
    ], style={'width': '45%','display': 'inline-block', 'vertical-align': 'middle'}),
html.Div([
            dcc.Graph(id='sales-by-payment')
    ], style={'width': '50%','display': 'inline-block', 'vertical-align': 'middle'}),
html.Div([
            dcc.Graph(id='sales-by-day')
    ], style={'width': '50%','display': 'inline-block', 'vertical-align': 'middle'})
    ])

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Supermarket Sales"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row(
            [
                dbc.Col(first_card, width=3),
                dbc.Col(second_card, width=9),
            ]
        )
            ])
        ], style={'width': '101.85%', 'display': 'flex', 'justify-content': 'center'})

@app.callback(
    Output(component_id='invoice-data', component_property='children'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_invoice(start_date, end_date, city_check, product_check, customer_check, gender_check, payment_check):
    df_NEW = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()

    if product_check != None:
        df_NEW = df_NEW[df_NEW['Product line'] == product_check]
        df_restore = df_NEW.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW = df_restore
            pname_check = "All Product"
    
    if city_check != None:
        df_NEW = df_NEW[df_NEW['City'] == city_check]
        df_restore = df_NEW.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW = df_NEW[df_NEW['Customer type'] == customer_check]
        df_restore = df_NEW.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW = df_NEW[df_NEW['Gender'] == gender_check]
        df_restore = df_NEW.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW = df_NEW[df_NEW['Payment'] == payment_check]
        df_restore = df_NEW.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW = df_restore
            pmname_check = "All Payment"

    invoice = df_NEW.groupby("Date", sort=False)["Invoice ID"].count().sum()
    return '{}'.format(invoice)

@app.callback(
    Output(component_id='total-sales', component_property='children'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_sales(start_date, end_date, city_check, product_check, customer_check, gender_check, payment_check):
    df_NEW = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()
    if product_check != None:
        df_NEW = df_NEW[df_NEW['Product line'] == product_check]
        df_restore = df_NEW.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW = df_restore
            pname_check = "All Product"
    
    if city_check != None:
        df_NEW = df_NEW[df_NEW['City'] == city_check]
        df_restore = df_NEW.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW = df_NEW[df_NEW['Customer type'] == customer_check]
        df_restore = df_NEW.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW = df_NEW[df_NEW['Gender'] == gender_check]
        df_restore = df_NEW.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW = df_NEW[df_NEW['Payment'] == payment_check]
        df_restore = df_NEW.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW = df_restore
            pmname_check = "All Payment"

    sales = round(df_NEW.groupby("Date", sort=False)["Total"].sum().sum(), 0)
    if sales > 100000:
        sales /= 1000
        sales = round(sales, 2)
        return '$ {}k'.format(sales)
    else:
        return '$ {}'.format(sales)

@app.callback(
    Output(component_id='income-per-purchase', component_property='children'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_sales(start_date, end_date, city_check, product_check, customer_check, gender_check, payment_check):
    df_NEW = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()
    if product_check != None:
        df_NEW = df_NEW[df_NEW['Product line'] == product_check]
        df_restore = df_NEW.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW = df_restore
            pname_check = "All Product"
    
    if city_check != None:
        df_NEW = df_NEW[df_NEW['City'] == city_check]
        df_restore = df_NEW.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW = df_NEW[df_NEW['Customer type'] == customer_check]
        df_restore = df_NEW.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW = df_NEW[df_NEW['Gender'] == gender_check]
        df_restore = df_NEW.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW = df_NEW[df_NEW['Payment'] == payment_check]
        df_restore = df_NEW.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW = df_restore
            pmname_check = "All Payment"

    invoice = df_NEW.groupby("Date", sort=False)["Invoice ID"].count().sum()
    sales = round(df_NEW.groupby("Date", sort=False)["Total"].sum().sum(), 0)
    IPP = round(sales/invoice, 2)

    return '$ {}'.format(IPP)

@app.callback(
    Output(component_id='rate-sales', component_property='children'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_sales(start_date, end_date, city_check, product_check, customer_check, gender_check, payment_check):
    df_NEW = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()
    if product_check != None:
        df_NEW = df_NEW[df_NEW['Product line'] == product_check]
        df_restore = df_NEW.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW = df_restore
            pname_check = "All Product"
    
    if city_check != None:
        df_NEW = df_NEW[df_NEW['City'] == city_check]
        df_restore = df_NEW.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW = df_NEW[df_NEW['Customer type'] == customer_check]
        df_restore = df_NEW.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW = df_NEW[df_NEW['Gender'] == gender_check]
        df_restore = df_NEW.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW = df_NEW[df_NEW['Payment'] == payment_check]
        df_restore = df_NEW.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW = df_restore
            pmname_check = "All Payment"

    rating = round(df_NEW.groupby("Date", sort=False)["Rating"].mean().mean(), 0)

    return '{}'.format(rating)

@app.callback(
    Output(component_id='quantity', component_property='children'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_sales(start_date, end_date, city_check, product_check, customer_check, gender_check, payment_check):
    df_NEW = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()
    if product_check != None:
        df_NEW = df_NEW[df_NEW['Product line'] == product_check]
        df_restore = df_NEW.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW = df_restore
            pname_check = "All Product"
    
    if city_check != None:
        df_NEW = df_NEW[df_NEW['City'] == city_check]
        df_restore = df_NEW.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW = df_NEW[df_NEW['Customer type'] == customer_check]
        df_restore = df_NEW.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW = df_NEW[df_NEW['Gender'] == gender_check]
        df_restore = df_NEW.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW = df_NEW[df_NEW['Payment'] == payment_check]
        df_restore = df_NEW.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW = df_restore
            pmname_check = "All Payment"

    quantity = round(df_NEW.groupby("Date", sort=False)["Quantity"].sum().sum(), 0)
    quantity = round(quantity/1000, 2)

    return '{}'.format(quantity)

@app.callback(
    Output(component_id='quantity-inv', component_property='children'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_sales(start_date, end_date, city_check, product_check, customer_check, gender_check, payment_check):
    df_NEW = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()
    if product_check != None:
        df_NEW = df_NEW[df_NEW['Product line'] == product_check]
        df_restore = df_NEW.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW = df_restore
            pname_check = "All Product"
    
    if city_check != None:
        df_NEW = df_NEW[df_NEW['City'] == city_check]
        df_restore = df_NEW.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW = df_NEW[df_NEW['Customer type'] == customer_check]
        df_restore = df_NEW.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW = df_NEW[df_NEW['Gender'] == gender_check]
        df_restore = df_NEW.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW = df_NEW[df_NEW['Payment'] == payment_check]
        df_restore = df_NEW.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW = df_restore
            pmname_check = "All Payment"

    inv = df_NEW.groupby("Date", sort=False)["Invoice ID"].count().sum()
    quantity = round(df_NEW.groupby("Date", sort=False)["Quantity"].sum().sum(), 0)
    result = round(quantity/inv, 2)

    return '{}'.format(result)

@app.callback(
    Output(component_id='sales-by-date', component_property='figure'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_sales(start_date, end_date, product_check, city_check, customer_check, gender_check, payment_check):
    df_NEW = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()
    if product_check != None:
        df_NEW = df_NEW[df_NEW['Product line'] == product_check]
        df_restore = df_NEW.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW = df_restore
            pname_check = "All Product"
    
    if city_check != None:
        df_NEW = df_NEW[df_NEW['City'] == city_check]
        df_restore = df_NEW.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW = df_NEW[df_NEW['Customer type'] == customer_check]
        df_restore = df_NEW.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW = df_NEW[df_NEW['Gender'] == gender_check]
        df_restore = df_NEW.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW = df_NEW[df_NEW['Payment'] == payment_check]
        df_restore = df_NEW.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW = df_restore
            pmname_check = "All Payment"

    df_NEW = df_NEW.sort_values(by = 'Date')
    df_NEW_TotSum = df_NEW.groupby("Date", sort=False)["Total"].sum()
    fig = px.line(df_NEW, x=df_NEW['Date'].unique(), y=df_NEW_TotSum, text=df_NEW_TotSum)
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.data[0].update(mode='markers+lines')
    fig.update_traces(hovertemplate='Date: %{x} <br>Revenue: $ %{y} ', line_color='#FF8000')
    fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ))
    fig.update_layout(title='Sales by Date in %s '%name_check , xaxis_title='Date', yaxis_title='Total Revenue', font_family="Arial",
    font_color="white",
    title_font_family="Arial",
    title_font_color="white"
)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return fig

@app.callback(
    Output(component_id='sales-by-category', component_property='figure'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_sales(start_date, end_date, city_check, customer_check, gender_check, payment_check):
    df_NEW_3 = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()
    
    if city_check != None:
        df_NEW_3 = df_NEW_3[df_NEW_3['City'] == city_check]
        df_restore = df_NEW_3.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW_3 = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW_3 = df_NEW_3[df_NEW_3['Customer type'] == customer_check]
        df_restore = df_NEW_3.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW_3 = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW_3 = df_NEW_3[df_NEW_3['Gender'] == gender_check]
        df_restore = df_NEW_3.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW_3 = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW_3 = df_NEW_3[df_NEW_3['Payment'] == payment_check]
        df_restore = df_NEW_3.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW_3 = df_restore
            pmname_check = "All Payment"

    df_TotSum = round(df_NEW_3.groupby("Product line", sort=False)["Total"].sum(), 0)
    df_newest = round(df_TotSum/1000, 1)
    fig_2 = px.bar(df_newest, x=df_NEW_3['Product line'].unique(), y=df_newest, text=df_newest, color=df_newest)
    fig_2.update_traces(texttemplate='%{text:.5s}')
    fig_2.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ))
    fig_2.update_traces(hovertemplate='Product Category: %{x} <br>Revenue: $ %{y}')
    fig_2.update_layout(title='Sales by Category for {}' .format(name_check), xaxis_title='Category', yaxis_title='Total Revenue', font=dict(
        family="Arial",
        size=12,
        color="White"
    )
)
    fig_2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return fig_2

@app.callback(
    Output(component_id='sales-by-payment', component_property='figure'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value')
)
def update_sales(start_date, end_date, product_check, city_check, customer_check, gender_check):
    df_NEW_4 = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()
    if product_check != None:
        df_NEW_4 = df_NEW_4[df_NEW_4['Product line'] == product_check]
        df_restore = df_NEW_4.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW = df_restore
            pname_check = "All Product"

    if city_check != None:
        df_NEW_4 = df_NEW_4[df_NEW_4['City'] == city_check]
        df_restore = df_NEW_4.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW_4 = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW_4 = df_NEW_4[df_NEW_4['Customer type'] == customer_check]
        df_restore = df_NEW_4.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW_4 = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW_4 = df_NEW_4[df_NEW_4['Gender'] == gender_check]
        df_restore = df_NEW_4.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW_4 = df_restore
            gname_check = "All Gender"

    df_Average = round(df_NEW_4.groupby("Payment", sort=False)["Total"].mean(), 2)
    fig_3 = px.bar(df_Average, x=df_Average, y=df_NEW_4['Payment'].unique(), text=df_Average, orientation='h', color= df_Average)
    fig_3.update_traces(texttemplate='%{text:.5s}', textposition='outside')
    fig_3.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ))
    fig_3.update_traces(hovertemplate='Revenue:$ %{x} <br>Payment: %{y}')
    fig_3.update_layout(title='Sales by Payment in {}' .format(name_check), xaxis_title='Total Revenue', yaxis_title='Payments',  font=dict(
        family="Arial",
        size=12,
        color="White"
    ))
    fig_3.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return fig_3

@app.callback(
    Output(component_id='sales-by-day', component_property='figure'),
    Input('date-check', 'start_date'),
    Input('date-check', 'end_date'),
    Input(component_id='product-check', component_property='value'),
    Input(component_id='city-check', component_property='value'),
    Input(component_id='customer-check', component_property='value'),
    Input(component_id='gender-check', component_property='value'),
    Input(component_id='payment-check', component_property='value')
)
def update_sales(start_date, end_date, product_check, city_check, customer_check, gender_check, payment_check):
    df_day = df['Date'].dt.day_name()
    df['Days'] = df_day
    df_NEW_5 = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_restore = pd.DataFrame()

    if product_check != None:
        df_NEW_5 = df_NEW_5[df_NEW_5['Product line'] == product_check]
        df_restore = df_NEW_5.copy()
        pname_check = product_check
    else:
        if len(df_restore) == 0:
            pname_check = "All Product"
        else:
            df_NEW_5 = df_restore
            pname_check = "All Product"
    
    if city_check != None:
        df_NEW_5 = df_NEW_5[df_NEW_5['City'] == city_check]
        df_restore = df_NEW_5.copy()
        name_check = city_check
    else:
        if len(df_restore) == 0:
            name_check = "Every City"
        else:
            df_NEW_5 = df_restore
            name_check = "Every City"

    if customer_check != None:
        df_NEW_5 = df_NEW_5[df_NEW_5['Customer type'] == customer_check]
        df_restore = df_NEW_5.copy()
        cname_check = customer_check
    else:
        if len(df_restore) == 0:
            cname_check = "All Customer"
        else:
            df_NEW_5 = df_restore
            cname_check = "All Customer"

    if gender_check != None:
        df_NEW_5 = df_NEW_5[df_NEW_5['Gender'] == gender_check]
        df_restore = df_NEW_5.copy()
        gname_check = gender_check
    else:
        if len(df_restore) == 0:
            gname_check = "All Gender"
        else:
            df_NEW_5 = df_restore
            gname_check = "All Gender"

    if payment_check != None:
        df_NEW_5 = df_NEW_5[df_NEW_5['Payment'] == payment_check]
        df_restore = df_NEW_5.copy()
        pmname_check = payment_check
    else:
        if len(df_restore) == 0:
            pmname_check = "All Payment"
        else:
            df_NEW_5 = df_restore
            pmname_check = "All Payment"

    df_TOTSUM_2 = round(df_NEW_5.groupby("Days", sort=False)["Total"].sum(), 2)
    fig_4 = px.bar(df_TOTSUM_2, x=df_NEW_5['Days'].unique(), y=df_TOTSUM_2, text=df_TOTSUM_2, color=df_TOTSUM_2)
    fig_4.update_traces(texttemplate='%{text:.4s}')
    fig_4.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig_4.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ))
    fig_4.update_traces(hovertemplate='Day: %{x} <br>Revenue:$ %{y}')
    fig_4.update_layout(title='Sales by Day in {}'.format(name_check), xaxis_title='Days', yaxis_title='Revenue',  font=dict(
        family="Arial",
        size=12,
        color="White"
    ))
    fig_4.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return fig_4
