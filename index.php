<?php
// Conexão com o banco de dados
$servername = "bz42.hostgator.com.br";
$username = "growup71_user_g2i";
$password = "Gas@2023#";
$dbname = "growup71_db_g2i";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica a conexão
if ($conn->connect_error) {
    die("Falha na conexão com o banco de dados: " . $conn->connect_error);
}

// Obtém o valor dos parâmetros GET e faz a Sanitização das entradas
$id_usuario = $conn->real_escape_string($_GET['id']);
$status = $conn->real_escape_string($_GET['stts']);
$dispositivo = $conn->real_escape_string($_GET['dispositivo']);

// Atualiza o campo na tabela com base no valor de STATUS e no ID_USUARIO
$sql = "INSERT INTO VERIFICADOR (
        ID_USUARIO, 
        STATUS_LOCATION, 
        DATAHORA_LOCATION, 
        DISPOSITIVO
        ) VALUES (
        '$id_usuario', 
        '$status',
        CURRENT_TIMESTAMP,
        '$dispositivo')";

if ($conn->query($sql) === TRUE) {
    if ($status == 1) {
        echo "Atualizado Status para Fora de Casa<br>";
        echo "Dispositivo: $dispositivo";
    } else {
        echo "Atualizado Status para Em Casa";
    }
} else {
    echo "Erro ao atualizar o status: " . $conn->error;
}

$conn->close();
?>
