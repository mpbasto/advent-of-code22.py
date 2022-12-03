
def int_list(filepath):
    """
    Parses input into list of type `int`.
        - filepath must be a `str`
    """
    with open(filepath, 'r') as file:
        return [int(line) for line in file.read().split()]
        

def str_list(filepath):
    """
    Reads input filepath and converts it into list of type `str`.
        - `filepath` must be a `str`
    """
    with open(filepath, 'r') as file:
        return file.read().splitlines()