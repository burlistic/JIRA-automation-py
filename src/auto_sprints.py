# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

class AutoSprint:
    
    def __init__(self, session=None):
        

        load_dotenv()

        self._baseurl = "https://cohezion-team.atlassian.net"
        self._boardId = 1
        self._email = os.getenv('JIRA_EMAIL')
        self._api_token = os.getenv('JIRA_API_TOKEN')
        self._auth = HTTPBasicAuth(self._email, self._api_token)
        self._headers = {
            "Accept": "application/json"
        }
        self._session = session or requests.Session()

    def get_sprints(self):
        """Returns the sprints for the given JIRA project and board"""

        url = f"{self._baseurl}/rest/agile/1.0/board/{self._boardId}/sprint"

        response = self._session.request(
          "GET",
          url,
          headers=self._headers,
          auth=self._auth,
          timeout=15
        )

        getBoardsResponse = response.json()

        openSprints = getBoardsResponse['total']
        values = getBoardsResponse['values']

        #Foreach
        firstSprint = values[0]
        firstSprintId = firstSprint['id']
        firstSprintName = firstSprint['name']

        result = []

        for x in values:
          result.append([x['id'] , x['name']])

        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

        return result
   
# Check there is one active sprint and two future

# Create a new future sprint

# Transfer issues from open sprint to the next

# Close the old sprint

# Start the new sprint