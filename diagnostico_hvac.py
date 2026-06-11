import os
import datetime
import getpass
from google import genai  # ¡Nueva librería oficial!

def configurar_cliente():
    """Configura la conexión segura utilizando el nuevo SDK de Google."""
    api_key = getpass.getpass("Ingresa tu API Key de Gemini (se ocultará al escribir/pegar): ")
    # En la nueva versión, se crea un "Cliente" de conexión
    return genai.Client(api_key=api_key)

def generar_diagnostico_hvac(cliente, t_ambiente, t_evaporador, presion_baja, amperaje_compresor, refrigerante="R-410A"):
    """Envía parámetros operativos a Gemini usando la nueva API."""
    
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
    
    print("\n[INFO] Conectando exitosamente con el modelo: gemini-2.5-flash (Nuevo SDK)")
    print("Generando diagnóstico con IA...")
    
    try:
        # Nueva sintaxis de generación de contenido
        respuesta = cliente.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return respuesta.text
    except Exception as e:
        return f"Error detallado de conexión con la API: {e}"

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    print("--- Sistema de Diagnóstico Predictivo HVAC con Gemini ---")
    
    # Inicializamos el cliente con la clave segura
    cliente_ia = configurar_cliente()
    
    print("\n[Ingresando datos de lectura del Manifold y Multímetro...]")
    reporte = generar_diagnostico_hvac(
        cliente=cliente_ia,
        t_ambiente=35.0,        
        t_evaporador=12.0,      
        presion_baja=105.0,     
        amperaje_compresor=8.5, 
        refrigerante="R-410A"
    )
    
    print("\n================ REPORTE TÉCNICO ================\n")
    print(reporte)
    print("\n=================================================")
