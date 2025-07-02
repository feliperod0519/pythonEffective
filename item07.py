def main():
    flavor_list = ['vainilla','chocolate','pecan','strawberry']

    #1
    #enumerate wraps any iterator with lazy generator
    it = enumerate(flavor_list)
    print(next(it))
    print(next(it))
    for i,flavor in enumerate(flavor_list,1):
        print(f'{i}: {flavor}')

if __name__ == '__main__':
    main()