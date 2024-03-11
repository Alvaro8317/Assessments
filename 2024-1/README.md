# Assessment Alvaro Garzón - 2024-1
Como dueño del banco quiero que cualquier cliente pueda iniciar su registro y un comercial en base a su perfil le pueda acompañar en la validación de los productos y adquisición sobre estos
## Lógica del dominio
¿Cuál sería la lógica del dominio para este problema? Es realizar transacciones, obtener productos financieros y llevar un control sobre estos, hay muchas más, pero el dominio se basa en productos financieros
## Casos de uso
- Obtener productos financieros
- Validaciones para qué productos un cliente puede ser apto
## Reglas de negocio
- Es una startup en crecimiento, de la cuál se valora mucho la mejora continua
- El enfoque es encontrar los productos financieros adecuados para cada cliente
- Cuenta con 6 productos para los clientes, cada producto tiene sus requerimientos
## Paso a seguir o flujo básido de trabajo
- Los servicios se ofrecen al cliente
- Los servicios se registran en una tabla
- Los clientes se registran con código, nombre y contraseña (Validar fallas de seguridad)
- Los comerciales pueden ingresar los siguientes datos: Ingresos, ciudad y edad
## Paso a seguir del software cliente -> servicio -> financiero
- Comercial obtiene una lista con los clientes y los productos que podrían ajustarse a cada cliente
- El sistema determina el servicio más adecuado, se analiza de forma instantánea y su proceso debe generar unas recomendaciones para el cliente.