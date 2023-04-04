import sys
from importlib import import_module
sys.path.append("/mnt/d/WSL/Ubuntu/code/leetcode/python")
target=import_module("main.0001两数之和")
import pytest


def test_twoSum():
    assert target.twoSum([1,2,5],3) in [[1,0],[0,1]]

@pytest.mark.demo
def test_demo1():
    assert True

@pytest.mark.demo
def test_demo2():
    assert False

@pytest.mark.skipif(True,reason="test")
def test_skip1():
    assert False
@pytest.mark.skipif(True,reason="test")

def test_skip2():
    assert False
@pytest.mark.skipif(True,reason="not implemented")
def test_skip():
    ...

