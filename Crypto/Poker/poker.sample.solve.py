from math import ceil, prod
from operator import lshift, rshift
from string import ascii_uppercase

HEARTS = "🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾"
SPADES = "🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮"
DIAMONDS = "🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎"
CLUBS = "🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞"
DECK = SPADES+HEARTS+DIAMONDS+CLUBS  # Bridge Ordering of a Deck
DECK_SIZE = 52
ALPHABET52 = ascii_uppercase + "abcdefghijklmnop_rstuvw{y}"

CARDS_PER_DEAL = 25
DEALS_PER_PUZZLE = 750
assert CARDS_PER_DEAL % 2 == 1
MAX_DEAL = prod(x for x in range(DECK_SIZE - CARDS_PER_DEAL + 1, DECK_SIZE + 1))
DEAL_BITS = MAX_DEAL.bit_length()

INTS_PER_DEAL = ceil(DEAL_BITS / 32)
MT_STATE_SIZE = 624
INT_MASK = 0xFFFFFFFF

############### Puzzle Solution Code ###############
def unxorshift(x, operator, shift, mask=INT_MASK):
    res = x
    for i in range(32):
        res = x ^ (operator(res, shift) & mask)
    return res

def untemper(random_int):
    random_int = unxorshift(random_int, rshift, 18)
    random_int = unxorshift(random_int, lshift, 15, 0xefc60000)
    random_int = unxorshift(random_int, lshift, 7, 0x9d2c5680)
    random_int = unxorshift(random_int, rshift, 11)
    return random_int

def temper(state_int):
    state_int ^= (state_int >> 11)
    state_int ^= (state_int << 7) & 0x9d2c5680
    state_int ^= (state_int << 15) & 0xefc60000
    state_int ^= (state_int >> 18)
    return state_int

def next_partial(i, i1):
    y = (i & 0x80000000) + (i1 & 0x7fffffff) 
    next = y >> 1
    if (y & 1) == 1:
        next ^= 0x9908b0df
    return next

def next_value(i, i1, i397):
    return next_partial(i, i1) ^ i397

def generate_next(current_state, next_state):
    accurate_predictions = 0
    for i in range(MT_STATE_SIZE):
        state_i1 = current_state[i + 1] if i + 1 < MT_STATE_SIZE else next_state[(i + 1) % MT_STATE_SIZE]
        state_i397 = current_state[i + 397] if i + 397 < MT_STATE_SIZE else next_state[(i + 397) % MT_STATE_SIZE]
        if current_state[i] and state_i1 and state_i397:
            next = next_value(current_state[i], state_i1, state_i397)
            if not next_state[i]:
                next_state[i] = next
            elif next_state[i] == next:
                accurate_predictions += 1
            else:
                print(f"MISMATCH: {i} - {current_state[i]} {state_i1} {state_i397} : {next} {next_state[i]}") 
                raise ValueError
    print(f"=== {accurate_predictions} Successful Predictions")
    return next_state

def backfill(current_state, next_state):
    for i in range(MT_STATE_SIZE):
        state_i1 = current_state[i + 1] if i + 1 < MT_STATE_SIZE else next_state[(i + 1) % MT_STATE_SIZE]
        if current_state[i] and state_i1 and next_state[i]:
            if i + 397 < MT_STATE_SIZE and not current_state[i + 397]:
                current_state[i + 397] = next_state[i] ^ next_partial(current_state[i], state_i1)
                print(f"---Backfill {i + 397}: {current_state[i + 397]}")
            elif i + 397 >= MT_STATE_SIZE and not next_state[(i + 397) % MT_STATE_SIZE]:
                next_state[(i + 397) % MT_STATE_SIZE] = next_state[i] ^ next_partial(current_state[i], state_i1)
                print(f"---Backfill {(i + 397) % MT_STATE_SIZE}: {next_state[(i + 397) % MT_STATE_SIZE]}")
    return current_state, next_state

