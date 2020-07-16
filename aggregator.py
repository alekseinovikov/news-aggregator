from habr.habr_aggregator import HabrAggregator

available_modules = {'habr': HabrAggregator()}

SEPARATOR = " --- "


def print_results(results):
    for res in results:
        print(str(res[0]) + SEPARATOR + "Rating:" + str(res[2]) + "\n" + SEPARATOR + str(res[1]) + "\n")


def aggregate(modules):
    module_results = []
    for module_name in modules:
        found_module = available_modules[module_name]
        if found_module is None:
            continue

        module_result = found_module.aggregate()
        module_results.append(module_result)

    results = [y for x in module_results for y in x]
    print_results(results)
