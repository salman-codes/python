import pytest
@pytest.fixture
def suply_params():
	param1 =12
	param2 =22
	return [param1, param2]

def test_comparewith_param1(suply_params):
	param3=42
	assert suply_params[0]==param3,"param1 and param3 comparison failed"

def test_comparewith_param2(suply_params):
	param3=22
	assert suply_params[1]==param3,"param2 and param3 comparison failed"