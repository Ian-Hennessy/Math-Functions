# input the list and stop when the user inputs stop

from random import randint
from typing import List

from get_input import get_user_input

N = 1

def get_avg(nums: List[int]) -> float:
    """Returns the arithmetic mean of nums"""
    ...

def get_nums() -> List[int]:
    """Returns a list of numbers entered by user"""
    ...

def run_trials(num_trials: int) -> None:
    """Performs num_trials averaging operations"""
    for trial in num_trials:
        # get_user_input
        # get_avg
        # print results
    ...


def get_input(prompt: str) -> int:
    """Uses prompt with input to retrieve user input"""
    ...


if __name__ == '__main__':
    run_trials(N)

num_list = []
while True:
    # fill list with random ints between [1, 100]
    # num_list = [randint(1, 100) for _ in range(2**16)]
    # ...
    num = input(
        "Please input a number. If you are finished, then inpunt 'done'"
    )
    if num == "done":
        break
    else:
        num_list.append(int(num))

print(num_list)

# calculate the mean

total = sum(num_list)
length = len(num_list)
final = total / length
print(f"The average of these numbers is {final}")
