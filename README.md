# Capítulo III: Requirements Specification

---

## 3.1. To-Be Scenario Mapping.  

| **FASES** | **DESCUBRIMIENTO** | **EVALUACIÓN** | **USO DE LA APP SMARTSTRESS** | **SEGUIMIENTO PERSONAL** |
| --- | --- | --- | --- | --- |
| **DOING** | Encuentra la app en la store recomendada por colegas.<br><br>Lee testimonios de usuarios con perfiles similares.<br><br>Descarga la versión gratuita. | Explora ejercicios guiados y test de estrés inicial.<br><br>Revisa precios accesibles.<br><br>Configura recordatorios en la app. | Realiza test semanales de estrés.<br><br>Usa ejercicios de respiración y meditación guiados.<br><br>Sigue rutinas personalizadas cortas. | Revisa métricas de progreso en la app.<br><br>Recibe recomendaciones automáticas.<br><br>Ajusta su rutina según alertas de la app. |
| **THINKING** | “Esto parece hecho para gente como yo.”<br><br>“Vale la pena probar, no necesito tanto tiempo libre.”<br><br>“Podría mejorar mi rendimiento en el trabajo.” | “Es más práctica que otras apps que probé.”<br><br>“El precio es accesible.”<br><br>“Los recordatorios me ayudarán a no abandonar.” | “Finalmente tengo algo estructurado.”<br><br>“Los ejercicios me calman rápido.”<br><br>“La rutina es realista y alcanzable.” | “Estoy logrando ser constante.”<br><br>“Los resultados son visibles.”<br><br>“Ya no me siento atrapado en el mismo ciclo de estrés.” |
| **FEELING** | Motivación inicial.<br><br>Confianza.<br><br>Alivio. | Curiosidad positiva.<br><br>Seguridad.<br><br>Optimismo. | Tranquilidad.<br><br>Constancia.<br><br>Satisfacción. | Orgullo personal.<br><br>Confianza en su progreso.<br><br>Esperanza a largo plazo. |

---

## 3.2. User Stories.  

# Epics

| EPIC ID | Nombre del EPIC                         |
|---------|----------------------------------------|
| EP01    | Registro y Gestión de Perfil de Huésped |
| EP02    | Registro y Gestión de Perfil de Anfitrión |
| EP03    | Gestión de Propiedades                  |
| EP04    | Búsqueda y Reserva de Estancias         |
| EP05    | Pagos y Facturación                     |
| EP06    | Reseñas y Calificaciones                |
| EP07    | Soporte y Ayuda                         |
| EP08    | Exploración como Visitante              |

# User Stories por Epic

## EP01 – Registro y Gestión de Perfil de Usuario

### User Stories

| User Story ID | Título                    |
|---------------|-------------------------|
| US01          | Registro de usuario      |
| US02          | Inicio de sesión seguro  |
| US03          | Recuperación de contraseña |
| US04          | Edición de perfil personal |

### Technical Stories

| Technical Story ID | Título                                         |
|--------------------|-----------------------------------------------|
| TS01              | Validar formularios de registro/login en frontend |

## EP02 – Registro y Gestión de Perfil de Psicólogo

### User Stories

| User Story ID | Título                               |
|---------------|-------------------------------------|
| US05          | Registro de psicólogo               |
| US06          | Verificación de credenciales profesionales |
| US07          | Configuración de datos de contacto  |
| US08          | Edición de perfil de psicólogo      |

### Technical Stories

| Technical Story ID | Título                                           |
|--------------------|-------------------------------------------------|
| TS02              | Validar documentos y credenciales en frontend    |

## EP03 – Gestión de Rutinas y Ejercicios

### User Stories

| User Story ID | Título                                      |
|---------------|-------------------------------------------|
| US09          | Registrar rutina personalizada            |
| US10          | Acceder a ejercicios de relajación y respiración |
| US11          | Editar o actualizar rutina diaria          |
| US12          | Eliminar rutina                            |

