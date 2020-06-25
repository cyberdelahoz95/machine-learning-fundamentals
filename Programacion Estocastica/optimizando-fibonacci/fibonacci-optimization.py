import sys
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_with_memo(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try: 
        return memo[n]
    except KeyError:
        resultado = fibonacci_with_memo(n - 1, memo) +  fibonacci_with_memo(n - 2, memo)
        memo[n] = resultado
        return resultado


if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    n = int(input("Escoger número: "))
    result = fibonacci_with_memo(n)
    print(result)