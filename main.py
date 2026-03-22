import re

def checar_senha(senha):
    erros = []
    pontos = 0

    # regra básica de tamanho
    if len(senha) < 8:
        erros.append("Senha muito curta (mínimo 8 caracteres)")
    else:
        pontos += 1

    # maiúscula
    if any(c.isupper() for c in senha):
        pontos += 1
    else:
        erros.append("Falta letra maiúscula")

    # minúscula
    if any(c.islower() for c in senha):
        pontos += 1
    else:
        erros.append("Falta letra minúscula")

    # número
    if any(c.isdigit() for c in senha):
        pontos += 1
    else:
        erros.append("Falta número")

    # especial
    if re.search(r"[^\w\s]", senha):
        pontos += 1
    else:
        erros.append("Falta caractere especial")

    # classificação simples
    if pontos <= 2:
        nivel = "fraca"
    elif pontos <= 4:
        nivel = "ok"
    else:
        nivel = "forte"

    return nivel, erros


def rodar():
    print("=== Teste de senha ===\n")

    senha = input("Digite sua senha: ").strip()

    if not senha:
        print("Nada digitado.")
        return

    nivel, erros = checar_senha(senha)

    print(f"\nResultado: {nivel.upper()}")

    if erros:
        print("\nDá pra melhorar:")
        for e in erros:
            print("-", e)
    else:
        print("Senha bem construída 👍")


if __name__ == "__main__":
    rodar()
