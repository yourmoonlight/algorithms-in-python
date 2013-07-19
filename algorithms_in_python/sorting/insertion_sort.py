#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Insertion Sort

import utils


def sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
