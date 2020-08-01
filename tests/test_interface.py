"""Test interface.py interface definition
"""
import pytest

from typing import Callable

from hamcrest import assert_that
from hamcrest import has_property

from iprovide import Interface
from iprovide import InterfaceDefException


def test_interface_with_concrete_attributes():
    """Exception raised as Interface cannot contain concrete implementation"""

    with pytest.raises(InterfaceDefException, match=r'.*'):
        class TestInterface(metaclass=Interface): # pylint: disable=unused-variable
            """Interface class that defines concrete attributes
            """
            a: int = 1
            b = 2
            c: float

def test_interface_with_only_anotations():
    """Annotations moved to internal state"""

    class TestInterface(metaclass=Interface):
        """Interface class that defines concrete attributes
        """
        a: int
        b: str
        c: float
        d: Callable[[int], str]

    expected_attributes = {
        'a': int,
        'b': str,
        'c': float,
        'd': Callable[[int], str],
    }

    assert_that(
        TestInterface,
        has_property('_attributes', expected_attributes),
    )
