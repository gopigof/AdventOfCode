import os


class InputFileTypes:
   TEST = "test"
   INPUT = "input"


def load_input_data(file_path: str, input_type: str):
   _fp, ext = os.path.splitext(file_path)
   year, day = _fp.split(os.sep)[-2:]

   if input_type in [InputFileTypes.INPUT, InputFileTypes.TEST]:
      input_data_path = os.path.join("data", year, f"{day}_{input_type}.txt")
      with open(input_data_path, "r") as fp:
         return [i for i in fp.read().split("\n") if i]
   else:
      raise ValueError("Input file type not supported!")
