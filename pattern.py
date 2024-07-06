def play():
    life_remaining = 3
    message = "Where do you want to go next? You are in the "
    current_room = "common room"

    while life_remaining > 0:
        if current_room == "common room":
            get_input = input(message + current_room + ": ").casefold()
            if get_input == 'n':
                current_room = "bear room"
            elif get_input == 's':
                life_remaining -= 1
                print(f"You hit the wall and left {life_remaining} life")
            else:
                life_remaining -= 1
                print(f"You hit the wall and left {life_remaining} life")
        elif current_room == "bear room":
            get_input = input(message + current_room + ": ").casefold()
            if get_input == 'e':
                current_room = "grave"
            else:
                life_remaining -= 1
                print(f"You hit the wall and left {life_remaining} life")
        elif current_room == "grave":
            get_input = input(message + current_room + ": ").casefold()
            if get_input == 's':
                current_room = "tunnel"
            else:
                life_remaining -= 1
                print(f"You hit the wall and left {life_remaining} life")
        elif current_room == "tunnel":
            get_input = input(message + current_room + ": ").casefold()
            if get_input == 'e':
                print("You won the game!!!")
                break
            else:
                life_remaining -= 1
                print(f"You hit the wall and left {life_remaining} life")
    else:
        print("You lost the game")

play()