# BigQueryToTableauExtractor

This is a 3-step script solution to extract data from Google Big Query at "lightining" speeds :)

It basically works in three steps:

1 - Using Google Bigquery Client API, export data from BigQuery and store it into a Google Cloud Storage Bucket (e.g. as multiple CSV files).

2- Using the [Google Cloud Storage gsutil tool](https://cloud.google.com/storage/docs/gsutil) , download all files from a bucket, using multi-threading, so we can parallelize the download task to maximize network utilization. 

Make sure you have a blazing fast SSD drive attached to your machine as well as , as it heavily
