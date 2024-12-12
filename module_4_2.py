def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
print("Вызов inner_function из test_function:")
test_function()
inner_function()