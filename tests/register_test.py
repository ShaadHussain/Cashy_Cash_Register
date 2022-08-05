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

@pytest.mark.five
def test_change_2():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10

    user_map = register.makeChange(100, 200.77, register_map)

    correct_map = {20.0: 5, 0.5: 1, 0.25: 1, 0.01: 2}
    assert user_map == correct_map

@pytest.mark.six
def test_change_3():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    user_map = register.makeChange(5, 187.92, register_map)

    correct_map = {20.0: 9, 1.0: 2, 0.5: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 2}
    assert user_map == correct_map

@pytest.mark.seven
def test_change_3_no_dimes():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    register_map[0.1] = 0

    user_map = register.makeChange(5, 187.92, register_map)

    correct_map = {20.0: 9, 1.0: 2, 0.5: 1, 0.25: 1, 0.05: 3, 0.01: 2}
    assert user_map == correct_map

@pytest.mark.eight
def test_change_4_no_quarters():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    register_map[0.25] = 0

    user_map = register.makeChange(10, 10.25, register_map)

    correct_map = {0.1: 2, 0.05: 1}
    assert user_map == correct_map

@pytest.mark.nine
def test_change_4_no_quarters_no_50c():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    register_map[0.25] = 0
    register_map[0.5] = 0

    register_map[0.1] = 8

    user_map = register.makeChange(10, 10.90, register_map)

    correct_map = {0.1: 8, 0.05: 2}
    assert user_map == correct_map

@pytest.mark.ten
def test_change_not_enough_in_register():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 0
    
    register_map[0.25] = 2
    register_map[0.5] = 1

    user_ret = register.makeChange(10, 12, register_map)

    # correct_map = {0.1: 8, 0.05: 2}
    correct_str = "No money in register!"
    assert user_ret == correct_str

@pytest.mark.ten
def test_bad_input_nonnumeric():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    user_ret = register.makeChange("ff", "t5", register_map)

    # correct_map = {0.1: 8, 0.05: 2}
    correct_str = "Error! Values are not numbers"
    assert user_ret == correct_str

@pytest.mark.eleven
def test_bad_input_negative():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    user_ret = register.makeChange(100, -200, register_map)

    # correct_map = {0.1: 8, 0.05: 2}
    correct_str = "Error! Non-negative numbers"
    assert user_ret == correct_str

