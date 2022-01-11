import csv
from meghan import climatetable, fetchECCC
import reports
from siteIDdb import findprov
from dailies import collectalldailies
#import graphdaily

def main():
  # importing from web https://dd.weather.gc.ca/climate/observations/
  #siteid = '6016527' #ottawa
  siteid = '8300060' #pei 
  province = findprov(siteid)
  url = "https://dd.weather.gc.ca/climate/observations/normals/csv/1981-2010/" + province + "/climate_normals_" + province + "_" + siteid + "_1981-2010.csv"

  reader = fetchECCC(url)

  # this function isn't done yet 
  dailydata = collectalldailies(siteid)
  with open("example5.csv", 'w') as f:
    csvwriter = csv.writer(f)
    for line in dailydata:
      csvwriter.writerow(line)

  chunked_reader = climatetable(reader)
  reports.final_report(chunked_reader)

if __name__ == "__main__":
  main()