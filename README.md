# NFL_Power_Rankings_Graph
# Alright, so let's see how bad I can mess this puppy up.

## Setup

To get started the only library you'll need to install is BeautifulSoup
```
sudo pip install beautifulsoup4
```

## Run the script!

Open the `ESPN_Scraper/Scrape_ListBuild.py` file and edit the `print` statement
at the end of the file to print out the power rankings for the team you want to
view. For example:
```
print BAL_list
```

Then run the script
```
python ESPN_Scraper/Scrape_ListBuild.py
```

You should see an array of rankings printed
```
[21, 14, 10, 18, 22, 18, 22, 25, 23, 20]
```
