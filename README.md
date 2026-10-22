# مصاحف المغرب (Masahif al-Maghrib)

<div align="center">

**دليل مصوَّر تفاعلي للمصاحف المخطوطة المؤرَّخة في عصور المغرب · من الأدارسة إلى العلويين**

[![Live Platform](https://img.shields.io/badge/Website-masahif--al--maghrib.com-10b981?style=for-the-badge&logo=google-chrome&logoColor=white)](https://masahif-al-maghrib.com/)
[![License](https://img.shields.io/badge/Data%20License-Public%20Domain%20%2F%20Open-blue?style=for-the-badge)](https://masahif-al-maghrib.com/)
[![Bilingual Promo Video](https://img.shields.io/badge/Promo%20Video-Arabic%20%26%20English-e11d48?style=for-the-badge&logo=youtube&logoColor=white)](https://masahif-al-maghrib.com/)
[![PageSpeed](https://img.shields.io/badge/PageSpeed-100%2F100-success?style=for-the-badge&logo=lighthouse&logoColor=white)](https://masahif-al-maghrib.com/)

[**🌐 زيارة المنصة المباشرة (masahif-al-maghrib.com)**](https://masahif-al-maghrib.com/) · [**English Overview**](#english-summary--architecture)

</div>

---

<div dir="rtl" style="text-align: start;">

دليل بصري وتاريخي موثق للمصاحف المؤرَّخة المعروفة الصاحب في عصور المغرب الحضارية السبعة، يجمع بين التحقيق المخطوطاتي الدقيق، والتحليل الخطي المقارن، والعرض البصري الرقمي فائق الدقة.

### صفحات العصور الحضارية

| العصر الحضاري | الفترة والتاريخ | الرابط المباشر |
|---|---|---|
| **الأدارسة** | 172هـ – 375هـ | [masahif-al-maghrib.com/adarisa/](https://masahif-al-maghrib.com/adarisa/) |
| **المرابطون** | 448هـ – 541هـ | [masahif-al-maghrib.com/murabitun/](https://masahif-al-maghrib.com/murabitun/) |
| **الموحدون** | 515هـ – 668هـ | [masahif-al-maghrib.com/muwahhidun/](https://masahif-al-maghrib.com/muwahhidun/) |
| **بنو مرين** | 642هـ – 869هـ | [masahif-al-maghrib.com/marini/](https://masahif-al-maghrib.com/marini/) |
| **الوطاسيون** | 876هـ – 961هـ | [masahif-al-maghrib.com/wattasi/](https://masahif-al-maghrib.com/wattasi/) |
| **السعديون** | 915هـ – 1069هـ | [masahif-al-maghrib.com/saadi/](https://masahif-al-maghrib.com/saadi/) |
| **العلويون** | 1076هـ – إلى العصر الحاضر | [masahif-al-maghrib.com/alawi/](https://masahif-al-maghrib.com/alawi/) |

---

## 📜 شرط الدليل وضوابط التوثيق

تدخل القائمة الأولى في كل عصر المصاحفُ التي اجتمع فيها شرطان تاريخيان حاسمان:
1. **تاريخ نسخ صريح**: مقيد ومثبت بنص الخاتمة الأصلية أو نص الوقفية المقترنة بزمن النسخ.
2. **اسم صاحب المصحف**: أي ناسخه أو مَن كُتب له المصحف، مع اشتراط نسخه داخل بلاد تلك الدولة في المغرب الأقصى.

وفي كل صفحة قسمان تكميليان:
- **مصاحف ذكرتها المصادر وضاعت أصولها**.
- **مصاحف مشهورة تقف على حافة الشرط** مع بيان علة التحفظ.

</div>

---

<a name="english-summary--architecture"></a>
## 🏗️ Architecture & Engineering System

```mermaid
flowchart TB
    subgraph DataSources ["📚 Scholarly Data & High-Res Archival Imagery"]
        MssData["Codico-historical Catalog\nExplicit colophons, scribes, patron, dimensions, provenance"]
        PlatesDir["High-Res Plates & Folios\nSurah headings, colophons, script close-ups"]
    end

    subgraph StaticCore ["⚡ Dynamic Modular Presentation Engine"]
        SiteJS["assets/site.js (Shared Viewer Core)\n- Chronological Timeline & Dynamic Table\n- Filter & Sort Matrix (Year, Scribe, Script Style)\n- High-Res Modal Zoom Viewer\n- Fullscreen Presentation Mode"]
        SiteCSS["assets/site.css (Design System)\n- Period-specific Chromatic Palettes\n- Strict RTL / Bidi Directionality Layout\n- Fluid Vector Typography (Amiri, Tajawal)"]
        DynastyData["<dynasty>/data.js\nStructured JSON-LD schema & manuscript metadata"]
    end

    subgraph ClientDelivery ["🌐 Client Viewport (masahif-al-maghrib.com)"]
        IndexPage["index.html\nGeneral Chronological Index & Dynasty Selector"]
        DynastyPages["<dynasty>/index.html\nDynasty Deep Dives (Adarisa, Murabitun, Muwahhidun, etc.)"]
        EnglishMirror["en/<dynasty>/index.html\nBilingual English Presentation"]
    end

    MssData --> DynastyData
    PlatesDir --> DynastyPages
    DynastyData --> SiteJS
    SiteJS --> IndexPage
    SiteJS --> DynastyPages
    SiteCSS --> IndexPage
    SiteCSS --> DynastyPages
    DynastyPages --> EnglishMirror
```

---

## 🔄 Sequence Diagram: High-Fidelity Plate Exploration Lifecycle

```mermaid
sequenceDiagram
    autonumber
    actor Visitor as 🔍 Researcher / Visitor
    participant Browser as 🌐 Client Browser
    participant Engine as ⚙️ site.js Engine
    participant Data as 🗄️ dynasty/data.js
    participant Modal as 🖼️ High-Res Plate Zoom

    Visitor->>Browser: Select historical dynasty & filter by century / script
    Browser->>Engine: Initialize view with URL parameters
    Engine->>Data: Parse codicological records & verified dates
    Engine->>Browser: Render chronological cards & interactive timeline
    Visitor->>Browser: Click specific manuscript plate (e.g., Al-Muwahhidun Colophon)
    Browser->>Modal: Open dedicated high-resolution inspection modal
    Modal->>Modal: Apply pinch-to-zoom / vector pan & load archival citations
    Visitor->>Modal: Inspect scribal calligraphy & colophon typography
    Modal-->>Visitor: Display verified repository, scribe, and historical metadata
```

---

## 🎬 Bilingual Promo Video Production & Multi-Agent Media Pipeline

As part of the platform's public launch, an automated **multi-agent media and video production pipeline** was orchestrated using **Claude Code** and generative media tools:

- **Bilingual Narrative Scripting**: Authored high-fidelity Arabic narration and synchronized English subtitles capturing the artistic evolution of the Moroccan Maghrebi scripts (Mabsut, Mujawhar, Thuluth Maghrebi).
- **Cinematic Pacing & Motion Graphics**: Orchestrated keyframe timing, fluid camera transitions across manuscript plates, and ambient acoustic mastering.
- **Multi-Format Export**: Rendered 16:9 widescreen master editions and 9:16 vertical video reels for cross-platform cultural dissemination.

---

## 📸 Visual Plates, Reader Interface & Video Snapshot Showcase

> [!NOTE]
> Below are placeholder cards for high-resolution manuscript plates, the interactive reader UI, and promotional video releases.

<div align="center">

| 📜 Historical Manuscript Plate Viewer | ⏳ Interactive Chronological Timeline |
|:---:|:---:|
| ![Manuscript Plate Placeholder](https://placehold.co/500x700/1e293b/38bdf8?text=High-Res+Colophon+Plate+Viewer) <br> *Deep-zoom inspection of historical scribal colophons* | ![Timeline Placeholder](https://placehold.co/500x700/1e293b/10b981?text=Dynasty+Chronological+Timeline) <br> *Cross-dynasty temporal sorting & verified dating* |

</div>

<br>

<div align="center">

| 🎬 Bilingual Promo Video Cut (Arabic / English) | 📱 Responsive Mobile Typography & Layout |
|:---:|:---:|
| ![Video Reel Placeholder](https://placehold.co/500x700/1e293b/e11d48?text=Promo+Video+Production+Cut) <br> *Cinematic multi-agent video release showcasing manuscript art* | ![Mobile Reader Placeholder](https://placehold.co/500x700/1e293b/f59e0b?text=Mobile+RTL+Reader) <br> *100/100 PageSpeed with bespoke Maghrebi typographic stack* |

</div>

---

<div dir="rtl" style="text-align: start;">

## ⚖️ حقوق الصور والمصادر

أكثر الصور من مكتبات ومتاحف عالمية تتيحها ملكاً عاماً أو بترخيص ثقافي مفتوح (المكتبة الوطنية للمملكة المغربية، الخزانة الحسنية بالرباط، خزانة القرويين بفاس، ومكتبات باريس وإسكوريال وإسطنبول). وتُذكر إحالة ومصدر كل مصحف تحته نصاً وتفصيلاً.

---

**إعداد وتحقيق:** إبراهيم حسني إدريسي، خطاط وباحث في الخطوط المغربية والمصاحف من فاس · [واتساب](https://wa.me/212681769161)  
**التصميم والهندسة الرقمية:** [خالد بنجلون](https://benjelloun.dev) (Khalid Benjelloun)

</div>
