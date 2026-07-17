<!--
  Mohamed Hekal — GitHub Profile
  Design: systems / architecture motif · teal × amber · bridge metaphor
-->

<p align="center">
  <img src="./assets/banner.svg" alt="Mohamed Hekal — Senior Backend, Laravel Architect, ERP & SaaS Builder" width="100%" />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=mohamedhekal&label=profile+views&color=0d9488&style=flat-square" alt="Profile views" />
  &nbsp;
  <img src="https://img.shields.io/badge/based_in-Egypt%20·%20MENA-0f172a?style=flat-square&labelColor=134e4a&color=f59e0b" alt="Based in Egypt MENA" />
  &nbsp;
  <img src="https://img.shields.io/badge/open_to-collaborations-0f172a?style=flat-square&labelColor=134e4a&color=2dd4bf" alt="Open to collaborations" />
</p>

<p align="center">
  <a href="https://linkedin.com/in/mohekal"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  &nbsp;
  <a href="mailto:mohamed.k.hekal@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  &nbsp;
  <a href="https://wa.me/201101013284"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp" /></a>
  &nbsp;
  <a href="https://github.com/mohamedhekal/oss-portfolio"><img src="https://img.shields.io/badge/OSS_Portfolio-0F172A?style=for-the-badge&logo=github&logoColor=2dd4bf" alt="OSS Portfolio" /></a>
</p>

---

<pre align="center">
┌─────────────────────────────────────────────────────────────┐
│  $ whoami                                                   │
│  > mohamed hekal · systems builder since 2014               │
│                                                             │
│  $ cat mission.txt                                          │
│  > ship production Laravel packages for SaaS, ERP,          │
│    shipping, multi-tenancy, and live classrooms             │
│                                                             │
│  $ echo $MANTRA                                             │
│  > packages — not tutorial demos                            │
└─────────────────────────────────────────────────────────────┘
</pre>

I started in high school (2014), went deep into software & infrastructure by 2016, and have since designed ERP platforms, led remote teams, and shipped client systems across Egypt, MENA, and beyond.

After launching a startup and weathering hard personal losses in 2024, I came back focused: **clean architecture, concurrency-safe backends, and open-source libraries other teams can actually adopt.**

---

## ▸ What I design for

<table>
<tr>
<td width="50%">

**Enterprise & SaaS backends**  
Multi-tenancy, feature flags, audit trails, idempotent APIs, webhook reliability, and order/inventory lifecycles.

</td>
<td width="50%">

**Integrations that survive production**  
Retries, circuit breakers, signed webhooks, carrier APIs, payment gateways, and third-party chaos — handled deliberately.

</td>
</tr>
<tr>
<td>

**Shipping & logistics SDKs**  
Unified create / track / label / return across Egypt, MENA, Turkey, and global carriers.

</td>
<td>

**EdTech realtime stacks**  
Live classrooms: sessions, WebRTC providers, collaborative whiteboards, Vue UI, and embeddable web components.

</td>
</tr>
</table>

---

## ▸ Featured systems

### ShipBridge — unified Laravel shipping

> One API. Many carriers. Normalized statuses.

