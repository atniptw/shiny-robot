import killersportsteam


class Offense(killersportsteam.KillerSportsTeam):
    def get_team_biggest_lead(self, week):
        return self._get_game_parameter("biggest lead", week)

    def get_team_completions(self, week):
        return self._get_game_parameter("completions", week)

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

    def get_team_fumbles(self, week):
        return self._get_game_parameter("fumbles", week)

    def get_team_fumbles_lost(self, week):
        return self._get_game_parameter("fumbles lost", week)

    def get_team_goal_to_go_attempted(self, week):
        return self._get_game_parameter("goal to go attempted", week)

    def get_team_goal_to_go_made(self, week):
        return self._get_game_parameter("goal to go made", week)

    def get_team_interceptions(self, week):
        return self._get_game_parameter("interceptions", week)
