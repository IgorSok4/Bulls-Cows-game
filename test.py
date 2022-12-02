import pytest
import classes

@pytest.mark.parametrize("word", [("qwer"), ("kopa"), ("zxcv"), ("polk"), ("jhgf"), ("dhfg")])
def test_claas_validator(word):
    assert classes.Validator.CheckIfIsogram(word) == True

@pytest.mark.parametrize("word", [("qweq"), ("kopasda"), ("zxcverwfgdds"), ("pasfgxcvrtwwolk"), ("jhgfss"), ("ddfhfg")])
def test_claas_validator_false(word):
    assert classes.Validator.CheckIfIsogram(word) == False

@pytest.mark.parametrize("computer, user, result", [("KURA","KROW", (1, 1)), ("asdf","awfe", (1, 1)), ("TWORY","TWYRO", (3, 2)), ("ABCDEF","POLIUH", (0, 0)), ("MEDYKA","MEDYKA", (6, 0)), ("ABCDE","EDACB", (0, 5))])
def test_class_Engine_def_returnBullsAndCows(computer, user, result):
    assert classes.Engine.returnBullsAndCows(computer, user) == result
