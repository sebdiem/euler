SUIT = 'H C S D'.split()
VALUES = {
          '2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9,
          'T': 10,
          'J': 11,
          'Q': 12,
          'K': 13,
          'A': 14
         }

def compare_hands(hands):
    """Returns 1 if the first hand wins over the second one else 0."""
    hand1, hand2 = split_hands(hands)
    hand1 = format_hand(hand1)
    hand2 = format_hand(hand2)
    return 1 if hand_value(hand1) > hand_value(hand2) else 0

def split_hands(hands):
    return (hands[:14], hands[15:])

assert split_hands('AH JH KH QH TH AH JH KH QH TH') == ('AH JH KH QH TH', 'AH JH KH QH TH')

def format_hand(hand):
    hand = hand.replace(' ','')
    value_suit = zip(hand[::2], hand[1::2])
    return ''.join([''.join(t) for t in sorted(value_suit, key=lambda x:VALUES[x[0]])])

assert format_hand('AH JH KH QH TH') == 'THJHQHKHAH'
assert format_hand('AH 6S KH 8D TH') == '6S8DTHKHAH'

def hand_value(hand):
    high_card = VALUES[hand[-2]]
    if royal_flush(hand):
        return 14**3*9 + high_card
    if straight_flush(hand):
        return 14**3*8 + high_card
    four_of_a_kind = n_of_a_kind(4, hand)
    if len(four_of_a_kind) > 0:
        return 14**3*7 + VALUES[four_of_a_kind[0]]
    if full_house(hand):
        return 14**3*6 + 14*VALUES[n_of_a_kind(3, hand)[0]] + VALUES[n_of_a_kind(2, hand)[0]]
    if flush(hand):
        return 14**3*5 + high_card
    if consecutive_values(hand):
        return 14**3*4 + high_card
    three_of_a_kind = n_of_a_kind(3, hand)
    if len(three_of_a_kind) == 1:
        return 14**3*3 + 14*VALUES[three_of_a_kind[0]]
    two_of_a_kind = sorted(n_of_a_kind(2, hand), key=lambda x: VALUES[x])
    if len(two_of_a_kind) == 2:
        return 14**3*2 + 14**2*VALUES[two_of_a_kind[1]] + 14*VALUES[two_of_a_kind[0]] + \
               VALUES[hand[::2].replace(two_of_a_kind[0], '').replace(two_of_a_kind[1], '')[-1]]
    if len(two_of_a_kind) == 1:
        return 14**3 + 14*VALUES[two_of_a_kind[0]] + \
               VALUES[hand[::2].replace(two_of_a_kind[0], '')[-1]]
    return high_card

def same_suit(hand):
    return hand[1::2] in (5*suit for suit in SUIT)

def consecutive_values(hand):
    return all([(VALUES[hand[i+2]] - VALUES[hand[i]]) == 1 for i in xrange(0, len(hand)-2, 2)])

def n_of_a_kind(n, hand):
    """Returns the values making the n_of_a_kind or []"""
    results = []
    for c in hand[::2]:
        if hand.count(c) == n and not c in results:
            results.append(c)
    return results

assert n_of_a_kind(2, '5H5C6S7SKD') == ['5']
assert n_of_a_kind(2, '2C3S8S8DTD') == ['8']

def royal_flush(hand):
    return same_suit(hand) and hand[0] == 'T' and consecutive_values(hand)
           
assert royal_flush('THJHQHKHAH')
assert royal_flush('THJDQSKHAH') == False
assert royal_flush('9HJHQHKHAH') == False
           
def straight_flush(hand):
    return same_suit(hand) and consecutive_values(hand)

assert straight_flush('2H3H4H5H6H')
assert straight_flush('2H3H4H5H7H') == False
assert straight_flush('2H3H4H5S6H') == False
assert straight_flush('2H3H4H5H6S') == False
assert straight_flush('2D3H4H5H6H') == False

def full_house(hand):
    return len(n_of_a_kind(3, hand)) == 1 and len(n_of_a_kind(2, hand)) == 1

assert full_house('6H6DTHTDTS')
assert full_house('6H6D6STDTS')
assert full_house('6H6D6STDKS') == False
assert full_house('5H6D6STDKS') == False
assert full_house('4H6DTHTDTS') == False

def flush(hand):
    return same_suit(hand)

def two_pairs(hand):
    return len(n_of_a_kind(2, hand)) == 2

assert two_pairs('4H4D8STDTH')
assert two_pairs('4H8D8STDTH')
assert two_pairs('4H4D8S8DTH')
assert two_pairs('3H4D8S8DTH') == False
assert two_pairs('3H4D6S8DTH') == False

def one_pair(hand):
    return len(n_of_a_kind(2, hand)) == 1

assert hand_value('2D3D4D5D6D') > hand_value('TSTDTHAHAD')
assert hand_value('4D9S9HQHQC') > hand_value('3D9D9HQDQS')
assert hand_value('5H5C6S7SKD') < hand_value('2C3S8S8DTD')
assert hand_value('5D8C9SJSAC') > hand_value('2C5C7D8SQH')
assert hand_value('2D9CASAHAC') < hand_value('3D6D7DTDQD')
assert hand_value('4D6S9HQHQC') > hand_value('3D6D7HQDQS')
assert hand_value('2H2D4C4D4S') > hand_value('3C3D3S9S9D')

def problem54():
    f = open('poker.txt')
    result = sum((compare_hands(hands) for hands in f))
    f.close()
    return result

print problem54()
