FINISH_GAME = '!'

WORDS_POOL =  {
    'APPLE': 'A fruit that can be red or green.',
    'TIGER': 'A large wild cat with orange fur and black stripes.',
    'BEACH': 'A sandy place next to the sea.',
    'CLOUD': 'A white or gray shape in the sky.',
    'PLANET': 'A large object that moves around a star.',
    'ROCKET': 'A vehicle used to travel into space.',
    'CASTLE': 'A large, old building where kings and queens lived.',
    'MONKEY': 'An animal that can climb trees and likes bananas.',
    'SHADOW': 'A dark shape made when something blocks the light.',
    'JOURNEY': 'The act of traveling from one place to another.',
    'WHISPER': 'To speak very quietly.',
    'PUZZLE': 'A game or problem that requires thinking to solve.',
    'DOLPHIN': 'A smart sea animal that breathes air.',
    'KNIGHT': 'A medieval warrior who often wore armor.',
    'TREASURE': 'Valuable objects such as gold, jewels, or coins.'
}

STAGES = [
    r"""
       +---+
       |   |
       O   |
           |
           |
           |
     =========
     """,
    r"""
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
     """,
    r"""
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
     """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========
     """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     =========
     """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
   !!DEADMAN!!
     """
]