from flask import Flask, request, jsonify

app = Flask(__name__)

class MergeSort:
    @staticmethod
    def sort(arr):
        if len(arr) > 1:
            # Divide the array into two halves
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            # Recursively sort the two halves
            MergeSort.sort(left)
            MergeSort.sort(right)

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

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json
    unsorted_arr = data['arr']
    ms = MergeSort()
    sorted_arr = ms.sort(unsorted_arr)
    return jsonify({'sorted_arr': sorted_arr})

if __name__ == '__main__':
    app.run(debug=True)