### Technical Stories

| Technical Story ID | Título                                           |
|--------------------|-------------------------------------------------|
| TS03              | Implementar reproductor de audio/video para ejercicios |

## EP04 – Evaluación y Seguimiento del Estrés

### User Stories

| User Story ID | Título                                           |
|---------------|-------------------------------------------------|
| US13          | Realizar test de nivel de estrés                |
| US14          | Ver resultados e historial de evaluaciones      |
| US15          | Recibir recomendaciones automáticas según resultados |
| US16          | Generar recordatorios para seguimiento          |

### Technical Stories

| Technical Story ID | Título                                      |
|--------------------|---------------------------------------------|
| TS04              | Desarrollar algoritmo de cálculo de nivel de estrés |

## EP05 – Pagos y Suscripciones

### User Stories

| User Story ID | Título                         |
|---------------|---------------------------------|
| US17          | Realizar pago de suscripción    |
| US18          | Consultar comprobantes de pago  |
| US19          | Actualizar plan de suscripción  |

### Technical Stories

| Technical Story ID | Título                           |
|--------------------|----------------------------------|
| TS05              | Integrar pasarela de pagos segura |

## EP06 – Reseñas y Calificaciones

### User Stories

| User Story ID | Título                        |
|---------------|-------------------------------|
| US20          | Dejar reseña sobre psicólogo  |
| US21          | Calificar ejercicios o rutinas |

---

## EP07 – Soporte y Ayuda

### User Stories

| User Story ID | Título                                  |
|---------------|----------------------------------------|
| US22          | Acceder a soporte técnico desde la app |
| US23          | Consultar preguntas frecuentes         |
| US24          | Reportar un problema                   |

### Technical Stories

| Technical Story ID | Título                          |
|--------------------|---------------------------------|
| TS06              | Implementar chat de soporte básico |

## EP08 – Exploración como Visitante

### User Stories

| User Story ID | Título                                                       |
|---------------|-------------------------------------------------------------|
| US25          | Explorar funcionalidades de la app sin registro              |
| US26          | Visualizar landing page con beneficios y testimonios         |

---

## EP01 – Registro y Gestión de Perfil de Usuario

| ID Épica | Épica                                  | ID  | Título                   | Descripción                                                                 | Criterios de Aceptación |
|---------|----------------------------------------|-----|------------------------|----------------------------------------------------------------------------|------------------------|
| EP01    | Registro y Gestión de Perfil de Usuario | US01 | Registro de usuario    | Como usuario, quiero registrarme en la plataforma para crear mi cuenta.    | **Escenario 1:** Registro exitoso → Dado que el usuario accede al formulario de registro, Cuando completa los campos requeridos y presiona “Crear cuenta”, Entonces el sistema registra al usuario y muestra un mensaje de bienvenida.<br>**Escenario 2:** Registro con datos incompletos → Dado que el usuario no completa todos los campos requeridos, Cuando intenta registrarse, Entonces el sistema muestra mensajes de validación en los campos vacíos. |
| EP01    | Registro y Gestión de Perfil de Usuario | US02 | Inicio de sesión seguro | Como usuario registrado, quiero iniciar sesión para acceder a mis funciones.| **Escenario 1:** Inicio exitoso → Dado que el usuario ya está registrado, Cuando ingresa credenciales válidas, Entonces accede al panel principal.<br>**Escenario 2:** Inicio fallido → Dado que el usuario ingresa correo o contraseña inválida, Cuando presiona “Iniciar sesión”, Entonces el sistema muestra un mensaje de error. |
| EP01    | Registro y Gestión de Perfil de Usuario | US03 | Recuperación de contraseña | Como usuario, quiero recuperar mi contraseña para poder acceder si la olvido.| **Escenario 1:** Recuperación exitosa → Dado que el usuario olvidó su contraseña, Cuando solicita la recuperación ingresando su correo, Entonces el sistema envía un enlace de restablecimiento.<br>**Escenario 2:** Correo no registrado → Dado que el usuario ingresa un correo no registrado, Cuando solicita la recuperación, Entonces el sistema muestra un mensaje de error indicando que el correo no existe. |
| EP01    | Registro y Gestión de Perfil de Usuario | US04 | Edición de perfil personal | Como usuario, quiero editar mi información personal para mantenerla actualizada.| **Escenario 1:** Edición exitosa → Dado que el usuario está logueado, Cuando modifica sus datos personales y guarda, Entonces el sistema actualiza la información correctamente.<br>**Escenario 2:** Error en el guardado → Dado que el usuario edita su información, Cuando el sistema presenta una falla en la actualización, Entonces se muestra un mensaje de error y no se guardan los cambios. |
| EP01    | Registro y Gestión de Perfil de Usuario | TS01 | Validaciones frontend registro/login | Como desarrollador, quiero validar formularios en frontend para evitar errores.| **Escenario 1:** Validación de campos vacíos → Dado que el usuario deja campos en blanco, Cuando intenta registrarse o iniciar sesión, Entonces el sistema muestra mensajes de validación.<br>**Escenario 2:** Validación de formato de correo → Dado que el usuario ingresa un correo con formato inválido, Cuando intenta guardar o iniciar sesión, Entonces el sistema muestra un mensaje indicando que el correo no es válido. |

