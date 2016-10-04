def partition(A, first, last):
    sred = 0
    if A[first] > A [sred]:
        A[first], A[sred] = A[sred], A[first]
    if A[first] > A [last]:
        A[first], A[last] = A[last], A[first]
    if A[sred] > A[last]:
        A[sred], A[last] = A[last], A[sred]
    A [sred], A [first] = A[first], A[sred]
    pivot = first
    i = first + 1
    j = last
    
    while True:
        while i <= last and A[i] <= A[pivot]:
            i += 1
        while j >= first and A[j] > A[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            A[i], A[j] = A[j], A[i]
    A[j], A[pivot] = A[pivot], A[j]
    return A
