import pytest
@pytest.mark.set1
def test_method1():
	x=12
	y=13
	assert x+1 == y,"test failed"
	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.set2
def test_method2():
	x=32
	y=33
	assert x+1 == y,"test failed"