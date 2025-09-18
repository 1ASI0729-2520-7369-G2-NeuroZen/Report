# Capítulo IV: Product Design

---

## 4.1. Style Guidelines.  

---

### 4.1.1. General Style Guidelines.  

**Tipografía:**

- Fuente primaria: Inter (fallback system-ui, Roboto, Arial).
- Jerarquía:
  - Títulos (h1, h2, h3) → peso 600–700.
  - Texto general → peso 400–500.
  - Labels secundarios → peso 400, .text-muted-600.

**Paleta de colores:**

- Verde (principal): #10b981 (--brand-green).
- Índigo (secundario): #6366f1 (--brand-indigo).
- Texto: #0f172a (--ink).
- Texto secundario: #475569 (--muted).
- Fondos suaves: #f8fafc + degradados.

**!Poner imagen de paleta de colores aquí!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**

**Componentes:**
- Botones redondeados estilo pill (.btn-pill).
- Tarjetas con bordes y sombras (.card-popular).
- Íconos en burbujas (.icon-bubble).

**!Poner imagen de ejemplos de botones e íconos aquí!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**


### 4.1.2. Web Style Guidelines.  

**Diseño general:**

- Minimalista, con mucho aire (espacios).  
- Fondos con gradientes suaves (`.bg-soft`) y blobs decorativos.  
- Teléfono mockup (`.phone`) para mostrar pantallas de la app.  

**!Poner imagen de la landing page principal aquí (ejemplo con hero y mockup)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**

**Imágenes recomendadas:**

- Hero section: mockup de app dentro de un `.phone`.  
- Features: ilustraciones pequeñas o íconos representativos.  
- Pricing: tabla de precios con iconografía.  
- CTA final: ilustración relajante (ej. meditación / naturaleza).  

**!Poner imagen de cada sección (hero, features, pricing, CTA) aquí!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**

**Accesibilidad:**

- Contraste fuerte verde/blanco.  
- Texto alternativo en imágenes (`alt`).  
- Botones con `aria-label` en íconos.

---

## 4.2. Information Architecture.  

---

### 4.2.1. Organization Systems.  

En la plataforma, se emplean diferentes sistemas de organización del contenido para mejorar la accesibilidad y experiencia de los usuarios, dependiendo del tipo de información que se presenta. Estos sistemas aseguran que los usuarios puedan navegar de manera intuitiva y eficiente por la aplicación. A continuación, se detallan los enfoques utilizados:

---

**Organización Visual del Contenido**

- **Jerárquica (Visual Hierarchy):**  
  La organización jerárquica se aplica en secciones donde es fundamental mostrar una estructura clara de importancia y relevancia, como en el dashboard, los reportes de progreso y las recomendaciones personalizadas.  
  Se emplean tamaños de texto diferenciados, títulos destacados y un orden lógico de presentación, resaltando los elementos más importantes (como botones de acción o métricas clave) para guiar al usuario de forma natural.

- **Secuencial (Step-by-Step):**  
  En tareas que requieren pasos consecutivos, como la autoevaluación emocional o la configuración de un perfil, se utiliza un enfoque paso a paso. Esto asegura que el usuario complete cada acción antes de pasar a la siguiente, reduciendo la confusión y aumentando la claridad del proceso.

---

**Esquemas de Categorización de Contenido**

- **Por Audiencia (Grupos de Usuarios):**  
  La plataforma distingue entre dos perfiles de usuario principales:  
  - **Empleados:** acceden a funciones de autoevaluación, detección temprana, recomendaciones personalizadas y seguimiento de su progreso.  
  - **Psicólogos:** tienen acceso a herramientas de análisis, consultas y soporte a empleados desde la plataforma.  

- **Por Tópicos:**  
  La categorización por temas se aplica en las secciones de ayuda y soporte. Los usuarios pueden acceder a diferentes categorías como **Preguntas Frecuentes**, **Política de Privacidad** y **Centro de Ayuda**, lo que facilita encontrar información relevante para resolver problemas específicos.

---

**Implementación en la Interfaz**

La organización jerárquica y secuencial se refleja en el diseño de la interfaz mediante menús claros, tarjetas con íconos, pasos visibles en formularios y botones de acción destacados.  
Los esquemas de categorización por audiencia y por tópicos están integrados en las pantallas de inicio y soporte, donde los usuarios encuentran rápidamente la información más relevante.  

Este enfoque asegura que la experiencia de navegación sea **intuitiva, eficiente y adaptada a las necesidades de cada perfil de usuario**, mejorando la usabilidad y efectividad de la plataforma.

---

### 4.2.2. Labeling Systems.  

La plataforma emplea un sistema de etiquetado **directo, simple y orientado a la acción**, con el fin de facilitar la comprensión rápida de los contenidos y la navegación fluida para ambos tipos de usuarios (empleados y psicólogos).  
Se prioriza la **claridad** en la presentación textual de las secciones, utilizando el menor número de palabras posible y apoyándose en **íconos visuales** para reforzar los mensajes clave.

