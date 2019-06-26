from google.cloud import bigquery

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\dev\GCP_keys\gcp_service_account_key.json"

project = "gcp-tableau-emea-partner-sc"
dataset_id = "data_london_gov_uk"
table_id = "prices_paid_database"
bucket_name = 'gbq_export_alex_test'

def export_to_bucket():
    client = bigquery.Client()
    destination_uri = "gs://{}/{}".format(bucket_name, "prices_paid_database-*.csv")
    dataset_ref = client.dataset(dataset_id, project=project)
    table_ref = dataset_ref.table(table_id)

    print("Data Export from BigQuery to bucket has started...")
    extract_job = client.extract_table(
        table_ref,
        destination_uri,
        # Location must match that of the source table.
        location="US",
    )  # API request
    extract_job.result()  # Waits for job to complete.

    print(
        "Exported {}:{}.{} to {}".format(project, dataset_id, table_id, destination_uri)
    )

if __name__ == '__main__':
    export_to_bucket()