import data


def get_move(move):
    return [move[0], move[1:]]

def rotate(code):
    arrow = 50
    count = 0
    for item in code:
        move = get_move(item)
        if move[0] == "L":
            arrow = (arrow - int(move[1]) + 100) % 100
            if arrow == 0:
                count += 1
        else:
            arrow = (arrow + int(move[1])) % 100
            if arrow == 0:
                count += 1
    return count

print(rotate(data.code))