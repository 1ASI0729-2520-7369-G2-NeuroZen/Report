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


### 5.2.1. Sprint 1  

### 5.2.1.1. Sprint Planning 1.  

A continuación, se presenta el Sprint Planning 1, en el que se documentan las evidencias de la planificación y la implementación de la Landing Page. Asimismo, se muestran los avances del proyecto y los aprendizajes obtenidos del trabajo colaborativo del equipo mediante GitHub.

| Campo                                  | Descripción                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sprint #**                           | Sprint 1                                                                                                                                                                                                                                                                                                                                      |
| **Sprint Planning Background**         |                                                                                                                                                                                                                                                                                                                                               |
| **Date**                               | 2025-08-16                                                                                                                                                                                                                                                                                                                                    |
| **Time**                               | 06:00 PM (GMT -5)                                                                                                                                                                                                                                                                                                                             |
| **Location**                           | Modalidad remota por Discord                                                                                                                                                                                                                                                                                                                  |
| **Prepared By**                        | Equipo NeuroZen                                                                                                                                                                                                                                                                                                                               |
| **Attendees (to planning meeting)**    | Fernández Garfias Alexander / Montes Ramos Henry / Nawrocki Loureiro Ian / Vila Guillen Miguel / Requena Gutiérrez Diego                                                                                                                                                                                                                      |
| **Sprint n – 1 Review Summary**        | Este es el primer sprint, por lo tanto, no hay una revisión de sprint anterior.                                                                                                                                                                                                                                                               |
| **Sprint n – 1 Retrospective Summary** | En esta primera etapa del proyecto se identificó la necesidad de reforzar conocimientos técnicos, especialmente en el uso de frameworks CSS. Además, se revisó el diseño del Landing Page en Figma, se discutió el contenido textual a incluir y se definió como objetivo central desplegar la página en GitHub Pages al finalizar el sprint. |
| **Sprint Goal & User Stories**         |                                                                                                                                                                                                                                                                                                                                               |
| **Sprint n Goal**                      | Publicar un Landing Page funcional, con diseño responsive y estructura clara, accesible desde GitHub Pages.                                                                                                                                                                                                                                   |
| **Sprint n Velocity**                  | 2                                                                                                                                                                                                                                                                                                                                             |
| **Sum of Story Points**                | 2                                                                                                                                                                                                                                                                                                                                             |


### 5.2.1.2. Aspect Leaders and Collaborators.  

En la primera iteración (Sprint 1), el equipo se enfocó en la **implementación de la Landing Page**, relacionada con el Epic **EP08 – Exploración como Visitante**.  

#### Historias de Usuario Abordadas

| ID   | Título                                               | Descripción                                                                                                                          | Estimación (Horas) | Asignado a | Estado |
|------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------|------------|--------|
| US25 | Explorar funcionalidades de la app sin registro       | Como visitante, quiero explorar las funcionalidades principales sin crear cuenta, para conocer el valor de la aplicación.            | 6                  | Equipo     | Done   |
| US26 | Visualizar landing page con beneficios y testimonios  | Como visitante, quiero ver información de beneficios y testimonios en la landing page, para entender la utilidad del producto.       | 7                  | Equipo     | Done   |
| US27 | Visualizar información general desde la landing page  | Como visitante, quiero visualizar información general del producto en la landing page, para obtener una visión clara de lo que ofrece NeuroZen. | 5                  | Equipo     | Done   |


**Evidencia en del avance en trello**

![sprint_trello](imgs/sprint_trello.png)

Este Sprint permitió entregar la **Landing Page inicial de NeuroZen**, proporcionando a los visitantes un primer acercamiento a las **funcionalidades**, **beneficios**, **testimonios** y **información general** de la aplicación.


### 5.2.1.3. Sprint Backlog 1.  

A continuación, se listan los commits que evidencian el desarrollo de la **Landing Page** en este primer sprint.  

#### Commits de Desarrollo (Landing Page)

| Autor | Fecha | Commit Message | Commit ID |
|-------|-------|----------------|-----------|
| Nawrocki Loureiro Ian Andre | 13/09/2025 | feat: add css styles for landing page | d0a47dd |
| Nawrocki Loureiro Ian Andre | 13/09/2025 | feat: add html content for landing page | 0298a7b |
| Nawrocki Loureiro Ian Andre | 13/09/2025 | chore: init | 3ac4653 |

**Evidencia de los commits del landing page**

![commitslanding](imgs/commitslanding.png)


#### Commits de Documentación y Diseño

