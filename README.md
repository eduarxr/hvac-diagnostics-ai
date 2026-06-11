# Asistente de Diagnóstico Predictivo HVAC con IA ⚙️❄️

Este proyecto fue desarrollado como una solución integral aplicando principios de Ingeniería Mecánica Eléctrica y automatización con inteligencia artificial. El sistema automatiza la evaluación termodinámica de sistemas de climatización y refrigeración por medio de la API oficial de Google Gemini.

Está diseñado como una herramienta de apoyo técnico para la industria del mantenimiento de aires acondicionados, agilizando la toma de decisiones en campo mediante el cálculo indirecto de variables como el sobrecalentamiento (Superheat) y la evaluación de eficiencia térmica.

## Características Principales
* **Análisis Termodinámico Avanzado:** Interpreta la relación entre la presión de succión, amperaje, temperatura ambiente y temperatura del evaporador para sistemas con R-410A.
* **Integración con SDK de Última Generación:** Utiliza la librería oficial y más reciente `google-genai` para una comunicación directa con el modelo `gemini-2.5-flash`.
* **Tolerancia a Fallos (Retry Loop):** Cuenta con un sistema de reintentos automáticos que evita caídas del programa si los servidores en la nube experimentan alta demanda (Errores 503).
* **Seguridad de Credenciales:** Implementa ocultamiento de caracteres nativo en consola mediante `getpass` para proteger las API Keys en entornos públicos o académicos.
* **Reportes Automatizados:** Genera un diagnóstico técnico estructurado, señalando posibles fallas operativas y emitiendo recomendaciones de mantenimiento preventivo y correctivo.

## Requisitos de Instalación y Ejecución
1. Clona este repositorio: `git clone https://github.com/tu_usuario/hvac-diagnostics-ai.git`
2. Instala la dependencia oficial más reciente de Google: `pip install google-genai`
3. Ejecuta el programa principal: `python diagnostico_hvac.py`
4. Ingresa tu API Key de Google Gemini cuando el sistema lo solicite. 
   *(Nota de seguridad: Por protección, la terminal no mostrará los caracteres mientras escribes o pegas la clave. Simplemente pégala y presiona Enter).*

## Desarrollador
* **Eduardo Jimenez** - Ingeniero Mecánico Electricista
* Proyecto académico - Universidad Juárez Autónoma de Tabasco (UJAT)
