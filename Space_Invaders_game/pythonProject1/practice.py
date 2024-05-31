class A:
    def __init__(self, id, name):
        self.id = id,
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers = +1
        self.following = +1

a = A("001", "Sushant")
b = A("001", "Rahul")

a.follow(b)
print(a.followers)
print(a.following)
print(b.followers)
print(b.following)

#
# a = A()
# a.id = "444"
#
# print(a.id)