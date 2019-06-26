import os

bucket_name = 'gbq_export_alex_test'
file_format = 'csv'
destination_path = 'c:\\tmp\gbqExtracts' #local path where you want to savethe files downloaded

def download_bucket_files():
    myCmd="gsutil -m cp -r gs://{}/*.{} {}".format(bucket_name,file_format,destination_path)
    print(myCmd)
    os.system(myCmd)

if __name__ == '__main__':
    download_bucket_files()
    