---

**Menú de navegación**  
En la barra superior se utilizan etiquetas claras y acompañadas de íconos:

- **Inicio** (icono de casa)  
- **Sobre nosotros** (icono de información)  
- **Servicios** (icono de herramientas)  
- **Cómo funciona** (icono de bombilla)  
- **Planes** (icono de moneda)  
- **Reseñas** (icono de comentarios)  
- **Contacto** (icono de sobre)

---

**Botón principal (CTA)**  
- **Registrarse** → llamada a la acción principal, válida tanto para empleados como para psicólogos.  

**!Poner imagen de botón CTA aquí!**

---

**Sección "Cómo funciona" para Empleados**  
- **Registrarse** (icono de usuario con +)  
- **Realizar autoevaluación** (icono de clipboard)  
- **Recibir recomendaciones** (icono de estrella o varita mágica)  
- **Hacer seguimiento de progreso** (icono de gráfico de líneas)  

**!Poner imagen de flujo empleados aquí!**

---

**Sección "Cómo funciona" para Psicólogos**  
- **Registrarse** (icono de usuario con +)  
- **Acceder a reportes** (icono de gráfico de barras)  
- **Conectar con pacientes** (icono de chat o persona)  
- **Dar seguimiento y ajustar terapias** (icono de calendario o check)  

**!Poner imagen de flujo psicólogos aquí!**

---

**Footer**  
En el pie de página se incluyen etiquetas claras y concisas:  

- Aviso legal  
- Política de privacidad  
- Política de cookies  
- Centro de ayuda  
- Contacto de soporte  

También se incorporan **íconos de redes sociales**: Facebook, Instagram, LinkedIn, Twitter.  

**!Poner imagen de footer aquí!**

---

### 4.2.3. SEO Tags and Meta Tags.  

Para la plataforma **SmartSay**, se definen etiquetas SEO y metaetiquetas con el fin de optimizar la visibilidad en buscadores y mejorar la experiencia de los usuarios en redes sociales y navegadores. A continuación, se detallan los ejemplos aplicados en la **Landing Page**:

#### Landing Page

<title>SmartSay - Bienestar emocional y apoyo psicológico en tu empresa</title>
<meta name="description" content="SmartSay conecta empleados y psicólogos en un espacio seguro para gestionar el bienestar emocional dentro de la empresa. Rápido, confidencial y accesible.">
<meta name="keywords" content="SmartSay, salud mental laboral, apoyo psicológico, bienestar emocional, estrés laboral, psicólogos online">
<meta name="author" content="Equipo SmartSay">

<!-- CSS & Icons -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" href="/images/logo.png" alt="Logo">



### 4.2.4. Searching Systems.  

- Buscador interno con **autocompletado**.  
- Filtros disponibles:  
  - Psicólogos (especialidad, disponibilidad, idioma).  
  - Rutinas (nivel de dificultad, duración, categoría).  
  - Ejercicios (tipo: respiración, meditación, mindfulness).  
- Resultados priorizados por **relevancia y popularidad**.  
- Barra de búsqueda visible en el **header** y en la sección de rutinas.  

**!Poner mockup de buscador con filtros aquí!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**

---

### 4.2.5. Navigation Systems.  

- **Navbar (superior):**  
  - Inicio  
  - Funcionalidades  
  - Rutinas  
  - Psicólogos  
  - Precios  
  - Soporte  

- **Footer:**  
  - Soporte  
  - FAQ  
  - Términos y condiciones  
  - Privacidad  
  - Contacto  

- **CTA constantes:**  
  - Botón **“Empieza ahora”** visible en:  
    - Hero section  
    - Pricing  
    - CTA final  

- **Versión móvil:**  
  - Menú hamburguesa lateral.  
  - Acceso rápido a CTA principal.  

**!Poner captura de navegación web y móvil aquí!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**

## 4.3. Landing Page UI Design.  

---

### 4.3.1. Landing Page Wireframe.  

---

### 4.3.2. Landing Page Mock-up.  

---

## 4.4. Web Applications UX/UI Design.  

---

### 4.4.1. Web Applications Wireframes.  

---

### 4.4.2. Web Applications Wireflow Diagrams.  

---

### 4.4.2. Web Applications Mock-ups.  

---

### 4.4.3. Web Applications User Flow Diagrams.  

---

## 4.5. Web Applications Prototyping.  

---

## 4.6. Domain-Driven Software Architecture.  

---

### 4.6.1. Software Architecture Context Diagram.  

---

### 4.6.2. Software Architecture Container Diagrams.  

---

### 4.6.3. Software Architecture Components Diagrams.  

---

## 4.7. Software Object-Oriented Design.  

---

### 4.7.1. Class Diagrams.  

---

### 4.7.2. Class Dictionary.  

---

## 4.8. Database Design.  

---

### 4.8.1. Database Diagram.  

---













