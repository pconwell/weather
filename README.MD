Goal: Conduct analysis of Integrated Surface Database (ISD) to determine location(s) with most consistant temprature and dew point, with the intent to generate a list of geographical areas that are the most comfortable to live. Ideal temperature range is 60°F ± 15°F and dewpoint range is 45°F ± 10°F.

Questions:
1. What defines 'consistant'? Are daily variations more or less important than seasonal variations?
2. Does time of day matter? For example, is the temperature at 2am relevant?
3. How many years of data are needed to show a trend?
4. What are realistic filters/heuristics to narrow down locations?
5. Are single extreme days better/worse than a greater number of less extreme outliers

Quick Intro

0. Set up your python environment, pipfile provided if using pipenv. Requirements are fairly minmal, so you may already have what you need installed:
   1. pandas
   2. requests
   3. csv
   4. json
   5. tarfile
   6. io
1. Download yearly data set: https://www.ncei.noaa.gov/data/global-hourly/archive/csv/
2. Unzip tar.gz (will be ~50GB/year)
3. Run `analysis.py`


More info on hourly integrated surface data here: https://www.ncdc.noaa.gov/isd
