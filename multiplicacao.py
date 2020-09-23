import time

def main():
        bits = 32
        a = '{0:0{bits}b}'.format(-5, bits= bits)
        b = '{0:0{bits}b}'.format(-7, bits= bits)

        sinal = int(a[0] + '1') * int(b[0] + '1')

        value = 0
        for a_idx, a_item in enumerate(a[::-1]):
            for b_idx, b_item in enumerate(b[::-1]):
                if a_item == '1' and b_item == '1':
                    value += 1 << (a_idx + b_idx)
        value = value * sinal
        
        print("O resultado da soma sucessiva é:", value)
        
inicio = time.time()
main()
fim = time.time()
print(fim - inicio)
