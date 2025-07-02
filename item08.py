import itertools

def main():
    #1
    print('#1')
    names = ['Cecilia','Lise','Marie']
    counts = [len(l) for l in names]
    print(counts)

    #2
    # use zip to run in parallel
    print('#2')
    z= zip(names,counts)
    for n,c in z:
        print(f'{n} {c}')
    #zip consumes the iterators it wraps one item at a time, which means
    # it can be used with infinitely long inputs
    # Make sure zips are operated on same length iterators

    #3
    #you can use itertools to solve the previous problem
    print('#3')
    names.append('Rosalind')
    for n,c in itertools.zip_longest(names,counts):
        print(f'{n} {c}')

if __name__ == '__main__':
    main()