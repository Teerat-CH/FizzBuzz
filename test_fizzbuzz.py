from main import fizzbuzz


def test_0_should_return_fizzbuzz():
    result = fizzbuzz(0)
    expected = "fizzbuzz"
    assert result == expected


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


def test_5_should_return_buzz():
    result = fizzbuzz(5)
    expected = "buzz"
    assert result == expected


def test_6_should_return_fizz():
    result = fizzbuzz(6)
    expected = "fizz"
    assert result == expected


def test_10_should_return_buzz():
    result = fizzbuzz(10)
    expected = "buzz"
    assert result == expected


def test_15_should_return_fizzbuzz():
    result = fizzbuzz(15)
    expected = "fizzbuzz"
    assert result == expected


def test_30_should_return_fizzbuzz():
    result = fizzbuzz(30)
    expected = "fizzbuzz"
    assert result == expected
