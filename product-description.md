# NYC Coronavirus (COVID-19) Data | New York City Department of Health

The source code outlining how this product gathers, transforms, revises and publishes its datasets is available at [https://github.com/rearc-data/nyc-doh-covid-19](https://github.com/rearc-data/nyc-doh-covid-19).

## Main Overview
This resource contains data assembled by the NYC Department of Health and Mental Hygiene (DOHMH)'s COVID-19 Response team, and provides insight into the current state of the COVID-19 pandemic in New York City. As DOHMH collects their data in realtime, the values in the included datasets are subject to change.

#### Data Source
There was a major update in the data source in November 9, 2020 and we reflect those changes in all revisions published on or after that date. Main updates include the following file name changes as well as addition of several new data files as described below: 

File name mapping from revisions published before and after November 9, 2020:

- `nyc-doh-covid-19-summary.csv` -> `nyc-doh-covid-19-totals-summary.csv`
- `nyc-doh-covid-19-case-hosp-death.csv` -> `nyc-doh-covid-19-trends-data-by-day.csv`
- `nyc-doh-covid-19-boro.csv` -> `nyc-doh-covid-19-totals-by-boro.csv`
- `nyc-doh-covid-19-by-age.csv` -> `nyc-doh-covid-19-totals-by-age.csv`
- `nyc-doh-covid-19-by-sex.csv` -> `nyc-doh-covid-19-totals-by-sex.csv`
- `nyc-doh-covid-19-tests-by-zcta.csv` -> `nyc-doh-covid-19-totals-data-by-modzcta.csv`
- `nyc-doh-covid-19-probable-confirmed-dod.csv` ->


The data files are in 3 categories: `totals`, `trends`, and `latest`. The category of a file can be identified from the filename following the pattern `nyc-doh-covid-19-<CATEGORY>-<FILENAME>`.

**Totals:**
- `nyc-doh-covid-19-totals-antibody-by-age.csv`
- `nyc-doh-covid-19-totals-antibody-by-boro.csv`
- `nyc-doh-covid-19-totals-antibody-by-modzcta.csv`
- `nyc-doh-covid-19-totals-antibody-by-poverty.csv`
- `nyc-doh-covid-19-totals-antibody-by-sex.csv`
- `nyc-doh-covid-19-totals-by-age.csv`
- `nyc-doh-covid-19-totals-by-boro.csv`
- `nyc-doh-covid-19-totals-by-poverty.csv`
- `nyc-doh-covid-19-totals-by-race.csv`
- `nyc-doh-covid-19-totals-by-sex.csv`
- `nyc-doh-covid-19-totals-data-by-modzcta.csv`
- `nyc-doh-covid-19-totals-deaths-by-boro-age.csv`
- `nyc-doh-covid-19-totals-deaths-by-race-age.csv`
- `nyc-doh-covid-19-totals-deaths-by-underlying-conditions.csv`
- `nyc-doh-covid-19-totals-group-cases-by-boro.csv`
- `nyc-doh-covid-19-totals-group-data-by-boro.csv`
- `nyc-doh-covid-19-totals-group-death-by-boro.csv`
- `nyc-doh-covid-19-totals-group-hosp-by-boro.csv`
- `nyc-doh-covid-19-totals-probable-confirmed-by-age.csv`
- `nyc-doh-covid-19-totals-probable-confirmed-by-boro.csv`
- `nyc-doh-covid-19-totals-probable-confirmed-by-location.csv`
- `nyc-doh-covid-19-totals-probable-confirmed-by-race.csv`
- `nyc-doh-covid-19-totals-probable-confirmed-by-sex.csv`
- `nyc-doh-covid-19-totals-summary.csv`

**Trends:**
- `nyc-doh-covid-19-trends-antibody-by-week.csv`
- `nyc-doh-covid-19-trends-caserate-by-modzcta.csv`
- `nyc-doh-covid-19-trends-covid-like-illness.csv`
- `nyc-doh-covid-19-trends-data-by-day.csv`
- `nyc-doh-covid-19-trends-percentpositive-by-modzcta.csv`
- `nyc-doh-covid-19-trends-testing-by-age.csv`
- `nyc-doh-covid-19-trends-testing-turnaround.csv`
- `nyc-doh-covid-19-trends-testrate-by-modzcta.csv`
- `nyc-doh-covid-19-trends-tests.csv`

**Latest:**
- `nyc-doh-covid-19-latest-last7days-by-modzcta.csv`
- `nyc-doh-covid-19-trends-now-covid-like-illness.csv`
- `nyc-doh-covid-19-trends-now-data-by-day.csv`
- `nyc-doh-covid-19-trends-now-summary.csv`
- `nyc-doh-covid-19-trends-now-testing-by-age.csv`
- `nyc-doh-covid-19-trends-now-tests.csv`
- `nyc-doh-covid-19-trends-pp-by-modzcta.csv`

## More Information
- Source - [GitHub | NYC Coronavirus (COVID-19) Data](https://github.com/nychealth/coronavirus-data)
- [NYC Health | COVID-19: Data](https://www1.nyc.gov/site/doh/covid/covid-19-data.page)
- Frequency: Daily
- Format: CSV

## Contact Details
- If you find any issues or have enhancements with this product, open up a GitHub [issue](https://github.com/rearc-data/nyc-doh-covid-19/issues) and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you are interested in any other open datasets, please create a request on our project board [here](https://github.com/rearc-data/covid-datasets-aws-data-exchange/projects/1).
- If you have questions about this source data, please contact the City of New York.
- If you have any other questions or feedback, send us an email at data@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.