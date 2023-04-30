#name: Angela(Qingchen) Hu, McGill student ID: 261075832
ROOM_NAME='Ruins'
AUTHOR='Angela'
PUBLIC=True

def escape_room():
    '''() -> NoneType
    Displays the description of the escape room and prompts the player to type in
    commands until the special command is found for escaping the room and
    exits the function. As the user interacts with a total of 4 objects, hints
    will be printed and the list of valid commands is updated. If an invalid command
    is entered, a message is displayed to alert the player and give prompts
    for another command.
    
    >>> escape_room()
    *You woke up in a ruin underground, surrounded by walls built with purple bricks and stones. 
    *A gigantic, terrifying creature is sleeping in the corner. You need to find a way up to the
    surface world before it awakes. 
    *In your sight, there is a small bush of yellow flowers in which something is shining.
    On your left, there is a narrow tunnel where the light does not reach. It looks like a path
    leading somewhere. There’s a chunky object on the wall, yet the abyss-like darkness inside
    the tunnel prevents you from investigating it.

    > examine flowers
    “Howdy!” One of the yellow flowers suddenly turns around and talks.
    As you tried to ask for help, it gives you a glowing germ, smiling:
    “Lightsources are really useful underground!” *(It fills you with determination.)

    > examine tunnel
    *With the glowing stone, you peer into the tunnel.
    There’re rows of sharp spikes smeared with crimson liquid. They blocked theladder.
    *The chunky object turns out to be a silver block, attached to thewall like a piece of machinery.

    > examine block
    *A faint light from yout stone illuminates the machine block.
    There was a switch on it and a small line engraved next to it: Professional
    Thorn Cleaning by THE GREAT PAPYRUS! Just one click to solve all your troubles.

    > flick switch
    **CRACK!**After a loud bang, the spikes are cleared by the blade, leaving you with just
    enough room to pass on the ladders.
    Hope fills your heart as the faint glow of the sky gradually appears overhead.
    *After you carefully climb up the ladder, you have finally reached the surface, congratulations!
    It’s a beautiful day outside... *You are filled with determination <3*
    >>> escape_room()
    *You woke up in a ruin underground, surrounded by walls built with purple bricks and stones. 
    *A gigantic, terrifying creature is sleeping in the corner. You need to find a way up to the
    surface world before it awakes. 
    *In your sight, there is a small bush of yellow flowers in which something is shining.
    On your left, there is a narrow tunnel where the light does not reach. It looks like a path
    leading somewhere. There’s a chunky object on the wall, yet the abyss-like darkness inside
    the tunnel prevents you from investigating it.

    > examine tunnel
    *It's too dark! You can't do anything. Using some shining objects might be helpful.

    > examine flowers
    “Howdy!” One of the yellow flowers suddenly turns around and talks.
    As you tried to ask for help, it gives you a glowing germ, smiling:
    “Lightsources are really useful underground!” *(It fills you with determination.)

    > examine tunnel
    *With the glowing stone, you peer into the tunnel.
    There’re rows of sharp spikes smeared with crimson liquid. They blocked theladder.
    *The chunky object turns out to be a silver block, attached to thewall like a piece of machinery.

    > look at block
    *A faint light from yout stone illuminates the machine block.
    There was a switch on it and a small line engraved next to it: Professional
    Thorn Cleaning by THE GREAT PAPYRUS! Just one click to solve all your troubles.

    > turn on switch
    **CRACK!**After a loud bang, the spikes are cleared by the blade, leaving you with just
    enough room to pass on the ladders.
    Hope fills your heart as the faint glow of the sky gradually appears overhead.
    *After you carefully climb up the ladder, you have finally reached the surface, congratulations!
    It’s a beautiful day outside... *You are filled with determination <3*
    >>> escape_room()
    *You woke up in a ruin underground, surrounded by walls built with purple bricks and stones. 
    *A gigantic, terrifying creature is sleeping in the corner. You need to find a way up to the
    surface world before it awakes. 
    *In your sight, there is a small bush of yellow flowers in which something is shining.
    On your left, there is a narrow tunnel where the light does not reach. It looks like a path
    leading somewhere. There’s a chunky object on the wall, yet the abyss-like darkness inside
    the tunnel prevents you from investigating it.

    > list commands
    examine flowers
    examine tunnel

    > walk
    Invalid command, try something else!

    > explore tunnel
    *It's too dark! You can't do anything. Using some shining objects might be helpful.

    > look at flowers
    “Howdy!” One of the yellow flowers suddenly turns around and talks.
    As you tried to ask for help, it gives you a glowing germ, smiling:
    “Lightsources are really useful underground!” *(It fills you with determination.)

    > examine tunnel
    *With the glowing stone, you peer into the tunnel.
    There’re rows of sharp spikes smeared with crimson liquid. They blocked theladder.
    *The chunky object turns out to be a silver block, attached to thewall like a piece of machinery.

    > examine block
    *A faint light from yout stone illuminates the machine block.
    There was a switch on it and a small line engraved next to it: Professional
    Thorn Cleaning by THE GREAT PAPYRUS! Just one click to solve all your troubles.

    > list commands
    examine flowers
    examine tunnel
    examine block
    flick switch

    > flick switch
    **CRACK!**After a loud bang, the spikes are cleared by the blade, leaving you with just
    enough room to pass on the ladders.
    Hope fills your heart as the faint glow of the sky gradually appears overhead.
    *After you carefully climb up the ladder, you have finally reached the surface, congratulations!
    It’s a beautiful day outside... *You are filled with determination <3*
    '''
    action=input('*You woke up in a ruin underground, surrounded by walls built with '
    'purple bricks and stones. \n*A gigantic, terrifying creature is sleeping in the corner. '
    'You need to find a way up to the\nsurface world before it awakes. \n'
    '*In your sight, there is a small bush of yellow flowers in which something is shining.\n'
    'On your left, there is a narrow tunnel where the light does not reach. It looks like a '
    'path\nleading somewhere. There’s a chunky object on the wall, yet the abyss-like '
    'darkness inside\nthe tunnel prevents you from investigating it.\n\n').lower()
    command1='examine flowers'
    command2='examine tunnel'
    command3='examine block'
    command4='flick switch'
    command_list=command1+'\n'+command2+'\n'
    darkness=0
    block=0
    switch=0
    in_progress=True
    while in_progress:
        if action=='list commands':
            print(command_list)
        elif action==command1 or action=='look at flowers' or action=='check flowers':       
            print('“Howdy!” One of the yellow flowers suddenly turns around and talks.\n'
            'As you tried to ask for help, it gives you a glowing germ, smiling:\n“Light '
            'sources are really useful underground!” '
            '*(It fills you with determination.)\n')
            darkness=1
        elif (action==command2 or action=='explore tunnel' or action=='investigate tunnel'): 
            if not darkness:
                print("*It's too dark! You can't do anything. Using some shining "
                'objects might be helpful.\n')
            else:
                print('*With the glowing stone, you peer into the tunnel.\n'
                'There’re rows of sharp spikes smeared with crimson liquid. They blocked the'
                'ladder.\n*The chunky object turns out to be a silver block, attached to the'
                'wall like a piece of machinery.\n')
                block=1
                command_list+=command3+'\n'
        elif (action==command3 or action=='look at block' or action=='check block') and block:
            print('*A faint light from yout stone illuminates the machine block.\n'
            'There was a switch on it and a small line engraved next to it: Professional\n'
            'Thorn Cleaning by THE GREAT PAPYRUS! Just one click to solve all your troubles.\n')
            switch=1
            command_list+=command4+'\n'
        elif (action==command4 or action=='turn on switch'or action=='click switch') and switch:
            print("**CRACK!**After a loud bang, the spikes are cleared by the "
            "blade, leaving you with just\nenough room to pass on the ladders.\nHope fills your "
            "heart as the faint glow of the sky gradually appears overhead.\n"
            "*After you carefully climb up the ladder, you have finally reached the surface, "
            "congratulations!\n"
            "It’s a beautiful day outside... *You are filled with determination <3*")
            in_progress=False
            break
        else:
            print("Invalid command, try something else!\n")
        action=input('').lower()