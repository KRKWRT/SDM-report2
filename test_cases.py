#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    def test_case1 (self): #有効数値
        self.assertEqual (21, calc(3,7)) #通常入力
        self.assertEqual (21, calc(7,3)) #逆にした場合
        self.assertEqual (250000, calc(500,500)) #同じ数値
        self.assertEqual (2, calc(1,2)) #最小境界値
        self.assertEqual (997002, calc(998,999)) #最大境界値

    def test_case2 (self): #無効数値
        self.assertEqual (-1, calc(0,1)) #最小境界値
        self.assertEqual (-1, calc(999,1000)) #最大境界値
        self.assertEqual (-1, calc(-1,-1)) #両方範囲外
        
    def test_case3 (self): #異常値
        self.assertEqual (-1, calc(1.5,2)) #左片方小数
        self.assertEqual (-1, calc(2,1.5)) #右片方小数
        self.assertEqual (-1, calc(1.5,1.5)) #両方小数
        self.assertEqual (-1, calc('a',1)) #左片方文字列
        self.assertEqual (-1, calc(1,'a')) #右片方文字列
        self.assertEqual (-1, calc('a','b')) #両方文字列
        self.assertEqual (-1, calc(None,1)) #左片方None
        self.assertEqual (-1, calc(1,None)) #右片方None
        self.assertEqual (-1, calc(None,None)) #両方None
        self.assertEqual (-1, calc([],5)) #左片方リスト
        self.assertEqual (-1, calc(5,[])) #右片方リスト
        self.assertEqual (-1, calc([],[])) #両方リスト
        self.assertEqual (-1, calc({},5)) #左片方辞書
        self.assertEqual (-1, calc(5,{})) #右片方辞書
        self.assertEqual (-1, calc({},{})) #両方辞書