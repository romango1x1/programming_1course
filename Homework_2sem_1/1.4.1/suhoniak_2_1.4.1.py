import math


class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __str__(self):
        return f"Vector: {self.coords}"

    def dim(self):
        return len(self.coords)

    def len(self):
        return math.sqrt(sum(x ** 2 for x in self.coords))

    def mean(self):
        return sum(self.coords) / len(self.coords) if self.coords else 0

    def max_comp(self):
        return max(self.coords, default=-math.inf)

    def min_comp(self):
        return min(self.coords, default=math.inf)


def max_dim_min_len(vectors):
    max_dim = max((v.dim() for v in vectors), default=0)
    max_dim_vectors = [v for v in vectors if v.dim() == max_dim]
    return min(max_dim_vectors, key=lambda x: x.len(), default=Vector())


def max_len_min_dim(vectors):
    max_len = max((v.len() for v in vectors), default=0)
    max_len_vectors = [v for v in vectors if v.len() == max_len]
    return min(max_len_vectors, key=lambda x: x.dim(), default=Vector())


def avg_len(vectors):
    if not vectors:
        return 0
    total_len = sum(v.len() for v in vectors)
    return total_len / len(vectors)


def count_above_avg_len(vectors):
    avg_length = avg_len(vectors)
    return sum(1 for v in vectors if v.len() > avg_length)


def max_min_comp(vectors):
    max_comp_vector = max(vectors, key=lambda x: x.max_comp(), default=Vector())
    min_comp_vector = min(vectors, key=lambda x: x.min_comp(), default=Vector())
    return max_comp_vector, min_comp_vector


def read_vectors(filename):
    vectors = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                coords = [float(coord) for coord in line.split()]
                vectors.append(Vector(*coords))
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except ValueError as e:
        print(f"Error processing file {filename}: {e}")
    return vectors


input_files = ["input01.txt", "input02.txt", "input03.txt"]

for filename in input_files:
    print(f"Results for {filename}:")

    # Read data from the current file
    vectors = read_vectors(filename)

    if vectors:
        result_max_dim_min_len_vector = max_dim_min_len(vectors)
        result_max_len_min_dim_vector = max_len_min_dim(vectors)
        result_avg_len = avg_len(vectors)
        result_count_above_avg_len = count_above_avg_len(vectors)
        result_max_comp_vector, result_min_comp_vector = max_min_comp(vectors)

        print(f"Vector with maximum dimension and minimum length: {result_max_dim_min_len_vector}")
        print(f"Vector with maximum length and minimum dimension: {result_max_len_min_dim_vector}")
        print(f"Average length of vectors: {result_avg_len:.4f}")
        print(f"Number of vectors above average length: {result_count_above_avg_len}")
        print(f"Vector with maximum maximum component: {result_max_comp_vector}")
        print(f"Vector with minimum minimum component: {result_min_comp_vector}")
    else:
        print("No vectors to process.")

    print()
