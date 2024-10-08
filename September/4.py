def main():
    
    
    score1, score2, score3 = float(input('Score 1: ')), float(input('Score 2: ')), float(input('Score 3: '))
    
    average = (score1 + score2 + score3) / 3
    
    if average < 0 or average > 100:
        print('scores invalid')
    elif average >= 60:
        print(f'{average:.01f} is a passing average.')
    else:    
        print(f'{average:.01f} is a failing average.')
main()
