class Piece:
    def __init__(self,input):
            self.code = input
            self.kind = input[:1]
            self.player = input[1:]


