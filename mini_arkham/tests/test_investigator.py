"""
Tests investigator instance
Command line: python -m pytest mini_arkham/tests/test_investigator.py
"""

import pytest
from mini_arkham.common.investigator import Investigator


@pytest.fixture
def investigator_values():
    return {'sanity': 5, 'stamina': 5, 'fight': 4, 'will': 3}


@pytest.fixture
def investigator_obj(investigator_values):
    return Investigator(**investigator_values)


def test_create_investigator(investigator_obj, investigator_values):
    investigator_values['insane'] = False
    investigator_values['unconscious'] = False
    for attr_name in investigator_values:
        assert getattr(investigator_obj, attr_name) == investigator_values[attr_name]


def test_reduce_sanity(investigator_obj):
    obj = investigator_obj
    obj.reduce("sanity", 3)
    assert obj.sanity == 2
    assert obj.insane == False


def test_insane(investigator_obj):
    obj = investigator_obj
    obj.reduce("sanity", 10)
    assert obj.sanity == 0
    assert obj.insane == True


def test_no_longer_insane(investigator_obj):
    obj = investigator_obj
    obj.sanity.value = 0
    obj.insane = True
    assert obj.insane == True
    obj.restore("sanity", 1)
    assert obj.sanity == 1
    assert obj.insane == False


def test_reduce_stamina(investigator_obj):
    obj = investigator_obj
    obj.reduce("stamina", 3)
    assert obj.stamina == 2
    assert obj.unconscious == False


def test_unconscious(investigator_obj):
    obj = investigator_obj
    obj.reduce("stamina", 10)
    assert obj.stamina == 0
    assert obj.unconscious == True


def test_no_longer_unconscious(investigator_obj):
    obj = investigator_obj
    obj.stamina.value = 0
    obj.unconscious = True
    assert obj.unconscious == True
    obj.restore("stamina", 1)
    assert obj.stamina == 1
    assert obj.unconscious == False