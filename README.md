
# Proyecto de Gestión de Gastos 💰

Este proyecto es una **aplicación web** desarrollada con **Django** que permite gestionar y filtrar **gastos de empleados** por **departamento**, proporcionando una vista clara y detallada de los **gastos por rango de fechas**. La aplicación incluye funcionalidades como el **registro de gastos**, **visualización de resultados** y **filtrado avanzado**.

## 📝 Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado:

- **Python 3.8** o superior 🐍
- **pip** (gestor de paquetes de Python) 📦
- **PostgreSQL** (opcional, se usa SQLite por defecto) 🗄️

## ⚙️ Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clonar el repositorio

Clona el repositorio usando el siguiente comando:

```bash
git clone <https://github.com/Lets21/GastosMiniCore.git>
cd <https://github.com/Lets21/GastosMiniCore.git>
```

### 2. Crear un entorno virtual (opcional, pero recomendado)

Es recomendable crear un entorno virtual para gestionar las dependencias:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

### 3. Instalar las dependencias

Instala las dependencias listadas en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configuración de la base de datos

Si decides usar **PostgreSQL** en lugar de SQLite, realiza las siguientes modificaciones:

- Asegúrate de tener una **base de datos** creada en PostgreSQL.
- Actualiza las configuraciones de la base de datos en `mincore/settings.py` para reflejar la conexión a PostgreSQL.

Si no deseas utilizar **PostgreSQL**, la base de datos **SQLite** se configura por defecto.

### 5. Aplicar migraciones

Aplica las migraciones necesarias para crear las tablas en la base de datos:

```bash
python manage.py migrate
```

### 6. Cargar datos iniciales (opcional)

Si deseas cargar datos iniciales, ejecuta el siguiente comando:

```bash
python manage.py loaddata initial_data.json
```

### 7. Recopilar archivos estáticos

Recopila los archivos estáticos para servirlos correctamente en el entorno de producción:

```bash
python manage.py collectstatic --no-input
```

## 🚀 Ejecución

Para ejecutar el servidor de desarrollo local, utiliza el siguiente comando:

```bash
python manage.py runserver
```

Luego, abre tu navegador y accede a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento. 🌐

## 📁 Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:

- **`gestion/`**: Contiene la aplicación principal con los modelos, vistas, formularios y plantillas.
- **`mincore/`**: Contiene la configuración general del proyecto Django, incluidas las configuraciones de base de datos, seguridad y middleware.
- **`requirements.txt`**: Lista las dependencias del proyecto necesarias para ejecutar la aplicación.
- **`manage.py`**: Herramienta de línea de comandos para interactuar con el proyecto Django, como ejecutar migraciones, iniciar el servidor, entre otros.

## 🔧 Funcionalidades

Este proyecto incluye las siguientes funcionalidades principales:

- **Filtrar gastos** por rango de fechas (inicio y fin).
- **Visualizar resultados** detallados de los gastos desglosados por empleado y departamento.
- **Interfaz de usuario amigable**, con un diseño limpio y eficiente utilizando **CSS** 🎨.
- **Registro de gastos**, permitiendo a los usuarios agregar nuevos gastos y asignarlos a departamentos específicos 📝.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un **fork** del repositorio 🍴.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`) 🌱.
3. Realiza tus cambios y haz **commit** (`git commit -m "Añadir nueva funcionalidad"`) 💻.
4. Envía un **pull request** describiendo los cambios realizados.

## 📝 Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles 📜.

## Contactos:
leonardo.tamayo@udla.edu.ec
leito.t210403@gmail.com
