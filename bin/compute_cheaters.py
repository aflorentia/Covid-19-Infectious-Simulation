from compute_M import compute_M

def compute_cheaters(Mgiven , P, I, D1, D2, S):

    print(Mgiven , P, I, D1, D2, S)

    # mid = P // 2
    # M = compute_M(P, I, mid, D1, D2, S)
    # print(M)
    # if M > Mgiven:
    #     for N in range( mid, 1, -1):
    #         M = compute_M(P, I, N, D1, D2, S)
    #         if M < Mgiven:
    #             print(M)
    #             return N
    # else:
    #     for N in range(mid, P):
    #         M = compute_M(P, I, N, D1, D2, S)
    #         if M > Mgiven:
    #             print(M)
    #             return N - 1


    for N in range(1, P):
        # print(N)
        M = compute_M(P, I, N, D1, D2, S)
        if M > Mgiven:
            # print(M)
            return N-1

