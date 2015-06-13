import KillerSportsTeam
from unittest import TestCase, mock, main
from datetime import date

class KillerSportsTeamTest(TestCase):
  def setUp(self):
    self.test_team = KillerSportsTeam.KillerSportsTeam("Colts", 2014)
    self.page_request = mock.MagicMock()
  
  def tearDown(self):
    pass

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamConference(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'conference\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [\'AFC\']   ]}   ] });\n'
    mock_request.return_value = self.page_request
    
    actual = self.test_team.get_team_conference()    
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "conference@team=Colts and season=2014"})
    self.assertEqual("AFC", actual)
  
  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamDivision(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'division\'], "groups": [ {    "sdql": "team = Colts and season = 2014" ,   "columns" : [     [\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\']   ]}   ] });\n'
    mock_request.return_value = self.page_request
    
    actual = self.test_team.get_team_division()
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "division@team=Colts and season=2014"})
    self.assertEqual("AFC South", actual)
  
  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamOpponent(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'o:team\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [\'Broncos\']   ]}   ] });\n'
    mock_request.return_value = self.page_request
    
    actual = self.test_team.get_team_opponent(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "o:team@team=Colts and season=2014 and week=1"})
    self.assertEqual("Broncos", actual)
    
  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamBiggestLead(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\' biggest lead\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_biggest_lead(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "biggest lead@team=Colts and season=2014 and week=1"})
    self.assertEqual(0, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamBlockedExtraPoints(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'blocked extra points\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_blocked_extra_points(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "blocked extra points@team=Colts and season=2014 and week=1"})
    self.assertEqual(0, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamBlockedFieldGoals(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'blocked field goals\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_blocked_field_goals(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "blocked field goals@team=Colts and season=2014 and week=1"})
    self.assertEqual(0, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamBlockedPunts(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'blocked punts\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_blocked_punts(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "blocked punts@team=Colts and season=2014 and week=1"})
    self.assertEqual(0, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamCompletions(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'completions\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [35]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_completions(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "completions@team=Colts and season=2014 and week=1"})
    self.assertEqual(35, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamDrives(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'drives\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [12]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_drives(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "drives@team=Colts and season=2014 and week=1"})
    self.assertEqual(12, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamFieldGoals(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'field goals\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [1]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_field_goals(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "field goals@team=Colts and season=2014 and week=1"})
    self.assertEqual(1, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamFieldGoalsAttempted(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'field goals\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [1]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_field_goals_attempted(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "field goals attempted@team=Colts and season=2014 and week=1"})
    self.assertEqual(1, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamFirstDowns(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'first downs\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [24]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_first_downs(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "first downs@team=Colts and season=2014 and week=1"})
    self.assertEqual(24, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamFourthDownsAttempted(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'fourth downs attempted\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [4]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_fourth_downs_attempted(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "fourth downs attempted@team=Colts and season=2014 and week=1"})
    self.assertEqual(4, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamFourthDownsMade(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'fourth downs made\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [2]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_fourth_downs_made(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "fourth downs made@team=Colts and season=2014 and week=1"})
    self.assertEqual(2, actual)

  @mock.patch('KillerSportsTeam.requests.get')
  def test_GetTeamGameDate(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'date\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [20140907]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_game_date(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "date@team=Colts and season=2014 and week=1"})
    self.assertEqual(date(2014, 9, 7), actual)
    
if __name__ == '__main__':
  main()
