from flask import Flask, render_template, request
from calc import calculate

import wordstats
from wordstats import char_count, word_count, longest_word

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    current_value = ''
    if request.method == 'POST':
        current_value = request.form.get('current_value', '')
        num = request.form.get('num', None)
        clear = request.form.get('clear', None)

        current_value = calculate(current_value, num, clear)  # Use the calculate function

    return render_template('calc.html', current_value=current_value)

@app.route('/wordstats', methods=['GET', 'POST'])
def wordstatsindex():
    if request.method == 'POST':
        user_string = request.form['user_string']
        average_length = wordstats.average_length(user_string)
        words = wordstats.word_count(user_string)
        chars = wordstats.char_count(user_string)
        long_word = wordstats.longest_word(user_string)
        return render_template('wordstats.html', average_length=average_length, word_count=words, char_count=chars, longest_word=long_word)
    else:
        return render_template('wordstats.html', average_length=None, word_count=None, char_count=None)



if __name__ == '__main__':
    app.run()
