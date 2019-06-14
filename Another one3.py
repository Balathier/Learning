#! /usr/bin/env python3

# practicing input() variables, and some if/else

hentai = input('Do you like Hentai yes or no? ')

if hentai == ('yes' or 'Yes'):
    genre = input('What\'s your favourite genre? ')
    if genre == 'Mind Break':
        print(f'Man of fucking culture, I love {genre}')

    elif genre:
        dislike = input('What\'s your least favourite genre' )
        print(f'so you answered {hentai} to the first question, and your favourite genre is {genre},'
          f' and you dislike {dislike}')

elif hentai == 'no':
    print('Well you suck balls')

else:
    print('you didn\'t answer the question, please say yes or no next time.')





