from enum import Enum

example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split('\n')

input = ""
with open("data/2-input", 'r') as f:
    input = f.readlines()

class State(Enum):
    INCREASE = 1
    DECREASE = 2
    LEVEL = 3
    UNKNOWN = 4

def calculate_safe(input_data):
    unsafe = 0
    for report in input_data:
        data = [int(x) for x in report.split(' ')]
        current =data[0]
        state = State.UNKNOWN
        for i in range(1, len(data)):
            next =data[i]
            if abs(current - next) > 3:
                unsafe += 1
                break

            if next - current > 0 and state in [State.DECREASE]: 
                unsafe += 1
                break

            if next - current < 0 and state in [State.INCREASE]: 
                unsafe += 1
                break

            if next == current: 
                unsafe += 1
                break

            state = State.INCREASE if next > current else State.DECREASE
            current = next

    return len(input_data) - unsafe

if __name__ == '__main__':
    # print(calculate_safe(example))
    print(calculate_safe(input))