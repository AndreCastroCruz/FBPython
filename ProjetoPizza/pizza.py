import os
os.system("cls")



def main_menu():
    cart = []
    while True:
        print('-'*50)
        print("Olá tudo bem?")
        print("1 - Comprar")
        print("2 - Ver Carrinho")
        print("3 - Sair")
        choice = input("Digite sua opção: ")

        if choice == '1':
            buy_menu(cart)
        elif choice == '2':
            view_cart(cart)
        elif choice == '3':
            print("Obrigado! Até a próxima.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def buy_menu(cart):
    while True:
        print('-'*50)
        print("Escolha o sabor da pizza:")
        print("1 - Mussarela - R$48,00")
        print("2 - Calabresa - R$53,00")
        print("3 - Frango Catupiry - R$55,00")
        print("4 - Voltar")
        choice = input("Digite sua opção: ")

        if choice == '1':
            add_to_cart(cart, "Mussarela", 48)
        elif choice == '2':
            add_to_cart(cart, "Calabresa", 53)
        elif choice == '3':
            add_to_cart(cart, "Frango Catupiry", 55)
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def add_to_cart(cart, pizza_flavor, price):
    cart.append((pizza_flavor, price))
    print(f"{pizza_flavor} adicionada ao carrinho.")

def view_cart(cart):
    if not cart:
        print("Carrinho está vazio.")
        return
    
    print('-'*50)
    print("Seu carrinho:")
    total = 0
    for i, (pizza_flavor, price) in enumerate(cart, start=1):
        print(f"{i} - {pizza_flavor} - R${price}")
        total += price
    print(f"Total: R${total}")
    
    while True:
        print('-'*50)
        print("1 - Confirmar compra")
        print("2 - Voltar")
        choice = input("Digite sua opção: ")

        if choice == '1':
            confirm_order(cart, total)
            break
        elif choice == '2':
            break
        else:
            print("Opção inválida. Tente novamente.")

def confirm_order(cart, total):
    print('-'*50)
    address = input("Digite o seu endereço: ")
    print('-'*50)
    print("Pedido:")
    for pizza_flavor, price in cart:
        print(f"- {pizza_flavor} - R${price}")
    print(f"Total: R${total}")
    print('-'*50)
    print("Sua compra chega de 30 a 50 minutos. \nObrigado pela compra!")
    cart.clear()

if __name__ == "__main__":
    main_menu()