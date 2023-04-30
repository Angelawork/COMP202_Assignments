#name: Angela(Qingchen) Hu, McGill student ID: 261075832
MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

def get_nth_row_from_map(treasure_map, n, width, height):
    '''(str, int, int, int) -> str
    Returns the treasure map's nth row given its width and height.
    If the nth row is not valid, an empty string is returned.
    
    >>> get_nth_row_from_map('^..>v>..v', 3, 3, 3)
    ''
    >>> get_nth_row_from_map('>.+>.^..<', 2, 3, 3)
    '..<'
    >>> get_nth_row_from_map('>...<<', 1, 2, 3)
    '>.'
    '''
    output=''
    index=n*width
    
    if n<height:
        for i in range(width):
            output+=treasure_map[index]
            index+=1
    return output

def print_treasure_map(treasure_map, width, height):
    '''(str, int, int) -> NoneType
    Displays a treasure map line by line, with each line
    representing one row as the map's width and height are
    given.
    
    >>> print_treasure_map('<..v>v..^', 3, 3)
    <..
    v>v
    ..^
    >>> print_treasure_map('^..>>>..', 4, 2)
    ^..>
    >>..
    >>> print_treasure_map('<.>v.v', 6, 1)
    <.>v.v
    '''
    for i in range(height):
        nth_row=get_nth_row_from_map(treasure_map, i, width, height)
        print(nth_row)
        
def change_char_in_map(treasure_map, row, col, char, width, height):
    '''(str, int, int, str, int, int) -> str
    Returns a given treasure map string's copy with the character
    at given row and col index replaced by the given char, as the
    map's width and height are given.
    If both indices or one of them are given as out of bounds of
    the map's width and height, the treasure map is returned unchanged.
    
    >>> change_char_in_map('.>....<..', 1, 1, 'X', 3, 3)
    '.>..X.<..'
    >>> change_char_in_map('.>....<..', 5, 6, 'X', 3, 3)
    '.>....<..'
    >>> change_char_in_map('.>v>', 0, 1, 'X', 2, 2)
    '.Xv>'
    '''
    output=''
    if (not row>=height) and (not col>=width):
        for i in range(len(treasure_map)):
            if i==row*width+col:
                output+=char
            else:
                output+=treasure_map[i]
    else:
        output=treasure_map
    return output

def get_proportion_travelled(treasure_map):
    '''(str) -> float
    Returns the percentage of the travelled portion in
    the given treasure_map string, rounded to 2 decimal
    places. The travelled portion is represented by the
    BREADCRUMB_SYMBOL.
    
    >>> get_proportion_travelled('.X.')
    0.33
    >>> get_proportion_travelled('XX')
    1.0
    >>> get_proportion_travelled('..')
    0.0
    '''
    count=0
    length=len(treasure_map)
       
    if length!=0:
        for i in range(length):
            if treasure_map[i]==BREADCRUMB_SYMBOL:
                count+=1
        result=round(count/length,2)
    else:
        result=0
    return result

def get_nth_map_from_3D_map(treasure_map, n, width, height, depth):
    '''(str, int, int, int, int) -> str
    Returns the map on the nth depth of a given 3D treasure map.
    as the map's width, height and depth are given. An empty string
    is returned if the given n is an invalid depth index.

    >>> get_nth_map_from_3D_map('.X.>>>.X..v.vX>.v.', 1, 3, 3, 2)
    '.v.vX>.v.'
    >>> get_nth_map_from_3D_map('.X.>>>.X..v.vX>.v.', 3, 3, 3, 2)
    ''
    >>> get_nth_map_from_3D_map('.X.>>>.X', 0, 2, 2, 2)
    '.X.>'
    '''
    output=''
    index=n*width*height
    
    if not n>=depth:
        for i in range(width*height):
            output+=treasure_map[index]
            index+=1
    return output

def print_3D_treasure_map(treasure_map, width, height, depth):
    '''(str, int, int, int) -> NoneType
    Displays a 3D treasure map with rows on their lines, with maps
    on different depth indices separated by a blank line, as the
    map's width, height and depth are given.
    
    >>> print_3D_treasure_map('.X.>>>.X', 2, 2, 2)
    .X
    .>

    >>
    .X
    >>> print_3D_treasure_map('.X.>>>.X..v.....v.', 3, 3, 2)
    .X.
    >>>
    .X.

    .v.
    ...
    .v.
    >>> print_3D_treasure_map('.X.>>>.X.', 3, 3, 1)
    .X.
    >>>
    .X.
    '''
    if len(treasure_map)!=0:
        for i in range(depth):
            nth_map=get_nth_map_from_3D_map(treasure_map, i, width, height, depth)
            print_treasure_map(nth_map, width, height)
            if (i+1)!=depth:
                print()
    else:
        print(end='')
        
def change_char_in_3D_map(treasure_map, row, col, dep_index, char, width, height, depth):
    '''(str, int, int, int, str, int, int, int) -> str
    Returns a given 3D treasure map string's copy with the character
    at given row, col and dep_index indices replaced by the given char,
    as the map's width, height and depth are given.
    If both indices or one of them are given as out of bounds of the
    map's width, height and depth, the 3D treasure map is returned
    unchanged.
    
    >>> change_char_in_3D_map('.X.>v>.X..v.vXv.v.', 1, 1, 1, '#', 3, 3, 2)
    '.X.>v>.X..v.v#v.v.'
    >>> change_char_in_3D_map('.X.>v>.X..v.vXv.v.', 1, 1, 3, '#', 3, 3, 2)
    '.X.>v>.X..v.vXv.v.'
    >>> change_char_in_3D_map('>v.>.>..', 1, 1, 0, 'X', 2, 2, 2)
    '>v.X.>..'
    '''
    output=''
    if row>=height or col>=width or dep_index>=depth:
        output=treasure_map
        
    else:
        for i in range(len(treasure_map)):
            if i==(row*width+col)+(width*height*dep_index):
                output+=char
            else:
                output+=treasure_map[i]
    return output