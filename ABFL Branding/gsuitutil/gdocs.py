import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def gdocs(ID, onlybody=True):
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

    # The ID of a sample document.
    DOCUMENT_ID = ID

    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('gsuitutil/tokendocs.pickle'):
        with open('gsuitutil/tokendocs.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'gsuitutil/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('gsuitutil/tokendocs.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds, cache_discovery=False)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    
    if onlybody == False:
        return document
    else:
        retval = ''
        for i in document['body']['content']:
            para = i.get('paragraph')
            if para:
                retval += para['elements'][0]['textRun']['content']

        return [document.get('title'),retval]
                

if __name__ == '__main__':
    data = gdocs('1oSL2p7b_K_DMBw5nrFeGTrb96EWQdp8Sc3nrBV9Lits')
    print(data)