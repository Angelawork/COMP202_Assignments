#name: Angela(Qingchen) Hu, McGill student ID: 261075832
import musicalbeeps

class Note:
    '''A class to represent a music note.

    Instance attributes:
    * duration: float
    * pitch: str
    * octave: int
    * accidental: str
    
    Class attributes:
    * OCTAVE_MIN: int
    * OCTAVE_MAX: int
    '''
    OCTAVE_MIN=1
    OCTAVE_MAX=7
    
    def __init__(self,duration,pitch,octave=1,accidental='natural'):
        ''' (float, str, int, str) -> NoneType
        Creates an object of the type Note.
        An AssertionError is raised if the inputted
        values are in wrong types or format.
        
        >>> note = Note(1.25, "A", 3, "natural")
        >>> note.octave
        3
        >>> note = Note(1.5, "B")
        >>> note.octave
        1
        >>> note = Note(1, 2)
        Traceback (most recent call last):
        AssertionError: The inputted values are not of the correct type.
        >>> note = Note(1.25, "A", 11, "natural")
        Traceback (most recent call last):
        AssertionError: One or more of the inputted values are invalid.
        >>> note = Note(1.25, "ABC", 5, "natural")
        Traceback (most recent call last):
        AssertionError: The format of the inputted values is not correct.
        '''
        valid_pitch=['A','B','C','D','E','F','G','R']
        valid_acci=['sharp', 'flat', 'natural']
        if type(duration)!=float or type(pitch)!=str or type(octave)!=int or type(accidental)!=str:
            raise AssertionError('The inputted values are not of the correct type.')
        elif duration<=0 or octave not in range(Note.OCTAVE_MIN,Note.OCTAVE_MAX+1):
            raise AssertionError('One or more of the inputted values are invalid.')
        elif pitch not in valid_pitch or accidental not in valid_acci:
            raise AssertionError('The format of the inputted values is not correct.')
        
        self.duration=duration
        self.pitch=pitch
        self.octave=octave
        self.accidental=accidental
        
    def __str__(self):
        ''' () -> str
        Returns a string containing instance attributes
        duration, pitch, octave and accidental in order
        with 1 space in-between.
        
        >>> note = Note(1.5, "C", 3, "natural")
        >>> print(note)
        1.5 C 3 natural
        >>> note = Note(.25, "A", 2, "natural")
        >>> print(note)
        0.25 A 2 natural
        >>> note = Note(0.5, "B")
        >>> print(note)
        0.5 B 1 natural
        '''
        return str(self.duration)+' '+self.pitch+' '+str(self.octave)+' '+self.accidental
    
    def play(self, player):
        '''(Player) -> NoneType
        Constructs a note string with the pitch attribute
        and passes it with duration attribute to the
        inputted player object to let the Note get played
        through the speakers.
        '''
        if self.pitch=='R':
            note_string='pause'
        else:
            note_string=self.pitch+str(self.octave)
            if self.accidental=='sharp':
                note_string+='#'
            elif self.accidental=='flat':
                note_string+='b'
        player.play_note(note_string, self.duration)