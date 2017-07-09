#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Battle(object):


class RandomBattle(Battle):

    enemies = [
        'ghost',
        'wolf',
        'karakuri puppet',
    ]

    def __init__(self):
        self.wolf = Status().wolf
        self.ghost = Status().ghost
        self.karakuri_puppet = Status().karakuri_puuppet

    def EnemyAppear(self):
        print('A {} appears'.format(enemies[randint(0,2)]))


class FinalBattle(Battle):


class LionBattle(Battle):


class GuardianBattle(Battle):
