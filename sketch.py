# from sketchpy import library as lib
# from sketchpy import canvas
# # obj = lib.vijay()
# # obj.draw()
#
# obj = canvas.sketch_from_image('"E:\Received\BeautyPlus_20180630161226_fast.jpg"')
# obj = draw(threshold=127)


class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"


doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")