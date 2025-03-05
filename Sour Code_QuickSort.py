def tukar(array, a, b):
    array[a], array[b] = array[b], array[a]

def partisi(array, kiri, kanan):
    pivot = array[kanan]
    i = kiri - 1
    for j in range(kiri, kanan):
        if array[j] <= pivot:
            i += 1
            tukar(array, i, j)
    tukar(array, i + 1, kanan)
    return i + 1

def quick_sort(array, kiri, kanan):
    if kiri < kanan:
        indeks_pivot = partisi(array, kiri, kanan)
        quick_sort(array, kiri, indeks_pivot - 1)
        quick_sort(array, indeks_pivot + 1, kanan)

# Fungsi utama
if __name__ == "__main__":
    data = [35, 20, 15, 40, 50, 10]
    print("Data sebelum diurutkan:", data)
    quick_sort(data, 0, len(data) - 1)
    print("Data setelah diurutkan:", data)