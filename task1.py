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

amazon_river = solution(A[0] = 4, B[0] = 0,
                        A[1] = 3, B[1] = 1,
                        A[2] = 2, B[2] = 0,
                        A[3] = 1, B[3] = 0,
                        A[4] = 5, B[4] = 0
                        )
print(amazon_river)
