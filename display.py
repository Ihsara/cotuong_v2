
class Display(object): 
    def __init__(self, set_side):

        #Define basics const for cheesboard
        _CHESSBOARD_LENGTH_WITH_BORDER = 10
        _CHESSBOARD_WIDTH_WITH_BORDER = 9
        _CHESSBOARD_LENGTH_WITHOUT_BORDER = 12
        _CHESSBOARD_WIDTH_WITHOUT_BORDER = 11
        #Define CLI display 
        _CHESSBOARD_SYMBOLS_FOR_HORIZONTAL_BORDER = '_'
        _CHESSBOARD_SYMBOLS_FOR_VERTICAL_BORDER = '|'
        _CHESSBOARD_SYMBOLS_FOR_CONRNER_BORDER = '#'
        _CHESSBOARD_SYMBOLS_FOR_EMPTY_INTERSECTION = '.'

        self.side_distribution = self.side_division(set_side)

    def display(self):
        pass

    def side_division(self, set_side):
        pass