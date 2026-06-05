# Contribuyendo a los Proyectos de A&C

¡Gracias por tu interés en contribuir a los repositorios de **A&C**! 

Nuestra filosofía de trabajo se basa en la **cero improvisación** y en una ejecución técnica impecable. Para mantener nuestros altos estándares de calidad arquitectónica (MACH, API-first, Cloud-native) y seguridad (DevSecOps), te pedimos que sigas estas pautas al contribuir en cualquier proyecto de la organización.

## 1. Filosofía de Arquitectura (Cero Deuda Técnica)

Todo código aportado debe alinearse con nuestros principios de **Enterprise Standards**:
- **Agnóstico y Modular**: Privilegiamos la arquitectura basada en microservicios y soluciones escalables.
- **Calidad Predictible**: Todo cambio debe estar respaldado por pruebas unitarias/de integración automatizadas. No consideramos un trabajo "Terminado" (Definition of Done) hasta que supera los umbrales de validación y seguridad.
- **Eficiencia**: En A&C consideramos el tiempo como una variable crítica. Evita soluciones "temporales" que incrementen la deuda técnica.

## 2. Proceso de Contribución (A&C Agile Delivery Framework)

1. **Issues Primero**: Antes de crear un Pull Request (PR) masivo, abre un Issue para discutir la arquitectura y el enfoque del cambio.
2. **Branching Model**: Utilizamos una estrategia estandarizada. 
   - `feature/nombre-de-funcionalidad` para nuevos desarrollos.
   - `bugfix/descripcion-del-bug` para resolución de errores.
   - `hotfix/incidencia-critica` para parches urgentes en producción.
3. **Commits Semánticos**: Los mensajes de commit deben ser descriptivos (ej. `feat: add AI governance module`, `fix: resolve auth race condition`).
4. **Revisión por Pares (Peer Review)**: Todo PR debe ser revisado y aprobado por al menos un arquitecto o líder técnico del repositorio antes de ser integrado.

## 3. Seguridad por Diseño (DevSecOps)

- **Cero Credenciales**: NUNCA confirmes contraseñas, secretos, tokens o claves de API en el código fuente.
- **Gobernanza de IA**: Si tu contribución involucra el uso de modelos de Inteligencia Artificial o prompts automatizados, asegúrate de cumplir con la *Política Maestra de Seguridad de la Información (PMSI)* de A&C.
- **Análisis de Vulnerabilidades**: El código será evaluado por nuestras herramientas automatizadas de CI/CD. Asegúrate de corregir cualquier hallazgo de seguridad (SAST/DAST) antes de solicitar la revisión.

## 4. Estructura de Entregables (Regla del 3)

Nuestra comunicación técnica es directa, sin ruido visual y altamente ejecutiva. Cuando documentes PRs o Issues:
1. **El Contexto**: ¿Qué problema se resuelve?
2. **La Solución**: ¿Cómo se abordó técnicamente?
3. **El Impacto/Acción**: ¿Qué dependencias afecta y cómo validarlo?

¡Agradecemos profundamente tu talento hiper-especializado y tu compromiso con la excelencia!