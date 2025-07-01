def main():
    
    #tuples are immutable
    snack_calories = { 'chips':140,'popcorn':80,'nuts':190 }
    #1
    print('#1')
    items = tuple(snack_calories)
    print(items)
    #2
    print('#2')
    items = tuple(snack_calories.items())
    print(items)
    #3
    print('#3')
    item = ('Peanut butter','Jelly')
    first = item[0]
    second = item[1]
    print(first,'and',second)
    #4
    print('#4')
    pair = ('Chocolate','Peanut butter')
    try:
        pair[0] = 'what-ever'
    except:
        print('tuples are immutable')
    #5
    print('#5 --- unpacking')
    item = ('Peanut butter','Jelly')
    first,second = item
    print(first,'and',second)
    #6
    print('#6 --- complex unpackaging')
    print('function parameters by ref, lists are mutable')
    favorite_snacks = {
        'salty':('pretzels',100),
        'sweet':('cookies',180),
        'veggie':('carrots',20),
    }
    ((type1,(name1,cals1)),(type2,(name2,cals2)),(type3,(name3,cals3))) = favorite_snacks.items()
    print(f'Favorite {type1} is {name1} with {cals1} calories')
    print(f'Favorite {type2} is {name2} with {cals2} calories')
    print(f'Favorite {type3} is {name2} with {cals3} calories')
    #6.1 
    names = ['pretzels','carrots','arugula','bacon']
    print('#6.1 Old sort')
    bubble_sort_Old_Style(names)
    print(names)
    #6.2 
    names = ['pretzels','carrots','arugula','bacon']
    print('#6.2 New sort')
    bubble_sort(names)
    print(names)
    #7
    print('#7')
    snacks = [('bacon',350),('donut',240),('muffin',190)]
    for i,(name,calories) in enumerate(snacks,1):
        print(f'->{i}:{name} has {calories} calories')

def bubble_sort_Old_Style(a):
    for _ in range(len(a)):
        #print(f'{_}',)
        for i in range(1,len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

def bubble_sort(a):
    for _ in range(len(a)):
        #print(f'{_}',)
        for i in range(1,len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]



if __name__ == '__main__':
    main()