def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = [f'Hello, my name is {name}.' for name in names]
    return badges

def assign_rooms(names):
    room = 1
    list = []
    for name in names:
        list.append(f"Hello, {name}! You'll be assigned to room {room}!")
        room += 1
    return list

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
