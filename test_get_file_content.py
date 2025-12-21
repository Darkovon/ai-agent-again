from functions.get_file_content import get_file_content


def test_one_file():
    result = get_file_content("calculator", "main.py")
    print(result)

def test_file_in_dir():
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

def test_forbidden():
    result = get_file_content("calculator", "/bin/cat")
    print(result)

def test_doesnot_exist():
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)


if __name__ == "__main__":
    test_one_file()
    test_file_in_dir()
    test_forbidden()
    test_doesnot_exist()
