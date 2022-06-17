#Cartoon Program
#Demonstrates user input and the elif clause
#Console based starter Pokemon

print("Hello there! Welcome to the world of Pokémon!"\
      + "My name is Oak! People call me the Pokémon Prof!"\
      + "This world is inhabited by creatures called Pokémon!"\
      + "For some people, Pokémon are pets. Others use them for fights.")
pokemon = input("\nWhich pokemon would you like? Choose from 1-3... ")

if pokemon == "1":
    #bulbasaur
    print("You have chosen BULBASAUR, the grass type Pokémon!\n\n")
    print( 
        r"""
                                     /
                        _,.------....___,.' ',.-.
                     ,-'          _,.--\"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \.\
       ____      |___._.  |       __               \ `.
     .'    `---\"\"       ``\"-.--\"'`  \               .  \
    .  ,            __               `              |   .
    `,'         ,-\"'  .               \             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,\".   `--'                      >.      ,'     |
 . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
/ L:_  |                 .  \"' :_;                `.'.'
.    \"\"'                  \"\"\"\"\"'                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \`._        ___....----\"'  ,'   .'  \ |   '  \  .
   /   `. \"`-.--\"'         _,' ,'     `---' |    `./  |
  .   _  `\"\"'--.._____..--"   ,             '         |
  | .\" `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
 `\"^--'..'   '-`-^-'\"--    `-^-'`.''\"\"\"\"\"`.,^.`.--' kr
            """)

elif pokemon == "2":
    #squirtle
    print("You have chosen SQUIRTLE, the water type Pokémon!\n\n")
    print( 
        r"""
               _,........__
            ,-'            \"`-.
          ,'                   `-.
        ,'                        \
      ,'                           .
      .'\               ,\"\".       `
     ._.'|             / |  `       \
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | \
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -\" \  .     `
`.\"\"\"\"\"'-.`-...,---------','         `. `....__.
.'        `\"-..___      __,'\          \  \     \
\_ .          |   `\"\"\"\"'    `.           . \     \
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7\"\"' |  ,      |
            ` `      `            /     |  |      |    _,-'\"\"\"`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              \
               \/    `\"\"\\"\"\"\"\"\"\"`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         .\"     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |\"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'kr
        """)

elif pokemon == "3":
    #charmander
    print("You have chosen CHARMANDER, the fire type Pokémon!\n\n")
    print( 
        r"""
            _.--\"\"`-..
            ,'          `.
          ,'          __  `.
         /|          \" __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,\".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .
  `,         \"\"\"\"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\
   -\" /`.         _,'     | _  _  _.|
    \"\"--'---\"\"\"\"\"'        `' '! |! /
                            `\" \" -' kr
        """)
else:
    print("That's not right!")



input("Press the enter key to exit.")
