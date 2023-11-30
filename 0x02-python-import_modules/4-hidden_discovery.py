#!/usr/bin/python3
import dis
import importlib.util

def print_hidden_names(module_path):
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith("__")]

    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    module_path = "hidden_4.pyc"
    print_hidden_names(module_path)
