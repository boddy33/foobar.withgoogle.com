def solution(data, n):
    if n <= 0:
        return []
    output_dict = dict()
    output = list()
    for i in range(len(data)):
        if data[i] in output_dict.keys():
            output_dict[data[i]] += 1
        else:
             output_dict[data[i]] = 1
    for i in range(len(data)):
        if output_dict[data[i]] <= n:
            output.append(data[i])
    
    return output

def main():
    print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))

if __name__ == '__main__':
    main()