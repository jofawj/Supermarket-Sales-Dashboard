import dash_html_components as html
import dash_bootstrap_components as dbc
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Welcome to the My Dashboard",
                className="text-center"),
                className="mb-2 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Hi my name is Naufal! This is my multiple page dash dashboard!'),
                className="text-center"),
                className="mb-4")
        ]),
 
        dbc.Row([
            dbc.Col(
                html.H5(children='This dashboard contains two main pages, there are interactive visualization of the datasets and my hypotesis testing'),
                className="mb-5")
        ]),
 
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Get the original dataset here',
                        className="text-center"),
                        dbc.Button("Supermarket Sales Dataset",
                        href="https://www.kaggle.com/aungpyaeap/supermarket-sales",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
 
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Visit my Github Page',
                        className="text-center"),
                        dbc.Button("GitHub",
                        href="https://github.com/jofawj",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
    ])
 
])