
import random

def start():

    # open config file
    config = open("config.txt", "r")

    # get info from config file into dictionary
    for line in config:

        field = line.split("=")

        if len(field) == 2:
            if field[0] == "decks":
                decks = field[1]
                deck_ammount = int(decks.rstrip("\n"))
                print("Decks = {:g}".format(deck_ammount))
            if field[0] == "shuffle_at":
                when_to_shuffle = int(field[1].rstrip("\n"))
                print("Decks will be shuffled after {:g} decks".format(when_to_shuffle))


    # setup
    card_deck = []
    card_deck = shuffel_deck(card_deck, deck_ammount)
    # main loop

    #print("Total card amount = {:g}".format(52 * deck_ammount))
    #print("Cards = {:s}".format(str(card_deck)))

    main(card_deck, deck_ammount, when_to_shuffle)

def main(card_deck, deck_ammount, when_to_shuffle):
    blackjack_game(card_deck, deck_ammount, when_to_shuffle)


def blackjack_game(card_deck, deck_ammount, when_to_shuffle):
    while True:
        player_hand = []
        game_master_hand = []
        player_hand_value = 0
        game_master_hand_value = 0

        player_choice_on = True

        for x in range(0, 2):
            player_hand.append(card_generator(card_deck))
            game_master_hand.append(card_generator(card_deck))

        # player choice
        while player_choice_on == True:
            print("Player hand is {:}".format(player_hand))
            hand = player_hand
            print("Players count is {:}".format(hand_value(player_hand)))
            print("Gamemasters hand is {:}".format(game_master_hand[1]))

            if hand_value(hand) == 21:
                print("Blackjack for player")

            if hand_value(hand) > 21:
                print("Player is over")
                break

            player_move = input(print("Do you want to hit (h) or stand (s)"))

            if player_move == "h":
                player_hand.append(card_generator(card_deck))

            else:
                player_choice_on = False
                player_hand_value = hand_value(hand)

        while True:
            game_master_hand_value = hand_value(game_master_hand)
            print("Gamemasters hand is {:}".format(game_master_hand))
            print("Gamemaster count is {:}".format(game_master_hand_value))

            if game_master_hand_value < 17:
                game_master_hand.append(card_generator(card_deck))

            elif game_master_hand_value == 21:
                print("Blackjack for gamemaster")
                break

            elif game_master_hand_value > 21:
                print("Gamemaster over")
                break
            else:
                break

        player_hand_value = hand_value(player_hand)
        game_master_hand_value = hand_value(game_master_hand)

        if game_master_hand_value > 21:
            print("Player wins")
        elif player_hand_value == game_master_hand_value:
            print("Even")
        elif player_hand_value > game_master_hand_value and player_hand_value < 22:
            print("Player wins")
        else:
            print("House wins")

        if len(card_deck) < (when_to_shuffle * 52):
            shuffel_deck(card_deck, deck_ammount)
            print("Deck was shuffeled")

        if input(print("New game Yes = (y) No = (n)\n")) == "n":
            break




def card_generator(card_deck):
    random_card = random.choice(card_deck)
    card_deck.remove(random_card)
    return random_card



def shuffel_deck(card_deck, deck_ammount):
    card_deck.clear()

    card_types = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
    card_shuffle_count = 0
    suit_types = ["c", "d", "h", "s"]
    suit_shuffle_count = 0
    deck = 1

    while deck <= deck_ammount:

        next_card = suit_types[suit_shuffle_count] + card_types[card_shuffle_count]
        card_shuffle_count += 1

        if card_shuffle_count == 13:
            card_shuffle_count = 0
            suit_shuffle_count += 1

            if suit_shuffle_count == 4:
                suit_shuffle_count = 0
                deck += 1

        card_deck.append(next_card)

    return card_deck



def hand_value(hand):
    hand_value = 0
    for i in range(len(hand)):

        if hand[i][1] == "a":
            hand_value += 11
        elif hand[i][1] == "j" or hand[i][1] == "q" or hand[i][1] == "k" or \
                hand[i][1] == "10":
            hand_value += 10
        else:
            hand_value += int(hand[i][1])
    return hand_value




start()