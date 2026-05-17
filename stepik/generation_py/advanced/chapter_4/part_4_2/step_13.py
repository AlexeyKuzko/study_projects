"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 2 / Step 13."""

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)

print(list1)
