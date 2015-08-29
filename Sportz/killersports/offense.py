import killersportsteam
import requests
from datetime import date


class Offense(killersportsteam.KillerSportsTeam):
    def get_team_biggest_lead(self, week):
        return self._get_game_parameter("biggest lead", week)

    def get_team_game_date(self, week):
        game_date = str(self._get_game_parameter("date", week))
        return date(int(game_date[:4]), int(game_date[4:6]), int(game_date[6:8]))

    def get_team_conference(self):
        query = "conference@team={0} and season={1}".format(self.team, self.season)
        payload = {"output": "json", "api_key": "guest", "sdql": query}
        result = requests.get(killersportsteam.BASE_URL, params=payload)
        jsonResult = self._format_string_to_JSON(result.text)

        return jsonResult['groups'][0]['columns'][0][0]

    def get_team_completions(self, week):
        return self._get_game_parameter("completions", week)

    def get_team_division(self):
        query = "division@team={0} and season={1}".format(self.team, self.season)
        payload = {"output": "json", "api_key": "guest", "sdql": query}
        result = requests.get(killersportsteam.BASE_URL, params=payload)
        jsonResult = self._format_string_to_JSON(result.text)

        return jsonResult['groups'][0]['columns'][0][0]

    def get_team_drives(self, week):
        return self._get_game_parameter("drives", week)

    def get_team_field_goals(self, week):
        return self._get_game_parameter("field goals", week)

    def get_team_field_goals_attempted(self, week):
        return self._get_game_parameter("field goals attempted", week)

    def get_team_first_downs(self, week):
        return self._get_game_parameter("first downs", week)

    def get_team_fourth_downs_attempted(self, week):
        return self._get_game_parameter("fourth downs attempted", week)

    def get_team_fourth_downs_made(self, week):
        return self._get_game_parameter("fourth downs made", week)

    def get_team_fumble_return_touchdowns(self, week):
        return self._get_game_parameter("fumble return touchdowns", week)

    def get_team_fumbles(self, week):
        return self._get_game_parameter("fumbles", week)

    def get_team_fumbles_lost(self, week):
        return self._get_game_parameter("fumbles lost", week)

    def get_team_goal_to_go_attempted(self, week):
        return self._get_game_parameter("goal to go attempted", week)

    def get_team_goal_to_go_made(self, week):
        return self._get_game_parameter("goal to go made", week)

    def get_team_interception_return_yards(self, week):
        return self._get_game_parameter("interception return yards", week)

    def get_team_interception_returns(self, week):
        return self._get_game_parameter("interception returns", week)

    def get_team_interception_touchdowns(self, week):
        return self._get_game_parameter("interception touchdowns", week)

    def get_team_interceptions(self, week):
        return self._get_game_parameter("interceptions", week)

    def get_team_opponent(self, week):
        return self._get_game_parameter("o:team", week)
