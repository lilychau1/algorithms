def add_n_bit_binary(arr1: list, arr2: list, n_bits: int) -> list:
    assert (max(set(arr1)) <= 1 and min(arr1) >= 0), 'arr1 can only contain 0 and 1'
    assert (max(set(arr2)) <= 1 and min(arr2) >= 0), 'arr2 can only contain 0 and 1'
    # Number of bits
    result = [0] * n_bits
    
    # Add padding zeros
    arr1 = [0] * (n_bits - len(arr1)) + arr1
    arr2 = [0] * (n_bits - len(arr2)) + arr2
    
    carry = 0
    for i in range(n_bits - 1, -1, -1):
        result[i] = (arr1[i] + arr2[i] + carry) % 2
        carry = (arr1[i] + arr2[i] + carry) // 2
    assert carry != 1, 'overflow'
    return result

if __name__ == '__main__':
    add_n_bit_binary([1, 1, 1], [1, 0], 9)