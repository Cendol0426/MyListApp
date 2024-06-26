import os

def get_variables(filepath=r"C:\Users\chong\PycharmProjects\pythonProject\venv\ExperimentI\experiments_I.txt"):
    """ Read a text file and return the list of items"""
    if not os.path.exists("experiments_I.txt"):
        with open("experiments_I.txt", "w") as file:
            pass
    with open(filepath, 'r') as file_local:
        result_local = file_local.readlines()
    return result_local
def ouput_variables(result_arg, filepath=r"C:\Users\chong\PycharmProjects\pythonProject\venv\ExperimentI\experiments_I.txt"):
    """ Write the item list in text file"""
    if not os.path.exists("experiments_I.txt"):
        with open("experiments_I.txt", "w") as file:
            pass
    with open(filepath, 'w') as file:
        file.writelines(result_arg)