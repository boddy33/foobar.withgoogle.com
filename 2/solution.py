def solution(s):
    if len(s) == 1:
        return 0
    salute_cnt = 0
    left_cnt = 0
    """ left_salute_cnt = 0
    right_cnt = 0
    right_salute_cnt = 0 """

    for char in s:
        if char == '-':
            pass
        if char == '>':
            left_cnt += 1
        if char == '<':
            salute_cnt += left_cnt*2    
        
    return salute_cnt

def main():
    print(solution('<<>><'))

if __name__ == '__main__':
    main()