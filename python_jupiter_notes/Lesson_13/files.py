import os

base_path = os.path.dirname(__file__)

text_file_path = os.path.join(os.path.dirname(os.path.dirname(base_path)), "md", "file.txt")
file_path = os.path.join(base_path, "data.txt")
new_file_path = os.path.join(base_path, "data2.txt")


def read_file():
    with open(file_path, "r") as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open(new_file_path, "a") as new_file:
        data_line = data_line.replace(".", "").replace(",", "")
        new_file.write(data_line)


with open(text_file_path) as text_file:
    print(text_file.read())
