

from functions.write_files import write_file


def test_file_write():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

def test_makedir_write():
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)


def test_fail():
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

if __name__ == "__main__":
    test_file_write()
    test_makedir_write()
    test_fail()
