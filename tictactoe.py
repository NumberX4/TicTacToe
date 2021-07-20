#TIC TAC TOE
    
tictac=[1,2,3,4,5,6,7,8,9]
import random
#function to print the box
def ticte(tictac=[]):
	    print('______')
	    print('|',end='')
	    print(tictac[0],end='')
	    print(tictac[1],end='')
	    print(tictac[2],end='')
	    print('|')
	    print('|',end='')
	    print(tictac[3],end='')
	    print(tictac[4],end='')
	    print(tictac[5],end='')
	    print('|')
	    print('|',end='')
	    print(tictac[6],end='')
	    print(tictac[7],end='')
	    print(tictac[8],end='')
	    print('|')
	    print('______')


#func. to determine if someone won
def winner(tictac=[]):
    if(tictac[0]==tictac[1] and tictac[1]==tictac[2] and tictac[0]=='X'):#012
       return 2;
    if(tictac[0]==tictac[3] and tictac[3]==tictac[6] and tictac[0]=='X'):#036
       return 2;
    if(tictac[0]==tictac[4] and tictac[4]==tictac[8] and tictac[0]=='X'):#048
       return 2;
    if(tictac[3]==tictac[4] and tictac[4]==tictac[5] and tictac[3]=='X'):#345
       return 2;
    if(tictac[6]==tictac[7] and tictac[7]==tictac[8] and tictac[6]=='X'):#678
       return 2;
    if(tictac[1]==tictac[7] and tictac[7]==tictac[4] and tictac[4]=='X'):#147
       return 2;
    if(tictac[2]==tictac[5] and tictac[5]==tictac[8] and tictac[5]=='X'):#258
       return 2;
    if(tictac[2]==tictac[4] and tictac[4]==tictac[6] and tictac[6]=='X'):#246
       return 2;
    if(tictac[0]==tictac[1] and tictac[1]==tictac[2] and tictac[0]=='O'):#012o
       return 1;
    if(tictac[0]==tictac[3] and tictac[3]==tictac[6] and tictac[0]=='O'):#036o
       return 1;
    if(tictac[0]==tictac[4] and tictac[4]==tictac[8] and tictac[0]=='O'):#048o
       return 1;  
    if(tictac[6]==tictac[7] and tictac[7]==tictac[8] and tictac[6]=='O'):#678o
       return 1;
    if(tictac[3]==tictac[4] and tictac[4]==tictac[5] and tictac[3]=='O'):#345o
       return 1;
    if(tictac[1]==tictac[7] and tictac[7]==tictac[4] and tictac[4]=='O'):#147o
       return 1;
    if(tictac[2]==tictac[5] and tictac[5]==tictac[8] and tictac[5]=='O'):#258o
       return 1;
    if(tictac[2]==tictac[4] and tictac[4]==tictac[6] and tictac[6]=='O'):#2460
        return 1;
    else:
       return 0;

#multiplayer
def play(tictac=[]):
     while True:
             ticte(tictac)
             print('Player 1s turn')
             a=input()
             a=int(a)
             tictac[a-1]='X'
             ticte(tictac)
             if winner(tictac)==2:
                     print('Player 1 wins \n')
                     break
             if(tictac[0]!=1 and tictac[1]!=2 and tictac[2]!=3 and tictac[3]!=4 and tictac[4]!=5 and tictac[5]!=6 and tictac[6]!=7 and tictac[7]!=8 and tictac[8]!=9):
                     print('draw')
                     break
             print('Player 2s turn')
             
             a=input()
             a=int(a)
             tictac[a-1]='O'
             
             if winner(tictac)==1:
                     print('Player 2 wins \n')
                     break
             if(tictac[0]!=1 and tictac[1]!=2 and tictac[2]!=3 and tictac[3]!=4 and tictac[4]!=5 and tictac[5]!=6 and tictac[6]!=7 and tictac[7]!=8 and tictac[8]!=9):
                     print('draw')
                     break
