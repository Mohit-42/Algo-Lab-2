def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
 
    L1 = [arr[p + i] for i in range(n1)]
    R = [arr[q + i + 1] for i in range(n2)]
 
    L1.append(float('inf'))
    R.append(float('inf'))
 
    i, j = 0, 0
 
    for k in range(p, r+1):
        
        if L1[i] < R[j]:
            arr[k] = L1[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        
        
 
def merge_sort(arr, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
      