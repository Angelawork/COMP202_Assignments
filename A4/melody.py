#name: Angela(Qingchen) Hu, McGill student ID: 261075832
from note import *

class Melody:
    '''A class to represent a melody of notes.

    Instance attributes:
    * title: str
    * author: str
    * notes: list<Note>
    '''
    def __init__(self,filename):
        ''' (str) -> NoneType
        Creates an object of the type Melody.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> print(happy_birthday.notes[4])
        0.5 G 4 natural
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> print(hot_cross_buns.notes[10])
        0.25 A 4 natural
        >>> fobj=open('song1.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 A 3 NATURAL false")
        35
        >>> fobj.close()
        >>> song1 = Melody("song1.txt")
        >>> print(song1.notes[0])
        0.25 A 3 natural
        '''
        sheet=[]
        fobj=open(filename,'r')
        for line in fobj:
            sheet.append(line.strip('\n'))
        fobj.close()
        
        self.title=sheet[0]
        self.author=sheet[1]
        self.notes=[]
        i=2
        first_count=True
        repeat_once=False
        previous=[]
        
        while i < len(sheet):
            item=sheet[i].split(' ')
            if item[1]!='R':
                note_item=Note(float(item[0]),item[1],int(item[2]),item[3].lower())
                note_item2=Note(float(item[0]),item[1],int(item[2]),item[3].lower())
                repeat_value=item[4]
            else:
                note_item=Note(float(item[0]),item[1])
                note_item2=Note(float(item[0]),item[1])
                repeat_value=item[2]
            self.notes.append(note_item)
            
            if repeat_value=='true' and first_count:
                first_count=False
                repeat_once=True
                previous.append(note_item2)
            elif repeat_value=='false' and repeat_once:
                previous.append(note_item2)
            elif repeat_value=='true' and not first_count:
                previous.append(note_item2)
                self.notes+=previous
                previous=[]
                first_count=True
                repeat_once=False    
            i+=1

    def play(self, player):
        '''(Player) -> NoneType
        Calls the play method for the note attribute's
        each Note object in order and passes the inputted
        player object every time.
        '''
        for item in self.notes:
            item.play(player)
    
    def get_total_duration(self):
        '''() -> float
        Returns the Melody's total duration.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        >>> fobj=open('song1.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 A 3 NATURAL false")
        35
        >>> fobj.close()
        >>> song1 = Melody("song1.txt")
        >>> song1.get_total_duration()
        0.25
        >>> fobj=open('song2.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 A 3 NATURAL true\\n0.25 B 3 NATURAL false\\n0.25 C 3 NATURAL true")
        79
        >>> fobj.close()
        >>> song2 = Melody("song2.txt")
        >>> song2.get_total_duration()
        1.5
        '''
        result=0.0
        for item in self.notes:
            result+=item.duration
        return result

    def change_octave(self, limit, value):
        '''(int, int) -> bool
        Changes the octave attribute of the note attribute's
        each Note object by the inputted value. Returns True
        if all the Note objects satisfies the limit, otherwise
        no changes would be done and returns False.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_octave(Note.OCTAVE_MIN, -1)
        True
        >>> fobj=open('song1.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 D 1 NATURAL false")
        35
        >>> fobj.close()
        >>> song1 = Melody("song1.txt")
        >>> song1.change_octave(Note.OCTAVE_MIN, -1)
        False
        >>> fobj=open('song2.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 A 7 NATURAL false")
        35
        >>> fobj.close()
        >>> song2 = Melody("song2.txt")
        >>> song2.change_octave(Note.OCTAVE_MAX, +1)
        False
        '''
        for item in self.notes:
            if item.octave==limit and item.pitch!='R':
                return False
        for item in self.notes:
            if item.pitch!='R':
                item.octave+=value
        return True
             
    def lower_octave(self):
        '''() -> bool
        Lowers the octave attribute of the song's
        each Note object by 1. Returns True if all the Note
        objects don't have an octave of 1, otherwise
        no changes would be done and returns False.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
        >>> fobj=open('song1.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 D 1 NATURAL false")
        35
        >>> fobj.close()
        >>> song1 = Melody("song1.txt")
        >>> song1.lower_octave()
        False
        >>> fobj=open('song2.txt','w')
        >>> fobj.write("title\\nauthor\\n1.5 A 2 NATURAL false")
        34
        >>> fobj.close()
        >>> song2 = Melody("song2.txt")
        >>> song2.lower_octave()
        True
        >>> song2.notes[0].octave
        1
        '''
        return self.change_octave(Note.OCTAVE_MIN, -1)
    
    def upper_octave(self):
        '''() -> bool
        Increases the octave attribute of the song's
        each Note object by 1. Returns True if all the Note
        objects don't have an octave of 7, otherwise
        no changes would be done and returns False.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        5
        >>> fobj=open('song1.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 A 7 NATURAL false")
        35
        >>> fobj.close()
        >>> song1 = Melody("song1.txt")
        >>> song1.upper_octave()
        False
        >>> fobj=open('song2.txt','w')
        >>> fobj.write("title\\nauthor\\n1.5 A 6 NATURAL false")
        34
        >>> fobj.close()
        >>> song2 = Melody("song2.txt")
        >>> song2.upper_octave()
        True
        >>> song2.notes[0].octave
        7
        '''
        return self.change_octave(Note.OCTAVE_MAX, 1)
    
    def change_tempo(self,time):
        '''(float) -> NoneType
        Multiplies the duration attribute of the
        note attribute's each Note object by the
        inputted time.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        >>> fobj=open('song1.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 A 3 NATURAL false")
        35
        >>> fobj.close()
        >>> song1 = Melody("song1.txt")
        >>> song1.change_tempo(0.5)
        >>> song1.get_total_duration()
        0.125
        >>> fobj=open('song2.txt','w')
        >>> fobj.write("title\\nauthor\\n0.25 A 3 NATURAL true\\n0.25 B 3 NATURAL false\\n0.25 C 3 NATURAL true")
        79
        >>> fobj.close()
        >>> song2 = Melody("song2.txt")
        >>> song2.change_tempo(1)
        >>> song2.get_total_duration()
        1.5
        '''
        for item in self.notes:
            item.duration*=time