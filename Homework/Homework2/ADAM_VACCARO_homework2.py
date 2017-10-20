# ADAM_VACCARO_homework2.py
# INF 510 - Homework 2
# Adam Vaccaro
# Purpose: (1) Load in csv files, (2) create classes, (3) perform compuations and return answer.

### import packages
import csv


### define Game, PredictorWeek, and Season classes:
## Terminology Guide:
#gweek = game week - refers to the week the game takes place in (weeks 1-17)
#pweek = predictor week - refers to the week when a prediction was made (weeks 1-4)


class Game:
    # contains information for a particular game (home team name/probability, away team name/probability, and game week number)
    def __init__(self,home_team,home_prob,away_team,away_prob,gweek_num):
        self.home_team = str(home_team) #home team name
        self.home_prob = float(home_prob) #home team probability
        self.away_team = str(away_team) #away team name
        self.away_prob = float(away_prob) #away team probability
        self.gweek_num = int(gweek_num) #game week number
 
class PredictorWeek:     
    # contains all games corresponding to a given predictor week (in .games attribute)
    def __init__(self,pweek): #,list_of_games,game_week_num):
        self.games = {} #create empty dictionary to be filled later
        self.pweek = pweek #predictor week string
        self.pweek_num = int(pweek[4]) #predictor week number

class Season:
    # Season.pweeks attribute contains a dictionary of PredictorWeek objects 
    # Season.get_answer() finds game with biggest change in probability compared to week 1 baseline and prints answer
    
    def __init__(self): #pweeks = predictor weeks
        self.pweeks = {} #create empty dictionary to be filled later

    def get_answer(season):
        biggest_change = 0
        for x in range(1,len(season.pweeks)): #for x = 1:3:
            pweek_num = x +1 #convert x to predictor week number by adding 1
            pweek = 'week' + str(pweek_num) #set predictor week string dynamically
            for key in season.pweeks[pweek].games:
                week1_game = season.pweeks['week1'].games[key] #week 1 prediction for current game in iteration
                week1_home_prob = week1_game.home_prob
                week1_away_prob = week1_game.away_prob
                weekx_game = season.pweeks[pweek].games[key] #week x prediction for current game in iteration
                weekx_home_prob = weekx_game.home_prob
                weekx_away_prob = weekx_game.away_prob
                # Find favorite team from week 1:
                if week1_home_prob > week1_away_prob: #if home team is favorite from week 1
                    change = abs(weekx_home_prob - week1_home_prob) #calculate change w.r.t. home team probability
                elif week1_away_prob > week1_home_prob: #if away team is favorite from week 1
                    change = abs(weekx_away_prob - week1_away_prob) #calculate change w.r.t. away team probability
                if change > biggest_change: #if change is larger than previous biggest change
                    biggest_change = change #store change as biggest change
                    # store game information (for use in output):
                    home_team = weekx_game.home_team  
                    weekx_home_prob_big = weekx_game.home_prob
                    week1_home_prob_big = week1_game.home_prob
                    away_team = weekx_game.away_team
                    weekx_away_prob_big = weekx_game.away_prob
                    week1_away_prob_big = week1_game.away_prob
                    gweek_num = weekx_game.gweek_num
        # prepare output text:
        line1 = 'Week 1 baseline: \n'
        line2 = home_team + ' ' + str(week1_home_prob_big) + '% vs. ' + away_team + ' ' + str(week1_away_prob_big) + '% (Week ' + str(gweek_num) + ') \n' 
        line3 = 'Week ' + str(pweek_num) + ' prediction: \n'
        line4 = home_team + ' ' + str(weekx_home_prob_big) + '% vs. ' + away_team + ' ' + str(weekx_away_prob_big) + '% (Week ' + str(gweek_num) + ') \n' 
        outputText = line1 + line2 + line3 + line4 #concatenate output text lines
        print(outputText) #print output


### define functionality for call from command line (load in .csv files, store data in objects, calculate biggest change):
def main():
    # prepare to load weekly data:
    pweeks = ['week1','week2','week3','week4'] #names for each predictor week
    season = Season() #create empty Season object
    for pweek in pweeks: #for each predictor week
        path = "hw2_probabilities_FIXED/" + pweek #path to predictor week folders
        pweek_num = int(pweek[4]) #number of the predictor week
        season.pweeks[pweek] = PredictorWeek(pweek) #create PredictorWeek object and store within Season object as dictionary value in attribute pweeks
        for i in range(pweek_num-1,17): # for each game week
            gweek_num = int(i + 1) #convert index to game number
            file = 'week_' + str(gweek_num) + '_probabilities.csv' #select game week file
            with open(path + '/' + file) as fid: # open csv file
                reader = csv.DictReader(fid) # open csv as dict
                # extract data from csv:
                for row in reader:
                    home_team = row['home team name']
                    home_prob = row['home team probability']
                    away_team = row['away team name']
                    away_prob = row['away team probability']
                    game = Game(home_team,home_prob,away_team,away_prob,gweek_num) #store data in Game object
                    game_key = (home_team,away_team,gweek_num) #define 3-tuple as unique key for each game
                    season.pweeks[pweek].games[game_key] = game #store game object inside games attribute of PredictorWeek class object
    season.get_answer()


### enable call-from-command-line functionality:
if __name__ == '__main__':
    main()