| Autor | Fecha | Commit Message | Commit ID |
|-------|-------|----------------|-----------|
| Fernandez Alexander Piero | 18/09/2025 | doc: add product backlog and impact mapping | 3f86c79 |
| Fernandez Alexander Piero | 17/09/2025 | doc: project reorganization | 133fb36 |
| Fernandez Alexander Piero | 17/09/2025 | doc: project reorganization | 53f8602 |
| Fernandez Alexander Piero | 17/09/2025 | doc: project reorganization | 620c459 |
| Fernandez Alexander Piero | 16/09/2025 | doc: format organization order | 01a620b |
| Fernandez Alexander Piero | 16/09/2025 | doc: project reorganization | a829adf |
| Fernandez Alexander Piero | 16/09/2025 | doc: organizing code order | 80a51ef |
| Fernandez Alexander Piero | 16/09/2025 | doc: organizing code order | fa53549 |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add target segments | 4b042b3 |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add lean ux canvas | db88fe9 |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add lean ux hypothesis statements | 4337aa6 |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add lean ux assumptions | 55bac85 |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add lean ux problem statements | 6fcde3f |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add lean ux process | 8684444 |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add background and problems | ed3150a |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add solution profile | 12a64d5 |
| Vila Guillén Miguel Ángel | 17/09/2025 | doc: add startup description | bbe4ea8 |
| Vila Guillén Miguel Ángel | 13/09/2025 | doc: add database design | 1590ef7 |
| Vila Guillén Miguel Ángel | 13/09/2025 | doc: add class diagram design | 8d7ce41 |
| Vila Guillén Miguel Ángel | 10/09/2025 | doc: add competitive analysis | 4f6126e |
| Vila Guillén Miguel Ángel | 10/09/2025 | doc: add strategies and tactics against competitors | 2a94a93 |
| Requena Gutiérrez Diego Gabriel | 17/09/2025 | doc: add product backlog | 89cba69 |
| Requena Gutiérrez Diego Gabriel | 17/09/2025 | doc: add impact mapping | 33767c7 |
| Requena Gutiérrez Diego Gabriel | 17/09/2025 | doc: add user stories | 0b8833e |
| Requena Gutiérrez Diego Gabriel | 17/09/2025 | doc: add to-be scenario mapping | 133fb36 |

**Evidencia de los commits del report**

![commits1](imgs/commits1.png)

![commits2](imgs/commits2.png)

### 5.2.1.4. Development Evidence for Sprint Review.  

En este primer sprint, el alcance se limitó al desarrollo de la **Landing Page**.  
Las evidencias de pruebas realizadas incluyen:

- **Pruebas funcionales manuales**  
  - Verificación de la correcta visualización de la página en navegadores Chrome, Firefox y Edge.  
  - Validación de la navegación entre secciones de la landing.  
  - Comprobación de carga de estilos CSS.  

- **Pruebas de despliegue en Vercel**  
  - Confirmación de despliegue automático con integración GitHub → Vercel.  
  - Validación de rutas accesibles desde la URL del proyecto.  

- **Resultados:**  
  - Todas las pruebas ejecutadas en este sprint fueron satisfactorias.  
  - No se reportaron errores críticos. 

### 5.2.1.5. Execution Evidence for Sprint Review.  

Después de finalizar el Sprint 1, hemos logrado implementar algunas de las secciones de nuestra Landing Page, aunque con algunos desperfectos en cuanto a diseño.

![wireframe1](imgs/wireframe1.png)

**Link del repositorio del informe:**  

[https://github.com/1ASI0729-2520-7369-G2-NeuroZen/landing-page]([https://github.com/1ASI0729-2520-7369-G2-NeuroZen/Report/tree/main](https://github.com/1ASI0729-2520-7369-G2-NeuroZen/landing-page))


### 5.2.1.6. Services Documentation Evidence for Sprint Review.  

Durante este Sprint 1, la documentación de servicios estuvo enfocada en dejar claros los lineamientos técnicos y funcionales de la **Landing Page**.  
Se registraron los siguientes entregables:

- **Arquitectura inicial de la aplicación**: descripción general de los componentes y su interacción.  
- **Diagramas de diseño**: modelo de base de datos y diagrama de clases preliminar para planificar futuras integraciones.  
- **Historias de usuario documentadas**: backlog inicial con priorización de funcionalidades relacionadas a la exploración como visitante (Epic 08).  
- **Documentación técnica en GitHub**: se mantuvo centralizada en el repositorio, facilitando el acceso a todos los miembros del equipo.  

Esta documentación asegura que los servicios y funcionalidades planificadas puedan evolucionar de forma ordenada en próximos sprints.

### 5.2.1.7. Software Deployment Evidence for Sprint Review.  

Para este Sprint, el despliegue de la **Landing Page** se realizó utilizando herramientas de control de versiones y hosting en la nube:  

- **Git**: para el control de versiones del código fuente.  
- **GitHub**: para almacenar el repositorio de la landing page, centralizando el trabajo colaborativo.  


### 5.2.1.8. Team Collaboration Insights during Sprint.  

La colaboración del equipo en Sprint 1 se centró en la **organización y versionado en GitHub**, asegurando un trabajo paralelo eficiente:  

- Un integrante configuró el repositorio inicial, estableciendo la estructura base del proyecto.  
- Se generaron ramas individuales por tarea, lo que permitió avanzar sin generar conflictos en el código.  
- Los miembros del equipo clonaron el repositorio localmente, realizaron las modificaciones necesarias y subieron los cambios mediante **pull requests**.  
- El historial de commits en GitHub refleja las contribuciones de cada miembro, sirviendo como evidencia del esfuerzo conjunto.  
- Las decisiones técnicas y ajustes se comunicaron mediante reuniones cortas (stand-ups) y registros en el repositorio.  

Esta metodología de colaboración permitió mantener una buena coordinación, acelerar la entrega de la landing page y sentar bases sólidas para futuros sprints.