## EP02 – Registro y Gestión de Perfil de Psicólogo

| ID Épica | Épica                                   | ID   | Título                        | Descripción                                                                 | Criterios de Aceptación |
|---------|-----------------------------------------|------|-----------------------------|----------------------------------------------------------------------------|------------------------|
| EP02    | Registro y Gestión de Perfil de Psicólogo| US05 | Registro de psicólogo        | Como psicólogo, quiero registrarme en la plataforma para ofrecer mis servicios.| **Escenario 1:** Registro exitoso → Dado que el psicólogo accede al formulario de registro, Cuando completa los campos requeridos y presiona “Crear cuenta”, Entonces el sistema registra al psicólogo y muestra un mensaje de bienvenida.<br>**Escenario 2:** Registro con datos incompletos → Dado que el psicólogo no completa todos los campos requeridos, Cuando intenta registrarse, Entonces el sistema muestra mensajes de validación en los campos faltantes. |
| EP02    | Registro y Gestión de Perfil de Psicólogo| US06 | Verificación de credenciales | Como psicólogo, quiero verificar mis credenciales para generar confianza en los usuarios.| **Escenario 1:** Documento válido → Dado que el psicólogo sube su título o licencia válida, Cuando el sistema lo recibe, Entonces el estado del perfil cambia a “En revisión”.<br>**Escenario 2:** Documento inválido → Dado que el psicólogo sube un archivo no permitido o ilegible, Cuando intenta verificar credenciales, Entonces el sistema muestra un mensaje de error indicando que debe subir un documento válido. |
| EP02    | Registro y Gestión de Perfil de Psicólogo| US07 | Configuración de datos de contacto | Como psicólogo, quiero configurar mis datos de contacto para que los pacientes puedan comunicarse conmigo.| **Escenario 1:** Configuración exitosa → Dado que el psicólogo edita su sección de contacto, Cuando guarda número de teléfono y correo, Entonces el sistema actualiza los datos correctamente.<br>**Escenario 2:** Datos inválidos → Dado que el psicólogo ingresa un correo con formato incorrecto o un número incompleto, Cuando intenta guardar, Entonces el sistema muestra mensajes de validación. |
| EP02    | Registro y Gestión de Perfil de Psicólogo| US08 | Edición de perfil de psicólogo | Como psicólogo, quiero editar mi información profesional para mantenerla actualizada.| **Escenario 1:** Edición exitosa → Dado que el psicólogo está logueado, Cuando modifica su información de especialidad, experiencia o tarifas y guarda, Entonces el sistema actualiza la información correctamente.<br>**Escenario 2:** Error en el guardado → Dado que el psicólogo edita su información, Cuando el sistema presenta un error de conexión, Entonces se muestra un mensaje indicando que los cambios no se guardaron. |
| EP02    | Registro y Gestión de Perfil de Psicólogo| TS02 | Validar campos de formulario en frontend | Como desarrollador, quiero validar los campos de formulario (correo, contraseña, documento) para asegurar calidad en los datos.| **Escenario 1:** Validación de correo → Dado que el usuario ingresa un correo inválido, Cuando intenta guardar, Entonces el sistema muestra un mensaje de error.<br>**Escenario 2:** Validación de documento → Dado que el psicólogo sube un archivo en un formato no permitido, Cuando intenta verificar identidad, Entonces el sistema muestra un mensaje de validación. |

