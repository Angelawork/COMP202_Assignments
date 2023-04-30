#name: Angela(Qingchen) Hu, McGill student ID: 261075832
import random
from treasure_utils import *

def generate_treasure_map_row(width, dimension):
    '''(int, bool) -> str
    Returns a single row of a treasure map which is created
    with the given width and dimension inputs. If dimension
    is set to False, each character has a 5/6 chance to be one of
    the MOVEMENT_SYMBOLS and a 1/6 chance to be an EMPTY_SYMBOL;
    if the dimension is set to True, then based on that, there's a
    a 50% chance for one character in the row to be replaced by
    one of the MOVEMENT_SYMBOLS_3D.
    
    >>> random.seed(2004)
    >>> generate_treasure_map_row(8, False)
    '><>.<<>v'
    >>> random.seed(2004)
    >>> generate_treasure_map_row(8, True)
    '><|.<<>v'
    >>> random.seed(3402)
    >>> generate_treasure_map_row(7, True)
    'v^v*v>^'
    '''
    treasure_map=''
    output=''
    if width==0:
        return output
    for i in range(width):
        chance_2d=random.randint(0,5)      
        if chance_2d<=4:
            treasure_map+=MOVEMENT_SYMBOLS[random.randint(0,3)]
        else:
            treasure_map+=EMPTY_SYMBOL
    output=treasure_map
    
    chance_3d=random.randint(0,1)
    if dimension and chance_3d:
        index=random.randint(0,width-1)
        chance_3d=random.randint(0,1)
        output=change_char_in_map(treasure_map, 0, index, MOVEMENT_SYMBOLS_3D[chance_3d], width, 1)     
    return output

def generate_treasure_map(width, height, dimension):
    '''(int, int, bool) -> str
    Returns a treasure map which is created with the given width,
    height and dimension inputs. The dimension boolean decides
    whether a MOVEMENT_SYMBOLS_3D would appear or not to create
    a 3D map. The map's first character always represents a
    right-pointing movement symbol. The rule of character generation
    would be the same as the function generate_treasure_map_row.
      
    >>> random.seed(2004)
    >>> generate_treasure_map(2, 3, False)
    '>><>.<'
    >>> random.seed(2004)
    >>> generate_treasure_map(2, 3, True)
    '>>*>.<'
    >>> random.seed(3402)
    >>> generate_treasure_map(3, 3, True)
    '>v^v>v>^*'
    '''
    if width!=0 and height!=0:
        treasure_map='>'
        treasure_map+=generate_treasure_map_row(width*height-1, dimension)
    else:
        treasure_map=''
    return treasure_map

def generate_3D_treasure_map(width, height, depth):
    '''(int, int, int) -> str
    Returns a 3D treasure map which is created with the
    given width, height and depth. The map's first character
    on the map's first depth would always represent a
    right-pointing movement symbol. The rule of character generation
    would be the same as the function generate_treasure_map_row.
    
    >>> random.seed(2004)
    >>> generate_3D_treasure_map(2, 3, 3)
    '>>*>.<>v<v*.^>><>v'
    >>> random.seed(2004)
    >>> generate_3D_treasure_map(1, 1, 1)
    '>'
    >>> random.seed(3500)
    >>> generate_3D_treasure_map(3, 3, 2)
    '>|<<<^>.v>^>^v^>^>'
    '''
    if width!=0 and height!=0 and depth!=0:
        output=generate_treasure_map(width, height, True)
        for i in range(depth-1):
            output+=generate_treasure_map_row(width*height, True)
    else:
        output=''
    return output

def follow_trail(treasure_map, row, col, dep_index, width, height, depth, tiles):
    '''(str, int, int, int, int, int, int, int) -> str
    Follows the character in the treasure_map starting at the given row,
    col and dep_index indices, as the width, height, and depth of the map
    is given. Stops until the number of tiles inputted is reached, or a
    tile previously encountered is reached. If tiles is set to -1, does
    not stop until reaches a tile previously encountered.
    Displays the amount of treasure collected and amount of symbols
    visited. Returns the travelled map with all visited movement symbols
    replaced by breadcrumb symbols.
    If the indices for the starting point are out of the map's bounds,
    the original treasure_map is returned.
    
    >>> follow_trail('>.v..<', 0, 2, 0, 3, 2, 1, 10)
    Treasures collected: 0
    Symbols visited: 4                     
    '>.X..X'
    >>> follow_trail('>+v^.<', 0, 2, 0, 3, 2, 1, 10)
    Treasures collected: 1
    Symbols visited: 6
    'X+XX.X'   
    >>> follow_trail('>+v..*..<...v.<*.|vvv+v+>.|', 0, 0, 0, 3, 3, 3, -1)
    Treasures collected: 1
    Symbols visited: 15
    'X+X..X..X...X.XX.Xvvv+v+X.X'
    '''
    treasures=0
    symbols=0
    i=(row*width+col)+(width*height*dep_index) 
    if row>=height or col>=width or dep_index>=depth:
        return treasure_map
    
    while tiles!=0 and treasure_map[i]!=BREADCRUMB_SYMBOL:
        if treasure_map[i]!=EMPTY_SYMBOL and treasure_map[i]!=TREASURE_SYMBOL:
            last_symbol=treasure_map[i]
            treasure_map=change_char_in_3D_map(treasure_map, row, col, dep_index, BREADCRUMB_SYMBOL, width, height, depth)            
        elif treasure_map[i]==TREASURE_SYMBOL:
            treasures+=1         
        
        if last_symbol==MOVEMENT_SYMBOLS[0]:
            col+=1
            col-=col*(col//width)
        elif last_symbol==MOVEMENT_SYMBOLS[1]:
            col-=width*((col-1)//width)+1
        elif last_symbol==MOVEMENT_SYMBOLS[2]:
            row+=1
            row-=row*(row//height)
        elif last_symbol==MOVEMENT_SYMBOLS[3]:
            row-=height*((row-1)//height)+1
        elif last_symbol==MOVEMENT_SYMBOLS_3D[0]:
            dep_index+=1
            dep_index-=dep_index*(dep_index//depth)
        elif last_symbol==MOVEMENT_SYMBOLS_3D[1]:
            dep_index-=depth*((dep_index-1)//depth)+1
            
        i=(row*width+col)+(width*height*dep_index)
        symbols+=1
        if tiles!=-1:
            tiles-=1               
    print('Treasures collected:', treasures)
    print('Symbols visited:', symbols)
    return treasure_map