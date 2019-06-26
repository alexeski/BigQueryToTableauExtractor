import os

# --- START YOUR CONFIGURATIONS HERE --- #
bucket_name = '<your-google-cloud-storage-bucket>'
file_format = 'csv'
destination_path = '<path-to-your-local-folder>' #local path where you want to savethe files downloaded
# --- END YOUR CONFIGURATIONS HERE --- #

def download_bucket_files():
    myCmd="gsutil -m cp -r gs://{}/*.{} {}".format(bucket_name,file_format,destination_path)
    print(myCmd)
    os.system(myCmd)

if __name__ == '__main__':
    download_bucket_files()
    
