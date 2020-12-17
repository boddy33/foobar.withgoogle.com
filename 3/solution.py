def solution(xs):
    if len(xs) == 1:
        return str(xs[0])
    xs = [number for number in xs if number != 0]
    new_len = len(xs)
    if not xs:
        return str(0)
    neg_cnt = len([number for number in xs if number < 0])
    # !! exceptional case - one negative number, the rest are zeroes
    if new_len == 1 and neg_cnt == 1:
        return str(0)
    xs.sort()
    if neg_cnt % 2 == 1:
        #we have odd number of negative numbers, remove the smallest one
        xs.pop(neg_cnt-1)
    product = 1
    for number in xs:
        product *= number

    return str(product)

def main():
    print(solution([0, 0, 0, 0, 0, 0, -1]))

if __name__ == '__main__':
    main()