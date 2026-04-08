Aplicación web para organizar y visualizar finanzas personales de manera intuitiva. Sirve como alternativa moderna a Excel, con formularios en español y gráficos interactivos.

---

## 🚀 Características
- Registro de ingresos, gastos y capital.
- Formularios en español para facilidad de uso.
- Visualización con gráficos dinámicos (Chart.js / Plotly).
- Flash messages estilizadas con Bootstrap.
- Plantillas reutilizables (`base.html`) para consistencia visual.
- Código limpio y preparado para despliegue.

---

## 📂 Estructura del proyecto

dashboard/ │── app.py │── requirements.txt │── templates/ │   ├── base.html │   ├── index.html │   ├── ingresos.html │   ├── gastos.html │   └── capital.html │── static/ │   ├── style.css │   └── charts.js


## ⚙️ Instalación
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/farofede01/dashboard-finanzas.git
   cd dashboard-finanzas

2. **Crear entorno virtual e instalar dependencias**:
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    pip install -r requirements.txt

3. **Ejecutar la aplicacion**
    flask run

## 🛠  Roadmap
• 	[ ] Integrar base de datos para persistencia.
• 	[ ] Exportar reportes en PDF/Excel.
• 	[ ] Añadir autenticación de usuarios.
• 	[ ] Mejorar gráficos con filtros dinámicos.
• 	[ ] Desplegar en un servicio cloud.

## 📌 Estado
Este proyecto está en desarrollo. Se irá mejorando de manera incremental para mostrar evolución y buenas prácticas en Flask.
