# NFL Power Rankings Graph

## Setup

To get started you'll BeautifulSoup, as well as Plot.ly Dash:
```
sudo pip install beautifulsoup4
```
and
```
pip install dash==0.19.0  # The core dash backend
pip install dash-renderer==0.11.1  # The dash front-end
pip install dash-html-components==0.8.0  # HTML components
pip install dash-core-components==0.14.0  # Supercharged components
pip install plotly --upgrade  # Latest Plotly graphing library
```
Plot.ly is used to create the visuals and for our app.
For more information on Plot.ly visit: https://plot.ly/

## Running the Demo Sraper script to view data!

If you're just working the example ESPN Scraper go ahead and open:
`demo_scraper.py`

This is an ESPN Scraper with a command line interface allowing you
to view the underlying code upon which the app.py is built.

There's a directory available if you're unsure of your team's city code
accessed by typing 'DIR'

To exit type 'xx'

## Using the Plotly Graph

Run `app.py`
It will open a graph of all 32 teams data plotted on one graph.

## Plotly Dash

Plot.ly provides a tool called Dash that enables user to modify the
information displayed graphically.  This is our logical next step.
This aspect will be developed now in `app_dash.py` in another
branch to build on what we have currently.