# EP03 – Gestión de Rutinas y Ejercicios

| ID Épica | Épica                          | ID   | Título                                    | Descripción                                                                 | Criterios de Aceptación |
|---------|--------------------------------|------|-------------------------------------------|-----------------------------------------------------------------------------|------------------------|
| EP03    | Gestión de Rutinas y Ejercicios | US09 | Registrar rutina personalizada            | Como usuario, quiero registrar una rutina personalizada para organizar mis prácticas de manejo del estrés. | **Escenario 1: Registro exitoso**<br>Dado que el usuario completa los campos de la rutina (nombre, duración, ejercicios),<br>Cuando guarda la rutina,<br>Entonces el sistema registra y muestra la rutina en su lista.<br><br>**Escenario 2: Campos incompletos**<br>Dado que el usuario deja campos vacíos,<br>Cuando intenta guardar,<br>Entonces el sistema muestra mensajes de validación en los campos faltantes. |
| EP03    | Gestión de Rutinas y Ejercicios | US10 | Acceder a ejercicios de relajación y respiración | Como usuario, quiero acceder a ejercicios guiados de relajación y respiración para reducir mi estrés. | **Escenario 1: Acceso exitoso**<br>Dado que el usuario selecciona un ejercicio de la lista,<br>Cuando presiona “Reproducir”,<br>Entonces el sistema inicia el ejercicio en formato audio/video.<br><br>**Escenario 2: Error de acceso**<br>Dado que el usuario selecciona un ejercicio,<br>Cuando ocurre un error de conexión,<br>Entonces el sistema muestra un mensaje de “Intente nuevamente”. |
| EP03    | Gestión de Rutinas y Ejercicios | US11 | Editar o actualizar rutina diaria          | Como usuario, quiero editar o actualizar mi rutina diaria para mantenerla al día con mis necesidades. | **Escenario 1: Edición exitosa**<br>Dado que el usuario abre una rutina guardada,<br>Cuando modifica duración o ejercicios y guarda,<br>Entonces el sistema actualiza correctamente.<br><br>**Escenario 2: Error en edición**<br>Dado que el usuario intenta editar una rutina,<br>Cuando ocurre un fallo en el guardado,<br>Entonces se muestra un mensaje indicando que no se pudieron guardar los cambios. |
| EP03    | Gestión de Rutinas y Ejercicios | US12 | Eliminar rutina                           | Como usuario, quiero eliminar una rutina que ya no utilizo para mantener mi lista organizada. | **Escenario 1: Eliminación exitosa**<br>Dado que el usuario selecciona una rutina,<br>Cuando presiona “Eliminar” y confirma,<br>Entonces el sistema borra la rutina de la lista.<br><br>**Escenario 2: Cancelación de eliminación**<br>Dado que el usuario selecciona una rutina para eliminar,<br>Cuando presiona “Cancelar”,<br>Entonces el sistema no realiza ningún cambio. |
| EP03    | Gestión de Rutinas y Ejercicios | TS03 | Implementar reproductor de audio/video para ejercicios | Como desarrollador, quiero implementar un reproductor de audio/video para guiar a los usuarios en los ejercicios. | **Escenario 1: Reproducción exitosa**<br>Dado que el usuario selecciona un archivo válido,<br>Cuando inicia la reproducción,<br>Entonces el reproductor funciona con controles básicos (play, pause, stop).<br><br>**Escenario 2: Error en archivo**<br>Dado que el usuario selecciona un archivo dañado o no compatible,<br>Cuando intenta reproducirlo,<br>Entonces el sistema muestra un mensaje de error. |

