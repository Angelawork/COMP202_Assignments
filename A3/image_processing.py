#name: Angela(Qingchen) Hu, McGill student ID: 261075832

def is_valid_image(my_list):
    '''(list<list>) -> bool 
    Returns True if a valid(non-compressed) PGM image matrix
    is represented by the inputted my_list. False is returned
    in other situations.
    
    >>> is_valid_image([[-1,0,0], [0,0,0]])
    False
    >>> is_valid_image([[23,45], [230,0]])
    True
    >>> is_valid_image([[255], [0,0]])
    False
    '''
    result=True
    row_length=len(my_list[0])
    
    for row in my_list:
        if len(row)!=row_length:
            result=False
        for item in row:
            if type(item)!=int or (item<0 or item>255):
                result=False
    return result

def is_valid_compressed_image(my_list):
    '''(list<list>) -> bool
    Returns True if a valid compressed PGM image matrix
    is represented by the inputted my_list. False is returned
    in other situations.
    
    >>> is_valid_compressed_image([["0x3", "230x2"], ["255x5"]])
    True
    >>> is_valid_compressed_image([[67, 22], [0,55]])
    False
    >>> is_valid_compressed_image([['67x', 22], [0,'55']])
    False
    '''
    result=True
    first_row=True
    for row in my_list:
        sum_b=0
        for i in range(len(row)):
            if type(row[i])!=str or row[i].count('x')!=1:
                return False
            for j in row[i]:
                if j not in '0123456789x':
                    return False
            numbers=row[i].split('x')
            if '' in numbers or (int(numbers[0])<0 or int(numbers[0])>255) or (int(numbers[1])<=0):
                return False
            
            sum_b+=int(numbers[1])
        if first_row:
            previous_sum_b=sum_b
            first_row=False 
        if previous_sum_b!=sum_b:
            result=False   
    return result

def load_regular_image(my_file):
    '''(str) -> list<list<int>>
    Loads and returns the inputted my_file as an image
    matrix, which is a nested list containing integers.
    A AssertionError is raised if during or after loading
    the image matrix generated is not in PGM format.
    
    >>> fobj=open('test1.txt','w')
    >>> fobj.write("a\\nb\\nc\\nd")
    7
    >>> fobj.close()
    >>> load_regular_image('test1.txt')
    Traceback (most recent call last):
    AssertionError: The inputted my_file is invalid as it's not in PGM format.
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> fobj=open('test2.pgm.compressed','w')
    >>> fobj.write("P2C\\n1 1\\n255\\n0x1")
    15
    >>> fobj.close()
    >>> load_regular_image('test2.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: The inputted my_file is invalid as it's not in PGM format.
    '''
    item=[]
    fobj=open(my_file,'r')
    for line in fobj:
        item.append([line])
    fobj.close()

    output=[]
    valid_content=[['P2\n'], [], ['255\n']]
    for i in range(0,3,2):
        if item[i] != valid_content[i]:
            raise AssertionError('The inputted my_file is invalid as'
            " it's not in PGM format.")
        
    file_info=item[1][0].strip('\n').split(' ')
    for char in file_info:
        if not char.isdecimal() or len(file_info)!=2:
            raise AssertionError('The inputted my_file is invalid as'
            " it's not in PGM format.")
        
    row_length=int(file_info[0])
    for element in item[3:]:
        string_list=element[0].strip().split(' ')
        row=[]
        for char in string_list:
            if not char.isdecimal() and char!='':
                raise AssertionError('The inputted my_file is invalid as'
                " it's not in PGM format.")
            elif char!='':
                row.append(int(char))
        if len(row)!=row_length:
            raise AssertionError('The inputted my_file is invalid as'
            " it's not in PGM format.")
        output.append(row)
        
    if len(output)!=int(file_info[1]):
        raise AssertionError('The inputted my_file is invalid as'
        " it's not in PGM format.")
    return output

