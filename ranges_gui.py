from tkinter import *
from tkinter import ttk

# card ranks
ranks = ['a', 'k', 'q', 'j', 't', '9', '8', '7', '6', '5', '4', '3', '2']

# positions
btn = []
co = []
hj = []
utg = []
sb = []
bb = []

counter = 0

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
    sb.append('a' + i)

for i in ranks[ranks.index('q'): ranks.index('7')]:
    sb.append('k' + i)

for i in ranks[ranks.index('j'): ranks.index('8')]:
    sb.append('q' + i)

for i in ranks[ranks.index('t'): ranks.index('8')]:
    sb.append('j' + i)

for i in ranks[ranks.index('9'): ranks.index('7')]:
    sb.append('t' + i)

# btn
btn = [i for i in sb if i not in ('j3s', 't5s', '95s', '85s', '74s', '64s', '53s', 'k7', 'q8', 'j8')]

# co
co = [i for i in btn if i not in ('33', '22', 'q4s', 'q3s', 'q2s', 'j6s', 'j5s', 'j4s', 't7s', 't6s', '96s', '86s', 
                                  'a7', 'a6', 'a4', 'a3', 'a2', 'k9', 'k8', 'q9', 'j9', 't9', 't8')]

# hj
hj = [i for i in co if i not in ('44', 'k4s', 'k3s', 'k2s', 'q7s', 'q6s', 'q5s', 'j8s', 'j7s', '97s', '87s', 'a8', 'qt', 'jt', 'a5')]

# utg
utg = [i for i in hj if i not in ('k8s', 'a2s', 'q8s', 't8s', '98s', 'a9', 'kt', 'qj')]

### 3-bet ranges ###

# utg raise
hj_vs_utg = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'ats', 'kqs', 'kjs', 'kts',
             'a5s', 'a4s', 'aq']

co_vs_utg = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'ats', 'kqs', 'kjs', 'kts',
             'qjs', 'a5s', 'a4s', 'aq', 'kq']

btn_vs_utg = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'kqs', 'kjs',
               'kts','qjs', 'a5s', 'a4s', 'aq', 'kq']

sb_vs_utg = ['aa', 'kk', 'qq', 'tt', 'aks', 'aqs', 'ajs', 'kqs', 'kjs', 'kts', 'qjs', 'qts',
             'a5s', 'a4s', 'ak', 'aq']

bb_vs_utg_raise = ['aa', 'kk', 'qq', 'aks', 'aqo', 'qjs', 'ak']

bb_vs_utg_call = ['jj', 'tt', '99', '88', '77', '66', '55', '44', '33', '22', 'ajs', 'ats',
                  'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'kqs', 'kjs', 'kts',
                  'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'qts', 'q9s', 'q8s', 'jts', 'j9s',
                  'j8s', 't9s', 't8s', 't7s', '98s', '97s', '96s', '87s', '86s', '85s', '76s', 
                  '75s', '65s', '64s', '54s', '53s', '43s', '42s', 'aq', 'aj', 'kq']

# hj raise
co_vs_hj = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'kqs', 'kjs', 
            'kts', 'qjs', 'qts', 'a5s', 'a4s', 'a3s', 'ak', 'aq', 'aj', 'kq']

btn_vs_hj = ['aa', 'kk', 'qq', 'jj', 'tt', '99', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'kqs', 
             'kjs', 'kts', 'qjs', 'qts', 'jts', 'a5s', 'a4s', 'a3s', 'ak', 'aq', 'aj', 'kq']

sb_vs_hj = ['aa, kk, qq, jj, tt, aks, aqs, ajs, ats, kqs, kjs, kts, qjs, a5s, a4s, ak, aq, kq']

bb_raise_vs_hj = ['aa', 'kk', 'qq', 'aks', 'aqs', 'qjs', 'ak', 'q8s']

bb_call_vs_hj = ['jj', 'tt', '99', '88', '77', '66', '55', '44', '33', '22', 'ajs', 'ats', 'a9s', 
                 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 
                 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', 'qjs', 'qts', 'q9s', 'q8s', 'jts', 'j9s', 
                 'j8s', 't9s', 't8s', 't7s', '98s', '97s', '96s', '87s', '86s', '85s', '76s', '75s', 
                 '74s', '65s', '64s', '54s', '53s', '43s', 'aq', 'aj', 'at', 'kq', 'kj', 'qj']