## EP04 – Evaluación y Seguimiento del Estrés

| ID Épica | **Título**                      | ID   | Título                                   | Descripción                                                                 | Criterios de Aceptación |
|----------|----------------------------------|------|------------------------------------------|-----------------------------------------------------------------------------|-------------------------|
| EP04     | Evaluación y Seguimiento del Estrés | US13 | Realizar test de nivel de estrés         | Como usuario, quiero realizar un test de nivel de estrés para conocer mi estado actual. | **Escenario 1: Test completado con éxito**<br>Dado que el usuario responde todas las preguntas,<br>Cuando presiona “Finalizar test”,<br>Entonces el sistema calcula y muestra el nivel de estrés.<br><br>**Escenario 2: Preguntas incompletas**<br>Dado que el usuario omite preguntas,<br>Cuando intenta finalizar,<br>Entonces el sistema muestra un aviso para completar todas las respuestas. |
| EP04     | Evaluación y Seguimiento del Estrés | US14 | Ver resultados e historial de evaluaciones | Como usuario, quiero ver mis resultados e historial de evaluaciones para dar seguimiento a mi progreso. | **Escenario 1: Consulta exitosa**<br>Dado que el usuario accede a su perfil,<br>Cuando selecciona la sección “Historial”,<br>Entonces el sistema muestra resultados anteriores con fecha y nivel de estrés.<br><br>**Escenario 2: Sin evaluaciones previas**<br>Dado que el usuario no ha realizado tests,<br>Cuando accede a “Historial”,<br>Entonces el sistema muestra un mensaje indicando que no hay datos disponibles. |
| EP04     | Evaluación y Seguimiento del Estrés | US15 | Recibir recomendaciones automáticas según resultados | Como usuario, quiero recibir recomendaciones automáticas basadas en mis resultados de estrés para mejorar mi bienestar. | **Escenario 1: Recomendaciones generadas**<br>Dado que el usuario completa un test,<br>Cuando se calculan los resultados,<br>Entonces el sistema muestra recomendaciones personalizadas (ejercicios, rutinas, consejos).<br><br>**Escenario 2: Error en la generación**<br>Dado que ocurre un fallo en el sistema,<br>Cuando intenta mostrar recomendaciones,<br>Entonces aparece un mensaje indicando que intente más tarde. |
| EP04     | Evaluación y Seguimiento del Estrés | US16 | Generar recordatorios para seguimiento     | Como usuario, quiero generar recordatorios para dar seguimiento a mis evaluaciones periódicas. | **Escenario 1: Recordatorio creado**<br>Dado que el usuario selecciona fecha y hora,<br>Cuando guarda el recordatorio,<br>Entonces el sistema lo agenda y lo muestra en su calendario o notificaciones.<br><br>**Escenario 2: Configuración inválida**<br>Dado que el usuario selecciona una fecha pasada,<br>Cuando intenta guardar,<br>Entonces el sistema muestra un mensaje de error. |
| EP04     | Evaluación y Seguimiento del Estrés | TS04 | Desarrollar algoritmo de cálculo de nivel de estrés | Como desarrollador, quiero implementar un algoritmo que calcule el nivel de estrés en base a las respuestas del usuario. | **Escenario 1: Cálculo correcto**<br>Dado que el usuario completa el test,<br>Cuando el sistema procesa las respuestas,<br>Entonces devuelve un puntaje y clasificación correcta (bajo, medio, alto).<br><br>**Escenario 2: Error de cálculo**<br>Dado que ocurre un fallo interno,<br>Cuando se procesa el test,<br>Entonces el sistema muestra un mensaje de error y no guarda resultados. |

