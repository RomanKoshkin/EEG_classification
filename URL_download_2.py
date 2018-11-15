# from apiclient import errors
# from apiclient import http

from googleapiclient import errors
from googleapiclient import http

# from apiclient.discovery import build
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import io

# from apiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaIoBaseDownload


class gdown(object):
    """
    to make it run:
    pip install --upgrade google-api-python-client
    """
    def __init__(self):
      super(gdown, self).__init__()
      # self.arg = arg

      # Setup the Drive v3 API
      self.SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
      self.store = file.Storage('credentials.json')
      self.creds = self.store.get()
      if not self.creds or self.creds.invalid:
          self.flow = client.flow_from_clientsecrets('client_secret_801600220437-idodf25dmrlebalv0fa2hj5thql3ltv9.apps.googleusercontent.com.json', SCOPES)
          self.creds = tools.run_flow(self.flow, self.store)
      self.service = build('drive', 'v3', http=self.creds.authorize(Http()))


    def print_file_metadata(self, file_id):
      """Print a file's metadata.

      Args:
        service: Drive API service instance.
        file_id: ID of the file to print metadata for.
      """
      try:
        file = self.service.files().get(fileId=file_id).execute()

        # print ('Title:', file['title'])
        print ('MIME type:', file['mimeType'])
      except errors.HttpError as error:
        print ('An error occurred:', error)

    def download_file(self, file_id):
      """Download a Drive file's content to the local filesystem.
      Args:
        service: Drive API Service instance.
        file_id: ID of the Drive file that will downloaded.
        local_fd: io.Base or file object, the stream that the Drive file's
            contents will be written to.
      """
      
      file = self.service.files().get(fileId=file_id).execute()
      file_name = file['name']
      print ('Name:', file_name)
      # print ('MIME type:', file['mimeType'])
      local_fd = open(file_name, "wb")
      request = self.service.files().get_media(fileId=file_id)
      media_request = http.MediaIoBaseDownload(local_fd, request)

      while True:
        try:
          download_progress, done = media_request.next_chunk()
        except errors.HttpError as error:
          print ('An error occurred:', error)
          return
        if download_progress:
          print ('Download Progress:', int(download_progress.progress() * 100))
        if done:
          print ('Download Complete')
          local_fd.close()
          return

    def ListGoogleDrive(self):
      # Call the Drive v3 API
      results = service.files().list(
          pageSize=10, fields="nextPageToken, files(id, name)").execute()
      items = results.get('files', [])
      if not items:
          print('No files found.')
      else:
          print('Files:')
          for item in items:
              print('{0} ({1})'.format(item['name'], item['id']))