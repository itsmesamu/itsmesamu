
<!DOCTYPE html>
<html>

<head>
    <title>Willkommen im Backand</title>
    <style>
        body {
            background: #f5f5f5;
            font-family: "Helvetica Neue";
        }
        .container {
            text-align: center;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.18); /* <-- von 0.08 auf 0.18 */
            width: 420px;
            margin: 60px auto;
            padding: 24px 32px;
            background: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        button {
            margin-top:30px;
            padding: 8px 20px;
            background: cadetblue;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #0056b3;
            cursor: pointer;
        }
        p {
            font-size: 20px;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Willkommen im Backend</h1>
        <p>Wenn du schon einen Account hast dann klicke auf Login</p>
        <div>
            <button onclick="window.location.href='einloggen.php'">Login</button>
        </div>
        <p>Wenn du noch keinen Account hast dann klicke auf Anmelden</p>
        <div>
            <button onclick="window.location.href='anmelden.php'">Anmelden</button>
        </div>
    </div>
</body>