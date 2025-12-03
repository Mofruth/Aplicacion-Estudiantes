# Campus - Sistema de Gestión Estudiantil

## Descripción

Campus es una aplicación web para la gestión de estudiantes, profesores, materias, calificaciones y horarios en una institución educativa.

## Requisitos

- Python 3.8+
- MySQL 5.7+
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Elvis094/EbookStudy.git
cd Campus
```

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

#### Opción A: Usar MySQL

1. Abre MySQL en tu equipo y crea la base de datos:

```sql
mysql -u root -p < Database/GestionEstduiante.sql
```

2. (Opcional) Cargar datos iniciales para pruebas:

```sql
mysql -u root -p GestionDeEstudiantes < Database/datos_iniciales.sql
```

#### Configurar credenciales de conexión

Edita `Config/database_connection.py`:

```python
connection = mysql.connector.connect(
    host='localhost',
    user='root',  # Tu usuario MySQL
    password='',  # Tu contraseña MySQL
    database='GestionDeEstudiantes'
)
```

### 5. Configurar credenciales de email (opcional)

Edita `config_email.py` si deseas usar la funcionalidad de envío de correos:

```python
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "tu_correo@gmail.com"
EMAIL_HOST_PASSWORD = "tu_contraseña_o_token"
```

## Estructura del Proyecto

```
Campus/
├── Config/                      # Configuraciones
│   ├── database_connection.py   # Conexión a BD
│   └── config.py               # Configuración general
├── Controllers/                 # Controladores
│   ├── admin_controller.py
│   ├── profesor_controller.py
│   ├── estudiante_controller.py
│   ├── horario_controller.py
│   └── autenticacion.py
├── Models/                      # Modelos
│   ├── estudiante.py
│   ├── profesor.py
│   ├── nota.py
│   ├── horario.py
│   ├── materia.py
│   └── ...
├── Views/                       # Templates HTML
│   ├── auth/                    # Autenticación
│   ├── admin/                   # Panel administrador
│   ├── profesor/                # Panel profesor
│   ├── estudiante/              # Panel estudiante
│   ├── padre/                   # Panel padre
│   └── error/                   # Páginas de error
├── Static/                      # CSS, JS, imágenes
├── Utils/                       # Utilidades y helpers
├── Database/                    # Scripts SQL
├── main.py                      # Aplicación principal
├── requirements.txt             # Dependencias
└── README.md                    # Este archivo
```

## Uso

### Ejecutar la aplicación

```bash
python main.py
```

La aplicación estará disponible en `http://localhost:5000`

### Roles y acceso

#### Administrador
- Usuario: `admin@example.com`
- Contraseña: (según datos iniciales)
- Acceso: Gestión de usuarios, materias, horarios e inscripciones

#### Profesor
- Usuario: `carlos@example.com`
- Contraseña: (según datos iniciales)
- Acceso: Asignar notas, crear notificaciones, ver estudiantes

#### Estudiante
- Usuario: `juan.delgado@example.com`
- Contraseña: (según datos iniciales)
- Acceso: Ver calificaciones, horarios, tareas y notificaciones

#### Padre
- Usuario: `padre.delgado@example.com`
- Contraseña: (según datos iniciales)
- Acceso: Ver información de sus hijos

## Funcionalidades principales

### Dashboard Estudiante
- Número de tareas pendientes
- Asistencia
- Materias inscritas
- Promedio general
- Rendimiento por materia
- Últimas notificaciones

### Dashboard Profesor
- Cantidad de estudiantes por materia
- Promedio de notas
- Asignar calificaciones
- Enviar notificaciones

### Dashboard Administrador
- Gestión de usuarios
- Gestión de materias
- Gestión de horarios
- Gestión de inscripciones

## API y Rutas principales

### Autenticación
- `GET/POST /` - Home
- `GET/POST /login` - Iniciar sesión
- `GET/POST /register` - Registrarse
- `GET /logout` - Cerrar sesión

### Estudiante
- `GET /estudiante/dashboard` - Dashboard
- `GET /estudiante/ver_notas` - Ver calificaciones
- `GET /estudiante/ver_clases` - Ver horario
- `GET /estudiante/horario` - Horario del estudiante

### Profesor
- `GET /profesor/dashboard` - Dashboard
- `GET/POST /profesor/asignar_nota` - Asignar calificaciones
- `GET/POST /profesor/cambiar_nota` - Modificar calificaciones
- `GET/POST /profesor/enviar_notificacion` - Enviar notificaciones

### Administrador
- `GET /admin/dashboard` - Dashboard
- `GET /admin/usuarios` - Gestión de usuarios
- `GET/POST /admin/materias` - Gestión de materias
- `GET/POST /admin/horarios` - Gestión de horarios
- `GET/POST /admin/inscripciones` - Gestión de inscripciones

## Notas importantes

1. **Seguridad**: Las contraseñas se almacenan con hash usando Werkzeug.
2. **Sesiones**: Las sesiones expiran después de 24 horas.
3. **Email**: Requiere credenciales válidas de Gmail o SMTP compatible.
4. **Base de datos**: Se usa MySQL con conexión directa (considera usar ORM en futuras versiones).

## Solución de problemas

### Error de conexión a la base de datos
- Verifica que MySQL esté ejecutándose
- Verifica las credenciales en `Config/database_connection.py`
- Verifica que la base de datos `GestionDeEstudiantes` exista

### Error de módulos no encontrados
- Ejecuta `pip install -r requirements.txt` nuevamente
- Verifica que estés en el entorno virtual correcto

### Error de sesión expirada
- Inicia sesión nuevamente
- Verifica que cookies estén habilitadas

## Contribuidores

- Elvis094
- Litber33

## Licencia

Este proyecto es propiedad de la institución educativa y se desarrolló como parte de un proyecto integrador.

## Contacto

Para reportar bugs o sugerencias, contacta a Elvis094, Litber33 en GitHub.
