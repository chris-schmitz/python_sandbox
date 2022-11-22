# * Here we're patching a direct reference of a method on a class.
# * The reference path needs to include multiple layers in dot notation:
# - the file path
# - the class name
# - the method name
def test_mocker_patch_a_class_method(mocker):
    mocker.patch('src.main.Greeter.greet', return_value="yo")
    from main import Greeter
    greeter = Greeter()
    assert greeter.greet() == "yo"


# * We can do the same for a regular function
def test_mocker_patch_a_regular_function(mocker):
    mocker.patch('src.main.hold_door', return_value="yeah I got it!!")
    from src.main import hold_door
    assert hold_door() == "yeah I got it!!"


# * With patch.object we can also patch a class' method. With patch.object we need to
# * already have a reference to the thing we're patching imported at we need to tell
# * the patch object:
# - the target, in this case the imported `Greeter` class defintion
# - the name of the attribute(method) to patch, in this case `greet`
# * if we provided just these two arguments, the patch.object method would return a reference
# * to the mock so that we could do stuff with it. Note that we don't _need_ to do anything with it,
# * we could just mock it so we can assert (verify) how it's called.
def test_mocker_patch_object_two_arguments(mocker):
    from src.main import Greeter
    from unittest.mock import MagicMock

    reference_to_now_mocked_method = mocker.patch.object(Greeter, 'greet')
    print(f"\n{reference_to_now_mocked_method}")
    reference_to_now_mocked_method.return_value = "sup!"

    greeter = Greeter()

    # ! the greeter class isn't a mock, it's still the concrete class
    assert isinstance(greeter, Greeter)

    # ! note that we didn't need to attach the mock for the greet method, mocker.patch.object already did that for us
    assert isinstance(greeter.greet, MagicMock)
    assert greeter.greet() == "sup!"

    # ! and because it's a mock we can assert that it's been called
    greeter.greet.assert_called_once()


# * With patch.object we can also shortcut the assignment of a return_value by specifying it as a third argument
def test_mocker_patch_object(mocker):
    from src.main import Greeter
    mocker.patch.object(Greeter, 'greet', return_value="hello")
    greeter = Greeter()

    assert greeter.greet() == "hello"


# ?? why is this failing now??
def test_mock_a_dependency_function_used_by_a_class(mocker):
    mocker.patch('src.main.hold_door', return_value="hold on, I got that")
    # mocker.patch('src.main.hold_door', return_value="hold on, I got that")
    from main import Greeter

    greeter = Greeter()
    assert greeter.hold_door_open() == "hold on, I got that"
