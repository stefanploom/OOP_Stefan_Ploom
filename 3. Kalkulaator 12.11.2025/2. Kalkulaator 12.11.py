class Kalkulaator:
    pi = 3.14159

    def summa(self, a, b):
        return a + b

    def vahe(self, a, b):
        return a - b

    def korrutis(self, a, b):
        return a * b

    def jagatis(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Viga: nulliga ei saa jagada"

    def ringi_umbermoot(self, raadius):
        return 2 * Kalkulaator.pi * raadius


calc = Kalkulaator()

print("Summa:", calc.summa(100, 24))
print("Vahe:", calc.vahe(4, 9))
print("Korrutis:", calc.korrutis(11, 234))
print("Jagatis:", calc.jagatis(100, 25))
print("Ringi ümbermõõt (r=10):", calc.ringi_umbermoot(10))
