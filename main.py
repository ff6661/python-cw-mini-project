# write your code here

def padel_court_cost(court_type):
    if court_type == 'indoors':
        return 30
    elif court_type == 'outdoors':
        return 20

def racket_cost(racket_brand):
    if racket_brand == 'nox':
        return 140
    elif racket_brand == 'siux':
        return 200
def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 5:
        return 5

def padel_game_cost():
    court_type = input("enter the court type: ")
    racket_brand = input("enter racket brand: ")
    ball_boxes = int(input("how many ball boxes do you want? "))
    total_cost = padel_court_cost(court_type) + racket_cost(racket_brand) + padel_balls_cost(ball_boxes)
    print(total_cost)


padel_game_cost()

