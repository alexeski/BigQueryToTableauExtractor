import os
from timeit import default_timer as timer

# Export data from Big Query to Bucket
start = timer()
os.system("python export_data.py")
end = timer()
print("Timer: " + str(round((end-start)/60,3)) + " minutes")

# Download data from Google Bucket to local drive
start = timer()
os.system("python download_bucket_files.py")
end = timer()
print("Timer: " + str(round((end-start)/60,3)) + " minutes")

# Trigger Extract refresh (asyncronous)
os.system("python refreshExtractByName.py -s http://localhost:8000 -u admin -pw admin -dn \"prices_paid_database (local CSV files with Union)\" ")
