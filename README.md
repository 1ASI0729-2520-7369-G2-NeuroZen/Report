<div align="center">
  <img src="imgs/logo.jpg" alt="Logo UPC" />
  
  <h2>Universidad: Universidad Peruana de Ciencias Aplicadas</h2>
  <p><strong>Carrera:</strong> Ingeniería de Software</p>
  <p><strong>Ciclo:</strong> 2025-2</p>

  <p><strong>Código del Curso : </strong> 1ASI0729</p>
  <p><strong>Nombre del Curso : </strong>  Desarrollo de Aplicaciones Open Source</p>
  <p><strong>Sección:</strong> 7369</p>

  <p><strong>Profesor:</strong> Wilder Julio Espinoza Bravo</p>

  <h3>Informe de Trabajo Final</h3>

  <p><strong>Startup:</strong> NeuroZen</p>
  <p><strong>Nombre del Producto:</strong> NeuroZen/p>
</div>

<h3 align="center">Relación de Integrantes:</h3>

<div align="center">
  <table>
    <tr>
      <th><strong>Código</strong></th>
      <th><strong>Apellidos y Nombres</strong></th>
    </tr>
    <tr>
      <td>U20231G054</td>
      <td>Fernandez Garfias Alexander Piero</td>
    </tr>
    <tr>
      <td>U20231B475</td>
      <td>Montes Ramos Henry Jaredt</td>
    </tr>
    <tr>
      <td>U20231G159</td>
      <td>Nawrocki Loureiro Ian Andre</td>
    </tr>
    <tr>
      <td>U20231G054</td>
      <td>Vila Guillen Miguel Angel</td>
    </tr>
    <tr>
      <td>U202321774</td>
      <td>Requena Gutiérrez, Diego Gabriel</td>
    </tr>
  </table>  
</div>


## Registro de Versiones del Informe

| **Versión** | **Fecha**   | **Autores**                                                                                     | **Descripción de Modificación**                                                                                                                                                                  |
|-------------|-------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | 09/09/2025  | - Fernandez Garfias Alexander Piero  <br> - Montes Ramos Henry Jaredt  <br> - Nawrocki Loureiro Ian Andre <br> - Vila Guillen Miguel Angel <br> - Requena Gutiérrez, Diego Gabriel | Se incluyeron los siguientes capítulos: <br>• Estructura del informe <br>• Capítulo I: Introducción <br>• Capítulo II: Requirements Elicitation & Analysis <br>• Capítulo III: Requirements Specification <br>• Capítulo IV: Product Design <br>• Capítulo V: Product Implementation, Validation & Deployment <br>• Landing Page |

---
## Project Report Collaboration Insights