[![shipbridge](https://img.shields.io/badge/core-shipbridge-0f172a?style=flat-square&labelColor=134e4a&color=2dd4bf)](https://github.com/mohamedhekal/shipbridge)
[![packagist](https://img.shields.io/packagist/v/mohamedhekal/shipbridge?style=flat-square&label=packagist&color=f59e0b)](https://packagist.org/packages/mohamedhekal/shipbridge)

Drivers for **Bosta · Aramex · Mylerz · Turbo · J&T · SMSA · FedEx · UPS · DHL · Egypt Post · MNG · HepsiJet · Yurtiçi · Aras · Sürat · PTT**.

```php
$shipment = ShipBridge::driver('bosta')->createShipment($request);
$label    = ShipBridge::driver('bosta')->label($shipment->id);
$track    = ShipBridge::driver('bosta')->track($shipment->trackingNumber);
```

### ClassBridge — live classrooms for Laravel

> Embeddable sessions · LiveKit · whiteboard · Vue · web components

[![classbridge](https://img.shields.io/badge/core-classbridge-0f172a?style=flat-square&labelColor=134e4a&color=2dd4bf)](https://github.com/mohamedhekal/classbridge)
[![sdk](https://img.shields.io/badge/sdk-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://github.com/mohamedhekal/classbridge-sdk)
[![vue](https://img.shields.io/badge/UI-Vue_3-42B883?style=flat-square&logo=vuedotjs&logoColor=white)](https://github.com/mohamedhekal/classbridge-vue)

### Laravel package constellation

| Package | Solves |
|:--------|:-------|
| [`tenantforge`](https://github.com/mohamedhekal/tenantforge) | Shared-DB multi-tenancy · domains · memberships · API keys |
| [`stockpulse`](https://github.com/mohamedhekal/stockpulse) | Inventory reserve / commit / release / transfer |
| [`ledgercore`](https://github.com/mohamedhekal/ledgercore) | Double-entry ledger for ERP & fintech |
| [`ordermachine`](https://github.com/mohamedhekal/ordermachine) | Order lifecycle state machine |
| [`flagdeck`](https://github.com/mohamedhekal/flagdeck) | Feature flags · rollouts · tenant targeting |
| [`hookrelay`](https://github.com/mohamedhekal/hookrelay) | Outbound webhooks + HMAC inbound ingest |
| [`integrator`](https://github.com/mohamedhekal/integrator) | Resilient HTTP · retry · rate-limit · circuit breaker |
| [`oncegate`](https://github.com/mohamedhekal/oncegate) | Stripe-style Idempotency-Key middleware |
| [`guardrail`](https://github.com/mohamedhekal/guardrail) | Roles · abilities · audited impersonation |
| [`testharness`](https://github.com/mohamedhekal/testharness) | Pest / Laravel testing utilities |

Full index → **[oss-portfolio](https://github.com/mohamedhekal/oss-portfolio)**

---

## ▸ Stack

<p align="center">
  <img src="https://img.shields.io/badge/PHP-8.2+-777BB4?style=for-the-badge&logo=php&logoColor=white" alt="PHP" />
  <img src="https://img.shields.io/badge/Laravel-11%2F12-FF2D20?style=for-the-badge&logo=laravel&logoColor=white" alt="Laravel" />
  <img src="https://img.shields.io/badge/Vue.js-3-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white" alt="Vue" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS" />
  <img src="https://img.shields.io/badge/Pest-18B69B?style=for-the-badge&logo=php&logoColor=white" alt="Pest" />
</p>

Also comfortable with: **Python / Django · Solidity / Web3 · Networking & IT infrastructure · CI/CD**.

---

## ▸ Experience snapshot

```text
Freelance Full-Stack  ·  ERP · CRM · HMS
  → Laravel · Vue · PostgreSQL · client systems worldwide

Full-Stack Engineer   ·  Kzamiza Affiliate Platform (sole owner)
  → end-to-end product · admin / vendor / affiliate · AWS & Azure

Backend Developer     ·  Oracle Media
  → REST APIs · high-traffic backends · performance work

Earlier roots         ·  IT Specialist / Network Admin / Solutions Manager
  → infrastructure · cloud · multi-site networks
```

---

## ▸ Pulse

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=mohamedhekal&show_icons=true&theme=transparent&hide_border=true&title_color=2dd4bf&icon_color=f59e0b&text_color=94a3b8&bg_color=00000000" alt="GitHub stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=mohamedhekal&layout=compact&theme=transparent&hide_border=true&title_color=2dd4bf&text_color=94a3b8&bg_color=00000000" alt="Top languages" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=mohamedhekal&theme=dark&hide_border=true&background=00000000&ring=2dd4bf&fire=f59e0b&currStreakLabel=94a3b8" alt="GitHub streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=mohamedhekal&bg_color=071018&color=2dd4bf&line=f59e0b&point=e2e8f0&area=true&hide_border=true" alt="Contribution graph" width="100%" />
</p>

---

## ▸ Let’s build

Open to **Laravel package collabs**, **ERP / SaaS architecture**, **shipping integrations**, and **EdTech realtime** work.

<p align="center">
  <a href="https://wa.me/201101013284"><img src="https://img.shields.io/badge/☕_Coffee_chat_on_WhatsApp-0f172a?style=for-the-badge&labelColor=134e4a&color=2dd4bf" alt="WhatsApp coffee chat" /></a>
</p>

<p align="center">
  <sub>Got a problem? I’ve got the architecture.</sub>
</p>
