class animal:
    def animal_level_1_method():
        return "im animal method"

class dog(animal):
    def dog_level_2_method():
        return "im dog method,in inherated from animal"


class puppy(dog):
    def puppy_level_3_method():
        return "im puppy method , im inherited from class dog"
    
obj1=puppy
print(obj1.animal_level_1_method())
print(obj1.dog_level_2_method())
print(obj1.puppy_level_3_method())
