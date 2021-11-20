def create_header(b):
    ret_str = ''
    for el in range(1, b + 1):
        ret_str += f"<th>{el}</th>"
    ret_str += f"</tr>\n"
    return ret_str


def mnozenia(a, b):
    ret_str = "<table><tr><th></th>"
    ret_str += create_header(b)
    for i in range(1, a + 1):
        ret_str += f"<tr><th>{i}</th>"
        for j in range(1, b + 1):
            ret_str += f"<td>{i * j}</td>"
        ret_str += "<tr>\n"
    ret_str += "</table>"
    return ret_str


def get_tabliczka(a=10, b=10):
    tab = []
    for i in range(1, a + 1):
        help = []
        for j in range(1, b + 1):
            help.append(i * j)
        tab.append(help)
    return tab








