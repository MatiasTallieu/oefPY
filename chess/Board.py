from Piece import *
class Board:
    def __init__(self):
        self.table = {
            'a1': Piece('Rw'), 'a2': Piece('pw'), 'a3': None, 'a4': None, 'a5': None, 'a6': None, 'a7': Piece('pb'), 'a8': Piece('Rb'),
            'b1': Piece('Nw'), 'b2': Piece('pw'), 'b3': None, 'b4': None, 'b5': None, 'b6': None, 'b7': Piece('pb'), 'b8': Piece('Nb'),
            'c1': Piece('Bw'), 'c2': Piece('pw'), 'c3': None, 'c4': None, 'c5': None, 'c6': None, 'c7': Piece('pb'), 'c8': Piece('Bb'),
            'd1': Piece('Qw'), 'd2': Piece('pw'), 'd3': None, 'd4': None, 'd5': None, 'd6': None, 'd7': Piece('pb'), 'd8': Piece('Qb'),
            'e1': Piece('Kw'), 'e2': Piece('pw'), 'e3': None, 'e4': None, 'e5': None, 'e6': None, 'e7': Piece('pb'), 'e8': Piece('Kb'),
            'f1': Piece('Bw'), 'f2': Piece('pw'), 'f3': None, 'f4': None, 'f5': None, 'f6': None, 'f7': Piece('pb'), 'f8': Piece('Bb'),
            'g1': Piece('Nw'), 'g2': Piece('pw'), 'g3': None, 'g4': None, 'g5': None, 'g6': None, 'g7': Piece('pb'), 'g8': Piece('Nb'),
            'h1': Piece('Rw'), 'h2': Piece('pw'), 'h3': None, 'h4': None, 'h5': None, 'h6': None, 'h7': Piece('pb'), 'h8': Piece('Rb')
        }
    
    def set_piece(self,piece,destination):
        if(isinstance(piece,Piece)):
            self.table[destination] = piece
        elif(piece == None):
            self.table[destination] = None
    
    def get_piece(self,adress):
            myPiece = self.table[adress]
            if (isinstance(myPiece,Piece)):
                return myPiece
            



            
    def display_board_state(self):
        myArray = []
        ans = ''
        for key , val  in self.table.items():
            piece = self.get_piece(key)
            if piece != None:
                myArray.append(piece.code)
            else:
                myArray.append(None)
        count =1
        posPrint = 7
        for i in range (8,0,-1):
             ans+= str(i)+ ': '
             for j in range(8):
                index =posPrint
                if(myArray[index]!= None):
                    ans+=" "+str(myArray[index])+ " |"
                else:
                    ans+="    |"
                posPrint = posPrint+7+1
             
                if j ==7:
                    count+=1
                    posPrint = (8-count)
                    ans+='\n'  
                    if i ==1:
                      ans+=  '    a     b    c    d    e    f    g    h'

        return ans



    def move_piece(self,start,end):
        piece = self.get_piece(start)
        piece2 = self.get_piece(end)
        if(piece == None):
            raise ValueError('Illegal move: no piece at start position')
        if(isinstance(piece,Piece) and isinstance(piece2, Piece)):
            if( piece.player != piece2.player):
                self.set_piece(None,start)
                self.set_piece(piece,end)
            else:
                raise ValueError('Illegal move: cannot move to friendly territory')
        else:
                self.set_piece(None,start)
                self.set_piece(piece,end)


    def process_movements(self,movements):
            for start,end  in movements:
                self.move_piece(start,end)

    def read_movement_file(self,file):
        with open(f"C://Users/matia/Downloads/Examenopgaves/chess/{file}",'r',encoding='utf-8') as File:
            lines= File.readlines()
            MyList = []
            for line in lines:
                start = line[0:2]
                end = line[5:len(line)-1]
                MyList.append((start,end))

        return MyList

    def save_state(self,file):
        with open(f"C://Users/matia/Downloads/Examenopgaves/chess/{file}",'w+',encoding='utf-8') as File:
            Lines = self.display_board_state()
            File.writelines(Lines)


    def process_chess_moves(self,movements,output):
        self.process_movements(self.read_movement_file(movements))
        self.save_state(output)




board = Board()

print(board.display_board_state())
board.process_chess_moves('movements.txt', 'output.txt')
print(board.display_board_state())
