class Heap:
    def __init__(self, data_list):
        self.data_list = data_list

        self._init_heap()

    def _compare(self, left, right):
        left_split, right_split = left.strip().split(' '), right.strip().split(' ')
        if int(left_split[-1]) > int(right_split[-1]):
            return 1
        elif int(left_split[-1]) < int(right_split[-1]):
            return -1
        else:
            return 0

    def _init_heap(self):
        total = len(self.data_list)
        for idx in range(total//2-1, -1, -1):
            cur_idx = idx
            while cur_idx < total:
                left_child_idx, right_child_idx = cur_idx*2+1, cur_idx*2+2

                if left_child_idx < total and right_child_idx < total:
                    max_child_idx = left_child_idx if self._compare(self.data_list[left_child_idx], self.data_list[right_child_idx]) == 1 else right_child_idx
                elif left_child_idx < total:
                    max_child_idx = left_child_idx
                else:
                    max_child_idx = -1

                if max_child_idx >= 0 and self._compare(self.data_list[max_child_idx], self.data_list[cur_idx]) == 1:
                    self.data_list[max_child_idx], self.data_list[cur_idx] = self.data_list[cur_idx], self.data_list[max_child_idx]
                    cur_idx = max_child_idx
                else:
                    break

    def reheapify(self):
        total = len(self.data_list)
        cur_idx = 0
        while cur_idx < total:
            left_child_idx, right_child_idx = cur_idx*2+1, cur_idx*2+2

            if left_child_idx < total and right_child_idx < total:
                max_child_idx = left_child_idx if self._compare(self.data_list[left_child_idx], self.data_list[right_child_idx]) == 1 else right_child_idx
            elif left_child_idx < total:
                max_child_idx = left_child_idx
            else:
                max_child_idx = -1

            if max_child_idx >= 0 and self._compare(self.data_list[max_child_idx], self.data_list[cur_idx]) >= 0:
                self.data_list[max_child_idx], self.data_list[cur_idx] = self.data_list[cur_idx], self.data_list[max_child_idx]
                cur_idx = max_child_idx
            else:
                break
