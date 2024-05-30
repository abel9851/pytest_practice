class Config:
    def __init__(self, env):
        self.base_url = {
            "dev": "dev_pytest.com",
            "qa": "qa_pytest.com"
        }[env]

        self.port = {
            "dev": 8080,
            "qa": 80
        }[env]
