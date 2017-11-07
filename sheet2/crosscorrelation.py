def cross_correlation(taus, train1, train2, time_step):
    result = list(range(len(taus)))
    num_elements = len(train1)
    for index in range(len(taus)):
        displacement_index = int(taus[index] / time_step)
        result[index] = sum([train1[i] * train2[i + displacement_index] for i in range(num_elements)
                             if 0 < i + displacement_index < num_elements])
    return result