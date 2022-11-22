from src.main import Greeter


def test_mocker_patch(mocker):
    mocker.patch('src.main.Greeter.greet', return_value="yo")
    greeter = Greeter()
    assert greeter.greet() == "yo"


def test_mocker_patch_object(mocker):
    mocker.patch.object(Greeter, 'greet', return_value="hello")
    greeter = Greeter()
    assert greeter.greet() == "hello"


def test_mock_a_dependency_function_used_by_a_class(mocker):
    mocker.patch('src.main.hold_door', return_value="hold on, I got that")
    greeter = Greeter()
    assert greeter.hold_door_open() == "hold on, I got that"
