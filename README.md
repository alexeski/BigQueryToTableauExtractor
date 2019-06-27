# BigQuery To Tableau Extractor

This is a 3-step script solution to extract data from Google Big Query at "lightining" speeds :)

It basically works in three steps:

1 - File: 1_export_data.py

Using [Google Bigquery API (Python library)](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries), export data from BigQuery and store it into a Google Cloud Storage Bucket (e.g. as multiple CSV files).

2- File: 2_download_bucket_files.py
 
Using the [Google Cloud Storage gsutil tool](https://cloud.google.com/storage/docs/gsutil) , download all files from a bucket, using multi-threading, so we can parallelize the download task to maximize network utilization. 

Make sure you have a blazing fast SSD drive attached to your machine, as well as very good bandwidth (e.g. 500 MBPS or more), as these two factors will greately impact the performance of this overall Extract solution. Afterall, we are talking about downloading tens of GBs of datas over the web and storing locally. I/O and Network latency and trhoughput are serious bottlenecks.

3- File: RefreshExtractByName.py

Now that all CSVs are local and visible to Tableau Server, we use Tableau's REST API, more specifically, the [Tableau Server Client - Python](https://tableau.github.io/server-client-python/#), to kick off a extract refresh off these files.

----

We've also included a 4th python file, which basically wraps the three scripts above into one single python file. You should run this one, but at the moment, the configurations are spread into each files (I know, this is not a best practices course at all ;) )

The full instructions how to use this code here: https://community.tableau.com/docs/DOC-23161
