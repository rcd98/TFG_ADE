# TFG_ADE
Aplicación en Python con Flask para la automatización de estrategias de opciones

Estructura de carpetas: 
-   Python: Todo lo relativo al servidor
    - calculoPrimasMetodos: Los calculos de Binomial y Black Scholes
    - Estrategias: todos los calculos para hacer las gráficas
        -basicas: call comprada, put comprada, call vendida y put vendida
        -mixtas: ratio call spread, call ratio backspread, ratio put spread y put ratio backspread
        -tendencia: spread y tunel
        -volatilidad: conos, cunas y mariposas
      
-static
    -img: almacena las gráficas

-templates: todo lo relativo al cliente (html)
- Estrategias: todos los calculos para hacer las gráficas
  - basicas: call comprada, put comprada, call vendida y put vendida
  - mixtas: ratio call spread, call ratio backspread, ratio put spread y put ratio backspread
  - tendencia: spread y tunel
  - volatilidad: conos, cunas y mariposas 
- MetodoBinomial: Calculo de la prima según método Binomial
- MetodoBlackScholes: Calculo de la prima según método Black Scholes

aplicacion.py: EJECUTAR



librerias necesarias: (hacer:  python3 -m pip install -r requirements.txt)
    - Python: 3.8
    - Flask
    - Numpy
    - Scipy
    - Matplotlib
    