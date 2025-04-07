# Demo: Chat + PostgreSQL + Flask Endpoint

Este repositorio contiene un demo simple de una API REST construida con **Flask**, que interactúa con una base de datos **PostgreSQL** para simular funcionalidades básicas de un sistema de chat.

## 🚀 Tecnologías usadas

- 🐍 Python (Flask)
- 🐘 PostgreSQL
- 🛆 SQLAlchemy
- 📡 API REST (GET, POST)
- 🧪 Postman (para pruebas de endpoints)

## 📁 Estructura del proyecto

```
.
├── app.py                # Archivo principal con endpoints Flask
├── config.py             # Configuración de conexión a PostgreSQL
├── models.py             # Definición de modelos con SQLAlchemy
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto
```

## 📌 Funcionalidades

- **GET /messages** → Retorna todos los mensajes almacenados en la base de datos.
- **POST /messages** → Permite enviar un nuevo mensaje (usuario + contenido).
- Conexión segura a base de datos con variables de entorno.

## 🔧 Cómo ejecutar localmente

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/danielabsola/demo_chat_postgres_flask_endpoint.git
   cd demo_chat_postgres_flask_endpoint
   ```

2. Instalá las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurá tu conexión a PostgreSQL en un archivo `.env` o dentro de `config.py`:
   ```
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=chatdb
   DB_USER=usuario
   DB_PASSWORD=contraseña
   ```

4. Ejecutá la aplicación:
   ```bash
   python app.py
   ```

5. Probá los endpoints con Postman, Insomnia o `curl`.

## 🧠 Aprendizajes y propósito

Este proyecto fue creado como práctica para conectar una API básica con una base de datos relacional y entender mejor cómo funcionan los endpoints REST, el manejo de formularios en Flask y la persistencia de datos.

## 😇 Autora

**Daniela Sola**  
[Gmail] (dbshoy@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/daniela-beatriz-sola-587b902b)  
[GitHub](https://github.com/danielabsola)
[Malt](https://www.malt.es/profile/danielabeatrizsola)

---

> Si este proyecto te resulta útil o interesante, ¡no olvides dejar una ⭐️!
v
