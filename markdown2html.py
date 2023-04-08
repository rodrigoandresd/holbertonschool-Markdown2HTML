import sys
import os
import markdown

# Verificar si se proporcionaron suficientes argumentos
if len(sys.argv) < 3:
    sys.stderr.write("Usage: {} input_file output_file\n".format(sys.argv[0]))
    sys.exit(1)

# Verificar si el archivo de entrada existe
input_file = sys.argv[1]
if not os.path.isfile(input_file):
    sys.stderr.write("Missing {}\n".format(input_file))
    sys.exit(1)

# Convertir el archivo de Markdown a HTML
output_file = sys.argv[2]
with open(input_file, 'r') as f:
    html = markdown.markdown(f.read(), output_format='html5')
with open(output_file, 'w') as f:
    f.write(html)

# Salir con un código de salida 0
sys.exit(0)
