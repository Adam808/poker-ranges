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
    btn.append(i+i)
    
# suited hands
for i in ranks[ranks.index('k'):]:
    btn.append('a' + i + 's')

for i in ranks[ranks.index('q'):]:
    btn.append('k' + i + 's')

for i in ranks[ranks.index('j'):]:
    btn.append('q' + i + 's')

for i in ranks[ranks.index('t'): ranks.index('3')]:
    btn.append('j' + i + 's')

for i in ranks[ranks.index('9'): ranks.index('5')]:
    btn.append('t' + i + 's')

for i in ranks[ranks.index('8'): ranks.index('5')]:
    btn.append('9' + i + 's')

for i in ranks[ranks.index('7'): ranks.index('5')]:
    btn.append('8' + i + 's')

for i in ranks[ranks.index('6'): ranks.index('4')]:
    btn.append('7' + i + 's')

# unsuited
for i in ranks[ranks.index('k'): ranks.index('2')]:
    btn.append('a' + i + 'o')

for i in ranks[ranks.index('q'): ranks.index('7')]:
    btn.append('k' + i + 'o')

for i in ranks[ranks.index('j'): ranks.index('8')]:
    btn.append('q' + i + 'o')

for i in ranks[ranks.index('t'): ranks.index('8')]:
    btn.append('j' + i + 'o')

for i in ranks[ranks.index('9'): ranks.index('7')]:
    btn.append('t' + i + 'o')

# singles
singles = [ '65s', '54s']
for i in singles:
    btn.append(i)

# sb
sb = list(btn)

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
        print(hand in range_dict[position])

play_hand()

    


        




