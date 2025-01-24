class Economy:
    def __init__(self, name, cpi, interest_rate, unemployment, consumer_confidence):
        self.name = name
        self.cpi = cpi
        self.interest_rate = interest_rate
        self.unemployment = unemployment
        self.consumer_confidence = consumer_confidence
        
        # Diccionario de rangos ideales por economía
        self.ideal_ranges = {
            "USA": {
                "cpi": (1.5, 2.5),
                "interest_rate": (0.5, 5.0),
                "unemployment": (0, 5.0),
                "consumer_confidence": (80, 120)
            },
            "UK": {
                "cpi": (1.5, 3.0),
                "interest_rate": (0.25, 4.0),
                "unemployment": (0, 5.0),
                "consumer_confidence": (75, 110)
            },
            # Agrega más países aquí
        }
        
    def calculate_trend(self, indicator):
        """
        Calcula la tendencia de un indicador (CPI, tasa de interés, desempleo, etc.)
        según los últimos 3 valores de la lista.
        """
        if len(indicator) < 3:
            return "Sin tendencia suficiente"  # Si no hay suficientes datos
        
        # Comparar los últimos 3 valores
        values = [item['value'] for item in indicator[-3:]]
        if values[0] < values[1] < values[2]:
            return "Alcista"
        elif values[0] > values[1] > values[2]:
            return "Bajista"
        else:
            return "Neutral"
        

    def analyze(self):
        # Análisis basado en los rangos ideales para cada economía
        analysis_result = []
        
        # Analizar el CPI
        cpi_current = self.cpi[-1]["value"]
        cpi_range = self.ideal_ranges[self.name]["cpi"]
        if cpi_current < cpi_range[0]:
            analysis_result.append(f"Inflación baja ({cpi_current}%) - Riesgo de deflación.")
        elif cpi_current > cpi_range[1]:
            analysis_result.append(f"Inflación alta ({cpi_current}%) - Riesgo inflacionario.")
        else:
            analysis_result.append(f"Inflación controlada ({cpi_current}%) - Estable.")
        
        # Analizar tasa de interés
        interest_rate_current = self.interest_rate[-1]["value"]
        interest_rate_range = self.ideal_ranges[self.name]["interest_rate"]
        if interest_rate_current < interest_rate_range[0]:
            analysis_result.append(f"Tasa de interés baja ({interest_rate_current}%) - Estimulante.")
        elif interest_rate_current > interest_rate_range[1]:
            analysis_result.append(f"Tasa de interés alta ({interest_rate_current}%) - Restrictiva.")
        else:
            analysis_result.append(f"Tasa de interés moderada ({interest_rate_current}%) - Aceptable.")
        
        # Analizar desempleo
        unemployment_current = self.unemployment[-1]["value"]
        unemployment_range = self.ideal_ranges[self.name]["unemployment"]
        if unemployment_current > unemployment_range[1]:
            analysis_result.append(f"Desempleo alto ({unemployment_current}%) - Preocupante.")
        else:
            analysis_result.append(f"Desempleo bajo ({unemployment_current}%) - Estable.")
        
        # Analizar confianza del consumidor
        consumer_confidence_current = self.consumer_confidence[-1]["value"]
        consumer_confidence_range = self.ideal_ranges[self.name]["consumer_confidence"]
        if consumer_confidence_current < consumer_confidence_range[0]:
            analysis_result.append(f"Confianza del consumidor baja ({consumer_confidence_current}) - Desconfianza.")
        elif consumer_confidence_current > consumer_confidence_range[1]:
            analysis_result.append(f"Confianza del consumidor alta ({consumer_confidence_current}) - Optimismo.")
        else:
            analysis_result.append(f"Confianza del consumidor moderada ({consumer_confidence_current}) - Estable.")
        
        # Retornar el análisis
        return f"Análisis de {self.name}:\n" + "\n".join(analysis_result)

#ejecucion luego de pruebas cambiar a un archivo separado
usa = Economy(
    name="USA",
    cpi=[{"date": "2024-01-01", "value": 2.0}],
    interest_rate=[{"date": "2024-01-01", "value": 5.0}],
    unemployment=[{"date": "2024-01-01", "value": 3.5}],
    consumer_confidence=[{"date": "2024-01-01", "value": 90}]
)
print(usa.analyze())
