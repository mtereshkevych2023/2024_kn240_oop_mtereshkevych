from flask import Flask, Response
import matplotlib.pyplot as plt
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>📈 Welcome to the New Math Visualizer!</h1>
        <p>Click the button to explore more functions!</p>
        <form action="/plot">
            <button style="padding: 10px 20px; font-size: 18px; background-color: #2196F3; color: white; border: none; border-radius: 5px;">
                Show New Plot 🔍
            </button>
        </form>
    '''

@app.route('/plot')
def plot():
    x = np.linspace(0.1, 10, 400)
    y1 = np.exp(x)
    y2 = np.log(x)
    y3 = np.sqrt(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label="exp(x)", color="purple", linestyle="-", linewidth=2)
    plt.plot(x, y2, label="log(x)", color="orange", linestyle="--", linewidth=2)
    plt.plot(x, y3, label="√x", color="teal", linestyle="-.", linewidth=2)

    plt.title("🔢 New Mathematical Functions", fontsize=18)
    plt.xlabel("x", fontsize=14)
    plt.ylabel("y", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return Response(buf.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
