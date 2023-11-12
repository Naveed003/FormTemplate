from googleapiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def form(variables, name):
    SCOPES = ["https://www.googleapis.com/auth/forms.body"]
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # if not creds or creds.invalid:

    #     flow = client.flow_from_clientsecrets('credentials.json', SCOPES)

    #     creds = tools.run_flow(flow, store)

    form_service = discovery.build('forms', 'v1', credentials=creds, discoveryServiceUrl=DISCOVERY_DOC,
                                   static_discovery=False)

    # Request body for creating a form
    NEW_FORM = {
        "info": {
            "title": name,
        }
    }
    result = form_service.forms().create(body=NEW_FORM).execute()


    for i in variables[::-1]:

        NEW_QUESTION = {
            "requests": [{

                "createItem": {
                    "item":
                        {
                            "title": f"{i}",
                            "questionItem": {
                                "question": {
                                    "required": True,
                                    "textQuestion": {
                                        'paragraph': False
                                    }
                                }
                            },
                        },

                    "location": {
                        "index": 0
                    }
                },

            }]
        }
        question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()
    NEW_QUESTION = {
        "requests": [{

            "createItem": {
                "item":
                    {
                        "title": f"Contract ID",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "textQuestion": {
                                    'paragraph': False
                                }
                            }
                        },
                    },

                "location": {
                    "index": 0
                }
            },

        }]
    }
    question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

    get_result = form_service.forms().get(formId=result["formId"]).execute()
    return [get_result['formId'],get_result['responderUri']]
