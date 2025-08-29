# peritacion-backend (mínimo viable para Lambda)

Estructura preparada para una Lambda en Python ejecutable

## Estructura
peritacion-backend/
├─ lambda_functions/
│ └─ hello_world/
│ ├─ app.py
│ └─ requirements.txt
├─ tests/
│ └─ test_hello_world.py
└─ README.md

## Ejecutar localmente

cd lambda_functions/hello_world
python app.py

## Test
cd tests
python test_hello_world.py

## Empaquetar zip
cd lambda_functions/hello_world
zip -r hello_world.zip .

## Handler
Archivo: lambda_functions/hello_world/app.py
Función: lambda_handler(event, context)
