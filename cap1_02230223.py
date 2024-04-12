###############################
# Rinchen Lhamo
# 1 ICE
# 02230223
###############################
# References
#
# Links that i have referred while coding
# https://youtu.be/Qcefu1jVPds?si=nJtdfnriyV_JrMP7
# https://youtu.be/fn68QNcatfo?si=yqdl_z2T5MewxIuD
# https://youtu.be/55tcf9AA9hQ?si=7CfyHd6W91lsGcAZ
###############################
# Solution
# Solution score:
# 49483
##############################
# Read the input_3_cap1.txt file
def read_input():
    with open('CSF101_CAP/input_3_cap1.txt', 'r') as f: 
        file = f.readline()
        input_value = []
        while file:
            input_value.append((file.split()[0], file.split()[1]))
            file = f.readline()
        return input_value   

# To calculate the score
def calculate_score(input_value):
    scores = {'A': 1,'B': 2,'C' : 3} #Store keys and valuse in dictionary
    outcome = {'X' : 0,'Y' : 3,'Z' : 6} 
    total_score = 0 
# Determine player's choice based on opponent's move and desired product
    for s in input_value:  
        opponent_choice, product = s
     
        if opponent_choice == 'A' and product == 'X':
            player_move = 'C'# Player should play 'C' to lose against 'A'
        elif opponent_choice == 'A' and product == 'Y':
            player_move = 'A'# Player should play 'A' to draw against 'A'
        elif opponent_choice == 'A' and product == 'Z':
            player_move = 'B'# Player should play 'B' to win against 'A'
        elif opponent_choice == 'B' and product == 'X':
            player_move = 'A'# Player should play 'A' to lose against 'B'
        elif opponent_choice == 'B' and product == 'Y':
            player_move = 'B'# Player should play 'B' to draw against 'B'
        elif opponent_choice == 'B' and product == 'Z':
            player_move = 'C'# Player should play 'C' to win against 'B'
        elif opponent_choice == 'C' and product == 'X':
            player_move = 'B'# Player should play 'B' to lose against 'C'
        elif opponent_choice == 'C' and product == 'Y':
            player_move = 'C'# Player should play 'C' to draw against 'C'
        elif opponent_choice == 'C' and product == 'Z':
            player_move = 'A' # Player should play 'A' to win against 'C'
        else:
            print('invalid input')
        
        total_score += scores[player_move] + outcome[product]
    return total_score

# call the function
input_value = read_input()
print(f"The total score is: {calculate_score(input_value)}")