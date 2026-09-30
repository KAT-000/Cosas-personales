# 🛡️️ Marco Ético, Legal y de Seguridad para Robots de Patrullaje Autónomo

La integración de robots autónomos con capacidades de visión artificial (reconocimiento facial, de cuerpos, placas y uniformes) en espacios físicos requiere un diseño estricto que cumpla con los estándares de privacidad, seguridad operativa y legalidad. 

Este documento establece las directrices técnicas y normativas implementadas en el desarrollo de este proyecto robótico.

---

## 1.  Ciberseguridad y Protección de Datos
*Garantizar que la información recopilada por el robot (rostros, patentes, video en tiempo real) no sea vulnerable a interceptaciones o robos.*

* **Cifrado de Datos:** 
  * Todo el streaming de video y la telemetría deben viajar cifrados utilizando protocolos estándar (ej. TLS/HTTPS o VPNs internas para la comunicación con la estación base).
  * Las bases de datos locales que almacenen registros biométricos o de matrículas deben estar cifradas en reposo (ej. AES-256).
* **Políticas de Retención de Datos (Privacy by Design):**
  * Definir un tiempo máximo de almacenamiento para los datos de personas autorizadas o visitas comunes. Los rostros que no representen una amenaza deben ser descartados o anonimizados automáticamente (ej. purga de registros visuales cada 24 a 48 horas si no existen incidentes de seguridad).
* **Control de Accesos (IAM):**
  * Acceso restringido al software del robot, logs y paneles de control mediante autenticación y roles de usuario definidos.

---

## 2.  Privacidad y Cumplimiento Normativo
*El reconocimiento facial y el tratamiento de datos biométricos están fuertemente regulados a nivel global y local.*

* **Transparencia y Señalética:**
  * Los espacios vigilados por el robot deben contar con señalización visible que advierta sobre la presencia de vigilancia robótica autónoma y el responsable del tratamiento de los datos.
* **Minimización de Datos:**
  * El sistema de Computer Vision (CV) se configura para procesar únicamente los rasgos necesarios para la identificación de amenazas o verificación de listas blancas/negras, evitando la grabación indiscriminada de áreas privadas o ajenas al perímetro objetivo.
* **Alineación con Normas de Protección de Datos:**
  * Diseño enfocado en cumplir con las leyes de protección de datos personales vigentes (como la Ley 19.628 en Chile o normativas internacionales equivalentes), garantizando los derechos de los ciudadanos sobre su información.

---

## 3.  Seguridad Física y Operativa (Safety)
*Un robot móvil autónomo es una masa pesada en movimiento; la seguridad de las personas en el entorno físico es la prioridad número uno.*

* **Sistemas de Parada de Emergencia (E-Stop):**
  * Botón físico de parada de emergencia altamente visible y accesible de forma inmediata en el chasis del robot.
  * Parada de emergencia por software ante pérdida de conexión con la estación base o fallo crítico en los nodos de control de ROS.
* **Sensores de Colisión y Navegación Segura:**
  * Uso de sensores perimetrales (LiDAR, sensores ultrasónicos, cámaras de profundidad o parachoques mecánicos con interruptores de presión) para la detección y evasión de obstáculos estáticos y dinámicos (personas, animales).
* **Limitación de Velocidad y Torque:**
  * Restricción estricta de la velocidad máxima del robot en zonas de alta concurrencia de personas para mitigar riesgos de impacto.

---

## 4. Arquitectura del Sistema de Visión y Privacidad
*Cómo se estructura el software para que la IA procese la información de forma segura.*

* **Procesamiento en el Borde (Edge Computing):**
  * El procesamiento de reconocimiento facial y de placas se ejecuta localmente en el ordenador de abordo del robot (Raspberry Pi / SBC o GPU dedicada), minimizando la exposición de video sin procesar en la red.
* **Listas Blancas y Negras:**
  * El sistema compara los rostros o uniformes detectados exclusivamente contra bases de datos preautorizadas (personal interno, residentes) para emitir alertas **únicamente** ante anomalías o ausencias de credenciales válidas.
* **Trazabilidad (Logs de Auditoría):**
  * Cada alerta de intrusión genera un registro con: marca de tiempo (timestamp), coordenadas de ubicación del robot, captura recortada de la infracción y el nivel de confianza del modelo de IA, manteniendo un registro forense auditable.