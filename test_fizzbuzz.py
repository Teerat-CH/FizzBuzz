from main import fizzbuzz


def test_1_should_return_1():
    result = fizzbuzz(1)
    expected = "1"
    assert result == expected


def test_2_should_return_2():
    result = fizzbuzz(2)
    expected = "2"
    assert result == expected


def test_3_should_return_fizz():
    result = fizzbuzz(3)
    expected = "fizz"
    assert result == expected
