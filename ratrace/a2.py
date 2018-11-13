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
    def __init__(self, maze, rat1, rat2):
        """(Maze, list of list of str, Rat, Rat) --> NoneType
        maze to be initialized; rat1 is the first rat in the maze; rat2 is the second rat in the maze
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \ 
        ['#', '.', '.', '.', '.', '.', '#'], \
        ['#', '.', '#', '#', '#', '.', '#'], \
        ['#', '.', '.', '@', '#', '.', '#'], \ 
        ['#', '@', '#', '.', '@', '.', '#'], \ 
        ['#', '#', '#', '#', '#', '#', '#']], \
        Rat("J", 1, 1, 0), Rat("P", 1, 4, 0))
        >>> maze.maze
        [['#', '#', '#', '#', '#', '#', '#'],\ 
        ['#', '.', '.', '.', '.', '.', '#'],\ 
        ['#', '.', '#', '#', '#', '.', '#'],\ 
        ['#', '.', '.', '@', '#', '.', '#'],\ 
        ['#', '@', '#', '.', '@', '.', '#'],\ 
        ['#', '#', '#', '#', '#', '#', '#']]
        >>> maze.rat2.symbol
        'P'
        >>> maze.rat1.column
        1
        >>> maze.num_sprouts_left
        3
        """
        
        self.maze = maze
        self.rat1 = rat1
        self.rat2 = rat2
        
        count = 0
        for i in range(0, len(maze)):
            for n in range(0, len(maze[0])):
                if self.maze[i][n] == SPROUT:
                    count += 1
        
        self.num_sprouts_left = count
# =============================================================================
#         
#     def is_wall (self, row, col):
#         """ (Maze, int, int) -> bool
#         
#         Maze is the maze; row is the row; col is the col. Returns true iff there is a wall at the given row and column of the maze
#         >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
#         ['#', '.', '.', '.', '.', '.', '#'],
#         ['#', '.', '#', '#', '#', '.', '#'],
#         ['#', '.', '.', '@', '#', '.', '#'],
#         ['#', '@', '#', '.', '@', '.', '#'],
#         ['#', '#', '#', '#', '#', '#', '#']],
#         Rat("J", 1, 1, 0), 
#         Rat("P", 1, 4, 0))
#         >>> maze.is_wall (0,0)
#         True
#         >>> maze.is_wall(1, 2)
#         False
#         >>> maze.is_wall(3, 3)
#         False
#         """
#         
#         if self.maze[row][col] == WALL:
#             return True
#         else:
#             return False
#         
# =============================================================================
        

if __name__ == '__main__':
# =============================================================================
#     paul = Rat("P", 1, 4, 0)
#     jen = Rat("J", 1, 1, 0)
# =============================================================================
    
    doctest.testmod()
    