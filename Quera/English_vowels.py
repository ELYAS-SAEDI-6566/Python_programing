#Find the number of vowels in the word
def get(word) :
    voises = word.count("a")
    voises += word.count("e")
    voises += word.count("i")
    voises += word.count("o")
    voises += word.count("u")
    return voises
#______________example runable code______________#
# import English_vowels
# def test(word , number, testnum):
#     if English_vowels.get(word) == number :
#         print(f"test{testnum} {word} OK")
#     else:
#         print(f"wrong {testnum}")

# test("quera", 3 , 1)
# test("talent", 2 , 2)
# test("college", 3 , 3)
# test("contest", 2 , 4)
# test("child", 1 , 5)
# test("lms", 0 , 6)