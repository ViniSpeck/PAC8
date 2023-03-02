class MergeSort:
    def sort(self, arr):
        if len(arr) > 1:
            # Divide the array into two halves
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            # Recursively sort the two halves
            self.sort(left)
            self.sort(right)

            # Merge the sorted halves
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr

arr = [64, 34, 25, 12, 22, 11, 90]
ms = MergeSort()
sorted_arr = ms.sort(arr)
print(sorted_arr)