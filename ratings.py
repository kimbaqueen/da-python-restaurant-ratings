"""Restaurant rating lister."""


# put your code here


def process_scores():
    scores_txt = open("scores.txt")

    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)
    
    return scores

def add_restaurant(scores):
    print("Please rate your favorite restuarant!")
    restaurant = input("Restaurant name: ")
    rating = int(input("Your Rating: "))

    scores[restaurant] = rating

    