# co raise
btn_vs_co = ['aa', 'kk', 'qq', 'jj', 'tt', '99', '88', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 
             'a6s', 'a5s', 'a4s', 'a3s', 'kqs', 'kjs', 'kts', 'k9s', 'qjs', 'qts', 'jts', 'aj', 'kq']

sb_vs_co = ['aa', 'kk', 'qq', 'jj', 'tt', '99', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'kqs', 'kjs', 'kts',
            'qjs', 'qts', 'jts', 'a5s', 'a4s', 'ak', 'aqo', 'aj', 'kq', 'kj']

bb_raise_vs_co = ['aa', 'kk', 'qq', 'jj', 'aks', 'aqs', 'q6s', 'q4s', 'j7s', 'kj']

bb_call_vs_co = ['tt', '99', '88', '77', '66', '55', '44', '33', '22', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 
                 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 
                 'k4s', 'k3s', 'k2s', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q5s', 'jts', 'j9s', 'j8s',
                 't9s', 't8s', 't7s', '98s', '97s', '96s', '87s', '86s', '85s', '76s', '75s', '74s', 
                 '65s', '64s', '54s', '53s', '43s', '42s', 'aq', 'aj', 'at', 'a9', 'kq',
                 'kt', 'qj', 'qt', 'jt']

# btn raise
sb_vs_btn = ['aa', 'kk', 'qq', 'jj', 'tt', '99', '88', '77', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s',
             'a7s', 'a5s', 'a4s', 'kqs', 'kjs', 'kts', 'k9s', 'qjs', 'qts', 'q9s', 'jts', 't9s', 'ak', 
             'aq', 'aj', 'at', 'kq', 'kj']

bb_raise_vs_btn = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', 'aqs', 'ajs', 'kqs', 'kjs', 'j7s', 'j6s',
                   't9s', 't6s', 'ak', 'aq', 'a5', 'k9']

bb_call_vs_btn = ['99', '88', '77', '66', '55', '44', '33', '22', 'ats', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 
                  'a4s', 'a3s', 'a2s', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', 'qjs',
                  'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', 'jts', 'j9s', 'j8s', 'j5s',
                  'j4s', 't8s', 't7s', 't6s', '98s', '97s', '96s', '87s', '86s', '85s', '76s', '75s', '74s',
                  '65s', '64s', '63s', '54s', '53s', '43s', 'aq', 'aj', 'at', 'a9']

# sb raise
bb_raise_vs_sb = ['aa', 'kk', 'qq', 'jj', 'tt', '99', 'a5s', 'a4s', 'kqs', 'kjs', 'qjs', 'jts', 'j2s',
                  't9s', 't5s', 't3s', 't2s', '98s', '87s', '76s', '65s', '54s', 'ak', 'aq', 'a6'
                  'a3s', 'a2s', 'k7', 'j8']

bb_call_vs_sb = ['88', '77', '66', '55', '44', '33', '22', 'ats', 'a9s', 'a8s', 'a7s', 'a6s',
                 'a3s', 'a2s', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s',
                 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', 'j9s', 'j8s', 
                 'j7s', 'j6s', 'j5s', 'j4s', 'j3s', 't8s', 't7s', 't6s', 't4s', '97s', '96s', 
                 '95s',  '75s', '74s', '64s', '63s', '53s', '52s', '43s', '42s', '32s', 'at', 
                 'a9', 'a8', 'a5', 'a4', 'kj', 'kt', 'k9', 'qj', 'qt', 'q9', 'jt', 
                 'j9', 't9', 't8',]


