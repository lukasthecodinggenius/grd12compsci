from random import randint
from statistics import mean

def main():

    scores = []
    for i in range(10):
        num = randint(1,100)
        scores.append(num)
    scores = sorted(scores)
    threshold = input('Threshold: ')

    stats = calculate_statistics(scores)
    passed = count_passed_students(scores, threshold)

    print(f'list of scores: {scores}')
    print(f'lowest score: {stats[0]}')
    print(f'highest score: {stats[1]}')
    print(f'average score: {stats[2]}')
    print(f'students that passed: {passed}')

def calculate_statistics(scores):
    list = []
    list.append(scores[0])
    list.append(scores[-1])
    list.append(mean(scores))
    return list

def count_passed_students(scores, threshold):
    count = 0
    for i in scores:
        if i >= int(threshold):
            count += 1
    return count
