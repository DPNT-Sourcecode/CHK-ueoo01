from solutions.CHK import checkout_solution


class TestCheckout():

    def test_checkout(self):
        assert checkout_solution.checkout("x") == -1
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAAAA") == 310
        assert checkout_solution.checkout("AAABB") == 175