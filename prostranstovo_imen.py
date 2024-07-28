def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() #ничего не произошло
test_function()
#inner_function() ##выдает ошибку