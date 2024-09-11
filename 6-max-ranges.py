# imports
import itertools

# cards and suited labels
ranks = ['a', 'k', 'q', 'j', 't', '9', '8', '7', '6', '5', '4', '3', '2']

# positions
btn = []
co = []
hj = []
utg = []
sb = []

# btn pocket pairs
for i in ranks:
    sb.append(i+i)
    
# suited hands
for i in ranks[ranks.index('k'):]:
    sb.append('a' + i + 's')

for i in ranks[ranks.index('q'):]:
    sb.append('k' + i + 's')

for i in ranks[ranks.index('j'):]:
    sb.append('q' + i + 's')

for i in ranks[ranks.index('t'): ranks.index('2')]:
    sb.append('j' + i + 's')

for i in ranks[ranks.index('9'): ranks.index('4')]:
    sb.append('t' + i + 's')

for i in ranks[ranks.index('8'): ranks.index('4')]:
    sb.append('9' + i + 's')

for i in ranks[ranks.index('7'): ranks.index('4')]:
    sb.append('8' + i + 's')

for i in ranks[ranks.index('6'): ranks.index('3')]:
    sb.append('7' + i + 's')

for i in ranks[ranks.index('5'): ranks.index('3')]:
    sb.append('6' + i + s)

for i in ranks[ranks.index('4'): ranks.index('2')]:
    sb.append('5' + i + s)

# unsuited
for i in ranks[ranks.index('k'): ranks.index('2')]:
    sb.append('a' + i + 'o')

for i in ranks[ranks.index('q'): ranks.index('7')]:
    sb.append('k' + i + 'o')

for i in ranks[ranks.index('j'): ranks.index('8')]:
    sb.append('q' + i + 'o')

for i in ranks[ranks.index('t'): ranks.index('8')]:
    sb.append('j' + i + 'o')

for i in ranks[ranks.index('9'): ranks.index('7')]:
    sb.append('t' + i + 'o')

# sb
btn = [i for i in sb if i not in ('j3s', 't5s', '95s', '85s', '74s', '64s', '53s', 'k7o', 'q80', 'j8o')]

# co
co = [i for i in btn if i not in ('33', '22', 'q4s', 'q3s', 'q2s', 'j6s', 'j5s', 'j4s', 't7s', 't6s', '96s', '86s', 
                                  'a7o', 'a60', 'a4o', 'a3o', 'a2o', 'k9o', 'k8o', 'q9o', 'j9o', 't9o', 't8o')]

# hj
hj = [i for i in co if i not in ('44', 'k4s', 'k3s', 'k2s', 'q7s', 'q6s', 'q5s', 'j8s', 'j7s', '97s', '87s', 'a8o', 'qto', 'jto', 'a5o')]

# utg
utg = [i for i in hj if i not in ('k8s', 'a2s', 'q8s', 't8s', '98s', 'a9o', 'kto', 'qjo')]

def play_hand():
    global btn, co, hj, utg, sb
    pos_list = ['sb', 'btn', 'co', 'hj', 'utg']
    range_dict = {'btn': btn, 'co': co, 'hj': hj, 'utg': utg, 'sb': sb}
    positions = itertools.cycle(range(len(pos_list)))
    while True:
        position = pos_list[next(positions)]
        hand = input('{}: '.format(position).upper())
        hand = hand.split()
        if len(hand) == 1:
            print(hand[0] in range_dict[position])
        elif len(hand) == 2:

        

play_hand()

    


        