def resolve_shuffle_possibilities(states, possibles):
    for i, deal_list in possibles.items():
        deal_index = i % INTS_PER_DEAL
        current_state = states[i // MT_STATE_SIZE][i % MT_STATE_SIZE]
        if i in possibles and current_state and len(possibles[i]) > 1:
            print(f"==== Resolve {i} {deal_index}: {possibles[i]} - {current_state}")
            for value in deal_list:
                computed = untemper(value >> (deal_index * 32) & INT_MASK)
                if computed == current_state:
                    for j, shift in enumerate(range(0, 32 * (INTS_PER_DEAL - 1), 32)):
                        offset = i - deal_index + j
                        if offset in possibles:
                            possibles[offset] = [untemper(value >> shift & INT_MASK)]
    for i in list(possibles.keys()):
        if i in possibles and len(possibles[i]) == 1:
            states[i // MT_STATE_SIZE][i % MT_STATE_SIZE] = possibles.pop(i)[0]  
    return states, possibles

def convert_deal_to_int(deal):
    total = 0
    for i in range(CARDS_PER_DEAL - 1, -1, -1):
        total = total * (DECK_SIZE - i) + [card for card in DECK if card not in deal[:i]].index(deal[i])
    return total

def load_state_arrays_from_deals(deals):
    rotations = ceil(len(deals) * INTS_PER_DEAL / MT_STATE_SIZE)
    state = [[None]*MT_STATE_SIZE for _ in range(rotations)]
    possibles = {}
    index = 0
    for deal in deals:
        shuffle = convert_deal_to_int(deal)
        if shuffle + MAX_DEAL >= (1 << DEAL_BITS) - 1:
            for i, shift in enumerate(range(0, 32 * (INTS_PER_DEAL - 1), 32)):
                state[(index + i) // MT_STATE_SIZE][(index + i) % MT_STATE_SIZE] = untemper(shuffle >> shift & INT_MASK)
        else:
            for i in range(0, INTS_PER_DEAL - 1):
                possibles[index + i] = []
                for possible_shuffle in range(shuffle, (1 << DEAL_BITS) - 1, MAX_DEAL):
                    possibles[index + i] += [possible_shuffle]
        index += INTS_PER_DEAL
    return state, possibles

def process_cards_file(filename):
    deals = []
    with open(filename, "r") as poker_file:
        for line in poker_file:
            cards_in_line = "".join([card for card in line if card in DECK])
            if "1: " == line[:3]: deals.append(cards_in_line)
            if "Table:" == line[:6]: deals[-1] += cards_in_line
    return deals

def solve_puzzle():
    deals = process_cards_file("cards.PATCHED.txt")
    print(f"Last Provided Deal... Rotation: {(len(deals) * INTS_PER_DEAL) // MT_STATE_SIZE} - State: {(len(deals) * INTS_PER_DEAL) % MT_STATE_SIZE}")
    states, possibles = load_state_arrays_from_deals(deals)

    has_changes = True
    while has_changes:
        has_changes = False
        print("..... Predicting missing values .....")
        for i in range((len(deals) * INTS_PER_DEAL) // MT_STATE_SIZE):
            current_nones = states[i].count(None) + states[i + 1].count(None)
            states[i], states[i + 1] = backfill(states[i], states[i + 1])
            states[i + 1] = generate_next(states[i], states[i + 1])
            has_changes = has_changes or not (current_nones == (states[i].count(None) + states[i + 1].count(None)))
        states, possibles = resolve_shuffle_possibilities(states, possibles)

    shuffle = 0
    for idx, state in enumerate(range(len(deals) * INTS_PER_DEAL, (len(deals) * INTS_PER_DEAL) + 10)):
        i = idx % INTS_PER_DEAL
        next_random32 = temper(states[state // MT_STATE_SIZE][state % MT_STATE_SIZE])
        print("Future Value {}: {} -> {}".format(i, untemper(next_random32), next_random32))
        shuffle = (next_random32 << (i * 32)) + shuffle
        if i == INTS_PER_DEAL - 1:
            shuffle = shuffle % MAX_DEAL
            print(f"Shuffle: {shuffle}")
            deck = list(DECK)
            deal = ""
            while shuffle > 0:
                deal += deck.pop(shuffle % len(deck))
                shuffle //= len(deck) + 1
            while len(deal) < CARDS_PER_DEAL:
                deal += deck.pop(0)
            print(f"Deal: {deal}")
            print(deal.translate(deal.maketrans(DECK, ALPHABET52)))
            shuffle = 0

print("Solving for games in cards.txt....")
solve_puzzle()



