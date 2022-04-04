
if __name__ == '__main__':
    f = open("wordle-keys.txt", "r")
    f_content = f.read()
    key_list = f_content.split("\n")
    f.close()

    f = open("5-letter.txt", "r")
    f_content = f.read()
    sol_list = f_content.split("\n")
    f.close()

    sol_dict = {}
    for word in sol_list:
        sol_dict[word] = 0

    for key in key_list:
        key_chars = [c for c in key]
        for sol in sol_list:
            sol_c_check = []
            sol_chars = [c for c in sol]
            for i in range(5):
                if sol_chars[i] in key and sol_chars[i] not in sol_c_check:
                    sol_dict[sol] += 1
                    sol_c_check += sol_chars[i]
                if sol_chars[i] == key_chars[i]:
                    sol_dict[sol] += 2

    f = open('scores.txt', 'w')
    c = 0
    for w in sorted(sol_dict, key=sol_dict.get, reverse=True):
        c += 1
        f.write('#' + str(c) + ': ' + w + ' ' + str(sol_dict[w]) + '\n')
    f.close()




