from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ''
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2


def test_withdraw():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(4)
    assert jar.size == 4
    jar.withdraw(2)
    assert jar.size == 2


def test_exceed_jar():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(12)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_empty_the_jar():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
