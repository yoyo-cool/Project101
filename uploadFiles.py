import dropbox
import os
from dropbox.files import WriteMode

class TransferData():
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self, file_to, file_from):
        dbx=dropbox.Dropbox(self.access_token)
        
        for root, dirs, files in os.walk("c:/Users/sachi/OneDrive/Desktop/Whitehat/photos"):
            for name in files:
                    file_path = os.path.join(root, name)
                    relative_path = os.path.relpath(file_path, file_from)
                    dropbox_path = os.path.join(file_to, relative_path)
                    with open(file_path,"rb") as f:
                        file_to="."
                        dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    i_transferDta = TransferData('sl.BeahvVTL0JltSSRZxGZ082mQCdabmfZCzz2WaMHGsrRbVduO3HX6dQfXml3QeaUkL4liweSSYG95gKkNqorq7BXcej9J12AaPOhnOgwRoBz1d0agdmDBuBW0O1zx70ab2JFbBQY')
    i_transferDta.upload_file()

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")  

    i_transferDta.upload_file(file_from,file_to)
    print("file has been moved !!!")


main()