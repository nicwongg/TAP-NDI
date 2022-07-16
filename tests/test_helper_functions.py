import pytest
import helper_functions


def test_get_call_records():
    assert len(helper_functions.get_call_records("S****252G")) == 5
    
def test_has_ongoing_call():
    assert helper_functions.has_ongoing_call("tom@moe.gov.sg") == False

def test_mark_call_as_on_going():
    helper_functions.mark_call_as_ongoing("tom@moe.gov.sg", "S****252G")
    assert helper_functions.has_ongoing_call("tom@moe.gov.sg") == True

def test_mark_call_as_on_ended():
    helper_functions.mark_call_as_ended("tom@moe.gov.sg")
    assert helper_functions.has_ongoing_call("tom@moe.gov.sg") == False
