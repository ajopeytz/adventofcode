#! /usr/bin/env python3.14
import pyaoc
import argparse
import os
import shutil
from dotenv import load_dotenv
from typing import Callable
import importlib.util
import sys
import typer
import timeit

# copied from pyaoc
def _load_solve_method(path: str) -> Callable[[str], int]:
    """Attempts to load the 'solve' method from the given Python file path."""
    # Checks that the given path exists
    if not os.path.exists(path):
        print(f"Error: Solution file not found at '{path}'.")
        raise typer.Exit(code=1)
    
    # Creates a module spec from the given path
    spec = importlib.util.spec_from_file_location("solution", path)
    if spec is None:
        print(f"Error: Could not create module spec from '{path}'.")
        raise typer.Exit(code=1)
    
    # Loads the solution module from its spec
    solution_module = importlib.util.module_from_spec(spec)
    sys.modules["solution"] = solution_module

    # Attempts to execute the solution module
    try:
        spec.loader.exec_module(solution_module)
    except Exception as e:
        print(f"Error executing solution file: {e}")
        raise typer.Exit(code=1)

    # Gets the 'solve' function from the module
    if not hasattr(solution_module, 'solve'):
        print(f"Error: No 'solve' method found in '{path}'")
        raise typer.Exit(code=1)
        
    # Returns a reference to the method
    return getattr(solution_module, 'solve')

parser = argparse.ArgumentParser()

year = 2015
for y in (next(os.walk('.'))[1]):
    if y.isdigit() and int(y) > year:
        year = int(y)
        break

parser.add_argument("--year", type=int, default=year)

day = 1
for _, days, _ in os.walk(str(year)):
    for d in days:
        if d.isdigit() and int(d) > day:
            day = int(d)
            break
        break

parser.add_argument("--day", type=int, default=day)
parser.add_argument("--part", type=int, default=0)
parser.add_argument("--runs", type=int, default=100)
parser.add_argument("--save", action="store_true", default=False)
parser.add_argument("--test", type=int, default=0)

parser.add_argument("command", type=str, choices=["init", "test", "run", "submit", "bench"], help="Command to execute")

args = parser.parse_args()

year = args.year
day = args.day
part = args.part
runs = args.runs
save = args.save

print ("Advent of Code CLI")
print("Executing command: ", args.command)

if part == 0:
    part = 1
    for _, _, files in os.walk(str(year)+"/"+f"{day:02d}"):
        if "part2.py" in files:
            part = 2
            break

print("Year: ", year, "Day: ", day, "Part: ", part)
print("--------------------------------")

#load session from .env
load_dotenv()

path = str(year)+"/"+f"{day:02d}"
if args.command == "init":
    if not os.path.exists(path):
        os.makedirs(path)
    shutil.copy("template.py", path+"/part1.py")
    pyaoc.save_day_input(year=year, day=day, path=path+"/input.txt")
    os.makedirs(path+"/tests/1/1")
    os.makedirs(path+"/tests/2/1")
    open(path+"/tests/1/1/input.txt", 'a').close()
    open(path+"/tests/1/1/result.txt", 'a').close()
    open(path+"/tests/2/1/input.txt", 'a').close()
    open(path+"/tests/2/1/result.txt", 'a').close()
elif args.command == "test":
    fn = _load_solve_method(path+"/part"+str(part)+".py")
    for _, tests, _ in os.walk(str(year)+"/"+f"{day:02d}"+"/tests/"+str(part)):
        if args.test != 0:
            tests = [str(args.test)]
        for test in tests:
            if os.path.exists(path+"/tests/"+str(part)+"/"+str(test)+"/input.txt") and os.path.exists(path+"/tests/"+str(part)+"/"+str(test)+"/result.txt"):
                print("Running Test",test)
                with open(path+"/tests/"+str(part)+"/"+str(test)+"/result.txt", "r") as f:
                    test_result = int(f.read())
                    print("Expected result: ", test_result)
                    print(pyaoc.test_solution(fn, test_result=test_result, path=path+"/tests/"+str(part)+"/"+str(test)+"/input.txt"))
            else:
                print(f"Test {test} not found")
elif args.command == "run":
    fn = _load_solve_method(path+"/part"+str(part)+".py")
    if os.path.exists(path+"/input.txt") and os.path.exists(path+"/tests/"+str(part)+"/result.txt"):
        with open(path+"/tests/"+str(part)+"/result.txt", "r") as f:
            result = int(f.read())
    else:
        result = 0

    if save:
        result = fn(path+"/input.txt")
        with open(path+"/tests/"+str(part)+"/result.txt", "w") as f:
            f.write(str(result))
    correct = pyaoc.test_solution(fn, test_result=result, path=path+"/input.txt")
    if correct and part == 1 and not os.path.exists(path+"/part2.py"):
        shutil.copy(path+"/part1.py", path+"/part2.py")

elif args.command == "submit":
    fn = _load_solve_method(path+"/part"+str(part)+".py")
    correct = pyaoc.submit(fn, part=part, year=year, day=day, path=path+"/input.txt", test=False)

    if correct:
        if not os.path.exists(path+"/tests/"+str(part)+"/result.txt"):
            result = fn(path+"/input.txt")
            with open(path+"/tests/"+str(part)+"/result.txt", "w") as f:
                f.write(str(result))
        if part == 1 and not os.path.exists(path+"/part2.py"):
            shutil.copy(path+"/part1.py", path+"/part2.py")

elif args.command == "bench":
    print("--- Benchmarking ---")
    print("Year: ", year, "Day: ", day, "Part: ", part)
    n = runs
    print("Number of iterations: ", n)
    fn = _load_solve_method(path+"/part"+str(part)+".py")
    time = timeit.timeit(lambda: fn(path+"/input.txt"), number=n)
    print("Time: ", time)
    print("Time per iteration: ", time/n)
