def solution(A, B):
    winners = 0
    flowing_downstream = []
    downstream = 0
    for i in range(len(A)):
        if B[i] == 1:
            flowing_downstream.append(A[i])
            downstream += 1
        else:
            while downstream != 0:
                if flowing_downstream[-1] < A[i]:
                    downstream -= 1
                    flowing_downstream.pop()
                else:
                    break
            else:
                winners += 1
    winners += len(flowing_downstream)
    return winners
