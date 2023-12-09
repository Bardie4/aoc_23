from dataclasses import dataclass
from enum import Enum


# constant mapping
strength = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 0,
    "Q": 11,
    "K": 12,
    "A": 13,
}


class HandValue(Enum):
    HighCard = 1
    Pair = 2
    TwoPair = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7


@dataclass
class Hand:
    input: str
    bid: int

    def __post_init__(self):
        self.cards = self.get_cards()
        self.hand_value = self.get_highest_hand_value(self.cards)

    def get_cards(self) -> list[int]:
        return [strength[char] for char in self.input]

    def get_highest_hand_value(self, cards) -> HandValue:
        res = self.get_hand_value(cards)
        if 0 not in cards:
            return res

        joker_options = [item for item in strength.values() if item != 0]
        print(joker_options)

        for value in joker_options:
            cards = self.cards.copy()
            # Replace all occurences of 0 with value in list
            for index, card in enumerate(cards):
                if card == 0:
                    cards[index] = value
            
            hand_value = self.get_hand_value(cards)
            if hand_value.value > res.value:
                res = hand_value

        return res

    def get_hand_value(self, cards) -> HandValue:
        unique_cards = list(set(cards))
        if len(unique_cards) == 1:
            return HandValue.FiveOfAKind
        elif len(unique_cards) == 2:
            if cards.count(unique_cards[0]) == 4 or cards.count(unique_cards[1]) == 4:
                return HandValue.FourOfAKind
            else:
                return HandValue.FullHouse
        elif len(unique_cards) == 3:
            if (
                cards.count(unique_cards[0]) == 3
                or cards.count(unique_cards[1]) == 3
                or cards.count(unique_cards[2]) == 3
            ):
                return HandValue.ThreeOfAKind
            else:
                return HandValue.TwoPair
        elif len(unique_cards) == 4:
            return HandValue.Pair
        else:
            return HandValue.HighCard


if __name__ == "__main__":
    with open("mission.txt", "r") as f:
        input = f.read().splitlines()

    hands: list[Hand] = []
    for line in input:
        _hand, bid = line.split(" ")
        hand = Hand(_hand, int(bid))
        hands.append(hand)

    hands = sorted(hands, key=lambda hand: (hand.hand_value.value, hand.cards))

    for hand in hands:
        print(hand, hand.hand_value.name, hand.hand_value.value, hand.cards)

    bag = 0
    for index, hand in enumerate(hands, start=1):
        bag += hand.bid * index

    print(bag)
