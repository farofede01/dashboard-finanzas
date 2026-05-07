# 💰 AppFinanzas

Aplicación web desarrollada con Flask para gestionar ingresos y gastos personales de manera simple, visual y segura.

---

# 🚀 Demo Online

👉 https://appfinanzas.onrender.com



## 🔑 Usuario de prueba

Email: demo@app.com  
Contraseña: demo123

# ✨ Características

✅ Registro de usuarios  
✅ Inicio y cierre de sesión  
✅ Autenticación segura con Flask-Login  
✅ Contraseñas protegidas con Bcrypt  
✅ Dashboard financiero interactivo  
✅ Registro de ingresos y gastos  
✅ Edición y eliminación de movimientos  
✅ Categorías personalizadas  
✅ Balance automático  
✅ Gráficos dinámicos con Chart.js  
✅ Diseño responsive con Bootstrap 5  
✅ Base de datos SQLite  

---

# 📸 Capturas

## Dashboard

![Dashboard](static/img/dashboard.png)

## Login

![Login](static/img/login.png)

---

# 🛠️ Tecnologías utilizadas

- Python
- Flask
- Flask-Login
- Flask-Bcrypt
- Flask-SQLAlchemy
- Bootstrap 5
- Chart.js
- SQLite
- HTML5
- CSS3

---

# 📂 Estructura del proyecto

```bash
APPFINANZAS/
│
├── app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── formulario.html
│   │   ├── editar.html
│   │   ├── login.html
│   │   ├── registro.html
│   │   └── inicio.html
│   │
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
│
├── static/
│   └── style.css
    └─ img
│
├── instance/
│   └── finanzas.db
│
├── run.py
├── requirements.txt
└── README.md

⚙️ Instalación local
1️⃣ Clonar repositorio
    git clone https://github.com/farofede01/dashboard-finanzas.git
2️⃣ Entrar al proyecto
    cd dashboard-finanzas
3️⃣ Crear entorno virtual
    Windows
    python -m venv venv
    venv\Scripts\activate
    Linux / Mac
    python3 -m venv venv
    source venv/bin/activate
4️⃣ Instalar dependencias
    pip install -r requirements.txt
5️⃣ Ejecutar aplicación
    python run.py


🔐 Seguridad implementada
Contraseñas encriptadas
Protección de rutas privadas
Manejo seguro de sesiones
Validación de autenticación
Restricción de acceso a datos de otros usuarios


📈 Funcionalidades del Dashboard
📊 Visualización de datos
Balance total
Ingresos vs gastos
Gastos por categoría
Evolución mensual
🧾 Gestión de movimientos
Crear registros
Editar registros
Eliminar registros
Clasificación por categorías


🎯 Objetivo del proyecto

Este proyecto fue desarrollado para practicar:

Backend con Flask
Autenticación de usuarios
CRUD completo
Bases de datos con SQLAlchemy
Diseño responsive
Visualización de información financiera


👨‍💻 Autor
Federico Farola
GitHub: https://github.com/farofede01
⭐ Estado del proyecto

✅ Funcional
✅ Responsive
✅ Desplegado online
✅ Ideal para portfolio

📌 Próximas mejoras
Exportar reportes PDF
Dashboard avanzado
Filtros inteligentes
PostgreSQL
API REST
Docker
Tests automáticos