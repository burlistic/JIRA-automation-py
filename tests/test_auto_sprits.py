from unittest.mock import Mock, patch
from src.auto_sprints import AutoSprint
import json

class TestDataParser:

    def test_getSprints_should_return_array_of_sprints(self):

        #arrange

        mock_session = Mock()
        mock_response = Mock()
        mock_response.json.return_value = {
            'total': 2,
            'values': [{'id': 1, 'name': 'Sprint 1'}, {'id': 2, 'name': 'Sprint 2'}]
        }
        mock_response.text = json.dumps(mock_response.json.return_value)
        mock_session.request.return_value = mock_response

        # Act
        auto_sprint = AutoSprint(session=mock_session)
        result = auto_sprint.getSprints()

        # Assert
        assert result == [[1, "Sprint 1"], [2, "Sprint 2"]]

        # mock_session.request.assert_called_once_with(
        #     "GET",
        #     "https://cohezion-team.atlassian.net/rest/agile/1.0/board/1/sprint",
        #     headers=auto_sprint._headers,
        #     auth=auto_sprint._auth,
        #     timeout=15
        # )
