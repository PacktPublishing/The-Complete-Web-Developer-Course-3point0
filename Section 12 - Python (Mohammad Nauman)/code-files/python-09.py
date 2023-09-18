#! /usr/bin/python

from random import randint

import cgi

# these two lines help us debug
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print('Content-type: text/html')
print('')


word_list = ['Water', 'Drink', 'Floor', 'Reply', 'Stone', 'Uncle', 'Tower',
             'Apple', 'Crowd', 'Peace', 'Right', 'Video', 'Offer', 'Horse', 'Dress', 'Force', ]


print('<h1>Wordule</h1>')
print('<p>Try to guess the word!</p>')


def get_new_word():
    # we need to pick a word from 0 to last_index in list
    last_index = len(word_list) - 1

    # get a random word
    new_word_index = randint(0, last_index)

    # get that word now from the list
    new_word = word_list[new_word_index]
    return new_word.upper()


def put_box(color):
    print('<span style="color:' + color + '; font-size: 3em">&#9632;</span>')


def print_guess_stats(word, guess):
    for i, c in enumerate(guess):
        if c == word[i]:
            put_box('green')
        elif c in word:
            put_box('blue')
        else:
            put_box('gray')

    if word == guess:
        print('<div>Yay! You got it in ' + str(guess_num) + ' gueses! </div>')


# if there is no guess, this is a new game
new_game = 'guess' not in form


if new_game:
    # first create the form to show
    word = get_new_word()
    guess = ''
    guess_num = 0

else:
    # we are working with an existing game
    word = form.getvalue('word')
    guess = form.getvalue('guess').upper()
    guess_num = int(form.getvalue('guess_num')) + 1

    # print stats for the guess
    print_guess_stats(word, guess)


print('<form method="post">')
print('<input type="text" name="guess" maxlength="5" value="' + guess + '">')
print('<input type="hidden" name="word" value = "' + word + '">')
print('<input type="hidden" name="guess_num" value = "' + str(guess_num) + '">')
print('<input type="submit" value="Guess!">')
print('</form>')