def load_compressed_image(my_file):
    '''(str) -> list<list<str>>
    Loads and returns the inputted my_file as a
    compressed image matrix, which is a nested
    list containing strings. A AssertionError is raised
    if during or after loading the image matrix
    generated is not in compressed PGM format.
    
    >>> fobj=open('test1.txt','w')
    >>> fobj.write("a\\nb\\nc\\nd")
    7
    >>> fobj.close()
    >>> load_compressed_image('test1.txt')
    Traceback (most recent call last):
    AssertionError: The inputted my_file is invalid as it's not in compressed PGM format.
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> fobj=open('test2.pgm.compressed','w')
    >>> fobj.write("P2C\\n1 1\\n255\\n0x1")
    15
    >>> fobj.close()
    >>> load_compressed_image('test2.pgm.compressed')
    [['0x1']]
    '''
    item=[]
    fobj=open(my_file,'r')
    for line in fobj:
        item.append([line])
    fobj.close()

    output=[]
    valid_content=[['P2C\n'], [], ['255\n']]
    for i in range(0,3,2):
        if item[i] != valid_content[i]:
            raise AssertionError('The inputted my_file is invalid as'
            " it's not in compressed PGM format.")
        
    file_info=item[1][0].strip('\n').split(' ')
    for char in file_info:
        if not char.isdecimal() or len(file_info)!=2:
            raise AssertionError('The inputted my_file is invalid as'
            " it's not in compressed PGM format.")
    
    row_length=int(file_info[0])
    for element in item[3:]:
        string_list=element[0].strip().split(' ')
        if not is_valid_compressed_image([string_list]):
            raise AssertionError('The inputted my_file is invalid as'
            " it's not in compressed PGM format.")
        row=[]
        count=0
        for char in string_list:
            if char!='':
                row.append(char)
                count+=int(char.split('x')[1])
        if count!=row_length:
            raise AssertionError('The inputted my_file is invalid as'
            " it's not in compressed PGM format.")
        output.append(row)
        
    if len(output)!=int(file_info[1]):
        raise AssertionError('The inputted my_file is invalid as'
        " it's not in compressed PGM format.")
    return output

def load_image(my_file):
    '''(str) -> list<list>
    In the inputted my_file, if the first line is
    'P2', loads and returns the inputted my_file as a
    image matrix; if the first line is 'P2C', loads
    and returns the inputted my_file as a compressed
    image matrix. In other scenarios, a AssertionError is
    raised.
    
    >>> load_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> fobj=open('test1.txt','w')
    >>> fobj.write("a\\nb\\nc\\nd")
    7
    >>> fobj.close()
    >>> load_image('test1.txt')
    Traceback (most recent call last):
    AssertionError: The inputted my_file is invalid as it's neither in PGM format or compressed PGM format.
    >>> fobj=open('test2.pgm.compressed','w')
    >>> fobj.write("P2C\\n1 1\\n255\\n0x1 ABC")
    19
    >>> fobj.close()
    >>> load_image('test2.pgm.compressed')
    Traceback (most recent call last):
    AssertionError: The inputted my_file is invalid as it's not in compressed PGM format.
    >>> fobj=open('test3.pgm','w')
    >>> fobj.write("P2\\n1 1\\n255\\nABC")
    14
    >>> fobj.close()
    >>> load_image('test3.pgm')
    Traceback (most recent call last):
    AssertionError: The inputted my_file is invalid as it's not in PGM format.
    '''
    fobj=open(my_file,'r')
    first_line=fobj.read().split('\n')[0]
    fobj.close()
        
    if first_line=='P2':
        return load_regular_image(my_file)
    elif first_line=='P2C':
        return load_compressed_image(my_file)
    else:
        raise AssertionError("The inputted my_file is invalid as it's"
        ' neither in PGM format or compressed PGM format.')
        
