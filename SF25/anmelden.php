<?php
$datenbank = new SQLite3('datenbank.db');

$datenbank->exec("CREATE TABLE IF NOT EXISTS NUTZER (name , passwort)");

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = $_POST["username"];
    $passwort = $_POST["password"];

    $datenbank->exec("INSERT INTO NUTZER (name, passwort) VALUES ('$name', '$passwort')");
    echo "Registrierung erfolgreich!";
}

$ergebnis = $datenbank->query("SELECT * FROM NUTZER");
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Willkommen im Backand</title>
    <style>
        body {
            text-align: center;
            font-family: "Helvetica Neue";
        }
        form {
            display: inline-block;
            text-align: left;
            margin-left: 40px;
            padding: 24px 32px;
            background: #f5f5f5;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        label {
            font-weight: bold;
        }
        input {
            width: 220px;
            padding: 8px;
            margin-top: 4px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        button {
            margin-top: 12px;
            padding: 8px 20px;
            background: cadetblue;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #0056b3;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Willkommen im Backend</h1>
    <p> Hier kannst du dich mit Namen und Passwort anmelden:</p>
    <form method="post">
        <label for="username">Benutzernamen erstellen:</label><br>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Passwort erstellen:</label><br>
        <input type="password" id="password" name="password" oninput="checkPasswords()"><br><br>
        <label for="password2">Passwort bestätigen:</label><br>
        <input type="password" id="password2" name="password2" oninput="checkPasswords()"><br><br>
        <button type="submit" id="submitBtn" disabled>Anmelden</button>
        <div style="margin-top:30px; font-weight: bold;">
            <p>Zurück zur Startseite:</p>
            <button type="button" onclick="window.location.href='index.php'">Startseite</button>
        </div>
    </form>
    
    <script>
    function checkPasswords() {
        const pw1 = document.getElementById('password').value;
        const pw2 = document.getElementById('password2').value;
        document.getElementById('submitBtn').disabled = !(pw1 && pw2 && pw1 === pw2);
    }
    window.onload = function() {
        document.getElementById('submitBtn').disabled = true;
    }
    </script>

    <h2>Alle registrierten Nutzer:</h2>
    <?php
    while ($zeile = $ergebnis->fetchArray()):
        echo htmlspecialchars($zeile["name"]);
        echo " ";
        echo htmlspecialchars($zeile["passwort"]);
        echo "<br>";
    endwhile;?>
    
</body>
</html>