endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

list_errors = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510]
list_success = [200, 201, 202, 203, 204, 205, 206, 207, 208]

for i in range(len(status)):
    success = 0
    errors = 0
    percent = 0
    classify = '-'

    for j in status[i]:
        if j in list_success:
            success += 1
        if j in list_errors:
            errors += 1

        percent =  (success / len(status[0])) * 100

        if percent >= 80 and percent <= 100:
            classify = "ESTÁVEL"
        elif percent >= 0 and percent < 80:
            classify = "INSTÁVEL"
        elif j and j+1 in list_errors:
            classify = "CRÍTICO"
        

    print(f"Endpoint: {endpoints[i]}")
    print(f"Quantidade Sucesso: {success}")
    print(f"Quantidade de erros: {errors}")
    print(f"Porcentagem total: {percent}%")
    print(f"Classificação: {classify}")
    print()