#easy
def play2(tictac=[]):
    tictac2=[1,2,3,4,5,6,7,8,9]
    while True:
        ticte(tictac)
        
        print('Player 1s turn')
        a=input()
        a=int(a)
        tictac[a-1]='X'
        ticte(tictac)

        tictac2.remove(a)
        if winner(tictac)==2:
                     print('Player 1 wins \n')
                     break
        if(tictac[0]!=1 and tictac[1]!=2 and tictac[2]!=3 and tictac[3]!=4 and tictac[4]!=5 and tictac[5]!=6 and tictac[6]!=7 and tictac[7]!=8 and tictac[8]!=9):
                     print('draw')
                     break
        x=random.randint(0,len(tictac2)-1)
        tictac[tictac2[x]-1]='O'
        tictac2[x]='O'
        tictac2.remove('O')
        print("Computer playing")
        
        if winner(tictac)==1:
                     ticte(tictac)
                     print('Computer wins \n')
                     break
        if(tictac[0]!=1 and tictac[1]!=2 and tictac[2]!=3 and tictac[3]!=4 and tictac[4]!=5 and tictac[5]!=6 and tictac[6]!=7 and tictac[7]!=8 and tictac[8]!=9):
                     print('draw')
                     break
#medium
def play3(tictac=[]):
    tictac2=[1,2,3,4,5,6,7,8,9]
    while True:
        ticte(tictac)
        
        print('Player 1s turn')
        a=input()
        a=int(a)
        tictac[a-1]='X'
        ticte(tictac)

        tictac2.remove(a)
        if winner(tictac)==2:
                     print('Player 1 wins \n')
                     break
        if(tictac[0]!=1 and tictac[1]!=2 and tictac[2]!=3 and tictac[3]!=4 and tictac[4]!=5 and tictac[5]!=6 and tictac[6]!=7 and tictac[7]!=8 and tictac[8]!=9):
                     print('draw')
                     break
#alpha
        for y in range(0,len(tictac2)-1):
            z=0
            m=tictac[tictac2[y]-1]
            tictac[tictac2[y]-1]='O'
            if winner(tictac)==1:
                x=y
                tictac[tictac2[y]-1]=m
                z=1
                break
            tictac[tictac2[y]-1]='X'
            if winner(tictac)==2:
                x=y
                tictac[tictac2[y]-1]=m
                z=1
                break
                
            tictac[tictac2[y]-1]=m
                
        if z==0:
            x=random.randint(0,len(tictac2)-1)
        
#beta

        
        tictac[tictac2[x]-1]='O'
        tictac2[x]='O'
        tictac2.remove('O')
        print("Computer playing")
        if winner(tictac)==1:
                     ticte(tictac)
                     print('Computer wins \n')
                     break
        if(tictac[0]!=1 and tictac[1]!=2 and tictac[2]!=3 and tictac[3]!=4 and tictac[4]!=5 and tictac[5]!=6 and tictac[6]!=7 and tictac[7]!=8 and tictac[8]!=9):
                     print('draw')
                     break
