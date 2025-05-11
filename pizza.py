def make_pizza(size,*args):#*args 是一种特殊的语法，用于在函数定义中接收任意数量的位置参数，通过*创建一个名为args的元组
    """Make a pizza with the given size and toppings."""
    print(f"Making a {size}-inch pizza with the following arg:")
    for arg in args:
        print(f"- {arg}")
    return