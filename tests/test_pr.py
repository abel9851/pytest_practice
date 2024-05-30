from pytest import mark


@mark.widget
def test_pr_functions_as_expected():
    assert True

@mark.enter
# @mark.skip(reason="fail case")
@mark.xfail(reason="just fail test")
def test_pr_fails():
    assert False
