# Andrew Li, 2014
# Short and greedy assignment algorithm


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def main():
    people = []  # size i
    prefs = []  # will be matrix of integers size i * j
    assignments = []  # triples of assignments size i * 3
    pref_counts = []  # counters of which is the best choice they can receive next size i
    cat_counts = []  # counter for each round of how many more people can join size j
    with open("pref.in") as f:
        for l in f:
            s = l.split()  # remove whitespace and parse input lines
            people.append(s[0])
            prefs.append(s[1:])
            pref_counts.append(1)
            assignments.append([])
    for j in xrange(len(prefs[0])):
        cat_counts.append(3)

    for i in xrange(len(prefs)):
        for j in xrange(len(prefs[i])):
            prefs[i][j] = num(prefs[i][j])

    """
    print people
    print prefs
    print assignments
    print pref_counts
    print cat_counts
    """

    # repeat six times, if necessary
    for k in xrange(len(prefs[0])):
        for j in xrange(len(prefs[0])):
            print prefs[i]
            for i in xrange(len(prefs)):
                print pref_counts[i]
                if prefs[i][j] == pref_counts[i]:
                    if cat_counts[j] > 0 and len(assignments[i]) < 3:
                        assignments[i].append(j + 1)
                        cat_counts[j] -= 1
                        print "yes."
                    pref_counts[i] += 1
    print assignments
main()
