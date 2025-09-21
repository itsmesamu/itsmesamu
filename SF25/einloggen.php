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
    <title>Willkommen im Backend</title>
    <style>
        body {
            text-align: center;
            font-family: "Helvetica Neue";
        }
        form {
            display: inline-block;
            text-align: left;
            margin-left: 30px;      
            padding: 12px 16px;     
            background: #f5f5f5;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            width: 240px;           
        }
        label {
            font-weight: bold;
            font-size: 17px;
        }
        input {
            width: 160px;           
            padding: 6px;
            margin-top: 2px;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 17px;
        }
        button {
            padding: 6px 14px;
            background: cadetblue;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 15px;
        }
        button:hover {
            background:  blue;
        }
        .pw-btn {
            margin-top: 6px;
            margin-bottom: 6px;
            font-size: 11px;
            background: none;
            color: cadetblue;
            border: none;
            cursor: pointer;
            text-decoration: underline;
            padding: 0;
        }
        .pw-btn:hover {
            color: cadetblue;
        }
        p {
            font-size: 20px;
        }

    </style>
</head>
<body>
    <h1>Willkommen im Backend</h1>
    <p>Hier kannst du dich mit Namen und Passwort einloggen:</p>
    <form method="post">
        <div style="margin-bottom: 18px;">
            <label for="username">Benutzername:</label><br>
            <input type="text" id="username" name="username" oninput="checkFields()">
        </div>
        <div style="margin-bottom: 6px;">
            <label for="password">Passwort:</label><br>
            <input type="password" id="password" name="password" oninput="checkFields()"><br>
            <button type="button" class="pw-btn" onclick="window.location.href='passwort_vergessen.php'">Passwort vergessen?</button>
        </div>
        <button type="submit" id="submitBtn" class="submit-btn" disabled>Anmelden</button>
        <div style= "margin-top: 30px; font-weight: bold;">
            <p>Zurück zur Startseite:</p>
            <button type="button" class="str-btn" onclick="window.location.href='index.php'">Startseite</button>
        </div>
    </form>
    <script>
    function checkFields() {
        const user = document.getElementById('username').value;
        const pw = document.getElementById('password').value;
        document.getElementById('submitBtn').disabled = !(user && pw);
    }
    window.onload = function() {
        document.getElementById('submitBtn').disabled = true;
    };
    </script>

    <h2>Alle registrierten Nutzer:</h2>
    <?php
    while ($zeile = $ergebnis->fetchArray()):
        echo htmlspecialchars($zeile["name"]);
        echo " ";
        echo htmlspecialchars($zeile["passwort"]);
        echo "<br>";
    endwhile;?>

    <?php
    $conn = new mysqli("localhost", "BENUTZER", "PASSWORT", "DATENBANK");
    if ($conn->connect_error) {
        die("Verbindung fehlgeschlagen: " . $conn->connect_error);
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = $_POST["name"];
        $passwort = $_POST["passwort"];

        $sql = "SELECT passwort FROM users WHERE name = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("s", $name);
        $stmt->execute();
        $stmt->bind_result($hash);
        if ($stmt->fetch() && password_verify($passwort, $hash)) {
            echo "Login erfolgreich!";
        } else {
            echo "Falscher Name oder Passwort!";
        }
        $stmt->close();
        $conn->close();
        exit;
    }
    ?>
    <form method="post">
        Name: <input type="text" name="name" required><br>
        Passwort: <input type="password" name="passwort" required><br>
        <button type="submit">Login</button>
    </form>
</body>

</html>