class TestBun:

    def test_get_name_return_correct_name_true(self, bun):
        assert bun.get_name() == "black bun"

    def test_get_price_return_correct_price_true(self, bun):
        assert bun.get_price() == 100
