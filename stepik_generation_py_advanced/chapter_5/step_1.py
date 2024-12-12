def every_n_elements(input_str, n_elems):
    lst_from_str = input_str.split()
    result_lists = [[] for _ in range(n_elems)]
    for i, elem in enumerate(lst_from_str):
        result_lists[i % n_elems].append(elem)
    return result_lists


input_str = str(input())
n_elems = int(input())

print(every_n_elements(input_str, n_elems))
