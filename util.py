
def csv_to_list(file):
    with open(file) as input:
        lines = input.readlines()

    return [line.strip() for line in lines]


#print(csv_to_list("listmaker_test.txt"))
