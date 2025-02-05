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
            result.append([x['id'] , x['name'], x['state']])

        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

        return result
    
    def check_sprints(self, sprints_input : list[int, str]):

        # todo - consider Python lamda?

        # test_input = [[1, "Sprint 1", "active"], [2, "Sprint 2", "future"], [3, "Sprint 3", "future"] ]

        # check number of sprints
        number_of_sprints = len(sprints_input)

        # check number of active sprints and confirm active sprint ID 
        active_sprints = 0
        active_sprint_id = 0

        for x in sprints_input:
            if x[2] == "active":
              active_sprints = active_sprints + 1 #todo - find a cleaner way to iterate
              active_sprint_id = x[0]


        # to do - Throw exception if more than one active sprints
        
        result = [["number of sprints", number_of_sprints], ["number of active sprints", active_sprints], ["active sprint ID", active_sprint_id] ]

        return result 