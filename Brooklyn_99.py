def add_per(report, name, cases):

    if name in report:
        report[name] += cases
    else:
        report[name] = cases




# if we want the key with the highest value:
def calculate_efficiency(report):
    average = sum(report.values())/ len(report)

    max_value = 0
    max_name = ""

    for name, cases in report.items():
        if cases > max_value:
            max_value = cases
            max_name = name


    return average, max_name


def print_det_cases(report):
    for name, cases in report.items():
        print(f"",name, cases)


def func(x,y):
    z = x-y
    w = x + y
    return z,w

value1 , value2 = func(16,4)


def display_report(report):
    # print(report)
    for name, cases in report.items():
        print(f"name: {name}, cases: {cases}")


    print("----------------")

    # print(f"the avg and top prefomer :{calculate_efficiency(report)}" )

    average, top_name = calculate_efficiency(report)

    print(f"the avg is : {average} and top name: {top_name}")


report = {
    "jake" : 1,
    "amy": 3,
    "charles" : 5
}

display_report(report)





