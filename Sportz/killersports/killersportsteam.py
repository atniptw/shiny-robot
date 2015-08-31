from datetime import date
import requests

BASE_URL = "http://api.sportsdatabase.com/nfl/query.json"


class KillerSportsTeam:
    def __init__(self, team, season):
        self.team = team
        self.season = season

    def get_team_game_date(self, week):
        game_date = str(self._get_game_parameter("date", week))
        return date(int(game_date[:4]), int(game_date[4:6]), int(game_date[6:8]))

    def get_team_conference(self):
        query = "conference@team={0} and season={1}".format(self.team, self.season)
        payload = {"output": "json", "api_key": "guest", "sdql": query}
        result = requests.get(BASE_URL, params=payload)
        jsonResult = self._format_string_to_JSON(result.text)

        return jsonResult['groups'][0]['columns'][0][0]

    def get_team_division(self):
        query = "division@team={0} and season={1}".format(self.team, self.season)
        payload = {"output": "json", "api_key": "guest", "sdql": query}
        result = requests.get(BASE_URL, params=payload)
        jsonResult = self._format_string_to_JSON(result.text)

        return jsonResult['groups'][0]['columns'][0][0]

    def get_team_opponent(self, week):
        return self._get_game_parameter("o:team", week)

    def _get_game_parameter(self, parameter, week):
        query = "{0}@team={1} and season={2} and week={3}".format(parameter, self.team, self.season, week)
        payload = {"output": "json", "api_key": "guest", "sdql": query}
        result = requests.get(BASE_URL, params=payload)
        jsonresult = self._format_string_to_JSON(result.text)

        return jsonresult['groups'][0]['columns'][0][0]

    def _format_string_to_JSON(self, result):
        result = result.replace('json_callback(', '')
        result = result.replace(');\n', '')
        result = result.replace('\t', '')
        return eval(result)
