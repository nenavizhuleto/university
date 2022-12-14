import bubble_sort
import insertion_sort
import quick_sort
from utils import *

def default_sort(array: list):
    array.sort()
    a = array
    return a

ALGORITHMS = [
            Algorithm("Bubble", bubble_sort.sort), 
              Algorithm("Insert", insertion_sort.sort), 
              Algorithm("Quick", quick_sort.sort), 
              Algorithm("Default", default_sort)]


def print_results(sort_name, result, exec_time):
    print(f"{sort_name}\n\tcorrect: {result}\n\ttime: {exec_time}\n")

def print_table(results: list[list], header=""):
    table = ""
    header = header.replace(' ', '\t')
    table += f"Method\t{header}\t\n"
    for method in results.keys():
        table += f"{method}\t" 
        for algo in results[method]:
            table += f"{algo['time']}s\t"

        table += "\n"

    print(table)
    return table

def test_algorithms(arrays, verbose=False):
    results = {}
    for algo in ALGORITHMS:
        results[algo.name] = []
        for array in arrays:
            [result, exec_time] = execution_time(algo.sort, array)
            correct = check_sort(result)
            results[algo.name].append({
                    "name": algo.name,
                    "result": result,
                    "correct": correct,
                    "time": exec_time
                })
            if verbose:
                print_results(algo.name, correct, exec_time)

    return results


def test(N):

    arrays = [generate_sorted_array(N), generate_reversed_array(N), generate_random_array(N)]
    results = test_algorithms(arrays)

    table = print_table(results, header="Sorted Reversed Random")
    print("Done.\n")
    return [table, arrays]

