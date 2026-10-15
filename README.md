<div align="center">

# 🌉 tech-business-skills

## You did great work.<br>Leadership asked: *"so what?"*

Claude Skills that translate engineering into what the business cares about:<br>
**money, customers and risk.** In English or Spanish. No made-up numbers.

**[⚡ Install in 1 minute](#-install-in-claude)** · [🧰 See the skills](#-pick-a-skill)

</div>

<br>

| 😬 What you wrote | 🎯 What leadership reads |
|---|---|
| *Downsized main DB from 32 to 24 vCPU on Oct 11. 2h maintenance window. Saves ~USD 1,200/month.* | 🟢 **[HIGHLIGHT] Infrastructure optimization:** On Oct 11, the SRE team reduced our main database by 25%, saving USD 1,200/month (≈ USD 14,400/year) in a planned 2-hour maintenance window.<br>**Owner:** SRE team |

<p align="center"><b>Same work. Now the CFO gets it.</b></p>

---

## 🧰 Pick a skill

<table>
<tr>
<td width="33%" valign="top">

### 📄 Short report

One technical topic → one **3–4 line business update** with a traffic light, a number and an owner.

*Status updates, incidents, risks.*

**[See it in action →](tech-to-business-short-report/README.md)**

</td>
<td width="33%" valign="top">

### 🎯 SMART objectives

One technical initiative → one **quarterly objective** leadership can approve and track.

*OKRs, Q planning, goals.*

**[See it in action →](tech-to-business-smart-objectives/README.md)**

</td>
<td width="33%" valign="top">

### 📘 FAQ one-pager

Something new you built → one **friendly page of FAQs** as an editable Word document.

*Launches, onboarding, "how this works".*

**[See it in action →](tech-to-business-faq-one-pager/README.md)**

</td>
</tr>
</table>

More are on the way. Install once and every new skill arrives on its own. Missing one? [Open an issue](../../issues) 💬

---

## 👋 Always start with your role

> [!IMPORTANT]
> Begin every message with **"I'm a…"** / **"My role is…"**, or in Spanish **"Soy…"** / **"Mi rol es…"**
>
> *"**I'm a backend developer.** …"* · *"**My role is SRE lead.** …"* · *"**Soy líder de datos.** …"*

Your role decides which numbers matter: adoption and bugs for a developer, availability and cost for SRE, exposure for security. Say it first and you get your answer in one shot. You don't need to name the skill; Claude picks the right one.

---

## ⚡ Install in Claude

**💻 Web or desktop app (no code)**

1. Open **[Customize → Plugins](https://claude.ai/customize/plugins)** and click **Add → Add marketplace**.
2. Paste `MaisfloroTech/tech-business-skills`.
3. Find **Tech Business Skills** and click **Add**. ✅

**⌨️ Claude Code**

```
/plugin install tech-business-skills --marketplace MaisfloroTech/tech-business-skills
```

<details>
<summary>Other ways to install, and troubleshooting</summary>

<br>

**New skill not in the `/` menu?** Reload the app (Cmd/Ctrl + R) or open a new chat. Still missing? Turn the plugin off and on in **Customize → Plugins**. In Claude Code, run `claude update` if the command isn't recognized.

**One skill as a zip (web or desktop):** download it from the [latest release](../../releases/latest) without unzipping, then **Customize → Skills → Upload skill**. You'll repeat this for every update.

**One skill folder (Claude Code):**

```bash
git clone https://github.com/MaisfloroTech/tech-business-skills.git
mkdir -p ~/.claude/skills
cp -r tech-business-skills/tech-to-business-short-report ~/.claude/skills/
```

**Plans:** you need Pro, Max, Team or Enterprise. On Team and Enterprise an admin may need to allow marketplaces, and can install it for the whole organization.

</details>

---

## 🇪🇸 English or Spanish

Write in English, get English. Escríbele en español y te responde en español. You can also mix: *"háblame en español pero el reporte en inglés para mi jefe"*.

---

## 🛡️ The honesty promise

- 🚫 **Nothing invented.** No numbers, dates, limits or contacts you didn't give.
- 🕳️ **Gaps stay visible** as UPPERCASE placeholders (`ENTER_DATE`, `INGRESA_MONTO`) for you to fill in before sending.
- 🧮 **Math shown** for anything calculated.

An honest gap beats a polished answer that falls apart at the first question.

---

<div align="center">

**Teams:** click **Use this template** for a private copy with your own examples · **Contribute:** [CONTRIBUTING.md](CONTRIBUTING.md)

⭐ If this helped you sound more like business and less like a changelog, give it a star.

Made with ☕ by [@maisfloro.tech](https://www.maisfloro.com/)

</div>
