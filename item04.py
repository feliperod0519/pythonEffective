def main():

    #C-style error prone
    #1
    print('#1')
    a = 0b10111011
    b = 0xc5f
    print('Binary is %d, hex is %d' % (a,b))

    #2
    print('#2')
    key = 'my_var'
    value = 1.234
    formatted = '%-10s = %.2f' % (key,value)
    print(formatted)

    #3
    print('#3')
    pantry = [('avocados',1.25),('bananas',2.5),('cherries',15)]
    for i, (item,count) in enumerate(pantry):
        print('#%d: %-10s = %.2f' % (i,item,count))
    
    #4
    print('#4')
    pantry = [('avocados',1.25),('bananas',2.5),('cherries',15)]
    for i, (item,count) in enumerate(pantry):
        print('->%d: %-10s = %.2f' % (
            i+1,
            item.title(),
            round(count)))

    #5
    print('#5')
    i=1
    for (item,count) in pantry:
        print('->%d: %-10s = %.2f' % (
            i,
            item.title(),
            round(count)))
        i+=1

    #6
    print('#6')
    key = 'my_var'
    value = 1.234
    old_way = '%-10s = %.2f' %(key,value)
    new_way = '%(key)-10s = %(value).2f' %{'key':key,'value':value}
    reordered = '%(key)-10s = %(value).2f' %{'value':value,'key':key}
    assert old_way == new_way == reordered
    print(old_way)
    print(new_way)
    print(reordered)

    #7
    print('#7')
    b = 'my string'
    a = 1234.5678
    formatted = format(a,'.2f')
    formattedStr = format(b,"^20s")
    print(formatted)
    print(formattedStr)

    #8
    print('#8')
    my_key = 'my_var'
    value = 1.234
    formatted = '{} = {}'.format(key,value)
    print(formatted)

    #9
    print('#9')
    formatted = '{1} = {0}'.format(key,value) 
    print(formatted)

    #10
    print('#10')
    name = 'FelipeRod'
    formatted = '{0} loves food. See {0} cook'.format(name)   
    print(formatted)

    #11
    print('#11')
    f_string = f'{key:<10} = {value:.2f}'
    print(f_string)
    c_tuple = '%-10s = %.2f' % (key,value)
    print(c_tuple)
    str_args = '{:<10} = {:.2f}'.format(key,value)
    print(str_args)
    str_kw = '{key:<10} = {value:.2f}'.format(key=key,value=value)
    print(str_kw)
    str_dict = '%(key)-10s = %(value).2f' % {'key':key,'value':value}
    print(str_dict)
    
if __name__ == '__main__':
    main()