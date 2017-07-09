#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sys import exit
from random import randint
from textwrap import dedent

# An adventure game about rescue princess from the evil witch
class Engine(object):


class Death(object):

    comment = [
    'fear',
    'greed',
    '',
    '',
    '',
    ]

    def __init__(self, scene_number):
        print('Such a pity! You died of {}'.format(comment[scene_number]))



class Item(object):
    items = {
    'key_1st': 0,
    'key_2nd': 0,
    'beaf': 0,
    'corn': 0,
    'gold': 0,
    'toxicide': 0,
    'bullet': 12,
    'excalibur': 0,
    'magic_armour': 0,
    }


class Gate(object):
    print(dedent("""
        You are the prince of Holy Kingdom, and engaged with the princess of
        Snow Kingdom who is the purest and most beatiful girl in the world.
        And fortunately, you love with each other. It seems that your future
        is bright and full of hope.
        However, one day an evil witch appeared, and she kidnap the princess
        and told you to go to her castle if you want to rescue your fiancee.
        You ignored all opposition, and finally arrived the castle.
        Now, you are in front of the huge gate of this castle surrounded with
        disgusting and horrible atmosphere. Though you've overcame hundreds of
        difficulties and obstacles, you still can't stop thrilling. You really
        want to run away and never back, if you could. So what would you do?
        1.Open the Gate and enter the castle
        2.Run away and never back
    """))
    choice = input('Please make your choice:\n> ')
    if choice == 1:

        return 'lobby'
    elif: choice == 2:
        print(dedent("""
            You run away!
            On your way back, you full of remorse and fall off the cliff!
        """))
        return 'death', 0
    else:
        print("Please make your decision!")


class Castle(object, start_scene):

    def __init__(self):
        self.start_scene = start_scene
        self.battle = RandomBattle()

    def opening_scene(self, scene_now):

    def next_scene():



class FirstFloor(object):

    rooms = {
    'lobby': Lobby(),
    'meat_room': Kitchen(),
    'bed_room': BedRoom(),
    'corn_room': CornRoom(),
    'toxicide_room': ToxicideRoom(),
    'key_room': KeyRoom(),
    'sword_room': SwordRoom(),
    'stair_room': StairRoom1(),
    'gold_room': GoldRoom(),
    }

    count = {
    'lobby': 0,
    'meat_room': 0,
    'bed_room': 0,
    'corn_room': 0,
    'toxicide_room': 0,
    'key_room': 0,
    'sword_room': 0,
    'stair_room': 0,
    'gold_room': 0,
    }


class Lobby(FirstFloor):

    action == input('>')

    if action == 'up':
        return 'gold_room'
    elif action == 'right':
        return 'bed_room'
    else:




class Kitchen(FirstFloor):

    def __init__(self):
        self.item = Item().items
        self.count = FirstFloor().counts

    if self.count['kitchen'] == 0:
        self.count['kitchen'] = 1
        print(dedent("""
            You enter the kitchen, and there are so many food that you have ever
            met. All of them seems dilicious and tempting, and you just feel a
            little hungry. So you will
            1.have some food
            2.just take some food seems harmless
            3.do nothing
        """))
        action = input('> ')
        if action == 1:
            print(dedent("""
                These food really delicious and you just cannot stop. Finally,
                you overeat to death.
            """))
            return 'death', 1
        elif action == 2:
            if self.item['meat'] == 0:
                self.item['meat'] = 1
                print('You got a piece of meat! It\'s seems tasty!')
            else:
                print('You\'ve already got one. Donot be greedy!')
        elif action == 3:
            print('You do nothing!')

    else:
        print(dedent("""
        You enter the kitchen.
        This is not 1st time you come here. Nothing is available
        """))

    print('Now, where would you go ahead?(up, down, left, right,)')
    input('> ')
    While True:
        if action == 'up':
            return 'toxicide_room'
        else:
            print('There\'s no door this way.')

class BedRoom(FirstFloor):

    if action == 'up':
        return 'corn_room'
    elif action == 'left':
        return 'lobby'
    else:

class CornRoom(FirstFloor):

    if action == 'up':
        return 'key_room'
    elif action == 'left':
        return 'gold_room'
    elif action == 'down':
        return 'bedroom'
    else:

class ToxicideRoom(FirstRoom):

    if action == 'up':
        return 'stair_room'
    elif action == 'right':
        return 'stair_room'
    elif action == 'down':
        return 'kitchen'
    else:



class KeyRoom(FirstFloor):

    if action == 'left':
        return 'sword_room'
    elif action == 'down':
        return 'corn_room'
    else:

class SwordRoom(FirstFloor):

    if action == 'right':
        return 'key_room'
    else:

class GoldRoom(FirstFloor):

    if action == 'right':
        return 'corn_room'
    elif action == 'left':
        return 'toxicide_room'
    elif action == 'down':
        return 'lobby'
    elif action == 'take the gold':
    else:

class StairRoom1(FirstFloor):


class SecondFloor(object):

    Rooms = {
    'start_room': StartRoom(),
    'magic_room': MagicRoom(),
    'lion_room': LionRoom(),
    'stair_room': StairRoom2(),
    }

    Count = {
    'start_room': 0,
    'magic_room': 0,
    'lion_room': 0,
    'stair_room': 0,
    }


class StartRoom(SecondFloor):

    if action == 'right':
        return 'magic_room'
    elif action == 'down':
        return 'stair_room'
    else:

class MagicRoom(SecondFloor):

    if action == 'left':
        return 'start_room'
    else:

class LionRoom(SecondFloor):

    if action == 'left':
        return 'stair_room'
    else:

class StairRoom2(SecondFloor):


class ThirdFloor(object):
    print(dedent("""
        Now you are on the third floor. And a luxurious door stand in front
        of you. You know that it must be that witch's room. There must be a
        dangerous fight you've never meet. Don't be frightened! You've conquer
        so many difficuties and come here, just move on and your fiancee is
        waiting for you!
        So, what will you do?
        1.Move on!
        2.Go ahead!
        3.Enter the room!
    """))
    choice = input('What would you do?\n>')




class LastRoom(ThirdFloor):
