from demo_poetry_package.demo_lib import DemoLib

def test_demo_lib():
    assert DemoLib.help() == "allo de la lib"