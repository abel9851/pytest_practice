from pytest import mark

def test_environment_is_dev(app_config):
    assert app_config.base_url == "dev_pytest.com"
    assert app_config.port == 8080

@mark.skip(reason="use dev env.")
def test_environment_is_qa(app_config):
    assert app_config.base_url == "qa_pytest.com"
    assert app_config.port == 80

def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.port
    # driver.get(base_url)