## EP05 – Pagos y Suscripciones

| ID Épica | **Título**             | ID   | Título                          | Descripción                                                                 | Criterios de Aceptación |
|----------|-----------------------|------|---------------------------------|-----------------------------------------------------------------------------|-------------------------|
| EP05     | Pagos y Suscripciones | US17 | Realizar pago de suscripción   | Como usuario, quiero realizar el pago de mi suscripción para acceder a los servicios premium de la app. | **Escenario 1: Pago exitoso**<br>Dado que el usuario ingresa datos válidos de su tarjeta,<br>Cuando confirma el pago,<br>Entonces el sistema procesa y confirma la suscripción mostrando un mensaje de éxito.<br><br>**Escenario 2: Pago rechazado**<br>Dado que los datos de la tarjeta son incorrectos o no hay fondos,<br>Cuando intenta pagar,<br>Entonces el sistema muestra un mensaje de error indicando que verifique la información. |
| EP05     | Pagos y Suscripciones | US18 | Consultar comprobantes de pago | Como usuario, quiero consultar mis comprobantes de pago para tener registro de mis transacciones. | **Escenario 1: Consulta exitosa**<br>Dado que el usuario tiene pagos realizados,<br>Cuando accede a la sección “Comprobantes”,<br>Entonces el sistema muestra la lista de pagos con fecha, monto y método.<br><br>**Escenario 2: Sin pagos registrados**<br>Dado que el usuario nunca ha pagado,<br>Cuando accede a la sección,<br>Entonces el sistema muestra un mensaje indicando que no hay registros disponibles. |
| EP05     | Pagos y Suscripciones | US19 | Actualizar plan de suscripción | Como usuario, quiero actualizar mi plan de suscripción para acceder a más beneficios. | **Escenario 1: Cambio exitoso de plan**<br>Dado que el usuario selecciona un plan superior,<br>Cuando confirma la actualización,<br>Entonces el sistema aplica el cambio y genera el cobro correspondiente.<br><br>**Escenario 2: Error en la actualización**<br>Dado que ocurre un fallo en el proceso,<br>Cuando el usuario intenta cambiar el plan,<br>Entonces el sistema muestra un mensaje indicando que lo intente más tarde. |
| EP05     | Pagos y Suscripciones | TS05 | Integrar pasarela de pagos segura | Como desarrollador, quiero integrar una pasarela de pagos segura para garantizar transacciones confiables. | **Escenario 1: Integración correcta**<br>Dado que el sistema procesa un pago,<br>Cuando la transacción es aceptada,<br>Entonces el sistema devuelve un estado de éxito y guarda la transacción.<br><br>**Escenario 2: Integración con error**<br>Dado que ocurre un problema con la pasarela,<br>Cuando se procesa el pago,<br>Entonces el sistema muestra un mensaje de error y no guarda el pago como exitoso. |

## EP06 – Reseñas y Calificaciones

| ID Épica | **Título**             | ID   | Título                          | Descripción                                                                 | Criterios de Aceptación |
|----------|-----------------------|------|---------------------------------|-----------------------------------------------------------------------------|-------------------------|
| EP06     | Reseñas y Calificaciones | US20 | Dejar reseña sobre psicólogo   | Como usuario, quiero dejar una reseña sobre el psicólogo después de mis sesiones, para compartir mi experiencia. | **Escenario 1: Reseña exitosa**<br>Dado que el usuario terminó una sesión,<br>Cuando accede a la opción “Dejar reseña” y escribe un comentario válido,<br>Entonces el sistema guarda la reseña y la muestra en el perfil del psicólogo.<br><br>**Escenario 2: Reseña inválida**<br>Dado que el usuario intenta guardar una reseña vacía o con caracteres no permitidos,<br>Cuando presiona guardar,<br>Entonces el sistema muestra un mensaje de error solicitando corrección. |
| EP06     | Reseñas y Calificaciones | US21 | Calificar ejercicios o rutinas | Como usuario, quiero calificar los ejercicios o rutinas para dar retroalimentación sobre su utilidad. | **Escenario 1: Calificación exitosa**<br>Dado que el usuario completó un ejercicio o rutina,<br>Cuando selecciona de 1 a 5 estrellas,<br>Entonces el sistema guarda la calificación y actualiza el promedio visible.<br><br>**Escenario 2: Error en calificación**<br>Dado que ocurre un error en la conexión,<br>Cuando el usuario intenta calificar,<br>Entonces el sistema muestra un mensaje indicando que intente nuevamente. |

