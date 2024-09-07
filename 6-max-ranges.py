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

for i in ranks[ranks.index('j'): ranks.index('3')]:
    btn.append('q' + i + 's')

for i in ranks[ranks.index('t'): ranks.index('5')]:
    btn.append('j' + i + 's')

for i in ranks[ranks.index('9'): ranks.index('5')]:
    btn.append('t' + i + 's')

for i in ranks[ranks.index('8'): ranks.index('4')]:
    btn.append('9' + i + 's')

for i in ranks[ranks.index('7'): ranks.index('3')]:
    btn.append('8' + i + 's')

for i in ranks[ranks.index('6'): ranks.index('3')]:
    btn.append('7' + i + 's')

for i in ranks[ranks.index('5'): ranks.index('2')]:
    btn.append('6' + i + 's')

for i in ranks[ranks.index('4'): ranks.index('2')]:
    btn.append('5' + i + 's')

# unsuited
for i in ranks[ranks.index('k'):]:
    btn.append('a' + i + 'o')

for i in ranks[ranks.index('q'): ranks.index('8')]:
    btn.append('k' + i + 'o')

for i in ranks[ranks.index('j'): ranks.index('8')]:
    btn.append('q' + i + 'o')

for i in ranks[ranks.index('t'): ranks.index('8')]:
    btn.append('j' + i + 'o')

# singles
singles = ['43s', '32s', 't9o', '98o']
for i in singles:
    btn.append(i)

# sb
sb = list(btn)

# co
co = [i for i in btn if i not in ('k5s', 'k4s', 'k3s', 'k2s', 'q7s', 'q6s', 'q5s', 'q4s', 'j7s', 'j6s', 't7s', 't6s', '96s', '95s', '85s', '84s', '74s', '63s', '53s',
                                 '43s', '32s', 'a9o', 'a8o', 'a7o', 'a6o', 'a5o', 'a4o', 'a3o', 'a2o', 'k9o', 'q9o', 'j9o', 't9o', '98o')]

# hj
hj = [i for i in co if i not in ('k7s', 'k6s', 'q8s', 'j8s', '86s', '75s', '64s', 'kto', 'qto', 'jto')]

# utg
utg = [i for i in hj if i not in ('k8s', 't8s', '97s', '54s', 'ato', 'kjo', 'qjo')]

def play_hand():
    global btn, co, hj, utg, sb
    range_dict = {'btn': btn, 'co': co, 'hj': hj, 'utg': utg, 'sb': sb}
    seat_hand = input('seat & hand: ')
    seat_hand = seat_hand.split()
    if seat_hand[0] in range_dict:
        print(seat_hand[1] in range_dict[seat_hand[0]])
    else:
        play_hand()

while True:
    play_hand()




