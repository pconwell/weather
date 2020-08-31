import tarfile
import pandas as pd
import csv
import io

# open tar and get names of individual csv files (stations)
tar = tarfile.open("./2018.tar")
members = tar.getnames()

# loop over all the files inside the tarball
for member in members:

   # read a given file inside tarball (convert to ascii to be legible)
   f = io.StringIO(tar.extractfile(member).read().decode('ascii'))
   df = pd.read_csv(f)

   # # generate csv of station names/locations. This is insanely slow, so if you need to do this for some reason
   # # I'd suggest you rewrite this to use native csv reader
   # df.head(1)[["STATION", "NAME", "LATITUDE", "LONGITUDE"]].to_csv("./out.csv", mode="a", header=False)

   # read temps, which are celcius without a decimal point + a 'quality' score
   # e.g. "+0311,1" would be positive 31.1 degrees celcius and ",1" == "passed all quality control checks"
   df['temp'] = (df['TMP'].str[1:5].astype(int)/10)

   # subset any temps below 60 degrees celcius to remove erronious data
   df = df[df['temp'] < 60]

   print(df['temp'].mean())