# Capítulo V: Product Implementation, Validation & Deployment

---

## 5.1. Software Configuration Management.  

A continuación, se describen los productos de software empleados en el desarrollo del proyecto **NeuroZen**. Esta sección tiene como objetivo facilitar la comprensión y continuidad del trabajo a los actuales y futuros desarrolladores, asegurando una colaboración efectiva a lo largo del ciclo de vida del producto digital.

#### Project Management

**Discord** – [https://discord.com/](https://discord.com/)  
Aunque originalmente su uso es más para la comunidad de gamers, Discord también se puede utilizar para mejorar la experiencia de trabajo en equipo a través de diferentes canales de comunicación, fijar mensajes y organizar actividades del grupo.

**WhatsApp** – [https://web.whatsapp.com/](https://web.whatsapp.com/)  
WhatsApp es una aplicación de mensajería instantánea que se utiliza para la comunicación en tiempo real. Aunque no es una herramienta de gestión de proyectos, se emplea para mantener contacto directo y rápido con los miembros del equipo.

**Trello** – [https://trello.com/](https://trello.com/)  
Se utilizó como herramienta de gestión de tareas. Permite visualizar el progreso del proyecto mediante tableros personalizables, organizando pendientes, tareas en desarrollo y finalizadas.


#### Requirements Management

**Google Docs** – [https://docs.google.com/](https://docs.google.com/)  
Empleada para la redacción, gestión y revisión de requisitos del sistema. Su funcionalidad colaborativa en tiempo real facilita el aporte y comentarios de todos los integrantes del equipo.


#### Product UX/UI Design

**Figma** – [https://www.figma.com/](https://www.figma.com/)  
Usado para el diseño de interfaces y la creación de prototipos interactivos (wireframes y mockups). Permite colaboración en tiempo real entre los equipos de diseño y desarrollo.

**UXPressia** – [https://uxpressia.com/](https://uxpressia.com/)  
Herramienta en línea para identificar y comprender problemas, necesidades y comportamientos del usuario. Fue utilizada para elaborar el *Empathy Map*, *Journey Map* e *Impact Map*.

**Miro** – [https://miro.com/es/](https://miro.com/es/)  
Plataforma colaborativa de pizarras digitales en tiempo real. Se utilizó en la creación del *As-Is* y *To-Be Scenario Map*.


#### Software Development

**Landing Page** – [https://www.jetbrains.com/](https://www.jetbrains.com/)
Desarrollada con tecnologías base del desarrollo web: **HTML5, CSS3, JavaScript**, junto con **React.js** y el framework **Tailwind CSS**, lo que permitió un desarrollo más ágil y modular.  
El entorno de desarrollo principal fue **IntelliJ IDEA Ultimate** por sus herramientas avanzadas de depuración y control de versiones.


#### Software Documentation

**GitHub** – [https://github.com/](https://github.com/)  
Plataforma de desarrollo colaborativo basada en Git. Se utilizó para alojar el código del proyecto, gestionar versiones y facilitar la colaboración entre desarrolladores.

**LucidChart** – [https://lucid.app/](https://lucid.app/)  
Herramienta de diagramación en línea usada para crear diagramas UML (como diagramas de clases), flujos y mapas mentales.

**Structurizr** – [https://www.structurizr.com/](https://www.structurizr.com/)  
Plataforma para modelado de diagramas de arquitectura de software mediante código. Se utilizó para construir los diagramas C4 del proyecto.

---

### 5.1.2. Source Code Management.  

El equipo utiliza Git y GitHub para el control de versiones y colaboración:

**Repositorios:**

**Link del repositorio del informe:**  
[https://github.com/1ASI0729-2520-7369-G2-NeuroZen/Report/tree/main](https://github.com/1ASI0729-2520-7369-G2-NeuroZen/Report/tree/main)

**Link de los repositorios de la organización:**  
[https://github.com/orgs/1ASI0729-2520-7369-G2-NeuroZen/repositories](https://github.com/orgs/1ASI0729-2520-7369-G2-NeuroZen/repositories)

#### Modelo de Ramas

Se sigue un modelo basado en **GitFlow simplificado**:

- `main` → rama principal, contiene versiones estables y listas para producción  
- `develop` → rama de desarrollo activo  
- `feature/{nombre-funcionalidad}` → ramas específicas para nuevas funcionalidades  
  - Ejemplo: `feature/chapter-1`, `feature/user-authentication`  

#### Convenciones de Versionado y Commits

- **Versionado semántico:** `MAJOR.MINOR.PATCH` (ejemplo: `1.0.0`)  
- **Mensajes de commit** siguen el estándar **Conventional Commits**:  
  - `feat:` agregar nueva funcionalidad  
  - `fix:` corrección de bug  
  - `docs:` cambios en documentación  
  - `style:` cambios de estilo sin afectar la funcionalidad  
  - `refactor:` mejoras internas sin cambios funcionales  
  - `test:` añadir pruebas  

---

### 5.1.3. Source Code Style Guide & Conventions.  

En el proyecto NeuroZen, hemos seguido una guía de estilos para mantener el código organizado, legible y fácil de mantener:

**React (Frontend)**

- Componentes funcionales: se prioriza el uso de functional components en lugar de clases.
- Nomenclatura en PascalCase para componentes.
  Ejemplo: Navbar, StressForm.
- Props y State: se usan para el manejo de datos dinámicos y comunicación entre componentes.
- Estructura modular: cada componente dentro de su propia carpeta cuando es complejo (ej. /components/StressForm/).
- JSX limpio: máximo de responsabilidad por componente (Single Responsibility Principle).

**Tailwind CSS**

- Uso de clases utilitarias para aplicar estilos de manera rápida y consistente.
- Nombres descriptivos en clases personalizadas si son necesarias.
  Ejemplo: .hero-section, .btn-submit.
- Evitar estilos inline excepto en casos específicos.

**JavaScript**

- Variables y funciones en camelCase.
  Ejemplo: handleSubmit, userEmail.
- Constantes en UPPER_CASE.
  Ejemplo: API_URL.
- Uso de ESLint + Prettier para mantener un formato uniforme.
- Modularización del código para evitar funciones largas o anidadas innecesariamente.

**HTML**

- Etiquetas correctamente cerradas.
  Ejemplo: <p>Welcome to NeuroZen</p>.
- Uso exclusivo de minúsculas en etiquetas y atributos.
- Valores de atributos siempre entre comillas dobles.
- Todas las imágenes con alt obligatorio.

**Git**

- Ramas organizadas bajo el modelo GitFlow:
  - main → versión estable en producción.
  - develop → versión de desarrollo.
  - feature/{nombre} → nuevas funcionalidades.

- Commits siguiendo Conventional Commits:
  - feat: add stress form component
  - fix: correct navbar responsive issue
  - docs: update README.

---

### 5.1.4. Software Deployment Configuration

El despliegue de **NeuroZen** se configuró de la siguiente manera:


#### Landing Page (React + Tailwind)

- **Plataforma:** Vercel  
- **Repositorio GitHub:** conectado directamente a Vercel  
- **Proceso:** despliegue automático al realizar *push* en la rama `main`  


#### Web Application (React + Node.js/FastAPI)

- **Frontend Web (React):** desplegado en Vercel, con soporte de rutas dinámicas mediante `vercel.json`  
- **Backend API (Node.js/FastAPI):** desplegado en Railway, empaquetado con `Dockerfile`  
- **CI/CD:** Railway ejecuta el despliegue automático al detectar cambios en la rama `main`  


#### Repositorios

- Todo el código se encuentra en **GitHub**, bajo la organización del equipo de **NeuroZen**.  
- El flujo de trabajo colaborativo se gestiona mediante **ramas y pull requests** siguiendo un modelo de desarrollo ágil.  


## 5.2. Landing Page, Services & Applications Implementation.  

---

### 5.2.1. Sprint 1  

---

### 5.2.1.1. Sprint Planning 1.  

---

### 5.2.1.2. Aspect Leaders and Collaborators.  

---

### 5.2.1.3. Sprint Backlog 1.  

---

### 5.2.1.4. Development Evidence for Sprint Review.  

---

### 5.2.1.5. Execution Evidence for Sprint Review.  

---

### 5.2.1.6. Services Documentation Evidence for Sprint Review.  

---

### 5.2.1.7. Software Deployment Evidence for Sprint Review.  

---

### 5.2.1.8. Team Collaboration Insights during Sprint.  

---