def save_regular_image(my_list, my_file):
    '''(list<list<int>>, str) -> NoneType
    Saves the inputted my_list in the PGM format to a file with
    the inputted my_file as the filename. A AssertionError is raised
    if the given my_list is not a valid PGM image matrix.
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> fobj.close()
    >>> save_regular_image([[245]*3, [6]*3], "test2.pgm")
    >>> fobj = open("test2.pgm", 'r')
    >>> fobj.read()
    'P2\\n3 2\\n255\\n245 245 245\\n6 6 6\\n'
    >>> fobj.close()
    >>> save_regular_image([['2x2','5x2']], "test3.pgm")
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given image matrix is not a valid PGM image matrix.
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The inputted my_list is invalid as this'
        ' given image matrix is not a valid PGM image matrix.')
    row_num=str(len(my_list[0]))
    col_num=str(len(my_list))
    
    fobj=open(my_file,'w')
    fobj.write('P2\n'+row_num+' '+col_num+'\n255\n')
    for row in my_list:
        for col in range(len(row)):
            fobj.write(str(row[col]))
            if col+1 != len(row):
                fobj.write(' ')
        fobj.write('\n')
    fobj.close()

def save_compressed_image(my_list, my_file):
    '''(list<list<str>>, str) -> NoneType
    Saves the inputted my_list in the compressed PGM format
    to a file with the inputted my_file as the filename. A
    AssertionError is raised if the given my_list is not a
    valid compressed PGM image matrix.

    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    >>> save_compressed_image([["255x2", "30x2"],["0x4"]], "test2.pgm.compressed")
    >>> fobj = open("test2.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n4 2\\n255\\n255x2 30x2\\n0x4\\n'
    >>> fobj.close()
    >>> save_compressed_image([[23,0]], "test3.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given image matrix is not a valid compressed PGM image matrix.
    '''
    if not is_valid_compressed_image(my_list):
        raise AssertionError('The inputted my_list is invalid as this'
        ' given image matrix is not a valid compressed'
        ' PGM image matrix.')
    col_num=str(len(my_list))
    row_num=0
    for char in my_list[0]:
        row_num+=int(char.split('x')[1])
            
    fobj=open(my_file,'w')
    fobj.write('P2C\n'+str(row_num)+' '+col_num+'\n255\n')
    for row in my_list:
        for col in range(len(row)):
            fobj.write(row[col])
            if col+1 != len(row):
                fobj.write(' ')
        fobj.write('\n')
    fobj.close()

def save_image(my_list, my_file):
    '''(list<list>, str) -> NoneType
    If the type of all elements in the inputted my_list
    is integer, my_list is saved as a PGM image matrix
    into a file with the inputted my_file as the filename;
    if the type of all elements is string, my_list is
    saved as a compressed PGM image matrix into a file
    with the inputted my_file as the filename.
    In other situations, a AssertionError is raised.
    
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    >>> save_image([[3,5,6], ["0x3"]], "test2.pgm")
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given image matrix is not a valid PGM image matrix.
    >>> save_image([['3',5,6], [0]], "test3.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given image matrix is not a valid compressed PGM image matrix.
    >>> save_image([[True], [0]], "test4.pgm")
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid since it's neither a nested list of integers or strings.
    '''
    element=type(my_list[0][0])
    if element==int:
        save_regular_image(my_list, my_file)
    elif element==str:
        save_compressed_image(my_list, my_file)
    else:
        raise AssertionError("The inputted my_list is invalid"
        " since it's neither a nested list of integers"
        " or strings.")
    
def invert(my_list):
    '''(list<list<int>>) -> list<list<int>>
    Inverts the inputted my_list and returns the
    inverted image matrix. A AssertionError is
    raised if inputted my_list is not in valid
    PGM image matrix format.
    
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> image == [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    True
    >>> invert([[0,0], [5,6]])
    [[255, 255], [250, 249]]
    >>> invert([['0x3'], ['253x3']])
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid PGM image matrix.
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The inputted my_list is invalid as this'
        ' given matrix is not a valid PGM image matrix.')
    
    output=[]
    for row in my_list:
        invert_row=[]
        for num in row:
            invert_row.append(255-num)
        output.append(invert_row)
    return output

def flip_horizontal(my_list):
    '''(list<list<int>>) -> list<list<int>>
    Flip the inputted my_list horizontally and
    returns the flipped image matrix.
    A AssertionError is raised if inputted
    my_list is not a valid PGM image matrix.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 6, 7, 8]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [8, 7, 6, 5, 5]]
    >>> flip_horizontal([[3,2,1],[1,2,3]])
    [[1, 2, 3], [3, 2, 1]]
    >>> flip_horizontal([[0,0],[1]])
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid PGM image matrix.
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The inputted my_list is invalid as this'
        ' given matrix is not a valid PGM image matrix.')
    
    output=[]
    for row in my_list:
        flip_row=[]
        for i in range(-1,-len(row)-1,-1):
            flip_row.append(row[i])
        output.append(flip_row)
    return output

def flip_vertical(my_list):
    '''(list<list<int>>) -> list<list<int>>
    Flip the inputted my_list vertically and
    returns the flipped image matrix.
    A AssertionError is raised if inputted
    my_list is not in valid PGM image matrix format.
    
    >>> image = [[1, 2, 2, 2, 1], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 2, 2, 1]]
    >>> flip_vertical([[3,2,1],[1,2,3]])
    [[1, 2, 3], [3, 2, 1]]
    >>> flip_vertical([[2,0],[0]])
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid PGM image matrix.
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The inputted my_list is invalid as this'
        ' given matrix is not a valid PGM image matrix.')
    
    output=[]
    for i in range(-1,-len(my_list)-1,-1):
        output.append(my_list[i])
    return output

def crop(my_list, row_index, col_index, rect_row, rect_col):
    '''(list<list<int>>, int, int, int, int) -> list<list<int>>
    Crops and returns the inputted my_list according to the
    target rectangle whose pixels are determined by the
    given row_index, col_index, rect_row, rect_col. A
    AssertionError is raised if inputted my_list is not
    in valid PGM image matrix format.
    
    >>> crop([[5, 5, 5], [6, 7, 6], [6, 6, 7]], 1, 0, 2, 1)
    [[6], [6]]
    >>> crop([[3, 4, 2, 1], [4, 6, 6, 7], [9, 9, 15, 11]], 0, 0, 3, 3)
    [[3, 4, 2], [4, 6, 6], [9, 9, 15]]
    >>> crop([['0x3'],['5x3']], 1, 0, 1, 1)
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid PGM image matrix.
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The inputted my_list is invalid as this'
        ' given matrix is not a valid PGM image matrix.')
    
    output=[]
    current_col=col_index
    
    for i in range(rect_row):
        get_row=[]
        count=0
        while count < rect_col:
            get_row.append(my_list[row_index][current_col])
            count+=1
            current_col+=1
        
        output.append(get_row)
        row_index+=1
        current_col=col_index
        
    return output

def find_end_of_repetition(my_list, index, target):
    '''(list<int>, int, int) -> int
    Returns the index of the given target's last consecutive
    occurrence, which is determined after looking through the
    inputted my_list starting after the given index.

    >>> find_end_of_repetition([5, 3, 5, 6, 5, -1, 0], 2, 5)
    2
    >>> find_end_of_repetition([11, 11, 5, 6, 11], 0, 11)
    1
    >>> find_end_of_repetition([11, 11, 11, 11, 11], 0, 11) 
    4
    '''
    if index+1 == len(my_list):
        result=len(my_list)-1
    else:
        while index<len(my_list) and my_list[index]==target:
            index+=1
        result=index-1

    return result

def compress(my_list):
    '''(list<list<int>>) -> list<list<str>>
    Compresses the inputted my_list with regards to
    the compression algorithm and returns the compressed
    matrix. A AssertionError is raised if inputted
    my_list is not in valid PGM image matrix format.
    
    >>> compress([[11, 11, 12, 11], [1, 5, 5, 7], [255, 255, 0, 0]])
    [['11x2', '12x1', '11x1'], ['1x1', '5x2', '7x1'], ['255x2', '0x2']]
    >>> compress([[0, 1, 0], [2, 3, 4]])
    [['0x1', '1x1', '0x1'], ['2x1', '3x1', '4x1']]
    >>> compress([[0],[2,2]])
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid PGM image matrix.
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The inputted my_list is invalid as this'
        ' given matrix is not a valid PGM image matrix.')
    
    output=[]
    for item in my_list:
        index=0
        last_index=-1
        row=[] 
        while index<len(item):
            index=find_end_of_repetition(item, index, item[index])           
            row.append(str(item[index])+'x'+str(index-last_index))
            last_index=index
            index+=1
            
        output.append(row)
    return output
    
