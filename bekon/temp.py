def mnozenia(a, b):
    ret_str = "<table><tr><th></th>"
    for el in range(1, b + 1):
        ret_str += f"<th>{el}</th>"
    ret_str += f"</tr>\n"
    for i in range(1, a + 1):
        ret_str += f"<tr><th>{i}</th>"

        for j in range(1, b + 1):
            ret_str += f"<td>{i * j}</td>"
        ret_str += "<tr>\n"
    ret_str += "</table>"
    return ret_str


mn = mnozenia(5, 5)
print(mn)