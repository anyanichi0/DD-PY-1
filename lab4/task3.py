def delete(list_, index=None):
    if index != None:
        return list_[slice(index)]+list_[slice(index+1, len(list_))]  # TODO реализовать функцию удаления элемента из списка по индексу
    else:
        return list_[slice(len(list_)-1)]


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
