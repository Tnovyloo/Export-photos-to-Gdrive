import pydrive
from os import listdir
from os.path import isfile, join
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
mypath = "C:/YourPath/YourPath"
photo_numer = 0

files = [f"{mypath}/{file}" for file in listdir(mypath) if isfile(join(mypath, file))]
print(files)


for upload_file in files:
    gfile = drive.CreateFile({'parents': [{'id': '1ciVEzXo6b-dKb99fDctGckLDKvyUjdYh'}]})
    gfile.SetContentFile(upload_file)
    gfile['title'] = f"{photo_numer}"
    photo_numer += 1
    gfile.Upload()