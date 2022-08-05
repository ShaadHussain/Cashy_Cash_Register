import pytest
import register
# from tests.register import makeChange


print("In pytest")


# Test Insufficient payment
@pytest.mark.one
def test_bad_payment():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 100

    user_map = register.makeChange(1.0, 0.5, register_map)

    assert user_map == {}

# Test Insufficient payment 2 (precision)
@pytest.mark.two
def test_bad_payment_precision():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 100

    user_map = register.makeChange(0.51, 0.5, register_map)

    assert user_map == {}

# Test no change
@pytest.mark.three
def test_no_change():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 100

    user_map = register.makeChange(12.53, 12.53, register_map)

    assert user_map == {}


@pytest.mark.four
def test_change_1():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10

    user_map = register.makeChange(0.89, 1.0, register_map)

    correct_map = {0.1: 1, 0.01: 1}
    assert user_map == correct_map

