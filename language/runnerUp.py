if __name__ == '__main__':
    n = int(input())
    org_list = list(map(int, input().split()))
    org_list_max = max(org_list)
    filtered_list = list([i for i in org_list if i != org_list_max])
    filtered_list.sort()
    print(filtered_list[-1])
