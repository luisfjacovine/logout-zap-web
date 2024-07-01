import mysql.connector
import subprocess
import time
import pyautogui

def verificar_status():
    # Dados de conexão ao banco de dados MySQL
    db_config = {
        'host': '',
        'user': '',
        'password': '',
        'database': '',
        'port': 3306  # Porta padrão do MySQL
    }
    
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Consulta SQL para obter o valor da coluna STATUS
        query = "SELECT STATUS_LOCATION, STATUS_WHATSAPP FROM VERIFICADOR WHERE ID_USUARIO = 1 ORDER BY DATAHORA_LOCATION DESC LIMIT 1"
        cursor.execute(query)
        
        # Obter o resultado da consulta
        result = cursor.fetchone()
        if result:
            status_location = result[0]
            status_whatsapp = result[1]
            print(f"Status atual: LOCATION={status_location}, WHATSAPP={status_whatsapp}")
            
            if status_location == 1 and (status_whatsapp == 1 or status_whatsapp is None):
                logout_successful = False
                for attempt in range(3):
                    subprocess.run(["python", "logout.py"])
                    time.sleep(20)  # Espera 20 segundos para permitir o logout

                    try:
                        if pyautogui.locateOnScreen('boas-vindas.jpg', confidence=0.6) is not None:
                            logout_successful = True
                            print("Logout realizado com sucesso.")
                            # Atualizar o status no banco de dados
                            update_query = """
                                UPDATE VERIFICADOR
                                JOIN (
                                    SELECT ID_USUARIO, MAX(DATAHORA_LOCATION) AS MAX_DATAHORA_LOCATION
                                    FROM VERIFICADOR
                                    GROUP BY ID_USUARIO
                                ) AS subquery
                                ON VERIFICADOR.ID_USUARIO = subquery.ID_USUARIO 
                                AND VERIFICADOR.DATAHORA_LOCATION = subquery.MAX_DATAHORA_LOCATION
                                SET VERIFICADOR.STATUS_WHATSAPP = 0, VERIFICADOR.DATAHORA_WHATSAPP = CURRENT_TIMESTAMP
                                WHERE VERIFICADOR.ID_USUARIO = 1;
                            """
                            cursor.execute(update_query)
                            conn.commit()
                            pyautogui.keyDown('Alt')
                            pyautogui.press('F4')
                            pyautogui.keyUp('Alt')
                            break
                        else:
                            print(f"Tentativa {attempt + 1} de logout falhou. Tentando novamente...")
                    except pyautogui.ImageNotFoundException:
                        print(f"Tentativa {attempt + 1} de logout falhou. Tentando novamente...")
                if not logout_successful:
                    print("Erro ao fazer logout após 3 tentativas.")
            else:
                print("Está em casa ou Está fora mas com Whatsapp já deslogado")
        else:
            print("Nenhum registro encontrado para ID_USUARIO = 1")
        
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados MySQL: {err}")
        
    finally:
        # Fechar conexão com o banco de dados
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    while True:
        verificar_status()
        # Aguardar 5 minutos antes de verificar novamente
        time.sleep(30)  # 300 segundos = 5 minutos
