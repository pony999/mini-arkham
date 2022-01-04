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

