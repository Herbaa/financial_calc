from  calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax
import pytest

#Первый тест
def test_compound_interest_normal():
    assert calculate_compound_interest(1000, 5, 2, 1) == 1102.5

def test_compound_interest_zero():
    assert calculate_compound_interest(0, 5, 2, 1) == 0.0
    assert calculate_compound_interest(1000, 0, 2, 1) == 1000.0
    
def test_compound_interest_error():
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, -5, 2)
    
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, 2.5)
        
        

#Второй тест
def test_simple_interest_normal():
    assert calculate_simple_interest(1000, 5, 2) == 100.0
    assert calculate_simple_interest(2000, 3, 4) == 240.0

def test_simple_interest_zero():
    assert calculate_simple_interest(0, 5, 2) == 0.0
    assert calculate_simple_interest(1000, 0, 2) == 0.0

def test_simple_interest_error():
    with pytest.raises(ValueError):
        calculate_simple_interest(-1000, 5, 2)



#Третий тест
def test_calculate_tax_normal():
    assert calculate_tax(1000, 100) == 1000.0
    assert calculate_tax(500, 0) == 0.0
    
def test_calculate_tax_error():
    with pytest.raises(ValueError):
        calculate_tax(1000, -5)