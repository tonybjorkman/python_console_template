import pytest
import os
import sys
print(os.getcwd())
from app.minimal import mytest

def test_sanity():
    assert mytest()

