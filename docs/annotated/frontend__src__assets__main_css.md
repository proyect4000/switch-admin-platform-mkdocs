# frontend/src/assets/main.css

## Propósito

Archivo del proyecto ubicado en `frontend/src/assets/main.css`.

## Código fuente

```css
:root {
  --bg: #f4f7fb;
  --card: #ffffff;
  --primary: #2563eb;
  --primary-dark: #1d4ed8;
  --danger: #dc2626;
  --success: #16a34a;
  --text: #1f2937;
  --border: #dbe2ea;
  --sidebar: #0f172a;
  --sidebar-hover: #1e293b;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: Arial, Helvetica, sans-serif; background: var(--bg); color: var(--text); }
button { border: none; cursor: pointer; border-radius: 8px; padding: 10px 14px; background: var(--primary); color: white; font-size: 14px; }
button:hover { background: var(--primary-dark); }
button.danger { background: var(--danger); }
button.success { background: var(--success); }
button.secondary { background: #64748b; }
input, select, textarea { width: 100%; padding: 10px 12px; border: 1px solid var(--border); border-radius: 8px; background: white; font-size: 14px; }
.page-layout { display: flex; min-height: 100vh; }
.page-content { flex: 1; padding: 24px; }
.page-title { font-size: 24px; font-weight: bold; margin-bottom: 20px; }
.card { background: var(--card); border-radius: 14px; border: 1px solid var(--border); padding: 18px; box-shadow: 0 8px 24px rgba(15,23,42,.05); }
.grid { display: grid; gap: 16px; }
.grid-2 { grid-template-columns: repeat(2,1fr); }
.grid-3 { grid-template-columns: repeat(3,1fr); }
.table-wrapper { overflow: auto; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 12px; border-bottom: 1px solid var(--border); text-align: left; font-size: 14px; }
.toolbar { display: flex; gap: 10px; margin-bottom: 16px; flex-wrap: wrap; }
.modal-backdrop { position: fixed; inset: 0; background: rgba(0,0,0,.45); display: flex; align-items: center; justify-content: center; z-index: 999; }
.modal { width: 92%; max-width: 900px; background: white; border-radius: 14px; padding: 18px; }
.modal.large { max-width: 1200px; }
.modal-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; }
.form-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 14px; }
.form-actions { display: flex; justify-content: flex-end; gap: 10px; margin-top: 18px; }
.login-page { min-height: 100vh; display: flex; justify-content: center; align-items: center; }
.login-card { width: 380px; background: white; padding: 24px; border-radius: 16px; border: 1px solid var(--border); box-shadow: 0 12px 30px rgba(15,23,42,.08); }
.badge { display: inline-block; padding: 5px 10px; border-radius: 999px; font-size: 12px; font-weight: bold; }
.badge.online { background: #dcfce7; color: #166534; }
.badge.offline { background: #fee2e2; color: #991b1b; }
.badge.unknown { background: #e5e7eb; color: #374151; }
@media (max-width: 900px) { .grid-2, .grid-3, .form-grid { grid-template-columns: 1fr; } .page-layout { flex-direction: column; } }
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `:root {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 2 | `  --bg: #f4f7fb;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 3 | `  --card: #ffffff;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 4 | `  --primary: #2563eb;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 5 | `  --primary-dark: #1d4ed8;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 6 | `  --danger: #dc2626;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 7 | `  --success: #16a34a;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 8 | `  --text: #1f2937;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 9 | `  --border: #dbe2ea;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 10 | `  --sidebar: #0f172a;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 11 | `  --sidebar-hover: #1e293b;` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 12 | `}` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 13 | `* { box-sizing: border-box; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 14 | `body { margin: 0; font-family: Arial, Helvetica, sans-serif; background: var(--bg); color: var(--text); }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 15 | `button { border: none; cursor: pointer; border-radius: 8px; padding: 10px 14px; background: var(--primary); color: white; font-size: 14px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 16 | `button:hover { background: var(--primary-dark); }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 17 | `button.danger { background: var(--danger); }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 18 | `button.success { background: var(--success); }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 19 | `button.secondary { background: #64748b; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 20 | `input, select, textarea { width: 100%; padding: 10px 12px; border: 1px solid var(--border); border-radius: 8px; background: white; font-s...` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `.page-layout { display: flex; min-height: 100vh; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 22 | `.page-content { flex: 1; padding: 24px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 23 | `.page-title { font-size: 24px; font-weight: bold; margin-bottom: 20px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 24 | `.card { background: var(--card); border-radius: 14px; border: 1px solid var(--border); padding: 18px; box-shadow: 0 8px 24px rgba(15,23,4...` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 25 | `.grid { display: grid; gap: 16px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 26 | `.grid-2 { grid-template-columns: repeat(2,1fr); }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `.grid-3 { grid-template-columns: repeat(3,1fr); }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 28 | `.table-wrapper { overflow: auto; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 29 | `table { width: 100%; border-collapse: collapse; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 30 | `th, td { padding: 12px; border-bottom: 1px solid var(--border); text-align: left; font-size: 14px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 31 | `.toolbar { display: flex; gap: 10px; margin-bottom: 16px; flex-wrap: wrap; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 32 | `.modal-backdrop { position: fixed; inset: 0; background: rgba(0,0,0,.45); display: flex; align-items: center; justify-content: center; z-...` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 33 | `.modal { width: 92%; max-width: 900px; background: white; border-radius: 14px; padding: 18px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 34 | `.modal.large { max-width: 1200px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 35 | `.modal-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 36 | `.form-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 14px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 37 | `.form-actions { display: flex; justify-content: flex-end; gap: 10px; margin-top: 18px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 38 | `.login-page { min-height: 100vh; display: flex; justify-content: center; align-items: center; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 39 | `.login-card { width: 380px; background: white; padding: 24px; border-radius: 16px; border: 1px solid var(--border); box-shadow: 0 12px 30...` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 40 | `.badge { display: inline-block; padding: 5px 10px; border-radius: 999px; font-size: 12px; font-weight: bold; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 41 | `.badge.online { background: #dcfce7; color: #166534; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 42 | `.badge.offline { background: #fee2e2; color: #991b1b; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 43 | `.badge.unknown { background: #e5e7eb; color: #374151; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 44 | `@media (max-width: 900px) { .grid-2, .grid-3, .form-grid { grid-template-columns: 1fr; } .page-layout { flex-direction: column; } }` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |