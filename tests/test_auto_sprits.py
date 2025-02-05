from unittest.mock import Mock, patch
from src.auto_sprints import AutoSprint
import json

class TestDataParser:

    def test_get_sprints_should_return_array_of_sprints(self):
        """ Test get_sprints"""

        #arrange

        mock_session = Mock()
        mock_response = Mock()
        mock_response.json.return_value = {
            'total': 2,
            'values': [{'id': 1, 'name': 'Sprint 1', 'state': 'active'}, {'id': 2, 'name': 'Sprint 2', 'state': 'future'}]
        }
        mock_response.text = json.dumps(mock_response.json.return_value)
        mock_session.request.return_value = mock_response

        # Act
        auto_sprint = AutoSprint(session=mock_session)
        result = auto_sprint.get_sprints()

        # Assert
        assert result == [[1, "Sprint 1", "active"], [2, "Sprint 2", "future"]]

        # mock_session.request.assert_called_once_with(
        #     "GET",
        #     "https://cohezion-team.atlassian.net/rest/agile/1.0/board/1/sprint",
        #     headers=auto_sprint._headers,
        #     auth=auto_sprint._auth,
        #     timeout=15
        # )

    def test_check_sprints_valid(self):
        """ Test check_sprints - wants to validate there is one active sprint and two future, 
        if this isn't the case, then this can be corrected before proceeding """

        #arrange

        test_input = [[1, "Sprint 1", "active"], [2, "Sprint 2", "future"], [3, "Sprint 3", "future"] ]

        #todo - move to a test set up method
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

        # Act
        result = auto_sprint.check_sprints(test_input)

        # Assert
        assert result == [["number of sprints", 3], ["number of active sprints", 1], ["active sprint ID", 1] ]

# Create a new future sprint

# Transfer issues from open sprint to the next

# Close the old sprint

# Start the new sprint
