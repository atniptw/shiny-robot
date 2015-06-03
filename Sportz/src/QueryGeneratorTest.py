import QueryGenerator
from unittest import TestCase, mock, main

class QueryGeneratorTest(TestCase):
  def setUp(self):
    self.test_team = QueryGenerator.KillerSportsTeam("Colts", 2014)
    self.page_request = mock.MagicMock()
  
  def tearDown(self):
    pass

  @mock.patch('QueryGenerator.requests.get')
  def test_GetTeamConference(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'conference\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [\'AFC\']   ]}   ] });\n'
    mock_request.return_value = self.page_request
    
    actual = self.test_team.get_team_conference()    
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "conference@team=Colts and season=2014"})
    self.assertEqual("AFC", actual)
  
  @mock.patch('QueryGenerator.requests.get')
  def test_GetTeamDivision(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'division\'], "groups": [ {    "sdql": "team = Colts and season = 2014" ,   "columns" : [     [\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\',\'AFC South\']   ]}   ] });\n'
    mock_request.return_value = self.page_request
    
    actual = self.test_team.get_team_division()
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "division@team=Colts and season=2014"})
    self.assertEqual("AFC South", actual)
  
  @mock.patch('QueryGenerator.requests.get')
  def test_GetTeamOpponent(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'o:team\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [\'Broncos\']   ]}   ] });\n'
    mock_request.return_value = self.page_request
    
    actual = self.test_team.get_team_opponent(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "o:team@team=Colts and season=2014 and week=1"})
    self.assertEqual("Broncos", actual)
    
  @mock.patch('QueryGenerator.requests.get')
  def test_GetTeamBiggestLead(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\' biggest lead\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_biggest_lead(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "biggest lead@team=Colts and season=2014 and week=1"})
    self.assertEqual(0, actual)

  @mock.patch('QueryGenerator.requests.get')
  def test_GetTeamBlockedExtraPoints(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'blocked extra points\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_blocked_extra_points(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "blocked extra points@team=Colts and season=2014 and week=1"})
    self.assertEqual(0, actual)

  @mock.patch('QueryGenerator.requests.get')
  def test_GetTeamBlockedPunts(self, mock_request):
    self.page_request.text = 'json_callback({  "headers": [\'blocked punts\'], "groups": [ {    "sdql": "team = Colts and season = 2014 and week = 1" ,   "columns" : [     [0]   ]}   ] });\n'
    mock_request.return_value = self.page_request

    actual = self.test_team.get_team_blocked_punts(1)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "blocked punts@team=Colts and season=2014 and week=1"})
    self.assertEqual(0, actual)
    
if __name__ == '__main__':
  main()
