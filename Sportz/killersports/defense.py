import killersportsteam
import requests
from datetime import date


class Defense(killersportsteam.KillerSportsTeam):
    def get_team_blocked_extra_points(self, week):
        return self._get_game_parameter("blocked extra points", week)

    def get_team_blocked_field_goals(self, week):
        return self._get_game_parameter("blocked field goals", week)

    def get_team_blocked_punts(self, week):
        return self._get_game_parameter("blocked punts", week)