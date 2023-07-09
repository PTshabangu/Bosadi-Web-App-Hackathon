from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/history')
def history():
    # Retrieve and display the history of past periods
    periods = ['2023-06-01', '2023-05-01', '2023-04-01']  # Replace with your own period history data
    return render_template('history.html', periods=periods)

if __name__ == '__main__':
    app.run(debug=True)
