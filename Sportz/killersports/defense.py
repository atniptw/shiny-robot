import killersportsteam


class Defense(killersportsteam.KillerSportsTeam):
    def get_team_blocked_extra_points(self, week):
        return self._get_game_parameter("blocked extra points", week)

    def get_team_blocked_field_goals(self, week):
        return self._get_game_parameter("blocked field goals", week)

    def get_team_blocked_punts(self, week):
        return self._get_game_parameter("blocked punts", week)

    def get_team_fumble_return_touchdowns(self, week):
        return self._get_game_parameter("fumble return touchdowns", week)

    def get_team_interception_return_yards(self, week):
        return self._get_game_parameter("interception return yards", week)

    def get_team_interception_returns(self, week):
        return self._get_game_parameter("interception returns", week)

    def get_team_interception_touchdowns(self, week):
        return self._get_game_parameter("interception touchdowns", week)