
def line():
    print("="* 40)

def hello():
    line()
    print("Olá, esse é o programa que calcula sua idade em dias")
    line()

def age():
    years = int(input("Digite os anos: "))
    months = int(input("Digite os meses: "))
    days = int(input("Digite os dias: "))
    print("A sua idade em dias é de", ((years*365) + (months *30) + days))


def end():
    print("Fim. Obrigada por usar este programa")
    
hello()
age()
end()
