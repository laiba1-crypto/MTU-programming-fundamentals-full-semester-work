# Author: laiba asif
# Purpose: challenge

team_name = input('enter team name:')
number_of_goals = int(input(f'how many goals were scored by {team_name}:'))
number_of_points = int(input(f'how many points were scored by{team_name}:'))

total_points = number_of_goals*3 + number_of_points

print(f'{team_name} scored {number_of_goals} goals and {number_of_points} points {total_points} points in total')