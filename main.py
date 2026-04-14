import random
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="ouvidoria"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM reclamacoes")
print(cursor.fetchall())

value = 0
complainList = {}

while value != 7:
    value = int(input("=== Menu do Reclame Aqui ===\n"
    "1 - Listar\n"
    "2 - Registrar\n"
    "3 - Pesquisar\n"
    "4 - Atualizar\n"
    "5 - Remover\n"
    "6 - Exibir total\n"
    "7 - Sair\n"
    "=== : "))

    if value == 1:
        # Listar no MySQL
        cursor.execute("SELECT * FROM reclamacoes")
        result = cursor.fetchall()

        if len(result) == 0:
            print("\nUé, não há reclamações registradas!\n")
        else:
            print("\n=== Lista de reclamações ===\n")
            for i in result:
                print(f"\nID: {i[0]}\nReclamação: {i[1]}\n")
    elif value == 2:
         # Registrar no MySQL
        idInput = random.randint(1000000, 9999999)
        claimInput = input(f"\n=== Iniciando registro de ID n° {idInput} ===\n"
                           "\nTranscreva a reclamação aqui: ")
    
        sql = "INSERT INTO reclamacoes (id, texto) VALUES (%s, %s)"
        val = (idInput, claimInput)

        cursor.execute(sql, val)
        conn.commit()

        print(f"\nReclamação de ID n° {idInput} registrada!\n")
    elif value == 3:
        # Pesquisar no MySQL
        idInput = int(input("\nDigite o ID da reclamação: "))

        cursor.execute("SELECT * FROM reclamacoes WHERE id = %s", (idInput,))
        result = cursor.fetchone()

        if result:
            print(f"\nID: {result[0]}\nReclamação: {result[1]}\n")
        else:
            print("\nReclamação não encontrada.\n")
    elif value == 4:
        # Atualizar no MySQL
        idInput = int(input("\nDigite o ID da reclamação: "))

        cursor.execute("SELECT * FROM reclamacoes WHERE id = %s", (idInput,))
        result = cursor.fetchone()

        if result:
            newComplainInput = input("Digite a nova reclamação: ")

            cursor.execute(
                "UPDATE reclamacoes SET texto = %s WHERE id = %s",
                (newComplainInput, idInput)
            )
            conn.commit()

            print("\nReclamação atualizada!\n")
        else:
            print("\nReclamação não encontrada.\n")
    elif value == 5:
        # Deletar no MySQL
        idInput = int(input("\nDigite o ID da reclamação: "))

        cursor.execute("SELECT * FROM reclamacoes WHERE id = %s", (idInput,))
        result = cursor.fetchone()

        if result:
            cursor.execute("DELETE FROM reclamacoes WHERE id = %s", (idInput,))
            conn.commit()

            print("\nReclamação removida!\n")
        else:
            print("\nReclamação não encontrada.\n")
    elif value == 6:
        # Listar no MySQL
        cursor.execute("SELECT COUNT(*) FROM reclamacoes")
        total = cursor.fetchone()[0]

        print(f"\nTotal de reclamações: {total}\n")
    elif value == 7:
        print("\nSaindo.")