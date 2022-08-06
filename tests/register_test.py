import pytest
import register

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

# Test zero change
@pytest.mark.three
def test_no_change():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 100

    user_map = register.makeChange(12.53, 12.53, register_map)

    assert user_map == {}

# Test 1 - 0.89
@pytest.mark.four
def test_change_1():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10

    user_map = register.makeChange(0.89, 1.0, register_map)

    correct_map = {0.1: 1, 0.01: 1}
    assert user_map == correct_map

# Test 200.77 - 100
@pytest.mark.five
def test_change_2():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10

    user_map = register.makeChange(100, 200.77, register_map)

    correct_map = {20.0: 5, 0.5: 1, 0.25: 1, 0.01: 2}
    assert user_map == correct_map

# Test 187.92 - 5
@pytest.mark.six
def test_change_3():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    user_map = register.makeChange(5, 187.92, register_map)

    correct_map = {20.0: 9, 1.0: 2, 0.5: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 2}
    assert user_map == correct_map

# Test 187.92 - 5, no dimes
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

# Test 10.25 - 10, no quarters
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

# Test 10.90 - 10, no quarters or 50¢
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

# Test 12 - 10, nothing in register
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

# Test non-numeric input
@pytest.mark.eleven
def test_bad_input_nonnumeric():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    user_ret = register.makeChange("ff", "t5", register_map)

    # correct_map = {0.1: 8, 0.05: 2}
    correct_str = "Error! Values are not numbers"
    assert user_ret == correct_str

# Test negative input
@pytest.mark.twelve
def test_bad_input_negative():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 10
    
    user_ret = register.makeChange(100, -200, register_map)

    # correct_map = {0.1: 8, 0.05: 2}
    correct_str = "Error! Non-negative numbers"
    assert user_ret == correct_str

# Testing replenishRegister() - We don't need to check for bad input 
# because it's a method internal to makeChange(), which already checks for that.
@pytest.mark.thirteen
def test_replenish_reg():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 0
    
    register.replenishRegister(1.53, register_map)

    assert register_map[1.0] == 1
    assert register_map[.5] == 1
    assert register_map[.01] == 3


# Testing replenishRegister() 2
@pytest.mark.fourteen
def test_replenish_reg_2():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 0
    
    register.replenishRegister(100.99, register_map)

    assert register_map[20] == 5
    assert register_map[.5] == 1
    assert register_map[.25] == 1
    assert register_map[.1] == 2
    assert register_map[.01] == 4

# Testing replenishRegister 3 
@pytest.mark.fifteen
def test_replenish_reg_3():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 0
    
    register.replenishRegister(35.43, register_map)

    assert register_map[20] == 1
    assert register_map[10] == 1
    assert register_map[5] == 1
    assert register_map[.25] == 1
    assert register_map[.1] == 1
    assert register_map[.05] == 1
    assert register_map[.01] == 3

# Testing Series of Transactions 1
@pytest.mark.sixteen
def test_series_1():
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    register_map = {}

    for amount in amounts:
        register_map[amount] = 50
    
    user_change_map = register.makeChange(100, 200.51, register_map)
    correct_user_map = {20: 5, 0.5: 1, 0.01: 1}

    # make sure you account for replenishing AFTER the change
    # correct_reg = {20.0: 45, 10.0: 50, 5.0: 50, 1.0: 50, 0.5: 49, 
    #                 0.25: 50, 0.1: 50, 0.05: 50, 0.01: 49}

    assert user_change_map == correct_user_map

    user_change_map = register.makeChange(27, 108.34, register_map)
    correct_user_map = {20.0: 4, 1.0: 1, 0.25: 1, 0.05: 1, 0.01: 4}

    assert user_change_map == correct_user_map

    user_change_map = register.makeChange(5, 17.24, register_map)
    correct_user_map = {10.0: 1, 1.0: 2, 0.1: 2, 0.01: 4}

    assert user_change_map == correct_user_map







    


