# imports
import itertools

# card ranks
ranks = ['a', 'k', 'q', 'j', 't', '9', '8', '7', '6', '5', '4', '3', '2']

# positions
btn = []
co = []
hj = []
utg = []
sb = []
bb = []

# sb pocket pairs
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
    sb.append('6' + i + 's')

for i in ranks[ranks.index('4'): ranks.index('2')]:
    sb.append('5' + i + 's')

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

# btn
btn = [i for i in sb if i not in ('j3s', 't5s', '95s', '85s', '74s', '64s', '53s', 'k7o', 'q80', 'j8o')]

# co
co = [i for i in btn if i not in ('33', '22', 'q4s', 'q3s', 'q2s', 'j6s', 'j5s', 'j4s', 't7s', 't6s', '96s', '86s', 
                                  'a7o', 'a60', 'a4o', 'a3o', 'a2o', 'k9o', 'k8o', 'q9o', 'j9o', 't9o', 't8o')]

# hj
hj = [i for i in co if i not in ('44', 'k4s', 'k3s', 'k2s', 'q7s', 'q6s', 'q5s', 'j8s', 'j7s', '97s', '87s', 'a8o', 'qto', 'jto', 'a5o')]

# utg
utg = [i for i in hj if i not in ('k8s', 'a2s', 'q8s', 't8s', '98s', 'a9o', 'kto', 'qjo')]


# 3-bet ranges
# utg raise
hj_vs_utg = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'ats', 'kqs', 'kjs', 'kts',
             'qjs', 'a5s', 'a4s', 'aqo']

co_vs_utg = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'ats', 'kqs', 'kjs', 'kts',
             'qjs', 'a5s', 'a4s', 'aqo', 'kqo']

btn_vs_utg = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'kqs', 'kjs',
               'kts','qjs', 'a5s', 'a4s', 'aqo', 'kqo']

sb_vs_utg = ['aa', 'kk', 'qq', 'tt', 'aks', 'aqs', 'ajs', 'kqs', 'kjs', 'kts', 'qjs', 'qts',
             'a5s', 'a4s', 'ako', 'aqo']

bb_vs_utg_raise = ['aa', 'kk', 'qq', 'aks', 'aqo', 'qjs', 'ako']

bb_vs_utg_call = ['jj', 'tt', '99', '88', '77', '66', '55', '44', '33', '22', 'ajs', 'ats',
                  'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'kqs', 'kjs', 'kts',
                  'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'qts', 'q9s', 'q8s', 'jts', 'j9s',
                  'j8s', 't9s', 't8s', 't7s', '98s', '97s', '96s', '87s', '86s', '85s', '76s', 
                  '75s', '65s', '64s', '54s', '53s', '43s', '42s', 'aqo', 'ajo', 'kqo']

# hj raise
co_vs_hj = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'kqs', 'kjs', 
            'kts', 'qjs', 'qts', 'a5s', 'a4s', 'a3s', 'ako', 'aqo', 'ajo', 'kqo']

btn_vs_hj = ['aa', 'kk', 'qq', 'jj', 'tt', '99', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'kqs', 
             'kjs', 'kts', 'qjs', 'qts', 'jts', 'a5s', 'a4s', 'a3s', 'ako', 'aqo', 'ajo', 'kqo']

sb_vs_hj = ['aa, kk, qq, jj, tt, aks, aqs, ajs, ats, kqs, kjs, kts, qjs, a5s, a4s, ako, aqo, kqo']

bb_raise_vs_hj = ['aa', 'kk', 'qq', 'aks', 'aqs', 'qjs', 'ako', 'q8s']

bb_call_vs_hj = ['jj', 'tt', '99', '88', '77', '66', '55', '44', '33', '22', 'ajs', 'ats', 'a9s', 
                 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 
                 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', 'qjs', 'qts', 'q9s', 'q8s', 'jts', 'j9s', 
                 'j8s', 't9s', 't8s', 't7s', '98s', '97s', '96s', '87s', '86s', '85s', '76s', '75s', 
                 '74s', '65s', '64s', '54s', '53s', '43s', 'aqo', 'ajo', 'ato', 'kqo', 'kjo', 'qjo']

# co raise
btn_vs_co = ['aa', 'kk', 'qq', 'jj', 'tt', '99', '88', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 
             'a6s', 'a5s', 'a4s', 'a3s', 'kqs', 'kjs', 'kts', 'k9s', 'qjs', 'qts', 'jts', 'ajo', 'kqo']

sb_vs_co = ['aa', 'kk', 'qq', 'jj', 'tt', '99', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'kqs', 'kjs', 'kts',
            'qjs', 'qts', 'jts', 'a5s', 'a4s', 'ako', 'aqo', 'ajo', 'kqo', 'kjo']

bb_raise_vs_co = ['aa', 'kk', 'qq', 'jj', 'aks', 'aqs', 'q6s', 'q4s', 'j7s', 'kjo']