#hard                    
def play4(tictac=[]):
    
    
    x=0
    tictac[6]='O'
    print("Computer playing first")
    while True:
        ticte(tictac)
        
        print('Player 1s turn')
        a=input()
        a=int(a)
        tictac[a-1]='X'
        ticte(tictac)

        if a==2 or a==4 or a==6:
            tictac[8]='O'
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a=input()
            a=int(a)
            tictac[a-1]='X'
            ticte(tictac)
            if a!=8:
                tictac[7]='O'
                print("Computer playing")
                ticte(tictac)
                print("Computer wins")
                break
            if a==8:
                tictac[4]='O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a=input()
                a=int(a)
                tictac[a-1]='X'
                ticte(tictac)
                if a==1:
                    tictac[2]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if a!=1:
                    tictac[0]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                    
        elif a==1 or a==3:
            tictac[8]='O'
            b=a
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a=input()
            a=int(a)
            tictac[a-1]='X'
            ticte(tictac)
            if a!=8:
                tictac[7]='O'
                print("Computer playing")
                ticte(tictac)
                print("Computer wins")
                break
            if a==8:
                tictac[3-b]='O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a=input()
                a=int(a)
                tictac[a-1]='X'
                ticte(tictac)
                if a!=5:
                    tictac[4]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if a==5:
                    tictac[6-b]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                    
        elif a==8:
            tictac[0]='O'
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a=input()
            a=int(a)
            tictac[a-1]='X'
            ticte(tictac)
            if a!=4:
                tictac[3]='O'
                print("Computer playing")
                ticte(tictac)
                print("Computer wins")
                break
            if a==4:
                tictac[2]='O'
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a=input()
                a=int(a)
                tictac[a-1]='X'
                ticte(tictac)
                if a==2:
                    tictac[4]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if a!=2:
                    tictac[1]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break        
                
        elif a==9:
            tictac[0]='O'
            
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a=input()
            a=int(a)
            tictac[a-1]='X'
            ticte(tictac)
            if a!=4:
                tictac[3]='O'
                print("Computer playing")
                ticte(tictac)
                print("Computer wins")
                break
            if a==4:
                tictac[2]='O'            
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a=input()
                a=int(a)
                tictac[a-1]='X'
                ticte(tictac)
                if a!=5:
                    tictac[4]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if a==5:
                    tictac[1]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                
        else:
            tictac[2]='O'            
            print("Computer playing")
            ticte(tictac)
            print('Player 1s turn')
            a=input()
            a=int(a)
            tictac[a-1]='X'
            ticte(tictac)
            if a==2 or a==4 or a==6 or a==8:
                tictac[9-a]='O'            
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a=input()
                a=int(a)
                tictac[a-1]='X'
                ticte(tictac)
                if True:
                    tictac[9-a]='O'            
                    print("Computer playing")
                    ticte(tictac)
                    if winner(tictac)==1:
                        
                        print('Computer wins')
                        break
                    if(tictac[0]!=1 and tictac[1]!=2 and tictac[2]!=3 and tictac[3]!=4 and tictac[4]!=5 and tictac[5]!=6 and tictac[6]!=7 and tictac[7]!=8 and tictac[8]!=9):
                        print('draw')
                        break
                    print('Player 1s turn')
                    a=input()
                    a=int(a)
                    tictac[a-1]='X'
                    ticte(tictac)
                    if True:
                       tictac[9-a]='O'            
                       print("Computer playing")
                       ticte(tictac)
                       if winner(tictac)==1:
                        
                          print('Computer wins')
                          break
                       if(tictac[0]!=1 and tictac[1]!=2 and tictac[2]!=3 and tictac[3]!=4 and tictac[4]!=5 and tictac[5]!=6 and tictac[6]!=7 and tictac[7]!=8 and tictac[8]!=9):
                          print('draw')
                          break
            if a==1 or a==9:
                b=a
                tictac[9-a]='O'            
                print("Computer playing")
                ticte(tictac)
                print('Player 1s turn')
                a=input()
                a=int(a)
                tictac[a-1]='X'
                ticte(tictac)
                if b==9 and a!=2:
                    tictac[1]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if b==9 and a==2:
                    tictac[3]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if b==1 and a!=8:
                    tictac[6]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                if b==1 and a==8:
                    tictac[5]='O'
                    print("Computer playing")
                    ticte(tictac)
                    print("Computer wins")
                    break
                
                
def playit():
    while True:
        g=input('''

TIC-TAC-TOE
if you want to play multiplayer, press 1
if you want to play single player-
a)easy press 2,
b)medium press 3,
c)hard, press 4,
and anything else to exit: \n''')
        tictac=[1,2,3,4,5,6,7,8,9]
        
        if g=='1':
           play(tictac)
        elif g=='2':
           play2(tictac)
        elif g=='3':
           play3(tictac)
        elif g=='4':
           play4(tictac)
        else:
            break
    


   
if __name__== "__main__":
	playit()
	
        

        
