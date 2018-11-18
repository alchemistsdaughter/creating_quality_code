# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:36:05 2018

@author: anna.whitehouse
"""
import doctest

# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """A rat caught in a maze"""
    def __init__(self, symbol, row, col, num_sprouts_eaten=0):
        """ (Rat, str, int, int) -> NoneType
        
        Initialize instance of Rat with a 1-character symbol for the rat, the row \ 
        where the rat is located, and the column where the rat is located.
        
        >>> paul = Rat('P', 1, 4, 0)
        >>> paul.symbol
        'P'
        >>> paul.row
        1
        >>> paul.col
        4
        >>> paul.num_sprouts_eaten
        0
        """
        
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten


    # Write your Rat methods here.
    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType
        
        Set the Rat's row and col instance variables to the given row and column
        
        >>> paul = Rat('P', 1, 4, 0)
        >>> paul.set_location(1, 2)
        >>> paul.row
        1
        >>> paul.col
        2
        """
        
        self.row = row
        self.col = col
    
    def eat_sprout(self):
        """(Rat) --> NoneType
        
        The first parameter represents a rat. Add one to the rat's instance variable
        
        >>> paul = Rat('P', 1, 4, 0)
        >>> paul.eat_sprout()
        >>> paul.num_sprouts_eaten
        1
        """
        
        self.num_sprouts_eaten += 1
        
    def __str__(self):
        """(Rat) -> str
        
        String representation of the rat in this format: symbol at (row,col) ate num_sprouts_eaten sprouts.
        
        >>> paul = Rat('P', 1, 4, 0)
        >>> paul.__str__()
        'P at (1, 4) ate 0 sprouts'
        >>> paul.eat_sprout()
        >>> paul.__str__()
        'P at (1, 4) ate 1 sprouts'
        """
        
        return '{0} at ({1}, {2}) ate {3} sprouts'.format(
                self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze_list, rat1, rat2):
        """(Maze, list, Rat, Rat) -> NoneType
        Initialize the mze; contents of the maze; first rat in the maze; second rat in the maze
        
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ... ['#', '.', '.', '.', '.', '.', '#'],
        ... ['#', '.', '#', '#', '#', '.', '#'],
        ... ['#', '.', '.', '@', '#', '.', '#'],
        ... ['#', '@', '#', '.', '@', '.', '#'],
        ... ['#', '#', '#', '#', '#', '#', '#']],
        ... Rat('J', 1, 1), Rat('P', 1, 4))
        """
        
        self.maze_list = maze_list
        self.rat1 = rat1
        self.rat2 = rat2
               
        count = 0
        for line in maze_list:
            for n in line:
                if n == SPROUT:
                    count += 1
        
        self.num_sprouts_left = count
        
    def is_wall (self, row, col):      
        if self.maze_list[row][col] == WALL:
            return True
        else:
            return False
    
    def get_character(self, row, col):
        """ (Maze) -> ch """
        if self.rat1.row == row and self.rat1.col == col:
            return self.rat1.symbol
        if self.rat2.row == row and self.rat2.col == col:
            return self.rat2.symbol
        return self.maze_list[row][col]
    
    def move(self, rat, verticalchange, horizontalchange):
        """ (Maze, Rat, int, int) -> NoneType
        Moves the rat in a given direction, unless there is a wall in the way. Also, check for Brussels sprouts at this location.
        If present have the rat eat the Brussels sprout; make that location a HALL; decrease the value that num_sprouts_left refers to by one;
        return True iff there wasn't a wall in the way
        
        >>> rat1 = Rat('J', 1, 1)
        >>> rat2 = Rat('P', 1, 4)
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ... ['#', '.', '.', '.', '.', '.', '#'],
        ... ['#', '.', '#', '#', '#', '.', '#'],
        ... ['#', '.', '.', '@', '#', '.', '#'],
        ... ['#', '@', '#', '.', '@', '.', '#'],
        ... ['#', '#', '#', '#', '#', '#', '#']],
        ... rat1, rat2)
        >>> maze.move(rat1, DOWN, NO_CHANGE)
        True
        >>> maze.get_character(2, 1)
        'J'
        >>> maze.get_character(1, 1)
        '.'
        """
               
        if verticalchange != NO_CHANGE:
            rat.set_location(rat.row + verticalchange, rat.col) #moving the rate
            if self.maze_list[rat.row + verticalchange][rat.col] == SPROUT:
                rat.eatsprout()
                self.num_sprouts_left -=1
                self.maze_list[rat.row + verticalchange][rat.col] = HALL
            self.maze_list[rat.row][rat.col] = HALL #changing the rat's previous location to a hall
            
        if horizontalchange != NO_CHANGE:
            rat.set_location(rat.row, rat.col + horizontalchange) #moving the rate
            if self.maze_list[rat.row][rat.col + horizontalchange] == SPROUT:
                rat.eatsprout()
                num_sprouts_left -=1
                self.maze_list[rat.row][rat.col + horizontalchange] = HALL
            self.maze_list[rat.row][rat.col] = HALL #changing the rat's previous location to a hall            
        
        return True
        
# =============================================================================
#     def __str__(self):
#         """ (Maze) -> str"""
#         
#         Returns a string representation of the maze.
#         maze = Maze(
#         #######
#         #J..P.#
#         #.###.#
#         #..@#.#
#         #@#.@.#
#         #######
#         , J at (1, 1) ate 0 sprouts
#         , P at (1, 4) ate 0 sprouts)
# 
# =============================================================================

if __name__ == '__main__':
# =============================================================================
#     paul = Rat("P", 1, 4, 0)
#     jen = Rat("J", 1, 1, 0)
# =============================================================================
    
    doctest.testmod()
    