
lis = [1,2,3,4,5,6,7,8,9]
p1 = input("Whats player name?:")
p2 = input("Whats player name?:")
playr = p1
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
jkl = 0
selected = []

while jkl==0:
    print("\n\t\t Tic_Tac_Toe")
    print(f"\n\t\t {lis[0]} | {lis[1]} | {lis[2]}")
    print("\t\t ---------")
    print(f"\t\t {lis[3]} | {lis[4]} | {lis[5]}")
    print("\t\t ---------")
    print(f"\t\t {lis[6]} | {lis[7]} | {lis[8]}")
    uio = int(input(f"\n\t\t {playr} turn:"))
    if len(selected)==9:
        print("No one won")
        break
    if uio not in selected:
        selected.append(uio)
        if playr == p1:
            playr = p2
            lis[uio-1] = 'X'
            
        else:
            playr = p1
            lis[uio-1] = 'O'
        for a,b,c in wins:
            if lis[a]==lis[b] and lis[b]==lis[c]:
                print(f"\n\t\t {playr} Wins!!!!!!!!")
                jkl = 1
                print(f"\n\t\t {lis[0]} | {lis[1]} | {lis[2]}")
                print("\t\t ---------")
                print(f"\t\t {lis[3]} | {lis[4]} | {lis[5]}")
                print("\t\t ---------")
                print(f"\t\t {lis[6]} | {lis[7]} | {lis[8]}")
    else:
        print("\n\t\t Already Selected Area, No Cheating")
    
    
