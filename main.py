import pydrive
from os import environ
from os import listdir
from os.path import isfile, join
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

drive_url = environ.get('URL')
key = environ.get('GoogleAuth')
google_auth = GoogleAuth(key)
drive = GoogleDrive(google_auth)
path = environ.get('PATH')
photo_number = 0

files = [f"{path}/{file}" for file in listdir(path) if isfile(join(path, file))]
print(files)

for upload_file in files:
    google_file = drive.CreateFile({'parents': [{'id': drive_url}]}) # Create file
    google_file.SetContentFile(upload_file) # Set current file to 'SetContentFile'
    google_file['title'] = f"{photo_number}" # Change file title to photo number
    photo_number += 1 # Iterate number of photos
    google_file.Upload() # Upload file