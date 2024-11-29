from flask import Flask, request, render_template
from translator import translate_code
from executor import execute_code

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_code = request.form['source_code']
        source_language = request.form['source_language']
        target_language = request.form['target_language']
        
        if source_language and target_language:
            translated_code = translate_code(source_code, source_language, target_language)
            result = execute_code(translated_code, language=target_language)
        else:
            result = {"output": "Translation not supported."}
        
        return render_template('index.html', result=result, code=translated_code)
    
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
