import google.generativeai as genai
import os
import datetime
import getpass  # Librería para ocultar contraseñas en la terminal

def configurar_api():
    """Configura la clave de API de Gemini de forma segura."""
    # getpass oculta el texto introducido por el usuario para evitar exponer la clave
    api_key = getpass.getpass("Ingresa tu API Key de Gemini (se ocultará al escribir/pegar): ")
    genai.configure(api_key=api_key)

def obtener_modelo_disponible():
    """Busca dinámicamente el modelo de texto más actualizado en el servidor."""
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                return m.name
        return None
    except Exception as e:
        print(f"Error al listar modelos: {e}")
        return None

def generar_diagnostico_hvac(t_ambiente, t_evaporador, presion_baja, amperaje_compresor, refrigerante="R-410A"):
    """Envía parámetros operativos a Gemini y extrae un análisis de ingeniería completo."""
    nombre_modelo = obtener_modelo_disponible()
    
    if not nombre_modelo:
        return "Error crítico: No se encontraron modelos compatibles con tu API Key."
        
    print(f"\n[INFO] Conectando exitosamente con el modelo: {nombre_modelo}")
    modelo = genai.GenerativeModel(nombre_modelo) 
    
    # Obtenemos la fecha actual del sistema
    fecha_hoy = datetime.date.today().strftime("%d de %B de %Y")
    
    prompt = f"""
    Actúa como un ingeniero mecánico electricista experto en sistemas de refrigeración y aire acondicionado.
    Analiza los siguientes datos operativos de un equipo de aire acondicionado que usa refrigerante {refrigerante}:
    
    - Temperatura ambiente exterior: {t_ambiente} °C
    - Temperatura del evaporador: {t_evaporador} °C
    - Presión de baja (succión): {presion_baja} psi
    - Amperaje del compresor: {amperaje_compresor} A
    
    Proporciona un reporte técnico estructurado que incluya:
    1. Evaluación general del sistema (¿Los parámetros son normales para este refrigerante?).
    2. Posibles fallas o ineficiencias detectadas.
    3. Tres recomendaciones de mantenimiento correctivo/preventivo.
    4. Una sugerencia para mejorar la eficiencia energética del equipo.
    
    Genera el reporte indicando formalmente que la fecha de emisión es el {fecha_hoy}.
    
    REQUISITO DE FIRMA CRÍTICO: Firma el reporte formalmente en el encabezado (De:) y en la despedida (Atentamente:) utilizando estrictamente el nombre "Eduardo Jimenez" seguido de tu título como Ingeniero Mecánico Electricista. No incluyas ningún texto genérico entre corchetes.
    """
    
    print("Generando diagnóstico con IA...")
    try:
        respuesta = modelo.generate_content(prompt)
        return respuesta.text
    except Exception as e:
        return f"Error detallado de conexión con la API: {e}"

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    print("--- Sistema de Diagnóstico Predictivo HVAC con Gemini ---")
    configurar_api()
    
    print("\n[Ingresando datos de lectura del Manifold y Multímetro...]")
    reporte = generar_diagnostico_hvac(
        t_ambiente=35.0,        
        t_evaporador=12.0,      
        presion_baja=105.0,     
        amperaje_compresor=8.5, 
        refrigerante="R-410A"
    )
    
    print("\n================ REPORTE TÉCNICO ================\n")
    print(reporte)
    print("\n=================================================")
