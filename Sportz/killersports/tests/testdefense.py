import defense
from unittest import TestCase, mock, main
from datetime import date


class TestDefense(TestCase):
    def setUp(self):
        self.test_team = defense.Defense("Colts", 2014)
        self.page_request = mock.MagicMock()

    def tearDown(self):
        pass

    @mock.patch('offense.requests.get')
    def test_GetTeamBlockedExtraPoints(self, mock_request):
        self.page_request.text = 'json_callback({  "headers": [\'blocked extra points\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
        mock_request.return_value = self.page_request

        actual = self.test_team.get_team_blocked_extra_points(1)
        mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json",
                                             params={"output": "json", "api_key": "guest",
                                                     "sdql": "blocked extra points@team=Colts and season=2014 and week=1"})
        self.assertEqual(0, actual)

    @mock.patch('offense.requests.get')
    def test_GetTeamBlockedFieldGoals(self, mock_request):
        self.page_request.text = 'json_callback({  "headers": [\'blocked field goals\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
        mock_request.return_value = self.page_request

        actual = self.test_team.get_team_blocked_field_goals(1)
        mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json",
                                             params={"output": "json", "api_key": "guest",
                                                     "sdql": "blocked field goals@team=Colts and season=2014 and week=1"})
        self.assertEqual(0, actual)

    @mock.patch('offense.requests.get')
    def test_GetTeamBlockedPunts(self, mock_request):
        self.page_request.text = 'json_callback({  "headers": [\'blocked punts\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
        mock_request.return_value = self.page_request

        actual = self.test_team.get_team_blocked_punts(1)
        mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json",
                                             params={"output": "json", "api_key": "guest",
                                                     "sdql": "blocked punts@team=Colts and season=2014 and week=1"})
        self.assertEqual(0, actual)

if __name__ == '__main__':
    main()
