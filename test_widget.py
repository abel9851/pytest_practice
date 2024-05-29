from pytest import mark


@mark.body
class BodyTests:

	@mark.door
	def test_body_fucntions_as_expected(self):
		assert True

	def test_bumper(self):
		assert True
	
	def test_whindshield(self):
		assert True
