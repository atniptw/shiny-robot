from urllib import quote_plus, urlopen

BASE_URL = "http://api.sportsdatabase.com/nfl/query.json?output=json&api_key=guest&sdql={}"

def GetTeamConferenceDivision(season):
  url = BASE_URL.format(quote_plus("team, conference, division@season={}".format(season)))
  result = _FormatStringToJSON(urlopen(url).read())

  teams = {}
  data = result['groups'][0]['columns']

  for i in range(len(data[0])):
    teams[data[0][i]] = {"conference": data[1][i], "division": data[2][i]}

  return teams

def GetTeamScheduleDatesOpponents(team, season):
  url = BASE_URL.format(quote_plus("date, o:team@team={0} and season={1}".format(team, season)))
  result = _FormatStringToJSON(urlopen(url).read())

  games = {}
  data = result['groups'][0]['columns']
  
  for i in range(len(data[0])):
    games[data[0][i]] = {"opponent": data[1][i]}
    
  return games

def _FormatStringToJSON(result):
  result = result.replace('json_callback(', '')
  result = result.replace(');\n', '')
  result = result.replace('\t', '')
  return eval(result)
  