**Link del repositorio del informe:**  
[https://github.com/1ASI0729-2520-7369-G2-NeuroZen/Report/tree/main](https://github.com/1ASI0729-2520-7369-G2-NeuroZen/Report/tree/main)

**Link de los repositorios de la organización:**  
[https://github.com/orgs/1ASI0729-2520-7369-G2-NeuroZen/repositories](https://github.com/orgs/1ASI0729-2520-7369-G2-NeuroZen/repositories)

El desarrollo de este informe se llevó a cabo de manera colaborativa a través de la plataforma GitHub, empleando la metodología GitFlow y la estandarización de Conventional Commits. La participación de cada integrante del equipo se materializó mediante la creación de ramas independientes, la realización de aportes individuales y la validación conjunta a través de revisiones de Pull Requests

---


## Contenido

- [Carátula](#carátula)
- [Registro de Versiones del Informe](#registro-de-versiones-del-informe)
- [Project Report Collaboration Insights](#project-report-collaboration-insights)
- [Contenido](#contenido)
- [Student Outcome](#student-outcome)
- [Capítulo I: Introducción](#capítulo-i-introducción)
  - [1.1 Startup Profile](#11-startup-profile)
    - [1.1.1 Descripción de la Startup](#111-descripción-de-la-startup)
    - [1.1.2 Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
  - [1.2 Solution Profile](#12-solution-profile)
    - [1.2.1 Antecedentes y problemática](#121-antecedentes-y-problemática)
    - [1.2.2 Lean UX Process](#122-lean-ux-process)
      - [1.2.2.1 Lean UX Problem Statements](#1221-lean-ux-problem-statements)
      - [1.2.2.2 Lean UX Assumptions](#1222-lean-ux-assumptions)
      - [1.2.2.3 Lean UX Hypothesis Statements](#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4 Lean UX Canvas](#1224-lean-ux-canvas)
  - [1.3 Segmentos objetivo](#13-segmentos-objetivo)

---

## Student Outcome

<img src="imgs/criterio_específico.png" alt="Student Outcome" /></p>

---

# Capítulo I: Introducción

## 1.1 Startup Profile

### 1.1.1 Descripción de la Startup
Nuestra startup llamada NeuroZen está enfocado en una rápida detección del estrés en el ámbito laboral de personas entre 20 a 50 años de edad. Abarcando temas como salud mental, presión laboral y servicios, el software facilita el tratamiento del estrés laboral.
Los usuarios pueden realizar un test que recabará información de salud, comportamiento, actitudes y patrones en la persona. La plataforma permite el contacto con un psicólogo. Además, fomenta diversas actividades para complementar el tratamiento contra el estrés.

Entre sus principales características destacan:

- Registro automático de huéspedes mediante sistemas digitales.
- Identificación de habitaciones ocupadas, libres o en mantenimiento.
- Monitoreo de temperatura, iluminación y consumo energético.
- Integración con dispositivos IoT para controlar persianas, temperatura del agua y otros aspectos del confort del huésped.
- Personalización de servicios, como programación de limpieza, room service o entrega de comidas en horarios flexibles.

---
### 1.1.2 Perfiles de integrantes del equipo
| Foto                                          | Nombre completo | Código     | Carrera                | Habilidades técnicas y rol                  |
|-----------------------------------------------|-----------------|------------|------------------------|---------------------------------------------|
| ![Alexander](imgs/foto_alexander.jpg) | Fernandez Garfias Alexander Piero | U20231B475 | Ingeniería de Software | Conocimientos en Java, Flutter, Node.js, HTML, C++, TypeScript |
| ![Henry](imgs/foto_henry.jpg) | Montes Ramos Henry Jaredt | U20231G159 | Ingeniería de Software | Manejo de Java, Node.js, HTML, C++, TypeScript |
| ![Ian](imgs/foto_ian.jpg) | Nawrocki Loureiro Ian Andre | U20231G054 | Ingeniería de Software | Enfoque en desarrollo Fullstack y Backend, además de experiencia en Java, Node.js, HTML, C++, TypeScript |
| ![Miguel](imgs/foto_miguel.jpg) | Vila Guillen Miguel Angel | U202321774 | Ingeniería de Software | Conocimientos en Java, Node.js, HTML, C++, TypeScript |
| ![Diego](imgs/foto_diego.jpg) | Requena Gutiérrez Diego Gabriel | U202321774 | Ingeniería de Software | Manejo de Java, Node.js, HTML, C++, TypeScript |

---

## 1.2 Solution Profile

Esta sección incluye dos secciones internas. La primera parte, Antecedentes y Problemática, consta del enunciado de problema, y una descripción de los puntos más importante que debe resolver la solución propuesta, así como objetivos y restricciones que delimitan el alcance del proyecto. La segunda parte, Lean UX Process, es resultado de la ejecución del Lean UX Process sobre el dominio del problema.

### 1.2.1 Antecedentes y problemática

El proyecto Neuro Zen consiste en desarrollar un sistema de identificación y gestión del estrés laboral dirigido específicamente a adultos entre 20 y 50 años, mediante la observación y registro de señales corporales visibles como postura corporal, tensión muscular facial, cambios en la respiración, sudoración visible, temblores, rojeces en la piel y otros indicadores físicos detectables a simple vista, integrando estos datos en una aplicación que permita a los usuarios autoevaluar sus niveles de estrés en el entorno laboral, recibir recomendaciones personalizadas y estrategias prácticas para la gestión del estrés, mejorando así el bienestar de los trabajadores y la productividad organizacional, mientras se previenen problemas de salud asociados al estrés crónico en la población económicamente activa.

**5 Ws y 2 Hs**

**What / Qué**
**¿Cuál es el problema?**
El problema es el estrés laboral que afecta negativamente la salud física y mental de los trabajadores adultos, reduciendo su productividad, aumentando el ausentismo y deteriorando su calidad de vida.

**¿Cuál es la relación con la persona en cuestión?**
La relación es directa, ya que el sistema ayudará a los usuarios a identificar sus propios niveles de estrés mediante señales corporales observables o técnicas de respiración, permitiéndoles tomar medidas preventivas y correctivas oportunas.

---

**When / Cuándo**
**¿Cuándo sucede el problema?**
El problema del estrés laboral sucede principalmente durante la jornada laboral, en momentos de alta presión, plazos ajustados, conflictos interpersonales, sobrecarga de trabajo o cuando existe un desequilibrio entre las exigencias y los recursos disponibles.

**¿Cuándo utiliza el cliente el producto?**
El cliente utilizará la aplicación tanto durante su jornada laboral para detectar señales tempranas de estrés, como en momentos específicos de autoevaluación programados durante el día o cuando sienta síntomas de tensión.

---

**Where / Dónde**
**¿Dónde está el cliente cuando usa el producto?**
El cliente estará principalmente en su entorno laboral: oficina, teletrabajo desde casa, o cualquier espacio donde desarrolle su actividad profesional.

**¿A dónde se dirige?**
Se dirige hacia un mejor estado de autoconocimiento y manejo del estrés, buscando mejorar su bienestar laboral y calidad de vida.

**¿Dónde surge el problema?**
El problema surge en el entorno laboral, donde factores como la carga de trabajo, las relaciones interpersonales, el clima organizacional o las condiciones físicas generan situaciones de estrés.

---

**Who / Quién**
**¿Quiénes están involucrados?**
Están involucrados principalmente los trabajadores adultos de 20 a 50 años, así como las empresas u organizaciones interesadas en mejorar la salud ocupacional de sus empleados.

**¿A quiénes le sucede el problema?**
El problema afecta a profesionales en edad productiva que experimentan presión laboral, especialmente en sectores con altas exigencias, responsabilidades o ambientes competitivos.

**¿Quién lo utilizará?**
Lo utilizarán adultos profesionales de 20 a 50 años con acceso a dispositivos móviles, interesados en monitorear y gestionar su estrés laboral de manera proactiva.

---

**Why / Por qué**
**¿Cuál es la causa del problema?**
Las causas incluyen: altas exigencias laborales, recursos insuficientes, inseguridad laboral, conflictos interpersonales, desequilibrio entre vida personal y profesional, falta de control sobre las tareas, y ausencia de herram


### 1.2.2 Lean UX Process
---
### 1.2.2.1 Lean UX Problem Statements

Nuestra app permite a los usuarios identificar y gestionar su estrés laboral mediante un 
test de autoevaluación y la observación de señales físicas visibles como la postura, la 
respiración y la tensión facial. Además, brinda acceso a psicólogos y actividades 
prácticas para mejorar el bienestar.

Hemos observado que muchos adultos entre 20 y 50 años sufren niveles elevados de 
estrés en el trabajo, pero no cuentan con herramientas simples, accesibles y efectivas 
para reconocer estos niveles a tiempo ni saber cómo actuar al respecto.

¿Cómo pueden los trabajadores detectar y manejar su estrés de forma temprana y
efectiva en su entorno laboral, usando una herramienta accesible, fácil de usar e 
integrada en su rutina diaria?
---
### 1.2.2.2 Lean UX Assumptions
Feature: Sistema de identificación y gestión del estrés laboral en NeuroZen

**Registro Biométrico y Perfil del Usuario:**
Creemos que nuestros usuarios (adultos de 20 a 50 años en el ámbito laboral) necesitan una forma sencilla y segura de registrar sus parámetros biométricos (por medio de la cámara o sensores de sus dispositivos móviles) junto con información de salud y comportamiento. Esto permitirá personalizar el seguimiento y el manejo del estrés en función de las características individuales.

**Detección Temprana de Estrés mediante Patrones Físicos:**
Creemos que la identificación de señales biométricas observables (postura, tensión muscular, patrones de respiración y sudoración) permitirá detectar de forma temprana niveles de estrés. Esto facilitará la intervención oportuna antes de que se agraven los síntomas, impactando positivamente en la salud mental y física de los usuarios.

**Integración de Evaluaciones Psicológicas y Recomendaciones Personalizadas:**
Creemos que los usuarios se beneficiarán al combinar la autoevaluación biométrica con tests emocionales y recomendaciones personalizadas (ejercicios de respiración, pausas activas, contacto con especialistas). Esta integración permitirá al usuario conocer su estado en tiempo real y acceder a soluciones prácticas y adaptadas a su contexto.

**Seguimiento y Análisis de Datos de Estrés:**
Creemos que disponer de un registro histórico del nivel de estrés y obtener estadísticas personalizadas ayudará al usuario a identificar patrones y cambios en su salud, promoviendo acciones preventivas y mejoras en su entorno laboral y personal.

**Business Outcomes (Resultados del negocio)**
Se aumentará la productividad laboral y se reducirá el ausentismo, ya que los trabajadores podrán identificar y gestionar su estrés de manera proactiva.

Se generarán ingresos a través de planes de suscripción individuales y acuerdos corporativos con empresas interesadas en el bienestar de sus empleados.

NeuroZen se posicionará como una herramienta innovadora y confiable para la salud mental en el ámbito laboral, ampliando su alcance en el mercado latinoamericano.

**Users (Usuarios)**
Profesionales y empleados de 20 a 50 años que desarrollan sus actividades en ambientes laborales exigentes y de alta presión.

Personas que desean mejorar sus niveles de bienestar integral mediante el monitoreo de señales físicas y emocionales.

Usuarios que utilizan dispositivos móviles y buscan soluciones digitales para la autogestión de su salud mental.

**User Outcomes (Beneficios para el usuario)**
Identificar sus niveles de estrés de manera temprana y objetiva, mediante el análisis de patrones biométricos.

Acceder a recomendaciones personalizadas que les ayuden a manejar y reducir los síntomas de estrés.

Visualizar estadísticas y tendencias de su bienestar, facilitando el seguimiento a lo largo del tiempo.

Mejorar su calidad de vida laboral y personal gracias a estrategias adaptadas a sus necesidades específicas.

**Features (Características)**
Registro de Datos Biométricos: Herramienta de captura de señales físicas a través de la cámara y sensores del móvil.


Autoevaluación Integral: Tests combinados que evalúan tanto aspectos emocionales como físicos del estrés.


Recomendaciones Personalizadas: Sugerencias de ejercicios, pausas activas y consejos de salud mental basados en el perfil del usuario.


Historial y Seguimiento: Dashboard interactivo que muestra evolución, tendencias y alertas de niveles de estrés.


Integración con Profesionales: Opción de contactar con psicólogos o especialistas en bienestar para intervenciones personalizadas.
---
### 1.2.2.3 Lean UX Hypothesis Statements

**Hipótesis 1: **
**Creemos que** la implementación de un sistema de registro biométrico y autoevaluación permitirá a los usuarios identificar tempranamente sus niveles de estrés laboral.

**Sabremos que** la hipótesis se confirma cuando se observe una correlación significativa entre los datos biométricos capturados y las autoevaluaciones realizadas por los usuarios.

**Cuando** al menos el 65% de los usuarios completen de forma regular la evaluación en la plataforma y se detecten cambios relevantes en sus patrones biométricos.

**Hipótesis 2: **
**Creemos que** al ofrecer recomendaciones personalizadas basadas en el análisis del estrés, los usuarios adoptarán prácticas de autogestión más efectivas para reducir sus síntomas.

**Sabremos que** la hipótesis es correcta cuando los usuarios reporten mejoras en su bienestar y se registre una disminución en los indicadores de estrés en los seguimientos mensuales.

**Cuando** se logre una reducción del 20% en la frecuencia e intensidad de síntomas reportados durante los primeros seis meses de uso.


**Hipótesis 3:** 
**Creemos que** la visualización de un historial interactivo y tendencias de estrés motivará a los usuarios a llevar un control continuo de su salud mental.

**Sabremos que** esto es cierto cuando se registre un aumento en la interacción con el dashboard y una mayor adherencia a las recomendaciones sugeridas.

**Cuando** el uso constante de las herramientas de seguimiento genere datos que indiquen una mayor consciencia y manejo proactivo del estrés en el entorno laboral

---
### 1.2.2.4 Lean UX Canvas

---
## 1.2.3 Segmentos objetivo.