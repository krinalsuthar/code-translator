from flask import Flask, render_template, request

app = Flask(__name__)

def python_to_java(python_code):
    replacements = {
        "print(": "System.out.println(",
        "def ": "void ",
        ":": " {",
    }
    java_code = []
    for line in python_code.splitlines():
        for py, java in replacements.items():
            line = line.replace(py, java)
        if line.strip().endswith(" {"):
            line += " }"
        java_code.append(line)
    return "\n".join(java_code)


def java_to_python(java_code):
    replacements = {
        "System.out.println(": "print(",
        "void ": "def ",
        "{": ":",
        "}": "",
    }
    python_code = []
    for line in java_code.splitlines():
        for java, py in replacements.items():
            line = line.replace(java, py)
        python_code.append(line.strip())
    return "\n".join(python_code)

def python_to_js(python_code):
#     """Translate Python code to JavaScript."""
    replacements = {
        "print(": "console.log(",
        "True": "true",
        "False": "false",
        "None": "null",
        "def ": "function ",
        ":": " {",
    }
    js_code = []
    for line in python_code.splitlines():
        for py, js in replacements.items():
            line = line.replace(py, js)
        if line.strip().endswith(" {"):
            line += " }"  # Close the block for JavaScript
        js_code.append(line)
    return "\n".join(js_code)


def js_to_python(js_code):
    """Translate JavaScript code to Python."""
    replacements = {
        "console.log(": "print(",
        "true": "True",
        "false": "False",
        "null": "None",
        "function ": "def ",
        "{": ":",
        "}": "",
    }
    python_code = []
    for line in js_code.splitlines():
        for js, py in replacements.items():
            line = line.replace(js, py)
        python_code.append(line.strip())
    return "\n".join(python_code)

def python_to_c(python_code):
    """Translate Python code to Java."""
    replacements = {
        "print(": "printf(",
        "def ": "void ",
        ":": " {",
    }
    C_code = []
    for line in python_code.splitlines():
        for py, C in replacements.items():
            line = line.replace(py, C)
        if line.strip().endswith(" {"):
            line += " }"
        C_code.append(line)
    return "\n".join(C_code)


def c_to_python(c_code):
    """Translate Java code to Python."""
    replacements = {
        "System.out.println(": "print(",
        "void ": "def ",
        "{": ":",
        "}": "",
    }
    python_code = []
    for line in c_code.splitlines():
        for c, py in replacements.items():
            line = line.replace(c, py)
        python_code.append(line.strip())
    return "\n".join(python_code)

def translate_code(source_code, source_lang, target_lang):
    """Handle the translation based on the source and target languages."""
    if source_lang == "Python" and target_lang == "Java":
        return python_to_java(source_code)
    elif source_lang == "Java" and target_lang == "Python":
        return java_to_python(source_code)
    elif source_lang == "C" and target_lang == "Python":
        return c_to_python(source_code)
    elif source_lang == "Python" and target_lang == "C":
        return python_to_c(source_code)
    elif source_lang == "JavaScript" and target_lang == "Python":
        return js_to_python(source_code)
    elif source_lang == "Python" and target_lang == "JavaScript":
        return python_to_java(source_code)
    # Add similar branches for C, C++, Ruby
    else:
        return "Translation not supported for the selected languages."
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        source_lang = request.form.get("source_lang")
        target_lang = request.form.get("target_lang")
        source_code = request.form.get("source_code")

        if not source_code:
            return render_template("index.html", error="Source code cannot be empty!", languages=["Python", "Java", "JavaScript", "C", "Ruby"])

        translated_code = translate_code(source_code, source_lang, target_lang)

        return render_template(
            "index.html",
            source_code=source_code,
            translated_code=translated_code,
            source_lang=source_lang,
            target_lang=target_lang,
            languages=["Python", "Java", "JavaScript", "C", "Ruby"]
        )
    else:
        return render_template("index.html", languages=["Python", "Java", "JavaScript", "C", "Ruby"])

if __name__ == "__main__":
    app.run(debug=True)
        