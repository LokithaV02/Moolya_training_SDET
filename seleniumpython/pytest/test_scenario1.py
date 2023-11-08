# Pytest is basically used for unit testing/TestNG/Junit
# Unit testing, Integration testing, end to end tests
# Before and After methods - Annotations
# Parameters, Skip, groups, Results/Marker
# any test file created should be start or end with test_ or _test
# method name also should start with test_ or end with _test
# py.test -v -s / pytest -v -s: will run all the pytest
# py.test {methodname} -v -s : will run only particular method
# pytest -k {regression} -v -s : -k will run only test methods with regression will run from two diff testcases
# pytest -m {sanity} -v -s : will execute the groups with 'pytest.mark.sanity'
# @pytest.mark.skip : will skip that particular test case
# pip install pytest-html : to install html report
# pytest --html=report.html : to generate HTML report
# py.test {methodname} -v -s --html=report.html : to generate particular testmethod report
#py.test -sv ./{filename} : to run particular file
import pytest
from conftest import setup

def test_case1():
    print("learning pytest")


@pytest.mark.xfail
@pytest.mark.sanity
def test_case2regression(setup):
    n = "test"
    assert n == "test"
    print("the result is pass")


