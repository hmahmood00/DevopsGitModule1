import argparse

parser = argparse.ArgumentParser(description='Fiml Reviews')
parser.add_argument('--film-name',
                    type=str,
                    dest ='fileName',
                    help='Name of the Film')
parser.add_argument('--stars',
                    type=int,
                    dest = 'stars',
                    help='Star Rating')

args = parser.parse_args()
print(args.stars)