import calculator

class Test:
       def test_addition(self):
           assert 6 == calculator.add(3,3)

       def test_subtraction(self):
            assert -1 == calculator.subtract(2,3)

       def test_division(self):
            assert 10 == calculator.division(100,10)

   
