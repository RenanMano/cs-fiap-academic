from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    status = input("Status do fluxo de vendas: ")

    # validar os dados 
    # agora, preciso modelar os dados
    # para isso, vamos usar o módulo model.py
    # preciso modelar os dados como um dict
    print(model_lead(name, email, status))

    # com os dados modelados... preciso enviar para o .json
    # vou usara o control para enviar o dicionario do lead
    control.create_lead(model_lead(name, email, status))

    print("Lead adicionado")
def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            print("Listar leads")
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")
if __name__ == "__main__":
    main()