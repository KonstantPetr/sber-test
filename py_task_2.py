def banking(n, k, dists):
    while k:
        modificator_i = 0
        max_dist = max(dists)
        i = dists.index(max_dist)

        while True:
            modificator_i += 1
            modificator_dist = max_dist / (modificator_i + 1)
            temp_dists = [_ for _ in dists if _ != max_dist]
            if modificator_i == k or (temp_dists and modificator_dist < max(temp_dists)):
                break

        dists[i] = int(modificator_dist) if int(modificator_dist) == modificator_dist else round(modificator_dist, 2)
        for _ in range(modificator_i):
            dists.insert(i + 1, dists[i])
        k -= modificator_i

    return dists


# cases
fast_tests = (
    (2, 2, [100]),
    (2, 3, [100]),
    (3, 1, [240, 20]),
    (3, 2, [240, 20]),
    (3, 4, [240, 20]),
    (3, 5, [240, 20]),
    (3, 5, [240, 50]),
    (6, 1, [180, 120, 50, 120, 20]),
    (6, 3, [180, 120, 50, 120, 20]),
    (6, 5, [180, 120, 50, 120, 20]),
    (20, 10, [50, 160, 20, 80, 110, 15, 415, 20, 50, 160, 90, 30, 76, 18, 310, 55, 140, 90, 60])
)
for n, k, initial_dists in fast_tests:
    print(f'initial input:\nn = {n}, k = {k}, initial_dists = {initial_dists}\nresult:')
    for dist in banking(n, k, initial_dists):
        print(dist)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
