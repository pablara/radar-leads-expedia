# ============================================================
# RADAR DE LEADS - Configuración
# ============================================================
# Editar estos valores para ajustar los filtros del scraper.
# Este archivo es leído por scraper_encuentra24.py
# ============================================================

# --- FILTROS DE VEHÍCULOS ---
YEAR_MIN = 2018
PRICE_MAX_GTQ = 600000
KM_MAX = 100000
TRANSMISSION = "automatic"    # "automatic" | "manual" | "all"

# --- MARCAS PREFERIDAS (dejar vacío para todas) ---
# Si se especifican marcas, solo se capturan esas.
# Si está vacío, se capturan todas las marcas de agencia.
PREFERRED_MAKES = []
# Ejemplo: PREFERRED_MAKES = ["Toyota", "Honda", "Mazda", "Kia", "Hyundai"]

# --- SCRAPING ---
MAX_PAGES = 35
DELAY_MIN_SECONDS = 2
DELAY_MAX_SECONDS = 5

# --- SCORING ---
# Pesos para el score de calidad del lead
SCORE_AGENCY = 20          # Bonus si es de agencia
SCORE_UNIQUE_OWNER = 10    # Bonus si es único dueño
SCORE_AGENCY_RECORD = 10   # Bonus si tiene récord de agencia
SCORE_LOW_KM = 10          # Bonus si <30,000 km
SCORE_MEDIUM_KM = 5        # Bonus si <50,000 km
SCORE_RECENT_YEAR = 5      # Bonus si año >= 2022
SCORE_FULL_NAME = 5        # Bonus si vendedor tiene nombre completo

# --- OUTPUT ---
OUTPUT_DIR = "output"

# --- EMAIL (para envío automático del reporte) ---
# Configurar cuando se implemente el envío por correo
EMAIL_ENABLED = False
EMAIL_TO = "pablo@expediamotors.com"
EMAIL_SUBJECT_PREFIX = "[Radar Leads]"
