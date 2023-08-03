FILEPATH = "todos.txt"
def print_list(list):
    # normal way
    # for index, item in enumerate(list):
    #     new_item = item.strip("\n")
    #     print(str(index + 1) + ". " + new_item)
    # LIST COMPREHENSION - same but quick method
    # formula: [happen_to_each_item FOR index, item IN LIST IF item > 10]
    [print(str(index + 1) + ". " + item.strip("\n")) for index, item in enumerate(list)]


def get_data(path=FILEPATH):
    """ Returns contents from file path that is passed as an argument"""
    # the old way
    # file = open(path, "r")
    # data = file.readlines()
    # file.close()
    # with context manager -> with this you do not need to .close() [new way]
    with open(path, "r") as file:
        return file.readlines()


# use of doc string that is between """ info """
# print(help(getData))


def write_data(data, path=FILEPATH):
    # file = open(path, "w")
    # file.writelines(data)
    # file.close()
    with open(path, "w") as file:
        file.writelines(data)