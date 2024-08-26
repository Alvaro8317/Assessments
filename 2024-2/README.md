# Agricultura

## Contexto

Somos una startup de innovación enfocado a los cultivos y agricultura. Nuestro enfoque actual es proveer a nuestros usuarios una experiencia agradable para facilitar la gestión de cultivos, conectar a agricultores con compradores y optimizar la cadena de suministro agrícola. La plataforma debe ser robusta, segura y escalable para adaptarse al crecimiento del sector.

### Servicios por ofrecer

- Gestión de Cultivos:

  - Registro detallado de cultivos (tipo, variedad, ubicación, tamaño, fechas de siembra/cosecha).
  - Monitoreo de variables climáticas (temperatura, humedad, precipitación) mediante sensores IoT y APIs externas.
  - Sistema de alertas tempranas para plagas, enfermedades y condiciones climáticas adversas.

- Marketplace Agrícola:

  - Plataforma de comercio electrónico para conectar agricultores con compradores (mayoristas, minoristas, procesadores).
  - Sistema de publicación de ofertas y demandas de productos agrícolas.
  - Gestión de pagos, facturación y logística integrada.

- Trazabilidad y Transparencia:

  - Seguimiento de la cadena de suministro desde la siembra hasta el consumidor final.
  - Registro de información relevante en cada etapa (certificaciones, tratamientos, transporte).
  - Acceso a la información de trazabilidad mediante códigos QR o números de lote.

- Análisis de Datos e Inteligencia Artificial:
  - Análisis de datos de cultivos, clima y mercado para optimizar la producción y la toma de decisiones.
  - Predicción de cosechas, detección temprana de enfermedades y recomendaciones de precios.

### Casos de Prueba

- Registro de Cultivo y Monitoreo: Simular el registro de un cultivo, la integración con sensores IoT y la generación de alertas por condiciones climáticas adversas.
- Publicación de Oferta y Compra en el Marketplace: Simular la publicación de una oferta de venta de un producto agrícola, la recepción de ofertas de compra y la realización de una transacción exitosa.
- Trazabilidad de un Producto: Simular el seguimiento de un producto desde la siembra hasta el consumidor final, verificando la información de trazabilidad en cada etapa.
- Análisis de Datos para Optimizar la Producción: Simular el análisis de datos históricos de cultivos y clima para identificar patrones y generar recomendaciones para mejorar la producción.

## Resolución

### DDD (Domain Drive Design)

#### Dominio

Para este problema se identificó y se definió que el principal dominio del problema a tratar será **facilitar la gestión de cultivos con su cadena de suministro y venta**, enfocando el dominio a lo esencial, simplificando el modelo de dominio con una escalabilidad natural para que a medida que la plataforma crezca, lo haga también su dominio y teniendo este enfoque simplificado, se podrá entregar valor más rapido
con menor riesgo, coste y un mayor ROI (Retorno de inversión).

#### Entidades, value objects y aggregates

##### `Entidades`

- `Cultivo` -> Atributos como tipo, variedad, ubicación, tamaño, fechas de siembre / cosecha
- `Usuario` -> Entidad genérica, puede ser agricultor o comprador, tiene atributos de nombre, ID, contacto y tipo de usuario
- `Agricultor` -> Tipo especifico de usuario que gestiona los cultivos
- `Comprador` -> Tipo especifico de usuario que realiza compras

##### `Value Objects`

- Ubicación
- Condiciones climáticas
- Precio

##### `Aggregates`

- Gestión de cultivos -> Contiene entidades como cultivo y value objects como ubicación y condiciones climáticas
- Transacción comercial -> Engloba la interacción entre agricultor y comprador, abarca entidades como producto agrícola y precio

#### Subcontextos anidados

Estos subcontextos anidados cuentan con una relación de interdependencia entre sí usando el patron de interacción "shared kernel" con el subcontexto `transacciones y cadena de suministro` como se observa en el diagrama `Context Map.drawio`, las operaciones compartidas entre los subcontextos son:

- Transacciones
- Cadena de suministro

##### Gestión de cultivos

Centrado en la gestión de los cultivos, incluyendo monitoreo, alertas y seguimiento de las fechas clave

##### Usuarios

Engloba los tipos de usuarios en la plataforma

##### Transacciones y cadena de suministro

Centrado en la interacción comercial, incluye ventas, pagos y trazabilidad.

#### Lenguaje ubicuo

- Entidad Raíz (Root Entity): La entidad principal en un agregado, que gestiona y controla las operaciones sobre las demás entidades y valores dentro de su agregado.
- Compra: Transacción en la que un comprador adquiere productos agrícolas de un agricultor. Incluye detalles como fecha, cantidad, precio, y estado.
- Marketplace Agrícola: Plataforma dentro del sistema donde los agricultores pueden ofrecer sus productos y los compradores pueden adquirirlos, gestionando la oferta y la demanda.
- Monitoreo de Cultivos: Proceso continuo de seguimiento de las condiciones de los cultivos, incluyendo aspectos como clima, crecimiento, y posibles amenazas (plagas, enfermedades).
- Trazabilidad: La capacidad de rastrear un producto agrícola desde su origen (cultivo) hasta el consumidor final, asegurando transparencia en todas las etapas de la cadena de suministro.
- Alertas Tempranas: Sistema automatizado que avisa a los agricultores sobre posibles amenazas o cambios en las condiciones que podrían afectar sus cultivos, como plagas, enfermedades, o clima adverso.
- Logística Agrícola: El conjunto de actividades necesarias para gestionar el transporte, almacenamiento, y distribución de productos agrícolas desde el punto de origen hasta el punto de venta o consumo.
- Facturación: Proceso de emisión de facturas por productos vendidos, incluyendo la gestión de pagos y cobros asociados a transacciones dentro del marketplace agrícola.
- Cadena de Suministro Agrícola: El proceso completo que sigue un producto agrícola desde su cultivo hasta el consumidor final, incluyendo etapas de producción, procesamiento, y distribución.
- Sensor IoT: Dispositivo utilizado para medir y monitorear variables del entorno agrícola, como temperatura y humedad, proporcionando datos en tiempo real para mejorar la gestión de cultivos.
- Predicción de Cosechas: Uso de datos históricos y análisis para estimar la cantidad y calidad de los productos agrícolas que se cosecharán en un futuro próximo.
