import pytest 
@pytest.mark.usefixtures("testing_fixture")
class TestExampleCLass:

    def test_1(self, testing_fixture):
        print("##############testing_fixture :", testing_fixture)
        assert False

    def test_2(self, testing_fixture):
        print("#######testing_fixture :", testing_fixture)
        assert False

def test_3(testing_fixture):
        print("#######testing_fixture :", testing_fixture)
        assert False