## EP07 – Soporte y Ayuda

| ID Épica | **Título**        | ID   | Título                              | Descripción                                                                 | Criterios de Aceptación |
|---------|-----------------|------|----------------------------------|-----------------------------------------------------------------------------|-------------------------|
| EP07    | Soporte y Ayuda | US22 | Acceder a soporte técnico desde la app | Como usuario, quiero acceder a soporte técnico dentro de la app para resolver problemas rápidamente. | **Escenario 1: Acceso exitoso**<br>Dado que el usuario navega al menú de ayuda,<br>Cuando selecciona “Soporte técnico”,<br>Entonces el sistema abre el canal de soporte (chat o formulario) correctamente.<br><br>**Escenario 2: Error de acceso**<br>Dado un fallo de conexión,<br>Cuando el usuario intenta abrir soporte,<br>Entonces el sistema muestra un mensaje indicando que intente más tarde. |
| EP07    | Soporte y Ayuda | US23 | Consultar preguntas frecuentes | Como usuario, quiero consultar preguntas frecuentes para resolver dudas comunes sin necesidad de soporte. | **Escenario 1: Consulta exitosa**<br>Dado que el usuario abre la sección de preguntas frecuentes,<br>Cuando selecciona una categoría o pregunta,<br>Entonces el sistema despliega la respuesta correspondiente.<br><br>**Escenario 2: Contenido no disponible**<br>Dado que no hay FAQs cargadas,<br>Cuando el usuario intenta acceder,<br>Entonces el sistema muestra un mensaje indicando “No hay información disponible”. |
| EP07    | Soporte y Ayuda | US24 | Reportar un problema | Como usuario, quiero reportar un problema dentro de la app para notificar errores o inconvenientes. | **Escenario 1: Reporte exitoso**<br>Dado que el usuario detecta un problema,<br>Cuando llena el formulario de reporte y lo envía,<br>Entonces el sistema guarda el reporte y muestra confirmación.<br><br>**Escenario 2: Reporte inválido**<br>Dado que el usuario deja el formulario vacío o incompleto,<br>Cuando presiona “Enviar”,<br>Entonces el sistema muestra mensajes de validación solicitando completar los campos. |
| EP07    | Soporte y Ayuda | TS06 | Implementar chat de soporte básico | Como desarrollador, quiero implementar un chat básico para que los usuarios puedan comunicarse en tiempo real con soporte. | **Escenario 1: Chat activo**<br>Dado que el usuario abre el chat de soporte,<br>Cuando envía un mensaje,<br>Entonces el sistema lo transmite correctamente y soporte puede responder.<br><br>**Escenario 2: Chat no disponible**<br>Dado que no hay agentes en línea,<br>Cuando el usuario intenta abrir el chat,<br>Entonces el sistema muestra un mensaje “Agente no disponible, intente más tarde”. |

## EP08 – Exploración como Visitante

