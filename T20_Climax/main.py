import random, pdb

class Batsmen():
    scoring_weightage = {
        "Virat Kohli" : {"runs": [0, 1, 2, 3, 4, 5, 6, "OUT"], "weightage": (5, 30, 25, 10, 15, 1, 9, 5)},
        "MS Dhoni" : {"runs": [0, 1, 2, 3, 4, 5, 6, "OUT"], "weightage": (10, 40, 20, 5, 10, 1, 4, 10)},
        "Jasprit Bumrah" : {"runs": [0, 1, 2, 3, 4, 5, 6, "OUT"], "weightage": (20, 30, 15, 5, 5, 1, 4, 20)},
        "Bhuvi Kumar" : {"runs": [0, 1, 2, 3, 4, 5, 6, "OUT"], "weightage": (30, 25, 5, 0, 5, 1, 4, 30)}
    }

class Bowler():
    wicket_taking_weightage = {
        "Murali Muttaiah": {"bowler_capab": [0, 1, 2, 4, 6, "OUT"], "weightage": (20, 30, 20, 10, 5, 20)},
        "Pollock": {"bowler_capab": [0, 1, 2, 4, 6, "OUT"], "weightage": (15, 20, 30, 15, 5, 10)}
    }

class Match(Batsmen, Bowler):

    def __init__(self, score_req, total_balls):
        self.score_req = score_req
        self.total_balls = total_balls
        self.batting_order = list(Batsmen.scoring_weightage.keys())
        self.bowling_order = list(Bowler.wicket_taking_weightage.keys())
        self.on_strike_batsmen = self.batting_order[0]
        self.off_strike_batsmen = self.batting_order[1]
        self.opening_bowler = self.bowling_order[0]
        self.scorecard = {"Batting": {}, "Bowling": {}}

    def update_scorecard(self, runs_scored):
        self.score_req -= runs_scored

        if self.scorecard["Batting"].get(self.on_strike_batsmen) is None:
            self.scorecard["Batting"][self.on_strike_batsmen] = {"Runs": 0, "Balls_Played": 0}

        self.scorecard["Batting"][self.on_strike_batsmen]["Runs"] += runs_scored
        self.scorecard["Batting"][self.on_strike_batsmen]["Balls_Played"] += 1


        if self.scorecard["Bowling"].get(self.opening_bowler) is None:
            self.scorecard["Bowling"][self.opening_bowler] = {"Overs": 1, "Runs_Given": 0}

        self.scorecard["Bowling"][self.opening_bowler]["Runs_Given"] += runs_scored

    def print_scorecard(self):
        print(f"{' '*5}MATCH SCOREBOARD\n")
        team_score = 0
        print(f"BATSMAN{' '*18}RUNS{' '*5}STRIKE-RATE")
        for player in self.scorecard['Batting']:
            team_score += self.scorecard['Batting'][player]['Runs']
            player_strike_rate = round(self.scorecard['Batting'][player]['Runs']/self.scorecard['Batting'][player]['Balls_Played'], 2) * 100
            print(f"{player}\t\t\t{self.scorecard['Batting'][player]['Runs']}({self.scorecard['Batting'][player]['Balls_Played']})\t\t{player_strike_rate}")
        print(f"\nLENG: {team_score}-{11 - len(self.batting_order)}\n")

        print(f"BOWLER{' '*18}OVERS{' '*3}RUNS{' '*3}ECONOMY-RATE")
        for player in self.scorecard['Bowling']:
            player_economy_rate = round(self.scorecard['Bowling'][player]['Runs_Given']/(self.scorecard['Bowling'][player]['Overs']*6), 2)
            print(f"{player}\t\t{self.scorecard['Bowling'][player]['Overs']}\t{self.scorecard['Bowling'][player]['Runs_Given']}\t{player_economy_rate}")



    def update_rem_balls(self):
        self.total_balls -= 1

    def match_update(self):
        if self.score_req <= 0:
            return "Completed"
        elif self.total_balls == 0:
            return "Completed"
        elif len(self.batting_order) < 2:
            return "Completed"

        return "Still Playing"

    def play(self):
        runs_scored = random.choices(Batsmen.scoring_weightage[self.on_strike_batsmen]["runs"], weights=Batsmen.scoring_weightage[self.on_strike_batsmen]["weightage"], k=1)[-1]
        runs_given = random.choices(Bowler.wicket_taking_weightage[self.opening_bowler]["bowler_capab"], weights=Bowler.wicket_taking_weightage[self.opening_bowler]["weightage"], k=1)[-1]

        if not any([runs_scored == "OUT", runs_given == "OUT"]):
            runs_scored = min(runs_scored, runs_given)

        print(f"Bowler coming from the Pavilion End {self.opening_bowler}")
        # After Ball Stats.
        # Evaluate the runs scored of the ball.
        if not any([runs_scored == 0, runs_scored == "OUT"]):
            self.update_scorecard(runs_scored)
            print(f"{self.on_strike_batsmen} Scored {runs_scored} runs")
        elif runs_scored == 0:
            print(f"Dot BALL for {self.on_strike_batsmen}")
        elif runs_scored == "OUT":
            print(f"OUT!! --> {self.on_strike_batsmen}.")

        self.update_rem_balls()

        # Reverse the strike,
        if runs_scored in [1,3,5]:
            tmp = self.on_strike_batsmen
            self.on_strike_batsmen = self.off_strike_batsmen
            self.off_strike_batsmen = tmp
            print(f"{self.on_strike_batsmen} on Strike Now!")

        # New Batsman takes the strike, whenever batsman gest OUT
        elif runs_scored in ["OUT"]:
            runs_scored = 0
            self.update_scorecard(runs_scored)
            self.batting_order.remove(self.on_strike_batsmen)
            if len(self.batting_order) > 1:
                self.on_strike_batsmen = self.batting_order[1]
                self.off_strike_batsmen = self.batting_order[0]
                print(f"{self.on_strike_batsmen} on Strike Now!")

        # Indeed It is
        if self.total_balls%6 == 0:
            print(f"\n Kit-Kat Break Zaroori hota hain!!\n")
            self.scorecard["Bowling"][self.opening_bowler]["Overs"] += 1
            self.print_scorecard()
            curr_bowler_index = self.bowling_order.index(self.opening_bowler)
            next_bowler_index = curr_bowler_index+1 if curr_bowler_index < len(self.bowling_order)-1  else 0
            self.opening_bowler = self.bowling_order[next_bowler_index]
            print(f"\nBowler coming from the Pavilion End {self.opening_bowler}")


        # Check the Match Status.
        match_update = self.match_update()
        if not "Completed" in match_update:
            print(f"\tRequired Score: {self.score_req} Runs in {self.total_balls} Balls")
        else:
            self.print_scorecard()
            if self.score_req <= 0:
                # Batting team won
                print(f"\tLengaburu won by {len(self.batting_order)} wickets.")
            else:
                # Bowling team won
                print(f"\tEnchai won by {self.score_req} Runs.")

        return match_update


if __name__ == '__main__':
    # Match can be custom-set
    match = Match(22, 12)
    match_output = ''
    while match_output != "Completed":
        match_output = match.play()
