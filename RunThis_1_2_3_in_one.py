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
os.system("python refreshExtractByName.py -s <your_Tableau_Server_URL_here> -u <your_admin_username> -pw <your_admin_password> -dn \"<your_unique_datasource_name_here>\" ")
