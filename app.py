import os
from flask import Flask, render_template_string, Response

app = Flask(__name__)


WELCOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>BY.PROJECT - Welcome</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:'Inter','Segoe UI',sans-serif}
body,html{height:100vh;overflow:hidden;background:#0d0e12}
.welcome-layer{position:fixed;top:0;left:0;width:100%;height:100%;display:flex;justify-content:center;align-items:center;background-image:linear-gradient(rgba(13,14,18,0.5),rgba(13,14,18,0.75)),url('https://ibb.co');background-size:cover;background-position:center}
.welcome-content{text-align:center;padding:45px 60px;background:rgba(20,22,29,0.55);border:1px solid rgba(255,255,255,0.08);backdrop-filter:blur(25px);-webkit-backdrop-filter:blur(25px);border-radius:24px;box-shadow:0 20px 50px rgba(0,0,0,0.6);animation:zoomIn 0.5s cubic-bezier(0.34,1.56,0.64,1)}
@keyframes zoomIn{from{transform:scale(0.93);opacity:0}to{transform:scale(1);opacity:1}}
.welcome-content h1{color:#fff;font-size:2.8rem;font-weight:900;margin-bottom:30px;letter-spacing:-0.5px;text-shadow:0 0 25px rgba(168,85,247,0.35)}
.welcome-btn{background:#a855f7;color:#fff;border:none;padding:16px 40px;font-size:1.15rem;font-weight:700;border-radius:12px;cursor:pointer;transition:all 0.25s;box-shadow:0 4px 15px rgba(168,85,247,0.4)}
.welcome-btn:hover{background:#b46eff;transform:translateY(-2px);box-shadow:0 6px 20px rgba(168,85,247,0.6)}
.welcome-btn:active{transform:translateY(0)}
</style>
</head>
<body>
<div class="welcome-layer">
    <div class="welcome-content">
        <h1>Я это делал всю ночь!!!</h1>
        <button class="welcome-btn" onclick="location.href='/presentation'">Перейти на главную</button>
    </div>
</div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(WELCOME_TEMPLATE)

@app.route('/presentation')
def presentation():
    try:
        with open('presentation.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        return Response(html_content, mimetype='text/html')
    except FileNotFoundError:
        return "Ошибка: Я облажался!", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
