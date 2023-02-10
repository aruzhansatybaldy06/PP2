class Myclass:
    def prime(self, num):
        if num == 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    def prime_1(self):
        self.x = lambda a : self.prime(a)
        list_1 = list(map(int, input().split()))
        list_1 = list(filter(self.x, list_1))
        print(list_1)

p1 = Myclass()
p1.prime_1()