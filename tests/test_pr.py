from pytest import mark


@mark.widget
def test_pr_functions_as_expected():
    assert True

@mark.enter
@mark.skip(reason="fail case")
def test_pr_fails():
    assert False
