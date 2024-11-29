def translate_code(source_code, source_language, target_language):
    # Define translation rules for different languages
    translation_rules = {
        'python_to_javascript': {
            'print(': 'console.log(',
            'def ': 'function ',
            'return': 'return',
            '# ': '// ',
            'True': 'true',
            'False': 'false'
        },
        'python_to_ruby': {
            'print(': 'puts ',
            'def ': 'def ',
            'return': 'return',
            '# ': '# ',
            'True': 'true',
            'False': 'false'
        },
        'javascript_to_python': {
            'console.log(': 'print(',
            'function ': 'def ',
            'return': 'return',
            '// ': '# ',
            'true': 'True',
            'false': 'False'
        },
        'javascript_to_ruby': {
            'console.log(': 'puts ',
            'function ': 'def ',
            'return': 'return',
            '// ': '# ',
            'true': 'true',
            'false': 'false'
        },
        'ruby_to_python': {
            'puts ': 'print(',
            'def ': 'def ',
            'return': 'return',
            '# ': '# ',
            'true': 'True',
            'false': 'False'
        },
        'ruby_to_javascript': {
            'puts ': 'console.log(',
            'def ': 'function ',
            'return': 'return',
            '# ': '// ',
            'true': 'true',
            'false': 'false'
        }
    }

    key = f"{source_language}_to_{target_language}"
    rules = translation_rules.get(key, {})
    
    translated_code = source_code
    for src, tgt in rules.items():
        translated_code = translated_code.replace(src, tgt)

    # Add closing parenthesis for `console.log` or `puts`
    if target_language in ['javascript', 'ruby']:
        translated_code = translated_code.replace(')', ');')

    return translated_code
