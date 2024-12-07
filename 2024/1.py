example = """3   4
4   3
2   5
1   3
3   9
3   3""".split('\n')

input = ""
with open("data/1-input", 'r') as f:
    input = f.readlines()

def calculate_distance(data):
    left, right = [], []

    for pair in data:
        l, r = pair.split('   ')
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    distance = 0
    for i in range(0, len(left)):
        distance += abs(left[i] - right[i])

    print(distance)


def calculate_similarity(data):
    left, right = [], []
    sim_left, sim_right = {}, {}
    
    for pair in data:
        l, r = pair.split('   ')
        r = r.strip()
        sim_left[l] = sim_left.get(l, 0) + 1
        sim_right[r] = sim_right.get(r, 0) + 1
        left.append(int(l))
        right.append(int(r))

    print(sim_right)

    similarity = 0
    for i in range(0, len(left)):
        similarity += left[i] * sim_right.get(str(left[i]), 0)
    
    print(similarity)



if __name__ == '__main__':
    # calculate_distance(example)
    # calculate_distance(input)
    # calculate_similarity(example)
    calculate_similarity(input)
