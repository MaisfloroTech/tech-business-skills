# Examples by role

All data is fictional. Each output uses only facts from its input, plus arithmetic and plain-language rewording. Anything missing is an UPPERCASE placeholder.

Read the example closest to the user's role.

---

## 👩‍💻 Backend developer → 🟢 HIGHLIGHT

Input: *"I'm a backend developer. On Oct 9 we released the new search filters in the web store, together with Product and Support. Search-related support tickets dropped from 120 to 45 per month."*

```
🟢 [HIGHLIGHT] Better search for customers: On Oct 9, the backend team released new search filters in our web store, together with the Product and Support teams. Since then, support tickets about search dropped from 120 to 45 per month (−63%), so customers find products with less help.
Owner: Backend team (ENTER_OWNER)
```

---

## 🛡️ Cybersecurity → 🟠 RISK – HIGH

Input: *"My role is security analyst. 3 critical vulnerabilities on the customer portal have been open for 30 days; our policy is 15. The patch needs a 1-hour downtime that Product hasn't approved yet. SOC 2 audit is on Nov 20."*

```
🟠 [RISK – HIGH] Customer portal security: three critical security gaps on our customer portal have been open for 30 days, twice our 15-day policy, and could be flagged in the SOC 2 external security audit on Nov 20. Fixing them needs a 1-hour planned downtime of the portal.
ASK: Product team to approve the 1-hour maintenance window by ENTER_DATE.
Owner: Security team (ENTER_OWNER)
```

---

## 📊 Data engineer → 🔴 LOWLIGHT

Input: *"I'm a data engineer. On Oct 6 the daily sales pipeline failed and the sales dashboard was 2 days out of date; the commercial team built the weekly forecast with old data. A source system changed its schema without notice. We added schema checks and alerts."*

```
🔴 [LOWLIGHT] Data availability for decisions: On Oct 6, our daily sales data stopped updating, so the sales dashboard was 2 days out of date and the commercial team built the weekly forecast with old data. A source system changed its data format without notice; the data engineering team added automatic format checks and alerts.
Owner: Data Engineering team (ENTER_OWNER)
```

---

## 📊 Data analyst / BI → 🟢 HIGHLIGHT (Spanish)

Input: *"Soy analista de BI. El 2 de octubre publicamos el tablero automático de cierre mensual para Finanzas. Antes armaban el reporte a mano en 5 días, en el cierre de septiembre les tomó 1 día."*

```
🟢 [HIGHLIGHT] Cierre mensual más rápido para Finanzas: El 2 de octubre, el equipo de BI publicó un tablero automático de cierre mensual para Finanzas, que antes armaba el reporte a mano. En el cierre de septiembre, el reporte pasó de 5 días a 1 (−80%), liberando 4 días de trabajo del equipo de Finanzas cada mes.
Responsable: Equipo de BI (INGRESA_RESPONSABLE)
```
