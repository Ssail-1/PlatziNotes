
Va, aquí es donde todo hace clic 🔥
Composición es la que realmente diferencia a alguien que **entiende diseño** vs alguien que solo “usa clases”.

---

### 4. Composición



## 🧠 Dirección (para que lo conectes con lo anterior)

```text
Casa ◆---- Habitación
```

👉 El rombo sólido (**◆**) está en `Casa`
👉 `Habitación` depende completamente de `Casa`

---

## 💻 Ejemplo en código

```java
class Habitacion {
}

class Casa {
    private List<Habitacion> habitaciones = new ArrayList<>();

    public Casa() {
        habitaciones.add(new Habitacion());
        habitaciones.add(new Habitacion());
    }
}
```

👉 Aquí:

* `Casa` crea las habitaciones
* `Casa` controla su vida
* ❌ No existen fuera de ella

---

## 🔥 Diferencia final (esto te deja todo claro)

| Relación    | ¿Puede vivir sin el todo? |
| ----------- | ------------------------- |
| Asociación  | ✔️ Sí                     |
| Agregación  | ✔️ Sí                     |
| Composición | ❌ No                      |

---

Si quieres en el siguiente paso hacemos un **mini resumen visual de las 4 relaciones juntas** (tipo tabla comparativa), eso te dejaría un bloque súper sólido en tu repo 🚀
