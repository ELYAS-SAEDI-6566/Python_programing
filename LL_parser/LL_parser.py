def get_gramer():
    rules_number = int(input("Enter number of rules : "))
    rules = {}
    for i in range(rules_number) :
        none_terminal = str(input(f"Enter none terminal {i+1} : "))
        none_terminal_result = str(input(f"{none_terminal} --> "))
        rules[none_terminal] = none_terminal_result
    return rules
#____________________________________________________________________________________#
def correction(geramer):
    corrected_geramer = {}
    for r in geramer:
        if geramer[r] == "ep":
            for dr in geramer:
                if r in geramer[dr]:
                    geramer[dr] =  geramer[dr].replace(r,"")
    for r in geramer:
        if geramer[r] != "ep":
            corrected_geramer[r] = geramer[r]
    return corrected_geramer
#____________________________________________________________________________________#
def get_none_terminals(gramer) :
    none_terminals = []
    for i in gramer:
        none_terminals.append(i)
    return none_terminals
#____________________________________________________________________________________________#
def get_terminals(gramer,none_terminals):
    terminals = [] 
    for rule in gramer:
        for symbol in gramer[rule]:
            if symbol not in terminals and symbol != "d" and symbol not in none_terminals:
                if symbol == "i":
                    if "id" not in terminals:
                        terminals.append("id")
                else:
                    terminals.append(symbol)
    return terminals+["$"]
#_______________________________________________________________________________________________________#
def firsts(gramer = dict ,none_terminals = list ) :
    firsts_dict = {}
    for t in gramer :
        if gramer[t][0:2] == "id" :
            firsts_dict[t] = gramer[t][0:2]
        elif gramer[t][0] in none_terminals :
            firsts_dict[t] = ""
            tg = gramer[t][0]
            while(firsts_dict[t] == ""):
                if gramer[tg][0] not in none_terminals :
                    if gramer[tg][0:2] == "id" :
                        firsts_dict[t] = gramer[tg][0:2]
                    else:
                        firsts_dict[t] = gramer[tg][0]
                else:
                    tg = gramer[tg][0]
        else:
            firsts_dict[t] = gramer[t][0]
    return firsts_dict
#_________________________________________________________________________________________________________________#
def follows(gramer = dict , firsts = dict , none_terminals = list):
    follows_dict = {}
    for rule in gramer:
        follows_dict[rule] = ""
    #rule 2
    for rule in gramer:
        for symbol in gramer[rule]:
            if symbol in none_terminals:
                n_t_s = symbol
                n_t_s_count = gramer[rule].count(n_t_s)
                n_t_s_indexes = []
                indx = 0
                for i in range(n_t_s_count):
                    indx = gramer[rule].index(n_t_s , indx)
                    n_t_s_indexes.append(indx)
                    indx += 1
                    for i in n_t_s_indexes:
                        string = gramer[rule]+"|"
                        if string[i+1] in none_terminals and first[string[i+1]] not in follows_dict[n_t_s]:
                                follows_dict[n_t_s] += first[string[i+1]]+','
                        elif string[i+1:i+3] == "id" and "id" not in follows_dict[n_t_s] :
                            follows_dict[n_t_s] += "id,"
                        elif string[i+1] != "|" and string[i+1] not in follows_dict[n_t_s] :
                            follows_dict[n_t_s] += string[i+1]+','
    #rule 3
    for rule in gramer :
        if gramer[rule][-1] in none_terminals:
            for symbol in follows_dict[rule] :
                if symbol not in follows_dict[gramer[rule][-1]]:
                    if symbol == "i":
                        if follows_dict[gramer[rule][-1]] == "":
                            follows_dict[gramer[rule][-1]] += "id"
                        else:
                            follows_dict[gramer[rule][-1]] += ",id"
                    elif symbol != ",":
                        if follows_dict[gramer[rule][-1]] == "":
                            follows_dict[gramer[rule][-1]] += symbol
                        else:
                            if follows_dict[gramer[rule][-1]][-1] != ",":
                                follows_dict[gramer[rule][-1]] += ","+symbol
                            else:
                                follows_dict[gramer[rule][-1]] += symbol
    for rule in follows_dict:
        if follows_dict[rule] != "" and follows_dict[rule][-1] == "," :
            follows_dict[rule] = follows_dict[rule][:-1]
    #rule 1 
    for rule in follows_dict:
        if follows_dict[rule] != "":
            follows_dict[rule] = follows_dict[rule]+",$"
        else:
            follows_dict[rule] = "$"
    return follows_dict
#______________________________________________________________________________________________________________________#
def creat_chart(gramer = dict,firsts = dict,follows = dict,none_terminals = list ,terminals = list):
    longest_len = 0
    for rule in gramer:
        if len(gramer[rule]) > longest_len:
            longest_len = len(gramer[rule])
    spaces = ""
    for i in range(longest_len):
        spaces += " "
    chart = []
    for i in range(len(none_terminals)+1):
        x = []
        for j in range(len(terminals)+1):
            x.append(" ")
        chart.append(x)
    chart[0][0] = " "
    for i in range (len(terminals)):
        chart[0][i+1] = terminals[i]
    for i in range (len(chart)-1):
        chart[i+1][0] = none_terminals[i]

    for i in range(len(chart)-1):
        for j in range(len(chart[0])-1):
            if firsts[chart[i+1][0]] == chart[0][j+1]:
                chart[i+1][j+1] = gramer[chart[i+1][0]]
    return chart
#________________________________________________________________________________________________#
def parse(string = str, chart = list, none_terminals = list, terminals = list):
    def make_list(st):
        s = []
        for symbol in st:
            if symbol == "d" :
                None
            elif symbol == "i":
                s.append("id")
            else :
                s.append(symbol)
        return s
    string = make_list(string)+["$"]
    stack = [none_terminals[0],"$"]
    i = 0
    pointer = string[i]
    while(True):
        if stack[0] == "$" :
            return "\033[1;32mSuccessful parse\033[0;37m"
        elif stack[0] in none_terminals :
            if chart[none_terminals.index(stack[0])+1][terminals.index(pointer)+1] == "" :
                return "\033[0;31mString not accepted\033[0;37m"
            else :
                rule_result = make_list(chart[none_terminals.index(stack[0])+1][terminals.index(pointer)+1])
                stack.pop(0)
                stack = rule_result+stack
        elif stack[0] == pointer:
            stack.pop(0)
            i += 1
            pointer = string[i]
        else:
            return "\033[0;31mString not accepted\033[0;37m"
#_______________________________________________________________________________________________________________________#
Gramer = get_gramer()
# Gramer = {"S":"aBb",
#         "B":"+C",
#         "C":"(D)",
#         "D":"id"}
Gramer =  correction(Gramer)
print("_______________gramer______________")
for i in Gramer:
    print( i ,"-->",Gramer[i])
none_terminals = get_none_terminals(Gramer)
first = firsts(Gramer , none_terminals)
print("_______________firsts______________")
for i in first:
    print( i ,"=",first[i])
follow = follows(Gramer , first, none_terminals)
print("_______________follows______________")
for i in follow :
    print( i ,"=",follow[i])
terminals = get_terminals(Gramer,none_terminals)
chart = creat_chart(Gramer,first,follow,none_terminals,terminals)
from tabulate import tabulate
print("\n"+tabulate(chart, tablefmt="simple_grid"),"\n")
string = str(input("Enter string for parsing : "))
print("\n"+parse(string,chart,none_terminals,terminals),"\n")