# programmieren_2_aufgabe_1

# Leistungskurve

> Kurze Beschreibung des Projekts – was macht es und warum?

---

## Inhaltsverzeichnis

- [Über das Projekt]
- [Voraussetzungen]
- [Installation]
- [Verwendung]
- [Projektstruktur]
- [Abhängigkeiten]
- [Lizenz]
- [Autor]

---

## Über das Projekt

Es werden Leistungsdaten analysiert und anschließend wird eine Leistungskurve ausgegeben die zeigt wie lange eine Testperson eine gewisse Leistung beibehalten kann.


---

## Voraussetzungen

- Python >= 3.13
- uv 
- Git

---

## Installation

```bash
uv Installation: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# Repository klonen
git clone https://github.com/dein-user/dein-repo.git
cd dein-repo

# Abhängigkeiten installieren
uv install
```

---

## Verwendung

```bash
# Programm starten
uv run python main.py
```

---

## Projektstruktur

```
dein-repo/
├── figures/          # Gespeicherte Plots
├── main.py           # Hauptprogramm
├── load_data.py      # Daten laden
├── sort.py           # Sortieralgorithmen
├── pyproject.toml    # PDM Projektkonfiguration
├── uv.lock          # Lockfile
├── .gitignore
└── README.md
```

---

## Abhängigkeiten

| Paket | Version | Zweck |
|-------|---------|-------|
| numpy | >= 1.x | Numerische Berechnungen |
| matplotlib | >= 3.x | Plotting |

Alle Abhängigkeiten sind in `pyproject.toml` definiert.

---

## Lizenz

No License

---

## Autor

**Dein Name**
- GitHub: [@dein-user](https://github.com/dein-user)