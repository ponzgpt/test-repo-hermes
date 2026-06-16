# Hermes-PKM-Toolkit

Libreria modular de protocolos cognitivos para agentes autonomos que operan sobre bovedas Markdown locales.

Hermes-PKM-Toolkit no reemplaza a Hermes. Hermes es el agente/runtime. Este repositorio aporta la capa minima para que Hermes, Moltbot u otro agente local pueda trabajar sobre una boveda Markdown/Obsidian usando protocolos cargables: Johnny.Decimal, GTD y PARA.

La base de datos es el sistema de archivos local. Git es el log de auditoria. Markdown es la interfaz.

## Filosofia a la carta

Carga solo lo que necesites:

| Caso de uso | Skills |
|---|---|
| Operar una boveda Markdown local con MCP | `00_CORE/base_skill.md` |
| Estructura numerica estable | `01_JOHNNY_DECIMAL/AGENT_jd_skill.md` |
| Captura rapida y triaje de tareas | `02_GTD/AGENT_gtd_skill.md` |
| Gestion accionable de proyectos/areas/recursos | `03_PARA/AGENT_para_skill.md` |

Las skills son Markdown deliberadamente simples. Se cargan como system prompt overrides, no como logica hardcodeada en Python.

## Estructura

```text
Hermes-PKM-Toolkit/
  00_CORE/
    hermes_mcp_server.py
    delta_tracker.py
    base_skill.md
  01_JOHNNY_DECIMAL/
    HUMANS_jd_guide.md
    AGENT_jd_skill.md
  02_GTD/
    HUMANS_gtd_guide.md
    AGENT_gtd_skill.md
  03_PARA/
    HUMANS_para_guide.md
    AGENT_para_skill.md
```

## Setup MCP

Requisitos:

- Python 3.10+
- SDK oficial de MCP para Python

Instala el SDK MCP en tu entorno local:

```bash
python3 -m pip install mcp
```

Define la raiz de tu boveda Markdown:

```bash
export HERMES_VAULT_ROOT="$HOME/Documents/MyVault"
```

Arranca el servidor MCP:

```bash
python3 00_CORE/hermes_mcp_server.py
```

El servidor expone estas tools:

- `list_resources`: lista archivos `.md` de la boveda.
- `read_resource`: lee un archivo `.md`.
- `append_to_file`: anade contenido a un archivo `.md`.
- `create_file`: crea un archivo `.md` nuevo sin sobrescribir.

Todas las rutas son relativas a `HERMES_VAULT_ROOT`. El servidor bloquea path traversal y rechaza archivos que no sean Markdown.

## Delta tracking

Para que el agente procese solo notas modificadas desde la ultima ejecucion:

```bash
python3 00_CORE/delta_tracker.py "$HERMES_VAULT_ROOT"
```

Esto crea o actualiza:

```text
<vault>/.hermes/delta_tracker.json
```

El tracker compara `sha256`, `mtime_ns` y `size` de cada `.md`. La salida JSON incluye:

- `added`
- `modified`
- `deleted`
- `unchanged_count`
- `state_path`

## Carga dinamica de skills

Flujo recomendado:

1. Carga `00_CORE/base_skill.md` como system prompt base.
2. Arranca `00_CORE/hermes_mcp_server.py` apuntando a la boveda.
3. Ejecuta `00_CORE/delta_tracker.py` al inicio de cada sesion.
4. Carga una o mas skills:
   - `01_JOHNNY_DECIMAL/AGENT_jd_skill.md`
   - `02_GTD/AGENT_gtd_skill.md`
   - `03_PARA/AGENT_para_skill.md`
5. El agente usa las tools MCP para leer, crear y anadir contenido Markdown.
6. El agente propone planes antes de mover, renombrar o archivar.

## Principios de seguridad

- No hay SQL ni NoSQL.
- No hay API REST.
- No hay estado oculto fuera de la boveda, salvo `.hermes/delta_tracker.json`.
- No se sobrescriben archivos desde `create_file`.
- No se borran archivos.
- No se mueven archivos en el core MCP actual.
- Toda operacion destructiva futura debe exigir confirmacion explicita.

## Estado

Toolkit temprano y deliberadamente pequeno para el ecosistema Machines Do It Better. La superficie estable actual es: MCP local, delta tracking, y skills Markdown modulares.
