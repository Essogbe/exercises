import operator
from string import ascii_lowercase
from typing import Tuple

#equation = "34 - -25 - -80 = -57 - m + -91"


operation ={
    "+":operator.add,
    "-":operator.sub
}



def solve_side(side_list) -> Tuple:
    """
    Take one side of the equation and return the sum of the numbers and the variable name Eg: 3+6-1+x =>8,x
    :param side_list:
    :return:
    """
    side = side_list.copy()
    res = 0
    var = ""
    if len(side)==1:#we just have one integer
        return int(side[0]),""


    #check if the 1st element is a var and replace it by 0. Eg: x+3 => 0+3
    if side[0][-1] in ascii_lowercase:
        var, side[0] = side[0], 0


    for i in range(len(side) - 1):

        #replace var(letter) by 0 and store letter preceded by its sign
        if side[i + 1][-1] in ascii_lowercase:
            var, side[i + 1] = side[i]+side[i + 1], 0 #

        if i % 2 != 0: #only  operands(not operator character) have odd index
            if i == 1:
                res += operation[side[i]](int(side[i - 1]), int(side[i + 1]))

            else:
                res = operation[side[i]](res, int(side[i + 1]))

    return res, var


def solve(equation):

    left, right = equation.split("=")
    left, right = left.split(), right.split()
    l, r = solve_side(left), solve_side(right)

    finalres = r[0] - l[0]

    if l[1] and  l[1][-1] in ascii_lowercase:
        var = l[1][-1]
        finalres = -finalres if l[1].startswith("-") else finalres
    else:
        var = r[1][-1]
        finalres = finalres if r[1].startswith("-") else -finalres

    return f"{var} = {finalres}"


with open("in.txt","r") as f:
    lines =f.readlines()
    print(lines)
    for line in lines:
        print(line,end="\n")
        print(solve(line),end="\n\n")
        print('==============')


