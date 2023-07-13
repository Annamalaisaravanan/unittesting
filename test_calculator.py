import calculator

class Test:
    def test_addition(self):
           assert 5 == calculator.add(3,2)

    def test_subtraction(self):
            assert -1 == calculator.subtract(2,3)