| ID Épica | **Título**                  | ID   | Título                                           | Descripción                                                                                   | Criterios de Aceptación |
|---------|-----------------------------|------|------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------|
| EP08    | Exploración como Visitante | US25 | Explorar funcionalidades de la app sin registro | Como visitante, quiero explorar las funcionalidades principales de la app sin registrarme para conocer su utilidad. | **Escenario 1: Exploración exitosa**<br>Dado que el visitante abre la app,<br>Cuando navega a la sección de exploración,<br>Entonces el sistema permite visualizar funcionalidades limitadas sin necesidad de cuenta.<br><br>**Escenario 2: Restricción de funciones**<br>Dado que el visitante intenta acceder a una función premium,<br>Cuando no tiene cuenta registrada,<br>Entonces el sistema muestra un mensaje invitando a registrarse. |
| EP08    | Exploración como Visitante | US26 | Visualizar landing page con beneficios y testimonios | Como visitante, quiero visualizar una página inicial con beneficios y testimonios para decidir si registrarme. | **Escenario 1: Visualización correcta**<br>Dado que el visitante abre la app o la web,<br>Cuando carga la landing page,<br>Entonces el sistema muestra beneficios, funcionalidades destacadas y testimonios.<br><br>**Escenario 2: Error de carga**<br>Dado que ocurre un problema de conexión,<br>Cuando el visitante intenta ver la landing page,<br>Entonces el sistema muestra un mensaje “Error al cargar, intente más tarde”. |

---

## 3.3. Impact Mapping.  

INSERTAR IMAGEN AQUI!!

---

## 3.4. Product Backlog.  

## Orden de User Stories y Technical Stories

| Orden | ID   | User Story / Technical Story                              | Story Points |
|------|------|---------------------------------------------------------|-------------|
| 01   | US01 | Registro de usuario                                     | 5           |
| 02   | US02 | Inicio de sesión seguro                                 | 3           |
| 03   | US03 | Recuperación de contraseña                              | 3           |
| 04   | US04 | Edición de perfil personal                              | 5           |
| 05   | TS01 | Validar formularios de registro/login en frontend       | 3           |
| 06   | US05 | Registro de psicólogo                                   | 5           |
| 07   | US06 | Verificación de credenciales profesionales              | 8           |
| 08   | US07 | Configuración de datos de contacto                      | 3           |
| 09   | US08 | Edición de perfil de psicólogo                          | 5           |
| 10   | TS02 | Validar documentos y credenciales en frontend           | 5           |
| 11   | US09 | Registrar rutina personalizada                          | 5           |
| 12   | US10 | Acceder a ejercicios de relajación y respiración        | 8           |
| 13   | US11 | Editar o actualizar rutina diaria                       | 5           |
| 14   | US12 | Eliminar rutina                                         | 3           |
| 15   | TS03 | Implementar reproductor de audio/video para ejercicios  | 8           |
| 16   | US13 | Realizar test de nivel de estrés                        | 5           |
| 17   | US14 | Ver resultados e historial de evaluaciones              | 5           |
| 18   | US15 | Recibir recomendaciones automáticas según resultados    | 8           |
| 19   | US16 | Generar recordatorios para seguimiento                  | 5           |
| 20   | TS04 | Desarrollar algoritmo de cálculo de nivel de estrés     | 8           |
| 21   | US17 | Realizar pago de suscripción                            | 5           |
| 22   | US18 | Consultar comprobantes de pago                          | 3           |
| 23   | US19 | Actualizar plan de suscripción                          | 5           |
| 24   | TS05 | Integrar pasarela de pagos segura                       | 8           |
| 25   | US20 | Dejar reseña sobre psicólogo                            | 3           |
| 26   | US21 | Calificar ejercicios o rutinas                          | 3           |
| 27   | US22 | Acceder a soporte técnico desde la app                  | 3           |
| 28   | US23 | Consultar preguntas frecuentes                          | 2           |
| 29   | US24 | Reportar un problema                                    | 3           |
| 30   | TS06 | Implementar chat de soporte básico                      | 5           |
| 31   | US25 | Explorar funcionalidades de la app sin registro         | 2           |
| 32   | US26 | Visualizar landing page con beneficios y testimonios    | 2           |

---

















