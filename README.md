# 🚗 Radar de Leads - Expedia Motors (Consignación)

## ¿Qué hace?
Scraper automatizado que barre **Encuentra24 Guatemala** diariamente para detectar personas vendiendo sus vehículos de agencia. Cada lead es un potencial cliente de **consignación** para Expedia Motors.

## Filtros aplicados
| Filtro | Valor |
|--------|-------|
| Año mínimo | 2018 |
| Precio máximo | Q600,000 |
| Kilometraje máximo | 100,000 km |
| Transmisión | Solo automáticos |
| Unidad de distancia | Solo KM (excluye millas = no es de agencia) |
| Tipo de vendedor | Particulares (excluye lotes/dealers) |

## Instalación

```bash
# Clonar o copiar el proyecto
cd radar-leads-expedia

# Instalar dependencias
pip install requests beautifulsoup4 openpyxl

# Ejecutar primera vez (todos los anuncios)
python scraper_encuentra24.py --all

# Ejecuciones siguientes (solo nuevos)
python scraper_encuentra24.py
```

## Uso

### Ejecución básica (solo anuncios nuevos)
```bash
python scraper_encuentra24.py
```

### Ejecución completa con detalle de cada anuncio
```bash
python scraper_encuentra24.py --full-detail
```
> ⚠️ Más lento pero más preciso. Visita cada anuncio para extraer descripción completa, teléfono y más señales.

### Ver todos los anuncios (incluyendo ya vistos)
```bash
python scraper_encuentra24.py --all
```

### Limitar páginas
```bash
python scraper_encuentra24.py --max-pages 5
```

## Output
- `output/leads_consignacion_YYYY-MM-DD.xlsx` — Excel con formato, colores y filtros
- `output/leads_consignacion_YYYY-MM-DD.csv` — CSV de respaldo
- `output/seen_ads.json` — Tracking de anuncios ya procesados

## Sistema de Scoring (0-100)

| Score | Significado | Color en Excel |
|-------|-------------|----------------|
| 70-100 | Lead caliente — contactar primero | 🟢 Verde |
| 50-69 | Lead tibio — vale la pena revisar | 🟡 Amarillo |
| 0-49 | Lead frío — prioridad baja | Sin color |

### Factores del score:
- ✅ +20 pts: Vehículo de agencia confirmado
- ✅ +10 pts: Único dueño
- ✅ +10 pts: Tiene récord de agencia
- ✅ +10 pts: Menos de 30,000 km
- ✅ +5 pts: Menos de 50,000 km
- ✅ +5 pts: Año 2022 o más reciente
- ❌ -30 pts: Parece ser dealer/lote
- ❌ -50 pts: Muestra millas (no es de agencia)
- ❌ -50 pts: Transmisión manual

## Automatización diaria

### Opción 1: Cron job (Linux/Mac)
```bash
# Editar crontab
crontab -e

# Agregar línea para ejecutar todos los días a las 6:00 AM
0 6 * * * cd /ruta/al/proyecto && python scraper_encuentra24.py --full-detail >> output/log.txt 2>&1
```

### Opción 2: GitHub Actions (gratis)
Crear `.github/workflows/scraper.yml` para ejecución automática en la nube.

### Opción 3: Claude Code Cloud
Ejecutar como tarea recurrente en Claude Code web con `--remote`.

## Próximos pasos
1. [ ] Agregar envío automático del Excel por email
2. [ ] Integrar con WhatsApp Business API para notificaciones
3. [ ] Expandir a otras fuentes (OLX, Facebook Marketplace)
4. [ ] Agregar detección de leads de compra (para Naves)
5. [ ] Dashboard web para visualizar leads en tiempo real

## Estructura del proyecto
```
radar-leads-expedia/
├── scraper_encuentra24.py   # Script principal del scraper
├── config.py                # Configuración de filtros
├── README.md                # Esta documentación
├── requirements.txt         # Dependencias Python
└── output/                  # Archivos generados
    ├── leads_consignacion_YYYY-MM-DD.xlsx
    ├── leads_consignacion_YYYY-MM-DD.csv
    └── seen_ads.json
```
