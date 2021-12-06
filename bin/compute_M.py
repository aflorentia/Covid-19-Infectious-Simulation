from random import randrange
import numpy as np


def compute_M(P, I, N, D1, D2, S):
    population = list()
    session = list()

    Days = 1
    kappa = 0
    M = list()

    for i in range(0, P):
        population.append('he althy')
        session.append(False)

    while population.count('infected') != I:

        temp = randrange(P)
        population[temp] = 'infected'
        session[temp] = Days
    # print(population.count('infected'))
    # print(session.count(Days))
    # print(population.count('healthy'))
    # print(population)
    # print(session)
    # print("Karantina")
    while population.count('infected') != 0:
        infectious = 0

        # print(population.count('immune'))
        # print(population)
        # print(session)
        # print(Days)

        randoms = list()
        while 1:
            visitor = randrange(P)
            hosts = randrange(P)

            # print(visitor)
            # print(hosts)

            if session[visitor] or session[hosts]:
                # print("hello")
                # print(Days)
                visitorRange = range(session[visitor] + D1, session[visitor] + D2)
                hostsRange = range(session[hosts] + D1, session[hosts] + D2)
                if Days in visitorRange or Days in hostsRange:
                    # print(Days)
                    # print(visitorRange)
                    # print(hostsRange)
                    # print(session[visitor])
                    # print(session[hosts])

                    # print(Days)
                    # print(session[visitor])
                    # print(population[visitor])
                    health_status = ['healthy', 'infected']
                    luck = np.random.choice(health_status, 1, p=[1 - S, S])
                    if luck == 'infected':
                        if not session[visitor]:
                            population[visitor] = 'infected'
                            session[visitor] = Days

                        if not session[hosts]:
                            population[hosts] = 'infected'
                            session[hosts] = Days
                    else:
                        kappa = kappa + 1

            randoms.append(visitor)
            a_set = set(randoms)
            number_of_unique_values = len(a_set)
            if number_of_unique_values == N:
                break
            # if Days > 50:
            #     break

        for i in range(0, len(session)):
            if population[i] == 'infected':
                if Days == session[i] + D2:
                    population[i] = 'immune'
            if population[i] == 'infected':
                if Days > session[i]+D1:
                    infectious = infectious+1

        Days = Days + 1
        # M.append(population.count('infected'))
        M.append(infectious)


        # if Days > 50:
        #     break
    # print(population)
    # print(Days)
    print(M)
    print(max(M))

    # print(kappa)
    # print(population.count('healthy'))
    # print(population.count('immune'))
    # print(population.count('healthy')+population.count('immune'))

    return max(M)

