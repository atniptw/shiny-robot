import MockResults
import QueryGenerator
from unittest import TestCase, mock, main

class InsertionSortTests(TestCase):
  def setUp(self):
    self.page_request = mock.MagicMock()
  
  def tearDown(self):
    pass

  @mock.patch('QueryGenerator.requests.get')
  def test_GetTeamsConferenceAndDivision(self, mock_request):
    self.page_request.text = MockResults.TEAMS_CONFERENCE_AND_DIVISION
    mock_request.return_value = self.page_request
    
    actual = QueryGenerator.GetTeamConferenceDivision(2014)    
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "team,conference,division@season=2014"})
    self.assertEqual(MockResults.TEAMS_CONFERENCE_AND_DIVISION_SOLUTION, actual)
  
  @mock.patch('QueryGenerator.requests.get')
  def test_GetTeamScheduleDatesAndOpponents(self, mock_request):
    self.page_request.text = MockResults.TEAMS_SCHEDULE_AND_OPPONENT
    mock_request.return_value = self.page_request
    
    actaul = QueryGenerator.GetTeamScheduleDatesOpponents("Colts", 2014)
    mock_request.assert_called_once_with("http://api.sportsdatabase.com/nfl/query.json", params={"output" : "json", "api_key" : "guest", "sdql" : "date,o:team@team=Colts and season=2014"})
    self.assertEqual(MockResults.TEAMS_SCHEDULE_AND_OPPONENT_SOLUTION, actaul)

if __name__ == '__main__':
  main()
