from library import io
from typing import List, AnyStr, Optional


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __repr__(self, level=0):
        return "\t" * level + f"|F| {self.name} | Size: {self.size}" + "\n"


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children: List[Directory | File] = []

    def __repr__(self, level=0):
        ret = "\t" * level + f"|D| {self.name} " + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

    def get_total_size(self):
        return sum([child.size if isinstance(child, File) else child.get_total_size() for child in self.children])

    def get_parent(self):
        if self.parent:
            return self.parent
        raise ValueError("Root directory doesn't have a parent")

    def get_directory(self, dir_name: str):
        for item in self.children:
            if isinstance(item, Directory) and item.name == dir_name:
                return item
        raise ValueError(f"Directory not found as a child to current dir: {self.name}")

    def add_item(self, cmd_output: str):
        match cmd_output.split(" "):
            case ["dir", dir_name]:
                new_dir = Directory(name=dir_name, parent=self)
                self.children.append(new_dir)
            case [size, file_name]:
                new_file = File(file_name, size)
                self.children.append(new_file)


def process_input(terminal_output: List[AnyStr]):
    reading_list_command = False
    current_dir: Optional[Directory] = None
    root_dir: Optional[Directory] = None

    for line in terminal_output:
        match line.split(" "):
            case ['$', 'cd', '..']:
                current_dir = current_dir.get_parent()
                reading_list_command = False
            case ['$', 'cd', directory]:
                if current_dir is None and directory == "/":
                    root_dir = Directory(name='/')
                    current_dir = root_dir
                else:
                    current_dir = current_dir.get_directory(dir_name=directory)
                reading_list_command = False
            case ['$', 'ls']:
                reading_list_command = True
            case _:
                if reading_list_command:
                    current_dir.add_item(line)
    return root_dir


def part1(root: Directory) -> int:
    def fetch_total(root_: Directory) -> dict:
        sizes = {}
        for child in root_.children:
            if isinstance(child, Directory):
                sizes |= fetch_total(child)
                sizes[child.name] = child.get_total_size()
        return sizes

    dir_sizes = fetch_total(root)
    print(dir_sizes)
    return sum(filter(lambda x: x <= 100000, dir_sizes.values()))


def part2():
    ...


if __name__ == '__main__':
    test_fp = io.load_file_path(__file__)
    test_data = list(io.read_split_lines(test_fp))
    input_ = process_input(test_data)

    print(input_)
    print(input_.get_total_size())

    print("Part 1:\n", part1(input_), "\n")
    # print("Part 2:\n", part2(test_data), "\n")
