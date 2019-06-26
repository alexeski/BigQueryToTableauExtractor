from google.cloud import bigquery

import os

# --- START YOUR CONFIGURATIONS HERE --- #
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="<your-private-key-file.json>"

project = "<your-google-project-id>"
dataset_id = "<your-dataset-id>"
table_id = "<your-table-id>"
bucket_name = "<your-google-cloud-storage-bucket>" #the extracted files will go here
filename_pattern = "<exported_files-*.csv>"
# --- END YOUR CONFIGURATIONS HERE --- #

def export_to_bucket():
    client = bigquery.Client()
    destination_uri = "gs://{}/{}".format(bucket_name, filename_pattern)
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
