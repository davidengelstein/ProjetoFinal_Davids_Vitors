# -*- coding: utf-8 -*-

"""
Created on Mon May 11 20:01:53 2015
@author: vitor_000,vitor_kitahara
"""

import random
import time
from random import choice
from firebase import firebase


FIREBASE_URL = "https://car-game.firebaseio.com/"

if __name__ == '__main__':
    # Cria uma referência para a aplicação Firebase
    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Lê o dado da base de dados
    result = fb.put('/', "scores", [""])
