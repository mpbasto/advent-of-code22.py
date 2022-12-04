
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

def sub_list(filepath, separator='\n'):
    """
    Reads input filepath, splits it into sublists of `string` type and returns them within a list.
        - `filepath` must be a `str`
        - `separator` is used to split the string. If none provided, default is a line-break
    """
    with open(filepath, 'r') as data:
        output = []
        if separator:
            for i in data.read().split(sep=separator):
                output.append(i.split())
        else:
            for i in data.read().split("\n"):
                output.append(i.split())
        
    return output


