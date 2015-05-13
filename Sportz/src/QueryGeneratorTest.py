import MockResults
import unittest
import mock
import QueryGenerator

class InsertionSortTests(unittest.TestCase):
  def setUp(self):
    pass
  
  def tearDown(self):
    pass

  @mock.patch('QueryGenerator.urllib.urlopen')
  def test_GetTeamsConferenceAndDivision(self, mock_urlopen):
    page_request = mock.Mock()
    page_request.read.return_value = MockResults.TEAMS_CONFERENCE_AND_DIVISION
    mock_urlopen.return_value = page_request
    
    solution = {"Bears":{"conference":"NFC","division":"NFC North"},
                "Bengals":{"conference":"AFC","division":"AFC North"},
                "Bills":{"conference":"AFC","division":"AFC East"},
                "Broncos":{"conference":"AFC","division":"AFC West"},
                "Browns":{"conference":"AFC","division":"AFC North"},
                "Buccaneers":{"conference":"NFC","division":"NFC South"},
                "Cardinals":{"conference":"NFC","division":"NFC West"},
                "Chargers":{"conference":"AFC","division":"AFC West"},
                "Chiefs":{"conference":"AFC","division":"AFC West"},
                "Colts":{"conference":"AFC","division":"AFC South"},
                "Cowboys":{"conference":"NFC","division":"NFC East"},
                "Dolphins":{"conference":"AFC","division":"AFC East"},
                "Eagles":{"conference":"NFC","division":"NFC East"},
                "Falcons":{"conference":"NFC","division":"NFC South"},
                "Fortyniners":{"conference":"NFC","division":"NFC West"},
                "Giants":{"conference":"NFC","division":"NFC East"},
                "Jaguars":{"conference":"AFC","division":"AFC South"},
                "Jets":{"conference":"AFC","division":"AFC East"},
                "Lions":{"conference":"NFC","division":"NFC North"},
                "Packers":{"conference":"NFC","division":"NFC North"},
                "Panthers":{"conference":"NFC","division":"NFC South"},
                "Patriots":{"conference":"AFC","division":"AFC East"},
                "Raiders":{"conference":"AFC","division":"AFC West"},
                "Rams":{"conference":"NFC","division":"NFC West"},
                "Ravens":{"conference":"AFC","division":"AFC North"},
                "Redskins":{"conference":"NFC","division":"NFC East"},
                "Saints":{"conference":"NFC","division":"NFC South"},
                "Seahawks":{"conference":"NFC","division":"NFC West"},
                "Steelers":{"conference":"AFC","division":"AFC North"},
                "Texans":{"conference":"AFC","division":"AFC South"},
                "Titans":{"conference":"AFC","division":"AFC South"},
                "Vikings":{"conference":"NFC","division":"NFC North"}}
                
    actual = QueryGenerator.GetTeamConferenceDivision(2014)
    self.assertEqual(solution, actual)
  
  @mock.patch('QueryGenerator.urllib.urlopen')
  def test_GetTeamScheduleDatesAndOpponents(self, mock_urlopen):
    page_request = mock.Mock()
    page_request.read.return_value = MockResults.TEAMS_SCHEDULE_AND_OPPONENT
    mock_urlopen.return_value = page_request
    
    solution = {20140907:{"opponent":"Broncos"},
                20140915:{"opponent":"Eagles"},
                20140921:{"opponent":"Jaguars"},
                20140928:{"opponent":"Titans"},
                20141005:{"opponent":"Ravens"},
                20141009:{"opponent":"Texans"},
                20141019:{"opponent":"Bengals"},
                20141026:{"opponent":"Steelers"},
                20141103:{"opponent":"Giants"},
                20141116:{"opponent":"Patriots"},
                20141123:{"opponent":"Jaguars"},
                20141130:{"opponent":"Redskins"},
                20141207:{"opponent":"Browns"},
                20141214:{"opponent":"Texans"},
                20141221:{"opponent":"Cowboys"},
                20141228:{"opponent":"Titans"},
                20150104:{"opponent":"Bengals"},
                20150111:{"opponent":"Broncos"},
                20150118:{"opponent":"Patriots"}}
    
    actaul = QueryGenerator.GetTeamScheduleDatesOpponents("Colts", 2014)
    self.maxDiff = None
    self.assertEqual(solution, actaul)

if __name__ == '__main__':
  unittest.main()