def decompress(my_list):
    '''(list<list<str>>) -> list<list<int>>
    Decompresses the inputted my_list through
    reversing the compression algorithm and
    returns the decompressed matrix.
    A AssertionError is raised if inputted
    my_list is not in valid compressed PGM
    image matrix format.
    
    >>> decompress([['0x1', '1x1', '0x1'], ['2x1', '3x1', '4x1']])
    [[0, 1, 0], [2, 3, 4]]
    >>> decompress([['11x4','0x1'], ['1x4', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 0], [1, 1, 1, 1, 7], [255, 255, 255, 0, 255]]
    >>> decompress([['0x1'],[2,2]])
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid compressed PGM image matrix.
    '''
    if not is_valid_compressed_image(my_list):
        raise AssertionError('The inputted my_list is invalid as this'
        ' given matrix is not a valid compressed PGM image matrix.')
    
    output=[]
    for item in my_list:
        row=[]
        for element in item:
            number_list=element.split('x')
            for i in range(int(number_list[1])):
                row.append(int(number_list[0]))
        output.append(row)
    return output

def process_command(command):
    '''(str) -> NoneType
    Executes each command in the given
    command string. A AssertionError is
    raised if any unrecognized commands
    exist in the command string.
    
    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.pgm")
    >>> image == image2
    True
    >>> fobj=open('test.pgm.compressed','w')
    >>> fobj.write("P2C\\n3 2\\n255\\n23x1 200x2\\n0x3\\n")
    27
    >>> fobj.close()
    >>> process_command("LOAD<test.pgm.compressed> DC SAVE<test2.pgm>")
    >>> load_image('test2.pgm')
    [[23, 200, 200], [0, 0, 0]]
    >>> process_command("LOAD<test.pgm.compressed> dsklfj SAVE<test2.pgm>")
    Traceback (most recent call last):
    AssertionError: One or more unrecognized commands exist in the inputted command.
    >>> process_command("LOAD<comp.pgm> DC SAVE<comp2.pgm>")
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid compressed PGM image matrix.
    >>> process_command("LOAD<comp.pgm.compressed> CP SAVE<comp2.pgm.compressed>")
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid PGM image matrix.
    >>> process_command("LOAD<comp.pgm.compressed> INV SAVE<comp2.pgm.compressed>")
    Traceback (most recent call last):
    AssertionError: The inputted my_list is invalid as this given matrix is not a valid PGM image matrix.
    >>> fobj=open('test1.txt','w')
    >>> fobj.write("a\\nb\\nc\\nd")
    7
    >>> fobj.close()
    >>> process_command("LOAD<test1.txt> CP SAVE<test2.txt>")
    Traceback (most recent call last):
    AssertionError: The inputted my_file is invalid as it's neither in PGM format or compressed PGM format.
    '''
    valid_commands=['INV', 'FH', 'FV', 'CP', 'DC']
    command_list=command.split(' ')
    
    for char in command_list:
        if char=='':
            continue
        
        valid=False
        if char in valid_commands:
            valid=True
        elif char[:4]=='LOAD' or char[:4]=='SAVE':
            if char[4]=='<'and char[char.find('>'):]=='>':
                valid=True
        elif char[:2]=='CR':
            if char[2]=='<'and char[char.find('>'):]=='>':
                targets=char[3:char.find('>')].split(',')
                valid=True
        if not valid:
            raise AssertionError('One or more unrecognized commands'
            ' exist in the inputted command.')
        
        if 'LOAD' in char:
            my_file=char[5:-1]
            my_list=load_image(my_file)
        elif char=='INV':
            my_list=invert(my_list)
        elif char=='FH':
            my_list=flip_horizontal(my_list)
        elif char=='FV':
            my_list=flip_vertical(my_list)
        elif 'CR' in char:
            my_list=crop(my_list, int(targets[0]), int(targets[1]), int(targets[2]), int(targets[3]))
        elif char=='CP':
            my_list=compress(my_list)
        elif char=='DC':
            my_list=decompress(my_list)
        elif 'SAVE' in char:
            my_file=char[5:-1]
            save_image(my_list, my_file)