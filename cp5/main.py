# EX 1
status = {
    "/login": 200,
    "/usuarios": 404
}

print(
    "/login" in status,
    200 in status,
    ("/login", 200) in status.items()
)


# EX 2
usuarios = {
    "ana": 5,
    "bruno": 0,
    "carla": 3
}

for usuario, acessos in usuarios.items():
    if acessos == 0:
        del usuarios[usuario]

print(usuarios)


# EX 4
partidas = (
    ("Ana", 10),
    ("Bruno", 7),
    ("Carlos", 8),
    ("Ana", 5),
    ("Bruno", 10),
    ("Carlos", 4),
    ("Ana", 2),
)

pontos = {}

# 4.1
for jogador, valor in partidas:
    if jogador not in pontos:
        pontos[jogador] = 0
    pontos[jogador] += valor

campeao = ""
maior_pontuacao = None

for jogador in pontos:
    if maior_pontuacao is None or pontos[jogador] > maior_pontuacao:
        maior_pontuacao = pontos[jogador]
        campeao = jogador
print(campeao)


# 4.2
for jogador, valor in partidas:
    if jogador not in pontos:
        pontos[jogador] = valor
    else:
        pontos[jogador] = pontos[jogador] + valor

campeao = ""
maior_pontuacao = 0

for jogador in pontos:
    if pontos[jogador] >= maior_pontuacao:
        maior_pontuacao = pontos[jogador]
        campeao = jogador
print(campeao)


# 4.3
for jogador, valor in partidas:
    if jogador not in pontos:
        pontos[jogador] = 0

    pontos[jogador] += valor

campeao = ""

for jogador in pontos:
    campeao = jogador

print(campeao)


# 4.4
for jogador, valor in partidas:
    pontos[jogador] = valor

campeao = ""

for jogador in pontos:
    if pontos[jogador] > pontos[campeao]:
        campeao = jogador


# EX 5
logs = (
    ("/login", 200),
    ("/pedidos", 500),
    ("/login", 401),
    ("/pedidos", 201),
    ("/login", 200),
)

resultado = {}

for endpoint, codigo in logs:
    if endpoint not in resultado:
        resultado[endpoint] = [0, 0]

    resultado[endpoint][0] += 1

    if codigo >= 400:
        resultado[endpoint][1] += 1

print(resultado)


# EX 6
def registrar_acesso(dados):
    dados["acessos"] += 1
    return dados

sistema = {
    "acessos": 10
}

resultado = registrar_acesso(sistema)
resultado["acessos"] += 5

print(sistema["acessos"])


# EX 8
registro = ("API-01", [200, 200, 500])
registro[1].append(404)
print(registro)
