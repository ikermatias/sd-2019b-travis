import pytest
import demo

def test_add():
# GIVEN two numbers
# WHEN I invoke the method
# THEN I get the addition of two numbers
    add_result = demo.add(3,4)
    add_result2 = demo.add(1,1)
    assert add_result == 7
    assert add_result == 11


