from flask import Flask, render_template_string, request
import time

app = Flask(__name__)

# Global variables to track requests
request_count = 0
last_reset_time = time.time()
request_log = []

@app.route('/')
def home():
    global request_count, last_reset_time
    now = time.time()
    # Reset the counter every 10 seconds
    if now - last_reset_time > 10:
        request_count = 0
        last_reset_time = now

    request_count += 1

    if request_count > 50:  # Threshold for "under attack"
        popup = True
    else:
        popup = False
    request_log.append((request.remote_addr, time.time()))

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Alert Example</title>
            <script>
                {% if popup %}
                    window.onload = function() {
                        setInterval(function() {
                            alert("URGENT: UNDER ATTACK!");
                        }, 500);
                    }
                {% endif %}
            </script>
        </head>
        <body>
            <h1>Welcome to the site</h1>
            <p>{{ "Attack detected!" if popup else "Everything looks normal." }}</p>
        </body>
        </html>
    ''', popup=popup)

if __name__ == "__main__":
    app.run(debug=True)
