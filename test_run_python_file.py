from functions.run_python_file import run_python_file


def test_instructions():
    output = run_python_file("calculator", "main.py")
    print(output)

def test_run_calc():
    output = run_python_file("calculator", "main.py", ["3 + 5"])
    print(output)

def test_run_tests():
    output = run_python_file("calculator", "tests.py")
    print(output)

def test_dir_error():
    output = run_python_file("calculator", "../main.py")
    print(output)

def test_file_error():
    output = run_python_file("calculator", "nonexistent.py")
    print(output)

def test_text_error():
    output = run_python_file("calculator", "lorem.txt")
    print(output)

if __name__ == "__main__":
     test_instructions()
     test_run_calc()
     test_run_tests()
     test_dir_error()
     test_file_error()
     test_text_error()
