from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout(self):
        assert checkout_solution.checkout("x") == -1
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAABB") == 175
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("BBEEEE") == 160
        assert checkout_solution.checkout("BEEEE") == 160
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("KK") == 120
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("PPPPP") == 200
        assert checkout_solution.checkout("QQQ") == 80
        assert checkout_solution.checkout("RRRQ") == 150
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("VVVVV") == 220
        assert checkout_solution.checkout("VVV") == 130
        assert checkout_solution.checkout("STX") == 45
        assert checkout_solution.checkout("XYZ") == 45
        assert checkout_solution.checkout("ZZZ") == 45
        assert checkout_solution.checkout("ZZZSSS") == 90



