# BigQueryToTableauExtractor

This is a 3-step script solution to extract data from Google Big Query at "lightining" speeds :)

It basically works in three steps:

1 - Using Google Bigquery Client API, export data from BigQuery and store it into a Google Cloud Storage Bucket (e.g. as multiple CSV files).

2- Using the [Google Cloud Storage gsutil tool](https://cloud.google.com/storage/docs/gsutil) , download all files from a bucket, using multi-threading, so we can parallelize the download task to maximize network utilization. 

Make sure you have a blazing fast SSD drive attached to your machine, as well as very good bandwidth (e.g. 500 MBPS or more), as these two factors will greately impact the performance of this overall Extract solution. Afterall, we are talking about downloading tens of GBs of datas over the web and storing locally. I/O and Network latency and trhoughput are serious bottlenecks.

3- Now that all CSVs are local and visible to Tableau Server, we use Tableau's REST API to kick off a extract refresh off these files.


