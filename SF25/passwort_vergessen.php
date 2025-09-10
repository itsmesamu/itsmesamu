
<!DOCTYPE html>
<html>
<head>
    <title>Willkommen im Backand</title>
    <style>
        body {
            text-align: center;
            font-family: "Helvetica Neue";
        }
        label {
            font-size: 20px;
            font-weight: 700;
            margin-right: 76px;

        }
        input {
            width: 220px;
            padding: 8px;
            margin-top: 4px;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 16px;
        }
        button {
            padding: 8px 20px;
            background: cadetblue;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            margin-right: 124px;
        }
    </style>
</head>
<body>
    <h1>Willkommen im Backend</h1>
    <label for="email">E-Mail angeben:</label><br>
    <input type="email" id="email" name="email"><br><br>
    <button onclick="zeigeHinweis()">Absenden</button>
    <p id="hinweis" style="color: green; font-weight: bold;"></p>
    <script>
        function zeigeHinweis() {
            const email = document.getElementById('email').value;
            if(email) {
                document.getElementById('hinweis').innerText = "E-Mail wird gesendet";
            } else {
                document.getElementById('hinweis').innerText = "";
            }
        }
    </script>
    <div style="margin-top:25px; font-weight: bold;">
        <p>Zurück zur Startseite:</p>
        <button type="button" onclick="window.location.href='index.php'">Startseite</button>
    </div>
</body>
</html>