bb_call_vs_co = ['tt', '99', '88', '77', '66', '55', '44', '33', '22', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 
                 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 
                 'k4s', 'k3s', 'k2s', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q5s', 'jts', 'j9s', 'j8s',
                 't9s', 't8s', 't7s', '98s', '97s', '96s', '87s', '86s', '85s', '76s', '75s', '74s', 
                 '65s', '64s', '54s', '53s', '43s', '42s', 'aqo', 'ajo', 'ato', 'a9o', 'kqo',
                 'kto', 'qjo', 'qto', 'jto']

#btn raise
sb_vs_btn = ['aa', 'kk', 'qq', 'jj', 'tt', '99', '88', '77', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s',
             'a7s', 'a5s', 'a4s', 'kqs', 'kjs', 'kts', 'k9s', 'qjs', 'qts', 'q9s', 'jts', 't9s', 'ako', 
             'aqo', 'ajo', 'ato', 'kqo', 'kjo']

bb_raise_vs_btn = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'kqs', 'kjs', 'j7s', 'j6s',
                   't9s', 't6s', 'ako', 'aqo', 'a5o', 'k9o']

bb_call_vs_btn = ['99', '88', '77', '66', '55', '44', '33', '22', 'ats', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 
                  'a4s', 'a3s', 'a2s', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', 'qjs',
                  'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', 'jts', 'j9s', 'j8s', 'j5s',
                  'j4s', 't8s', 't7s', 't6s', '98s', '97s', '96s', '87s', '86s', '85s', '76s', '75s', '74s',
                  '65s', '64s', '63s', '54s', '53s', '43s', 'aqo', 'ajo', 'ato', 'a9o']

#sb raise
bb_raise_vs_sb = ['aa', 'kk', 'qq', 'jj', 'tt', '99', 'a5s', 'a4s', 'kqs', 'kjs', 'qjs', 'jts', 'j2s',
                  't9s', 't5s', 't3s', 't2s', '98s', '87s', '76s', '65s', '54s', 'ako', 'aqo', 'a6o'
                  'a3s', 'a2s', 'k7o', 'j8o']

bb_call_vs_sb = ['88', '77', '66', '55', '44', '33', '22', 'ats', 'a9s', 'a8s', 'a7s', 'a6s',
                 'a3s', 'a2s', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s',
                 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', 'j9s', 'j8s', 
                 'j7s', 'j6s', 'j5s', 'j4s', 'j3s', 't8s', 't7s', 't6s', 't4s', '97s', '96s', 
                 '95s',  '75s', '74s', '64s', '63s', '53s', '52s', '43s', '42s', '32s', 'ato', 
                 'a9o', 'a8o', 'a5o', 'a4o', 'kjo', 'kto', 'k9o', 'qjo', 'qto', 'q9o', 'jto', 
                 'j9o', 't9o', 't8o',]


def play_hand():
    global btn, co, hj, utg, sb, bb
    pos_list = ['sb', 'btn', 'co', 'hj', 'utg', 'bb']
    range_dict = {'btn': btn, 'co': co, 'hj': hj, 'utg': utg, 'sb': sb, 'bb': bb}
    positions = itertools.cycle(range(len(pos_list)))
    while True:
        position = pos_list[next(positions)]
        hand = input('{}: '.format(position).upper())
        hand = hand.split()
        if len(hand) == 1:
            print(hand[0] in range_dict[position])
        elif len(hand) == 2:
            if hand[0] == 'utg':
                if position == 'hj':
                    print(hand[1] in hj_vs_utg)
                elif position == 'co':
                    print(hand[1] in co_vs_utg)
                elif position == 'btn':
                    print(hand[1] in btn_vs_utg)
                elif position == 'sb':
                    print(hand[1] in sb_vs_utg)
                elif position == 'bb':
                    if hand[1] in bb_vs_utg_raise:
                        print('raise')
                    elif hand[1] in bb_vs_utg_call:
                        print('call')
                    else:
                        print('fold')
            elif hand[0] == 'hj':
                if position == 'co':
                    print(hand[1] in co_vs_hj)
                elif position == 'btn':
                    print(hand[1] in btn_vs_hj)
                elif position == 'sb':
                    print(hand[1] in sb_vs_hj)
                elif position == 'bb':
                    if hand[1] in bb_raise_vs_hj:
                        print('raise')
                    elif hand[1] in bb_call_vs_hj:
                        print('call')
                    else:
                        print('fold')
            elif hand[0] == 'co':
                if position == 'btn':
                    print(hand[1] in btn_vs_co)
                elif position == 'sb':
                    print(hand[1] in sb_vs_co)
                elif position =='bb':
                    if hand[1] in bb_raise_vs_co:
                        print('raise')
                    elif hand[1] in bb_call_vs_co:
                        print('call')
                    else:
                        print('fold')
            elif hand[0] == 'btn':
                if position == 'sb':
                    print(hand[1] in sb_vs_btn)
                elif position == 'bb':
                    if hand[1] in bb_raise_vs_btn:
                        print('raise')
                    elif hand[1] in bb_call_vs_btn:
                        print('call')
                    else:
                        print('fold')
            elif hand[0] == 'sb':
                if position == 'bb':
                    if hand[1] in bb_raise_vs_sb:
                        print('raise')
                    elif hand[1] in bb_call_vs_sb:
                        print('call')
                    else:
                        print('fold')
                
play_hand()

    


        




