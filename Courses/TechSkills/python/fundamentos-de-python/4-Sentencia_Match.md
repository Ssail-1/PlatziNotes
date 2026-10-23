
# Selección de patrones **(`match`, `case`)**

## **¿Qué es `match`?**

`match` es una estructura de control introducida en **Python 3.10** que permite **comparar un valor contra diferentes patrones** y ejecutar código dependiendo de cuál coincida.

Se parece a `switch` en otros lenguajes, pero es **más flexible y potente**, porque puede comparar:

* valores simples
* múltiples valores
* estructuras de datos
* patrones complejos

---

## 🧱 **Estructura básica**

```python
match variable:
    case valor1:
        # código si coincide
    case valor2:
        # código si coincide
    case _:
        # caso por defecto
```

📌 **Importante**

* `match` evalúa la variable una sola vez.
* `case` define cada patrón posible.
* `_` funciona como **valor por defecto** (similar a `default` o `else`).
* Solo se ejecuta **el primer `case` que coincida**.

---

## ⚙️ **Ejemplo simple**

```python
dia = "lunes"

match dia:
    case "lunes":
        print("Inicio de semana")
    case "viernes":
        print("Casi fin de semana")
    case "sábado" | "domingo":
        print("Es fin de semana")
    case _:
        print("Día normal")
```

Salida:

```bash
Inicio de semana
```

---

## 🧩 **Múltiples valores en un mismo `case`**

Puedes usar `|` para comparar varios valores en una misma condición.

```python
numero = 2

match numero:
    case 1 | 2 | 3:
        print("Número pequeño")
    case 4 | 5 | 6:
        print("Número mediano")
    case _:
        print("Número grande")
```

---

## 🧠 **Capturar valores**

`match` también puede **capturar valores** directamente.

```python
comando = "saludar"

match comando:
    case "saludar":
        print("Hola usuario")
    case otro:
        print(f"Comando desconocido: {otro}")
```

Aquí `otro` captura cualquier valor que no coincida antes.

---

## 🧩 **Usar `match` con estructuras**

Una de las ventajas de `match` es que puede comparar estructuras completas.

```python
punto = (0, 0)

match punto:
    case (0, 0):
        print("Origen")
    case (0, y):
        print(f"Sobre eje Y en {y}")
    case (x, 0):
        print(f"Sobre eje X en {x}")
    case (x, y):
        print(f"Punto en ({x}, {y})")
```

Esto se llama **pattern matching**.

---

## 💬 **Comparación con Java y JavaScript**

| Concepto           | Python                  | Java                    | JavaScript              |
|--------------------|-------------------------|-------------------------|-------------------------|
| Estructura         | `match` / `case`        | `switch` / `case`       | `switch` / `case`       |
| Caso por defecto   | `case _:`               | `default:`              | `default:`              |
| Bloques            | Indentación             | Llaves `{}`             | Llaves `{}`             |
| `break` necesario  | ❌ No                    | ✅ Sí                    | ✅ Sí                    |
| Comparación múltiple | `case 1 \| 2 \| 3:`   | Varios `case` seguidos  | Varios `case` seguidos  |
| Pattern matching   | ✅ Sí                    | ⚠️ Limitado             | ❌ No                    |

### **Estructura en Java y JavaScript**

```java
switch (variable) {
    case 1:
        System.out.println("Uno");
        break;
    case 2:
        System.out.println("Dos");
        break;
    default:
        System.out.println("Otro valor");
}
```

```javascript
switch (variable) {
  case 1:
    console.log("Uno");
    break;
  case 2:
    console.log("Dos");
    break;
  default:
    console.log("Otro valor");
}
```

---

## 🧠 **Resumen**

* `match` es una estructura similar a `switch`.
* Introducida en **Python 3.10**.
* Permite comparar **patrones complejos**.
* `case` define cada patrón.
* `_` funciona como caso por defecto.
* Más limpio que múltiples `elif`.

---