def play_hand():
    range_dict = {'btn': btn, 'co': co, 'hj': hj, 'utg': utg, 'sb': sb, 'bb': bb}
    pos_list = ['sb', 'btn', 'co', 'hj', 'utg', 'bb']
    new_hand = hand.get()
    position.set(pos_list[counter])
    disp_position.set(position.get().upper())
    if new_hand in range_dict[pos_list[counter]] and not raiser.get():
        action.set('Raise')
    elif not raiser.get():
        action.set('Fold')
    elif raiser.get() == 'UTG':
        if position.get() == 'hj':
            if new_hand in hj_vs_utg:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'co':
            if new_hand in co_vs_utg:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'btn':
            if new_hand in btn_vs_utg:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'sb':
            if new_hand in sb_vs_utg:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'bb':
            if new_hand in bb_vs_utg_raise:
                action.set('Raise')
            elif new_hand in bb_vs_utg_call:
                action.set('Call')
            else:
                action.set('Fold')
    elif raiser.get() == 'HJ':
        if position.get() == 'co':
            if new_hand in co_vs_hj:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'btn':
            if new_hand in btn_vs_hj:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'sb':
            if new_hand in sb_vs_hj:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'bb':
            if new_hand in bb_raise_vs_hj:
                action.set('Raise')
            elif new_hand in bb_call_vs_hj:
                action.set('Call')
            else:
                action.set('Fold')
    elif raiser.get() == 'CO':
        if position.get() == 'btn':
            if new_hand in btn_vs_co:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'sb':
            if new_hand in sb_vs_co:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() =='bb':
            if new_hand in bb_raise_vs_co:
                action.set('Raise')
            elif new_hand in bb_call_vs_co:
                action.set('Call')
            else:
                action.set('Fold')
    elif raiser.get() == 'BTN':
        if position.get() == 'sb':
            if new_hand in sb_vs_btn:
                action.set('Raise')
            else:
                action.set('Fold')
        elif position.get() == 'bb':
            if new_hand in bb_raise_vs_btn:
                action.set('Raise')
            elif new_hand in bb_call_vs_btn:
                action.set('Call')
            else:
                action.set('Fold')
    elif raiser.get() == 'SB':
        if position.get() == 'bb':
            if new_hand in bb_raise_vs_sb:
                action.set('Raise')
            elif new_hand in bb_call_vs_sb:
                action.set('Call')
            else:
                action.set('Fold')

def next_hand():
    global counter, hand
    pos_list = ['sb', 'btn', 'co', 'hj', 'utg', 'bb']
    counter = (counter + 1) % 6
    hand.set('')
    disp_hand.set('')
    action.set('')
    raiser.set('')
    position.set(pos_list[counter])
    disp_position.set(position.get().upper())

# player hand cards
def deal_ace():
    global hand
    if len(hand.get()) == 0:
        hand.set('a')
        disp_hand.set('A')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + 'a')
        disp_hand.set(disp_hand.get() + 'A')
    

def deal_king():
    global hand
    if len(hand.get()) == 0:
        hand.set('k')
        disp_hand.set('K')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + 'k')
        disp_hand.set(disp_hand.get() + 'K')

def deal_queen():
    global hand
    if len(hand.get()) == 0:
        hand.set('q')
        disp_hand.set('Q')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + 'q')
        disp_hand.set(disp_hand.get() + 'Q')

def deal_jack():
    global hand
    if len(hand.get()) == 0:
        hand.set('j')
        disp_hand.set('J')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + 'j')
        disp_hand.set(disp_hand.get() + 'J')

def deal_ten():
    global hand
    if len(hand.get()) == 0:
        hand.set('t')
        disp_hand.set('T')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + 't')
        disp_hand.set(disp_hand.get() + 'T')

def deal_nine():
    global hand
    if len(hand.get()) == 0:
        hand.set('9')
        disp_hand.set('9')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + '9')
        disp_hand.set(disp_hand.get() + '9')

def deal_eight():
    global hand
    if len(hand.get()) == 0:
        hand.set('8')
        disp_hand.set('8')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + '8')
        disp_hand.set(disp_hand.get() + '8')

def deal_seven():
    global hand
    if len(hand.get()) == 0:
        hand.set('7')
        disp_hand.set('7')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + '7')
        disp_hand.set(disp_hand.get() + '7')

def deal_six():
    global hand
    if len(hand.get()) == 0:
        hand.set('6')
        disp_hand.set('6')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + '6')
        disp_hand.set(disp_hand.get() + '6')

def deal_five():
    global hand
    if len(hand.get()) == 0:
        hand.set('5')
        disp_hand.set('5')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + '5')
        disp_hand.set(disp_hand.get() + '5')

def deal_four():
    global hand
    if len(hand.get()) == 0:
        hand.set('4')
        disp_hand.set('4')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + '4')
        disp_hand.set(disp_hand.get() + '4')

def deal_three():
    global hand
    if len(hand.get()) == 0:
        hand.set('3')
        disp_hand.set('3')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + '3')
        disp_hand.set(disp_hand.get() + '3')

def deal_two():
    global hand
    if len(hand.get()) == 0:
        hand.set('2')
        disp_hand.set('2')
    elif len(hand.get()) == 1:
        hand.set(hand.get() + '2')
        disp_hand.set(disp_hand.get() + '2')
    

def is_suited():
    global hand, disp_hand
    hand.set(hand.get() + 's')
    disp_hand.set(disp_hand.get() + 's')


# opponent position raise
def utg_raise():
    raiser.set('UTG')

def hj_raise():
    raiser.set('HJ')

def co_raise():
    raiser.set('CO')
    
def btn_raise():
    raiser.set('BTN')

def sb_raise():
    raiser.set('SB')

def clear():
    hand.set('')
    disp_hand.set('')
    raiser.set('')
    action.set('')

# gui
root = Tk()
root.title('6-Max Ranges')

hand = StringVar(root, '')
disp_hand = StringVar(root, '')

action = StringVar(root, '')

raiser = StringVar(root, '')

position = StringVar(root, '')
disp_position = StringVar(root, '')

frame = ttk.Frame(root, padding='2 2 2 2')
frame.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(frame, text='Hands').grid(column=0, row=0, sticky=W)
ttk.Button(frame, text='A', command=deal_ace).grid(column=0, row=1)
ttk.Button(frame, text='K', command=deal_king).grid(column=1, row=1)
ttk.Button(frame, text='Q', command=deal_queen).grid(column=2, row=1)
ttk.Button(frame, text='J', command=deal_jack).grid(column=3, row=1)
ttk.Button(frame, text='10', command=deal_ten).grid(column=4, row=1)
ttk.Button(frame, text='9', command=deal_nine).grid(column=0, row=2)
ttk.Button(frame, text='8', command=deal_eight).grid(column=1, row=2)
ttk.Button(frame, text='7', command=deal_seven).grid(column=2, row=2)
ttk.Button(frame, text='6', command=deal_six).grid(column=3, row=2)
ttk.Button(frame, text='5', command=deal_five).grid(column=4, row=2)
ttk.Button(frame, text='4', command=deal_four).grid(column=0, row=3)
ttk.Button(frame, text='3', command=deal_three).grid(column=1, row=3)
ttk.Button(frame, text='2', command=deal_two).grid(column=2, row=3)
ttk.Button(frame, text='Suited', command=is_suited).grid(column=3, row=3)
ttk.Button(frame, text='Clear', command=clear).grid(column=4, row=3)

ttk.Label(frame, text='Opponent').grid(column=0, row=4, sticky=W)
ttk.Button(frame, text='UTG', command=utg_raise).grid(column=0, row=5)
ttk.Button(frame, text='HJ', command=hj_raise).grid(column=1, row=5)
ttk.Button(frame, text='CO', command=co_raise).grid(column=2, row=5)
ttk.Button(frame, text='BTN', command=btn_raise).grid(column=3, row=5)
ttk.Button(frame, text='SB', command = sb_raise).grid(column=4, row=5)

ttk.Label(frame, text='Hand:').grid(column=0, row=6, sticky=W)
ttk.Label(frame, textvariable=disp_hand).grid(column=1, row=6, sticky=W)

ttk.Label(frame, text='Action:').grid(column=0, row=7, sticky=W)
ttk.Label(frame, textvariable=action).grid(column=1, row=7, sticky=W)

ttk.Label(frame, text='Raise:').grid(column=0, row=8, sticky=W)
ttk.Label(frame, textvariable=raiser).grid(column=1, row=8, sticky=W)

ttk.Label(frame, text='Position:').grid(column=0, row=9, sticky=W)
ttk.Label(frame, textvariable=disp_position).grid(column=1, row=9, sticky=W)

ttk.Button(frame, text='Play', command=play_hand).grid(column=3, row=9)
ttk.Button(frame, text='Next', command=next_hand).grid(column=4, row=9)
root.attributes('-topmost', True)

for child in frame.winfo_children():
    child.grid_configure(padx=1, pady=1)

root.mainloop()
