from unittest.mock import MagicMock  
temp = MagicMock(return_value = 20)  
print(temp(32, 12, debug = True), "\n")   
  
temp.assert_called_with(32, 12, debug = True) 
temp.assert_called_with(31, 11)