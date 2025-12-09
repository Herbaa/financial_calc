def calculate_simple_interest(principal, rate, time):
    if principal == abs(principal) and rate == abs(rate) and time == abs(time):
        return principal * rate * time / 100
    raise ValueError('Аргументы должны быть неотрицательными')
        
        
def calculate_compound_interest(principal, rate, time, n=1):
    if principal == abs(principal) and rate == abs(rate) and time == abs(time) and n > 0 and isinstance(n, int):
        return principal * (1 + rate/(100*n))**(n*time)
    raise ValueError('Неверный формат данных')
    
def calculate_tax(amount, tax_rate):
    if tax_rate >= 0 and tax_rate <= 100:
        return amount * tax_rate / 100
    raise ValueError('Налог должен быть от 1 до 100')