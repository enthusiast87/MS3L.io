---
layout: default
title: Research
---
{% assign bio   = site.data.research | where: "title", "Biorefinery"              | first %}
{% assign plas  = site.data.research | where: "title", "Plastic recycling"        | first %}
{% assign res   = site.data.research | where: "title", "Resource recovery"        | first %}
{% assign ene   = site.data.research | where: "title", "Energy-related applications" | first %}

<div class="page-wrap">
<div class="container research-page">

<div class="page-card">
  <h1>Research Themes</h1>
  <p>MS<sup>3</sup>L develops membrane-enabled separations for sustainable chemical processing,
  circular resource systems, and energy-related applications.</p>
</div>

<!-- ── Tab navigation ─────────────────────────────────── -->
<nav class="research-tab-nav" aria-label="Research themes">
  <button class="research-tab-btn active" data-tab="biorefinery">Biorefinery</button>
  <button class="research-tab-btn" data-tab="plastics">Plastic Recycling</button>
  <button class="research-tab-btn" data-tab="resource">Resource Recovery</button>
  <button class="research-tab-btn" data-tab="energy">Energy Applications</button>
</nav>

<!-- ══════════════════════════════════════════════════════
     TAB 1 — BIOREFINERY
     ══════════════════════════════════════════════════════ -->
<div class="research-tab-panel active" id="rtab-biorefinery">

  <p class="research-diagram-label">Process Diagrams — Membrane Principle &amp; Role</p>
  <div class="research-diagram-pair">

    <!-- Diagram 1: Diffusion Dialysis / MEM-IE -->
    <div class="research-diagram-box">
      <svg viewBox="0 0 265 195" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
        <rect width="265" height="195" fill="#f8fbff" rx="10"/>
        <!-- header -->
        <rect width="265" height="22" fill="#f1f5f9" rx="10"/><rect y="12" width="265" height="10" fill="#f1f5f9"/>
        <text x="10" y="15" font-size="9" font-weight="700" fill="#334155">Diffusion Dialysis / MEM-IE</text>
        <rect x="215" y="4" width="44" height="16" rx="8" fill="#dbeafe" stroke="#93c5fd" stroke-width="1"/>
        <text x="237" y="15" text-anchor="middle" font-size="8.5" font-weight="800" fill="#0050a4">Δc</text>
        <!-- feed -->
        <rect x="8" y="28" width="72" height="108" rx="7" fill="#dbeafe" stroke="#bfdbfe" stroke-width="1.2"/>
        <text x="44" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#1e40af">Feed</text>
        <circle cx="24" cy="65" r="9" fill="#93c5fd" stroke="#2563eb" stroke-width="1.2"/><text x="24" y="68" text-anchor="middle" font-size="7" font-weight="700" fill="#1e3a8a">A⁻</text>
        <circle cx="46" cy="76" r="9" fill="#93c5fd" stroke="#2563eb" stroke-width="1.2"/><text x="46" y="79" text-anchor="middle" font-size="7" font-weight="700" fill="#1e3a8a">A⁻</text>
        <circle cx="34" cy="92" r="7" fill="#fca5a5" stroke="#ef4444" stroke-width="1.2"/><text x="34" y="95" text-anchor="middle" font-size="6" font-weight="700" fill="#dc2626">Na⁺</text>
        <circle cx="57" cy="60" r="7" fill="#fca5a5" stroke="#ef4444" stroke-width="1.2"/><text x="57" y="63" text-anchor="middle" font-size="6" font-weight="700" fill="#dc2626">H⁺</text>
        <circle cx="57" cy="100" r="7" fill="#fca5a5" stroke="#ef4444" stroke-width="1.2"/><text x="57" y="103" text-anchor="middle" font-size="6" font-weight="700" fill="#dc2626">Na⁺</text>
        <!-- blocked indicator -->
        <line x1="66" y1="112" x2="74" y2="112" stroke="#ef4444" stroke-width="1.5"/>
        <line x1="67" y1="108" x2="73" y2="116" stroke="#ef4444" stroke-width="1.5"/>
        <!-- arrow to membrane -->
        <line x1="82" y1="82" x2="95" y2="82" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="95,78 102,82 95,86" fill="#94a3b8"/>
        <!-- AEM membrane -->
        <g transform="translate(103,26)">
          <rect width="28" height="112" rx="4" fill="#0050a4" fill-opacity="0.1" stroke="#0050a4" stroke-width="1.8"/>
          <circle cx="9" cy="10" r="4" fill="#0050a4" opacity="0.4"/><text x="9" y="13" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="20" cy="18" r="4" fill="#0050a4" opacity="0.4"/><text x="20" y="21" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="9" cy="32" r="4" fill="#0050a4" opacity="0.4"/><text x="9" y="35" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="20" cy="40" r="4" fill="#0050a4" opacity="0.4"/><text x="20" y="43" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="9" cy="54" r="4" fill="#0050a4" opacity="0.4"/><text x="9" y="57" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="20" cy="62" r="4" fill="#0050a4" opacity="0.4"/><text x="20" y="65" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="9" cy="76" r="4" fill="#0050a4" opacity="0.4"/><text x="9" y="79" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="20" cy="84" r="4" fill="#0050a4" opacity="0.4"/><text x="20" y="87" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="9" cy="98" r="4" fill="#0050a4" opacity="0.4"/><text x="9" y="101" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <circle cx="20" cy="106" r="4" fill="#0050a4" opacity="0.4"/><text x="20" y="109" text-anchor="middle" font-size="5.5" fill="white" font-weight="800">+</text>
          <text x="14" y="118" text-anchor="middle" font-size="7" font-weight="700" fill="#0050a4">AEM</text>
        </g>
        <!-- arrows out -->
        <line x1="133" y1="66" x2="146" y2="60" stroke="#22c55e" stroke-width="1.5"/>
        <polygon points="146,56 152,60 146,64" fill="#22c55e"/>
        <line x1="133" y1="96" x2="146" y2="102" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="146,98 152,102 146,106" fill="#94a3b8"/>
        <!-- permeate -->
        <rect x="154" y="28" width="100" height="50" rx="7" fill="#dcfce7" stroke="#86efac" stroke-width="1.2"/>
        <text x="204" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#166534">Permeate</text>
        <circle cx="174" cy="58" r="9" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="174" y="61" text-anchor="middle" font-size="7" font-weight="700" fill="#166534">A⁻</text>
        <circle cx="197" cy="52" r="9" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="197" y="55" text-anchor="middle" font-size="7" font-weight="700" fill="#166534">A⁻</text>
        <text x="240" y="68" text-anchor="middle" font-size="7" fill="#15803d">pure acid</text>
        <!-- retentate -->
        <rect x="154" y="86" width="100" height="50" rx="7" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
        <text x="204" y="100" text-anchor="middle" font-size="8" font-weight="700" fill="#475569">Retentate</text>
        <circle cx="174" cy="114" r="7" fill="#fca5a5" stroke="#ef4444" stroke-width="1.2"/><text x="174" y="117" text-anchor="middle" font-size="6" font-weight="700" fill="#dc2626">Na⁺</text>
        <circle cx="196" cy="108" r="7" fill="#fca5a5" stroke="#ef4444" stroke-width="1.2"/><text x="196" y="111" text-anchor="middle" font-size="6" font-weight="700" fill="#dc2626">H⁺</text>
        <text x="230" y="126" font-size="7" fill="#64748b">cation stream</text>
        <!-- dev -->
        <rect x="8" y="144" width="249" height="26" rx="6" fill="rgba(0,80,164,0.05)" stroke="#e2e8f0" stroke-width="1"/>
        <text x="16" y="156" font-size="7.5" font-weight="700" fill="#0050a4">→ Ion selectivity: monovalent vs. multivalent discrimination</text>
        <text x="16" y="168" font-size="7.5" fill="#64748b">→ CO₂ as benign base — simultaneous acid purification + mineralization</text>
      </svg>
    </div>

    <!-- Diagram 2: BMED -->
    <div class="research-diagram-box">
      <svg viewBox="0 0 265 195" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
        <rect width="265" height="195" fill="#f8fbff" rx="10"/>
        <rect width="265" height="22" fill="#f1f5f9" rx="10"/><rect y="12" width="265" height="10" fill="#f1f5f9"/>
        <text x="10" y="15" font-size="9" font-weight="700" fill="#334155">Bipolar Membrane Electrodialysis</text>
        <rect x="215" y="4" width="44" height="16" rx="8" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1"/>
        <text x="237" y="15" text-anchor="middle" font-size="8.5" font-weight="800" fill="#7c3aed">Δφ</text>
        <!-- feed -->
        <rect x="8" y="28" width="72" height="108" rx="7" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1.2"/>
        <text x="44" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#5b21b6">Feed</text>
        <circle cx="27" cy="65" r="11" fill="#c4b5fd" stroke="#7c3aed" stroke-width="1.2"/><text x="27" y="69" text-anchor="middle" font-size="6.5" font-weight="700" fill="#4c1d95">NaA</text>
        <circle cx="53" cy="78" r="11" fill="#c4b5fd" stroke="#7c3aed" stroke-width="1.2"/><text x="53" y="82" text-anchor="middle" font-size="6.5" font-weight="700" fill="#4c1d95">NaA</text>
        <circle cx="32" cy="98" r="11" fill="#c4b5fd" stroke="#7c3aed" stroke-width="1.2"/><text x="32" y="102" text-anchor="middle" font-size="6.5" font-weight="700" fill="#4c1d95">NaA</text>
        <text x="44" y="122" text-anchor="middle" font-size="7" fill="#6d28d9">salt feed</text>
        <!-- arrow -->
        <line x1="82" y1="82" x2="95" y2="82" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="95,78 102,82 95,86" fill="#94a3b8"/>
        <!-- BPM membrane -->
        <g transform="translate(103,26)">
          <rect y="0" width="28" height="56" rx="4" fill="#7c3aed" fill-opacity="0.12" stroke="#7c3aed" stroke-width="1.8"/>
          <rect y="56" width="28" height="56" rx="4" fill="#0050a4" fill-opacity="0.12" stroke="#0050a4" stroke-width="1.8"/>
          <text x="14" y="14" text-anchor="middle" font-size="6" font-weight="800" fill="#7c3aed">−</text>
          <text x="14" y="28" text-anchor="middle" font-size="6" font-weight="800" fill="#7c3aed">−</text>
          <text x="14" y="42" text-anchor="middle" font-size="6" font-weight="800" fill="#7c3aed">−</text>
          <line x1="0" y1="56" x2="28" y2="56" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>
          <text x="14" y="53" text-anchor="middle" font-size="4.5" fill="#ef4444" font-weight="700">H₂O split</text>
          <text x="14" y="70" text-anchor="middle" font-size="6" font-weight="800" fill="#0050a4">+</text>
          <text x="14" y="84" text-anchor="middle" font-size="6" font-weight="800" fill="#0050a4">+</text>
          <text x="14" y="98" text-anchor="middle" font-size="6" font-weight="800" fill="#0050a4">+</text>
          <text x="14" y="118" text-anchor="middle" font-size="7" font-weight="700" fill="#5b21b6">BPM</text>
        </g>
        <!-- arrows out -->
        <line x1="133" y1="66" x2="146" y2="60" stroke="#22c55e" stroke-width="1.5"/>
        <polygon points="146,56 152,60 146,64" fill="#22c55e"/>
        <line x1="133" y1="96" x2="146" y2="102" stroke="#3b82f6" stroke-width="1.5"/>
        <polygon points="146,98 152,102 146,106" fill="#3b82f6"/>
        <!-- permeate: acid -->
        <rect x="154" y="28" width="100" height="50" rx="7" fill="#dcfce7" stroke="#86efac" stroke-width="1.2"/>
        <text x="204" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#166534">Acid side</text>
        <circle cx="174" cy="59" r="10" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="174" y="63" text-anchor="middle" font-size="7" font-weight="700" fill="#166534">HA</text>
        <circle cx="198" cy="53" r="10" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="198" y="57" text-anchor="middle" font-size="7" font-weight="700" fill="#166534">HA</text>
        <!-- retentate: base -->
        <rect x="154" y="86" width="100" height="50" rx="7" fill="#dbeafe" stroke="#93c5fd" stroke-width="1.2"/>
        <text x="204" y="100" text-anchor="middle" font-size="8" font-weight="700" fill="#1e40af">Base side</text>
        <circle cx="172" cy="113" r="9" fill="#bfdbfe" stroke="#3b82f6" stroke-width="1.2"/><text x="172" y="117" text-anchor="middle" font-size="6" font-weight="700" fill="#1e3a8a">NaOH</text>
        <circle cx="200" cy="107" r="9" fill="#bfdbfe" stroke="#3b82f6" stroke-width="1.2"/><text x="200" y="111" text-anchor="middle" font-size="6" font-weight="700" fill="#1e3a8a">NaOH</text>
        <text x="226" y="128" font-size="7" fill="#1e40af">base recovered</text>
        <!-- dev -->
        <rect x="8" y="144" width="249" height="26" rx="6" fill="rgba(124,58,237,0.05)" stroke="#e2e8f0" stroke-width="1"/>
        <text x="16" y="156" font-size="7.5" font-weight="700" fill="#7c3aed">→ Scale-up: BMED stack design &amp; long-term stability</text>
        <text x="16" y="168" font-size="7.5" fill="#64748b">→ Water-free glycolysis / in-situ acid–base supply without neutralization</text>
      </svg>
    </div>
  </div>

  {% for item in site.data.research %}{% if item.title == "Biorefinery" %}
  <article class="research-detail-card no-image">
    <div class="research-detail-body">
      <div class="profile-label">{{ item.title }}</div>
      <h2>{{ item.one_liner }}</h2>
      <p>{{ item.why_it_matters }}</p>
      {% if item.topics %}<h3>Core topics</h3><ul>{% for t in item.topics %}<li>{{ t }}</li>{% endfor %}</ul>{% endif %}
      {% if item.key_methods %}<h3>Methods and approach</h3><ul>{% for m in item.key_methods %}<li>{{ m }}</li>{% endfor %}</ul>{% endif %}
      {% if item.selected_papers %}<h3>Selected papers</h3>
      <div class="card-grid two">{% for paper in item.selected_papers %}
        <div class="list-card publication-entry">
          <div class="list-meta">{{ paper.year }} | {{ paper.venue }}</div>
          <strong><a class="publication-link" href="{{ paper.url }}">{{ paper.title }}</a></strong>
        </div>{% endfor %}
      </div>{% endif %}
    </div>
  </article>
  {% endif %}{% endfor %}
</div>

<!-- ══════════════════════════════════════════════════════
     TAB 2 — PLASTIC RECYCLING
     ══════════════════════════════════════════════════════ -->
<div class="research-tab-panel" id="rtab-plastics">

  <p class="research-diagram-label">Process Diagrams — Membrane Principle &amp; Role</p>
  <div class="research-diagram-pair">

    <!-- Diagram 3: OSN/NF — size-selective -->
    <div class="research-diagram-box">
      <svg viewBox="0 0 265 195" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
        <rect width="265" height="195" fill="#f8fbff" rx="10"/>
        <rect width="265" height="22" fill="#f1f5f9" rx="10"/><rect y="12" width="265" height="10" fill="#f1f5f9"/>
        <text x="10" y="15" font-size="9" font-weight="700" fill="#334155">OSN / NF — Catalyst &amp; Monomer Sep.</text>
        <rect x="215" y="4" width="44" height="16" rx="8" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1"/>
        <text x="237" y="15" text-anchor="middle" font-size="8.5" font-weight="800" fill="#7c3aed">ΔP</text>
        <!-- feed -->
        <rect x="8" y="28" width="72" height="108" rx="7" fill="#fee2e2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="44" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#991b1b">Feed</text>
        <ellipse cx="28" cy="65" rx="15" ry="9" fill="#fca5a5" stroke="#ef4444" stroke-width="1" opacity="0.85"/><text x="28" y="68" text-anchor="middle" font-size="6.5" font-weight="700" fill="#991b1b">Cat.</text>
        <ellipse cx="52" cy="82" rx="14" ry="8" fill="#fca5a5" stroke="#ef4444" stroke-width="1" opacity="0.85"/><text x="52" y="85" text-anchor="middle" font-size="6.5" font-weight="700" fill="#991b1b">Cat.</text>
        <circle cx="30" cy="98" r="6" fill="#bbf7d0" stroke="#22c55e" stroke-width="1.2"/><text x="30" y="101" text-anchor="middle" font-size="6" font-weight="700" fill="#166534">M</text>
        <circle cx="55" cy="62" r="6" fill="#bbf7d0" stroke="#22c55e" stroke-width="1.2"/><text x="55" y="65" text-anchor="middle" font-size="6" font-weight="700" fill="#166534">M</text>
        <circle cx="60" cy="100" r="6" fill="#bbf7d0" stroke="#22c55e" stroke-width="1.2"/><text x="60" y="103" text-anchor="middle" font-size="6" font-weight="700" fill="#166534">M</text>
        <text x="44" y="122" text-anchor="middle" font-size="7" fill="#991b1b">reaction mixture</text>
        <!-- arrow -->
        <line x1="82" y1="82" x2="95" y2="82" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="95,78 102,82 95,86" fill="#94a3b8"/>
        <!-- NF membrane -->
        <g transform="translate(103,26)">
          <rect width="28" height="112" rx="4" fill="#7c3aed" fill-opacity="0.08" stroke="#7c3aed" stroke-width="1.8"/>
          <rect x="4" y="8"  width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="16" y="8" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="4" y="26" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="16" y="26" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="4" y="44" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="16" y="44" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="4" y="62" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="16" y="62" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="4" y="80" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="16" y="80" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="4" y="98" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <rect x="16" y="98" width="8" height="12" rx="2" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="0.7"/>
          <text x="14" y="118" text-anchor="middle" font-size="7" font-weight="700" fill="#7c3aed">NF/OSN</text>
        </g>
        <!-- arrows out -->
        <line x1="133" y1="66" x2="146" y2="60" stroke="#22c55e" stroke-width="1.5"/>
        <polygon points="146,56 152,60 146,64" fill="#22c55e"/>
        <line x1="133" y1="96" x2="146" y2="102" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="146,98 152,102 146,106" fill="#94a3b8"/>
        <!-- permeate: monomer -->
        <rect x="154" y="28" width="100" height="50" rx="7" fill="#dcfce7" stroke="#86efac" stroke-width="1.2"/>
        <text x="204" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#166534">Permeate</text>
        <circle cx="172" cy="59" r="7" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="172" y="62" text-anchor="middle" font-size="6" font-weight="700" fill="#166534">M</text>
        <circle cx="192" cy="52" r="7" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="192" y="55" text-anchor="middle" font-size="6" font-weight="700" fill="#166534">M</text>
        <circle cx="212" cy="60" r="7" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="212" y="63" text-anchor="middle" font-size="6" font-weight="700" fill="#166534">M</text>
        <text x="236" y="70" font-size="7" fill="#15803d">pure monomer</text>
        <!-- retentate: catalyst recycled -->
        <rect x="154" y="86" width="100" height="50" rx="7" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
        <text x="204" y="100" text-anchor="middle" font-size="8" font-weight="700" fill="#475569">Retentate</text>
        <ellipse cx="178" cy="113" rx="13" ry="8" fill="#fca5a5" stroke="#ef4444" stroke-width="1"/><text x="178" y="116" text-anchor="middle" font-size="6.5" font-weight="700" fill="#991b1b">Cat.</text>
        <text x="224" y="120" font-size="7" fill="#64748b">→ recycled</text>
        <!-- dev -->
        <rect x="8" y="144" width="249" height="26" rx="6" fill="rgba(124,58,237,0.05)" stroke="#e2e8f0" stroke-width="1"/>
        <text x="16" y="156" font-size="7.5" font-weight="700" fill="#7c3aed">→ Solvent-resistant NF in aprotic / harsh organic media</text>
        <text x="16" y="168" font-size="7.5" fill="#64748b">→ Broad polymer scope: PET, PS, polycarbonate, nylon</text>
      </svg>
    </div>

    <!-- Diagram 4: BMED for plastics -->
    <div class="research-diagram-box">
      <svg viewBox="0 0 265 195" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
        <rect width="265" height="195" fill="#f8fbff" rx="10"/>
        <rect width="265" height="22" fill="#f1f5f9" rx="10"/><rect y="12" width="265" height="10" fill="#f1f5f9"/>
        <text x="10" y="15" font-size="9" font-weight="700" fill="#334155">BMED — Acid / Base Regeneration</text>
        <rect x="215" y="4" width="44" height="16" rx="8" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1"/>
        <text x="237" y="15" text-anchor="middle" font-size="8.5" font-weight="800" fill="#7c3aed">Δφ</text>
        <!-- feed -->
        <rect x="8" y="28" width="72" height="108" rx="7" fill="#fef9c3" stroke="#fde047" stroke-width="1.2"/>
        <text x="44" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#713f12">Feed</text>
        <circle cx="27" cy="65" r="11" fill="#fde68a" stroke="#f59e0b" stroke-width="1.2"/><text x="27" y="69" text-anchor="middle" font-size="6.5" font-weight="700" fill="#78350f">salt</text>
        <circle cx="52" cy="80" r="11" fill="#fde68a" stroke="#f59e0b" stroke-width="1.2"/><text x="52" y="84" text-anchor="middle" font-size="6.5" font-weight="700" fill="#78350f">salt</text>
        <circle cx="30" cy="100" r="11" fill="#fde68a" stroke="#f59e0b" stroke-width="1.2"/><text x="30" y="104" text-anchor="middle" font-size="6.5" font-weight="700" fill="#78350f">salt</text>
        <text x="44" y="122" text-anchor="middle" font-size="7" fill="#78350f">reaction salt</text>
        <!-- arrow -->
        <line x1="82" y1="82" x2="95" y2="82" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="95,78 102,82 95,86" fill="#94a3b8"/>
        <!-- BPM -->
        <g transform="translate(103,26)">
          <rect y="0"  width="28" height="56" rx="4" fill="#7c3aed" fill-opacity="0.12" stroke="#7c3aed" stroke-width="1.8"/>
          <rect y="56" width="28" height="56" rx="4" fill="#0050a4" fill-opacity="0.12" stroke="#0050a4" stroke-width="1.8"/>
          <text x="14" y="14" text-anchor="middle" font-size="6" font-weight="800" fill="#7c3aed">−</text>
          <text x="14" y="28" text-anchor="middle" font-size="6" font-weight="800" fill="#7c3aed">−</text>
          <text x="14" y="42" text-anchor="middle" font-size="6" font-weight="800" fill="#7c3aed">−</text>
          <line x1="0" y1="56" x2="28" y2="56" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>
          <text x="14" y="53" text-anchor="middle" font-size="4.5" fill="#ef4444" font-weight="700">H₂O split</text>
          <text x="14" y="70" text-anchor="middle" font-size="6" font-weight="800" fill="#0050a4">+</text>
          <text x="14" y="84" text-anchor="middle" font-size="6" font-weight="800" fill="#0050a4">+</text>
          <text x="14" y="98" text-anchor="middle" font-size="6" font-weight="800" fill="#0050a4">+</text>
          <text x="14" y="118" text-anchor="middle" font-size="7" font-weight="700" fill="#5b21b6">BPM</text>
        </g>
        <!-- arrows out -->
        <line x1="133" y1="66" x2="146" y2="60" stroke="#22c55e" stroke-width="1.5"/>
        <polygon points="146,56 152,60 146,64" fill="#22c55e"/>
        <line x1="133" y1="96" x2="146" y2="102" stroke="#3b82f6" stroke-width="1.5"/>
        <polygon points="146,98 152,102 146,106" fill="#3b82f6"/>
        <!-- acid permeate -->
        <rect x="154" y="28" width="100" height="50" rx="7" fill="#dcfce7" stroke="#86efac" stroke-width="1.2"/>
        <text x="204" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#166534">Acid side</text>
        <circle cx="174" cy="58" r="9" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="174" y="62" text-anchor="middle" font-size="7" font-weight="700" fill="#166534">H⁺</text>
        <circle cx="198" cy="52" r="9" fill="#86efac" stroke="#22c55e" stroke-width="1.2"/><text x="198" y="56" text-anchor="middle" font-size="7" font-weight="700" fill="#166534">H⁺</text>
        <text x="240" y="68" font-size="7" fill="#15803d">acid stream</text>
        <!-- base retentate -->
        <rect x="154" y="86" width="100" height="50" rx="7" fill="#dbeafe" stroke="#93c5fd" stroke-width="1.2"/>
        <text x="204" y="100" text-anchor="middle" font-size="8" font-weight="700" fill="#1e40af">Base side</text>
        <circle cx="172" cy="113" r="9" fill="#bfdbfe" stroke="#3b82f6" stroke-width="1.2"/><text x="172" y="117" text-anchor="middle" font-size="6" font-weight="700" fill="#1e3a8a">OH⁻</text>
        <circle cx="199" cy="107" r="9" fill="#bfdbfe" stroke="#3b82f6" stroke-width="1.2"/><text x="199" y="111" text-anchor="middle" font-size="6" font-weight="700" fill="#1e3a8a">OH⁻</text>
        <text x="233" y="127" font-size="7" fill="#1e40af">→ reactor reuse</text>
        <!-- dev -->
        <rect x="8" y="144" width="249" height="26" rx="6" fill="rgba(124,58,237,0.05)" stroke="#e2e8f0" stroke-width="1"/>
        <text x="16" y="156" font-size="7.5" font-weight="700" fill="#7c3aed">→ Eliminates neutralization step — zero salt waste process</text>
        <text x="16" y="168" font-size="7.5" fill="#64748b">→ Integration with glycolysis / depolymerization reaction loops</text>
      </svg>
    </div>
  </div>

  {% for item in site.data.research %}{% if item.title == "Plastic recycling" %}
  <article class="research-detail-card no-image">
    <div class="research-detail-body">
      <div class="profile-label">{{ item.title }}</div>
      <h2>{{ item.one_liner }}</h2>
      <p>{{ item.why_it_matters }}</p>
      {% if item.topics %}<h3>Core topics</h3><ul>{% for t in item.topics %}<li>{{ t }}</li>{% endfor %}</ul>{% endif %}
      {% if item.key_methods %}<h3>Methods and approach</h3><ul>{% for m in item.key_methods %}<li>{{ m }}</li>{% endfor %}</ul>{% endif %}
      {% if item.selected_papers %}<h3>Selected papers</h3>
      <div class="card-grid two">{% for paper in item.selected_papers %}
        <div class="list-card publication-entry">
          <div class="list-meta">{{ paper.year }} | {{ paper.venue }}</div>
          <strong><a class="publication-link" href="{{ paper.url }}">{{ paper.title }}</a></strong>
        </div>{% endfor %}
      </div>{% endif %}
    </div>
  </article>
  {% endif %}{% endfor %}
</div>

<!-- ══════════════════════════════════════════════════════
     TAB 3 — RESOURCE RECOVERY
     ══════════════════════════════════════════════════════ -->
<div class="research-tab-panel" id="rtab-resource">

  <p class="research-diagram-label">Process Diagrams — Membrane Principle &amp; Role</p>
  <div class="research-diagram-pair">

    <!-- Diagram 5: OSN in organic liquids -->
    <div class="research-diagram-box">
      <svg viewBox="0 0 265 195" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
        <rect width="265" height="195" fill="#f8fbff" rx="10"/>
        <rect width="265" height="22" fill="#f1f5f9" rx="10"/><rect y="12" width="265" height="10" fill="#f1f5f9"/>
        <text x="10" y="15" font-size="9" font-weight="700" fill="#334155">OSN in Organic Liquids</text>
        <rect x="215" y="4" width="44" height="16" rx="8" fill="#dbeafe" stroke="#93c5fd" stroke-width="1"/>
        <text x="237" y="15" text-anchor="middle" font-size="8" font-weight="800" fill="#0050a4">ΔP·Δa</text>
        <!-- feed -->
        <rect x="8" y="28" width="72" height="108" rx="7" fill="#dbeafe" stroke="#bfdbfe" stroke-width="1.2"/>
        <text x="44" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#1e40af">Feed</text>
        <circle cx="26" cy="64" r="13" fill="#bfdbfe" stroke="#2563eb" stroke-width="1.2"/><text x="26" y="68" text-anchor="middle" font-size="7" font-weight="700" fill="#1e40af">V</text>
        <circle cx="52" cy="80" r="13" fill="#bfdbfe" stroke="#2563eb" stroke-width="1.2"/><text x="52" y="84" text-anchor="middle" font-size="7" font-weight="700" fill="#1e40af">V</text>
        <circle cx="28" cy="100" r="6" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1.2"/>
        <circle cx="48" cy="58" r="6" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1.2"/>
        <circle cx="62" cy="100" r="6" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1.2"/>
        <text x="44" y="122" text-anchor="middle" font-size="7" fill="#1e40af">org. solvent mix</text>
        <!-- arrow -->
        <line x1="82" y1="82" x2="95" y2="82" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="95,78 102,82 95,86" fill="#94a3b8"/>
        <!-- Dense OSN membrane -->
        <g transform="translate(103,26)">
          <rect width="28" height="112" rx="4" fill="#0050a4" fill-opacity="0.1" stroke="#0050a4" stroke-width="1.8"/>
          <path d="M2,6 Q8,2 14,6 Q20,10 26,6"   fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,16 Q8,12 14,16 Q20,20 26,16" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,26 Q8,22 14,26 Q20,30 26,26" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,36 Q8,32 14,36 Q20,40 26,36" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,46 Q8,42 14,46 Q20,50 26,46" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,56 Q8,52 14,56 Q20,60 26,56" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,66 Q8,62 14,66 Q20,70 26,66" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,76 Q8,72 14,76 Q20,80 26,76" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,86 Q8,82 14,86 Q20,90 26,86" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,96 Q8,92 14,96 Q20,100 26,96" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,106 Q8,102 14,106 Q20,110 26,106" fill="none" stroke="#0050a4" stroke-width="0.8" stroke-opacity="0.4"/>
          <text x="14" y="118" text-anchor="middle" font-size="7" font-weight="700" fill="#0050a4">Dense</text>
        </g>
        <!-- arrows out -->
        <line x1="133" y1="66" x2="146" y2="60" stroke="#0ea5e9" stroke-width="1.5"/>
        <polygon points="146,56 152,60 146,64" fill="#0ea5e9"/>
        <line x1="133" y1="96" x2="146" y2="102" stroke="#22c55e" stroke-width="1.5"/>
        <polygon points="146,98 152,102 146,106" fill="#22c55e"/>
        <!-- permeate: solvent -->
        <rect x="154" y="28" width="100" height="50" rx="7" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1.2"/>
        <text x="204" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#0369a1">Permeate</text>
        <circle cx="172" cy="59" r="6" fill="#7dd3fc" stroke="#0ea5e9" stroke-width="1.2"/>
        <circle cx="190" cy="52" r="6" fill="#7dd3fc" stroke="#0ea5e9" stroke-width="1.2"/>
        <circle cx="210" cy="60" r="6" fill="#7dd3fc" stroke="#0ea5e9" stroke-width="1.2"/>
        <text x="238" y="66" font-size="7" fill="#0369a1">solvent reused</text>
        <!-- retentate: concentrated value -->
        <rect x="154" y="86" width="100" height="50" rx="7" fill="#dcfce7" stroke="#86efac" stroke-width="1.2"/>
        <text x="204" y="100" text-anchor="middle" font-size="8" font-weight="700" fill="#166534">Retentate</text>
        <circle cx="174" cy="113" r="12" fill="#bfdbfe" stroke="#2563eb" stroke-width="1.2"/><text x="174" y="117" text-anchor="middle" font-size="7" font-weight="700" fill="#1e40af">V</text>
        <circle cx="202" cy="107" r="12" fill="#bfdbfe" stroke="#2563eb" stroke-width="1.2"/><text x="202" y="111" text-anchor="middle" font-size="7" font-weight="700" fill="#1e40af">V</text>
        <text x="235" y="126" font-size="7" fill="#166534">conc. value</text>
        <!-- dev -->
        <rect x="8" y="144" width="249" height="26" rx="6" fill="rgba(0,80,164,0.05)" stroke="#e2e8f0" stroke-width="1"/>
        <text x="16" y="156" font-size="7.5" font-weight="700" fill="#0050a4">→ Membrane stability in diverse organic solvents (Nat. Sust. 2025)</text>
        <text x="16" y="168" font-size="7.5" fill="#64748b">→ Solubility–diffusion selectivity tuning for challenging separations</text>
      </svg>
    </div>

    <!-- Diagram 6: Membrane Distillation -->
    <div class="research-diagram-box">
      <svg viewBox="0 0 265 195" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
        <rect width="265" height="195" fill="#f8fbff" rx="10"/>
        <rect width="265" height="22" fill="#f1f5f9" rx="10"/><rect y="12" width="265" height="10" fill="#f1f5f9"/>
        <text x="10" y="15" font-size="9" font-weight="700" fill="#334155">Membrane Distillation</text>
        <rect x="208" y="4" width="52" height="16" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1"/>
        <text x="234" y="15" text-anchor="middle" font-size="8" font-weight="800" fill="#b45309">Δp_vap</text>
        <!-- feed -->
        <rect x="8" y="28" width="72" height="108" rx="7" fill="#dbeafe" stroke="#bfdbfe" stroke-width="1.2"/>
        <text x="44" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#1e40af">Feed (hot)</text>
        <circle cx="24" cy="62" r="6" fill="#93c5fd" stroke="#3b82f6" stroke-width="1.2"/>
        <circle cx="42" cy="72" r="6" fill="#93c5fd" stroke="#3b82f6" stroke-width="1.2"/>
        <circle cx="32" cy="84" r="6" fill="#93c5fd" stroke="#3b82f6" stroke-width="1.2"/>
        <circle cx="54" cy="62" r="6" fill="#93c5fd" stroke="#3b82f6" stroke-width="1.2"/>
        <circle cx="48" cy="92" r="6" fill="#93c5fd" stroke="#3b82f6" stroke-width="1.2"/>
        <circle cx="26" cy="98" r="9" fill="#fde68a" stroke="#f59e0b" stroke-width="1.2"/><text x="26" y="101" text-anchor="middle" font-size="6" font-weight="700" fill="#78350f">Li⁺</text>
        <circle cx="54" cy="78" r="9" fill="#fde68a" stroke="#f59e0b" stroke-width="1.2"/><text x="54" y="81" text-anchor="middle" font-size="6" font-weight="700" fill="#78350f">Li⁺</text>
        <text x="44" y="122" text-anchor="middle" font-size="7" fill="#78350f">dilute brine (ΔT)</text>
        <!-- arrow -->
        <line x1="82" y1="82" x2="95" y2="82" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="95,78 102,82 95,86" fill="#94a3b8"/>
        <!-- Hydrophobic porous MD membrane -->
        <g transform="translate(103,26)">
          <rect width="28" height="112" rx="4" fill="#b45309" fill-opacity="0.08" stroke="#b45309" stroke-width="1.8"/>
          <ellipse cx="14" cy="10" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <ellipse cx="14" cy="22" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <ellipse cx="14" cy="34" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <ellipse cx="14" cy="46" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <ellipse cx="14" cy="58" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <ellipse cx="14" cy="70" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <ellipse cx="14" cy="82" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <ellipse cx="14" cy="94" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <ellipse cx="14" cy="106" rx="8" ry="4" fill="none" stroke="#b45309" stroke-width="0.8" stroke-dasharray="2,1.5"/>
          <text x="14" y="118" text-anchor="middle" font-size="7" font-weight="700" fill="#b45309">MD</text>
        </g>
        <!-- arrows out -->
        <line x1="133" y1="66" x2="146" y2="60" stroke="#38bdf8" stroke-width="1.5"/>
        <polygon points="146,56 152,60 146,64" fill="#38bdf8"/>
        <line x1="133" y1="96" x2="146" y2="102" stroke="#f59e0b" stroke-width="1.5"/>
        <polygon points="146,98 152,102 146,106" fill="#f59e0b"/>
        <!-- permeate: water -->
        <rect x="154" y="28" width="100" height="50" rx="7" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1.2"/>
        <text x="204" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#0369a1">Permeate</text>
        <circle cx="172" cy="59" r="6" fill="#bae6fd" stroke="#38bdf8" stroke-width="1.2"/>
        <circle cx="190" cy="52" r="6" fill="#bae6fd" stroke="#38bdf8" stroke-width="1.2"/>
        <circle cx="210" cy="59" r="6" fill="#bae6fd" stroke="#38bdf8" stroke-width="1.2"/>
        <text x="204" y="72" text-anchor="middle" font-size="7" fill="#0369a1">water vapour → condensed</text>
        <!-- retentate: concentrated Li -->
        <rect x="154" y="86" width="100" height="50" rx="7" fill="#fef9c3" stroke="#fde047" stroke-width="1.2"/>
        <text x="204" y="100" text-anchor="middle" font-size="8" font-weight="700" fill="#713f12">Retentate</text>
        <circle cx="174" cy="113" r="10" fill="#fde68a" stroke="#f59e0b" stroke-width="1.2"/><text x="174" y="117" text-anchor="middle" font-size="6" font-weight="700" fill="#78350f">Li⁺</text>
        <circle cx="200" cy="107" r="10" fill="#fde68a" stroke="#f59e0b" stroke-width="1.2"/><text x="200" y="111" text-anchor="middle" font-size="6" font-weight="700" fill="#78350f">Li⁺</text>
        <text x="235" y="126" font-size="7" fill="#713f12">→ crystallize</text>
        <!-- dev -->
        <rect x="8" y="144" width="249" height="26" rx="6" fill="rgba(180,83,9,0.05)" stroke="#e2e8f0" stroke-width="1"/>
        <text x="16" y="156" font-size="7.5" font-weight="700" fill="#b45309">→ Li⁺ / rare-earth concentration from dilute brine streams</text>
        <text x="16" y="168" font-size="7.5" fill="#64748b">→ Antifouling &amp; long-term pore wetting resistance</text>
      </svg>
    </div>
  </div>

  {% for item in site.data.research %}{% if item.title == "Resource recovery" %}
  <article class="research-detail-card no-image">
    <div class="research-detail-body">
      <div class="profile-label">{{ item.title }}</div>
      <h2>{{ item.one_liner }}</h2>
      <p>{{ item.why_it_matters }}</p>
      {% if item.topics %}<h3>Core topics</h3><ul>{% for t in item.topics %}<li>{{ t }}</li>{% endfor %}</ul>{% endif %}
      {% if item.key_methods %}<h3>Methods and approach</h3><ul>{% for m in item.key_methods %}<li>{{ m }}</li>{% endfor %}</ul>{% endif %}
      {% if item.selected_papers %}<h3>Selected papers</h3>
      <div class="card-grid two">{% for paper in item.selected_papers %}
        <div class="list-card publication-entry">
          <div class="list-meta">{{ paper.year }} | {{ paper.venue }}</div>
          <strong><a class="publication-link" href="{{ paper.url }}">{{ paper.title }}</a></strong>
        </div>{% endfor %}
      </div>{% endif %}
    </div>
  </article>
  {% endif %}{% endfor %}
</div>

<!-- ══════════════════════════════════════════════════════
     TAB 4 — ENERGY
     ══════════════════════════════════════════════════════ -->
<div class="research-tab-panel" id="rtab-energy">

  <p class="research-diagram-label">Process Diagrams — Membrane Principle &amp; Role</p>
  <div class="research-diagram-pair">

    <!-- Diagram 7: Pervaporation -->
    <div class="research-diagram-box">
      <svg viewBox="0 0 265 195" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
        <rect width="265" height="195" fill="#f8fbff" rx="10"/>
        <rect width="265" height="22" fill="#f1f5f9" rx="10"/><rect y="12" width="265" height="10" fill="#f1f5f9"/>
        <text x="10" y="15" font-size="9" font-weight="700" fill="#334155">Pervaporation — Bio-alcohol Recovery</text>
        <rect x="215" y="4" width="44" height="16" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1"/>
        <text x="237" y="15" text-anchor="middle" font-size="8.5" font-weight="800" fill="#b45309">Δa</text>
        <!-- feed -->
        <rect x="8" y="28" width="72" height="108" rx="7" fill="#dbeafe" stroke="#bfdbfe" stroke-width="1.2"/>
        <text x="44" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#1e40af">Feed</text>
        <circle cx="22" cy="62" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <circle cx="38" cy="72" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <circle cx="28" cy="84" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <circle cx="52" cy="60" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <circle cx="48" cy="88" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <circle cx="62" cy="75" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <circle cx="34" cy="100" r="9" fill="#fed7aa" stroke="#f97316" stroke-width="1.2"/><text x="34" y="104" text-anchor="middle" font-size="5.5" font-weight="700" fill="#7c2d12">BuOH</text>
        <circle cx="60" cy="98" r="9" fill="#fed7aa" stroke="#f97316" stroke-width="1.2"/><text x="60" y="102" text-anchor="middle" font-size="5.5" font-weight="700" fill="#7c2d12">BuOH</text>
        <text x="44" y="122" text-anchor="middle" font-size="7" fill="#7c2d12">ferm. broth (~1%)</text>
        <!-- arrow -->
        <line x1="82" y1="82" x2="95" y2="82" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="95,78 102,82 95,86" fill="#94a3b8"/>
        <!-- Dense pervap membrane -->
        <g transform="translate(103,26)">
          <rect width="28" height="112" rx="4" fill="#b45309" fill-opacity="0.1" stroke="#b45309" stroke-width="1.8"/>
          <path d="M2,6 Q8,2 14,6 Q20,10 26,6"   fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,16 Q8,12 14,16 Q20,20 26,16" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,26 Q8,22 14,26 Q20,30 26,26" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,36 Q8,32 14,36 Q20,40 26,36" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,46 Q8,42 14,46 Q20,50 26,46" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,56 Q8,52 14,56 Q20,60 26,56" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,66 Q8,62 14,66 Q20,70 26,66" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,76 Q8,72 14,76 Q20,80 26,76" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,86 Q8,82 14,86 Q20,90 26,86" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,96 Q8,92 14,96 Q20,100 26,96" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <path d="M2,106 Q8,102 14,106 Q20,110 26,106" fill="none" stroke="#b45309" stroke-width="0.8" stroke-opacity="0.4"/>
          <text x="14" y="118" text-anchor="middle" font-size="7" font-weight="700" fill="#b45309">Pervap</text>
        </g>
        <!-- arrows out -->
        <line x1="133" y1="66" x2="146" y2="60" stroke="#f97316" stroke-width="1.5"/>
        <polygon points="146,56 152,60 146,64" fill="#f97316"/>
        <line x1="133" y1="96" x2="146" y2="102" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="146,98 152,102 146,106" fill="#94a3b8"/>
        <!-- permeate: enriched BuOH -->
        <rect x="154" y="28" width="100" height="50" rx="7" fill="#ffedd5" stroke="#fdba74" stroke-width="1.2"/>
        <text x="204" y="42" text-anchor="middle" font-size="8" font-weight="700" fill="#9a3412">Permeate</text>
        <circle cx="172" cy="58" r="10" fill="#fed7aa" stroke="#f97316" stroke-width="1.2"/><text x="172" y="62" text-anchor="middle" font-size="5.5" font-weight="700" fill="#7c2d12">BuOH</text>
        <circle cx="198" cy="52" r="10" fill="#fed7aa" stroke="#f97316" stroke-width="1.2"/><text x="198" y="56" text-anchor="middle" font-size="5.5" font-weight="700" fill="#7c2d12">BuOH</text>
        <text x="240" y="70" font-size="7" fill="#c2410c">→ distill</text>
        <!-- retentate: broth back -->
        <rect x="154" y="86" width="100" height="50" rx="7" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
        <text x="204" y="100" text-anchor="middle" font-size="8" font-weight="700" fill="#475569">Retentate</text>
        <circle cx="172" cy="113" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <circle cx="188" cy="107" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <circle cx="204" cy="113" r="5" fill="#bfdbfe" stroke="#60a5fa" stroke-width="1.2"/>
        <text x="204" y="128" text-anchor="middle" font-size="7" fill="#64748b">depleted broth → bioreactor</text>
        <!-- dev -->
        <rect x="8" y="144" width="249" height="26" rx="6" fill="rgba(180,83,9,0.05)" stroke="#e2e8f0" stroke-width="1"/>
        <text x="16" y="156" font-size="7.5" font-weight="700" fill="#b45309">→ High-flux alcohol-selective TFC membranes</text>
        <text x="16" y="168" font-size="7.5" fill="#64748b">→ In-situ product removal prevents bioreactor inhibition</text>
      </svg>
    </div>

    <!-- Diagram 8: PRO & Battery Separator -->
    <div class="research-diagram-box">
      <svg viewBox="0 0 265 195" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
        <rect width="265" height="195" fill="#f8fbff" rx="10"/>
        <rect width="265" height="22" fill="#f1f5f9" rx="10"/><rect y="12" width="265" height="10" fill="#f1f5f9"/>
        <text x="10" y="15" font-size="9" font-weight="700" fill="#334155">PRO &amp; TR-Polymer Battery Separator</text>
        <rect x="210" y="4" width="50" height="16" rx="8" fill="#d1fae5" stroke="#6ee7b7" stroke-width="1"/>
        <text x="235" y="15" text-anchor="middle" font-size="8" font-weight="800" fill="#009e73">Δπ · σ</text>
        <!-- PRO section (top half of main area) -->
        <rect x="8" y="28" width="72" height="52" rx="7" fill="#dbeafe" stroke="#bfdbfe" stroke-width="1.2"/>
        <text x="44" y="42" text-anchor="middle" font-size="7.5" font-weight="700" fill="#1e40af">Seawater</text>
        <text x="44" y="55" text-anchor="middle" font-size="7" fill="#3b82f6">(high π)</text>
        <line x1="8" y1="82" x2="78" y2="82" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,2"/>
        <rect x="8" y="84" width="72" height="52" rx="7" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1.2"/>
        <text x="44" y="99" text-anchor="middle" font-size="7.5" font-weight="700" fill="#0369a1">River water</text>
        <text x="44" y="112" text-anchor="middle" font-size="7" fill="#38bdf8">(low π)</text>
        <!-- separator label -->
        <line x1="8" y1="140" x2="78" y2="140" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,2"/>
        <text x="44" y="125" text-anchor="middle" font-size="7" fill="#64748b">PRO mode</text>
        <!-- arrow -->
        <line x1="82" y1="82" x2="95" y2="82" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="95,78 102,82 95,86" fill="#94a3b8"/>
        <!-- TFC membrane -->
        <g transform="translate(103,26)">
          <rect width="28" height="112" rx="4" fill="#009e73" fill-opacity="0.1" stroke="#009e73" stroke-width="1.8"/>
          <path d="M2,6 Q8,2 14,6 Q20,10 26,6"   fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,16 Q8,12 14,16 Q20,20 26,16" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,26 Q8,22 14,26 Q20,30 26,26" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,36 Q8,32 14,36 Q20,40 26,36" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,46 Q8,42 14,46 Q20,50 26,46" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,56 Q8,52 14,56 Q20,60 26,56" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,66 Q8,62 14,66 Q20,70 26,66" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,76 Q8,72 14,76 Q20,80 26,76" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,86 Q8,82 14,86 Q20,90 26,86" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,96 Q8,92 14,96 Q20,100 26,96" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <path d="M2,106 Q8,102 14,106 Q20,110 26,106" fill="none" stroke="#009e73" stroke-width="0.8" stroke-opacity="0.45"/>
          <text x="14" y="118" text-anchor="middle" font-size="7" font-weight="700" fill="#009e73">TFC</text>
        </g>
        <!-- PRO output: water flux + power -->
        <rect x="154" y="28" width="100" height="108" rx="7" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
        <text x="204" y="46" text-anchor="middle" font-size="8" font-weight="700" fill="#166534">PRO Output</text>
        <text x="204" y="60" text-anchor="middle" font-size="8" fill="#166534">Water flux →</text>
        <text x="204" y="73" text-anchor="middle" font-size="8" fill="#166534">diluted brine</text>
        <text x="204" y="88" text-anchor="middle" font-size="9" font-weight="700" fill="#009e73">⚡ 87 W/m²</text>
        <text x="204" y="100" text-anchor="middle" font-size="7.5" fill="#16a34a">pressure → power</text>
        <line x1="154" y1="110" x2="254" y2="110" stroke="#d1d5db" stroke-width="1" stroke-dasharray="3,2"/>
        <text x="204" y="122" text-anchor="middle" font-size="7.5" font-weight="700" fill="#475569">Battery Separator</text>
        <text x="204" y="133" text-anchor="middle" font-size="7" fill="#475569">TR-polymer → high Li⁺</text>
        <text x="204" y="144" text-anchor="middle" font-size="7" fill="#475569">conductivity at 60°C+</text>
        <!-- dev -->
        <rect x="8" y="144" width="249" height="26" rx="6" fill="rgba(0,158,115,0.05)" stroke="#e2e8f0" stroke-width="1"/>
        <text x="16" y="156" font-size="7.5" font-weight="700" fill="#009e73">→ TFC on TR-polymer support: record 87 W/m² PRO power density</text>
        <text x="16" y="168" font-size="7.5" fill="#64748b">→ TR-polybenzoxazole as stable high-temp Li-ion battery separator</text>
      </svg>
    </div>
  </div>

  {% for item in site.data.research %}{% if item.title == "Energy-related applications" %}
  <article class="research-detail-card no-image">
    <div class="research-detail-body">
      <div class="profile-label">{{ item.title }}</div>
      <h2>{{ item.one_liner }}</h2>
      <p>{{ item.why_it_matters }}</p>
      {% if item.topics %}<h3>Core topics</h3><ul>{% for t in item.topics %}<li>{{ t }}</li>{% endfor %}</ul>{% endif %}
      {% if item.key_methods %}<h3>Methods and approach</h3><ul>{% for m in item.key_methods %}<li>{{ m }}</li>{% endfor %}</ul>{% endif %}
      {% if item.selected_papers %}<h3>Selected papers</h3>
      <div class="card-grid two">{% for paper in item.selected_papers %}
        <div class="list-card publication-entry">
          <div class="list-meta">{{ paper.year }} | {{ paper.venue }}</div>
          <strong><a class="publication-link" href="{{ paper.url }}">{{ paper.title }}</a></strong>
        </div>{% endfor %}
      </div>{% endif %}
    </div>
  </article>
  {% endif %}{% endfor %}
</div>

</div><!-- /.container -->
</div><!-- /.page-wrap -->

<script>
(function() {
  var btns = document.querySelectorAll('.research-tab-btn');
  var panels = document.querySelectorAll('.research-tab-panel');
  btns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      btns.forEach(function(b) { b.classList.remove('active'); });
      panels.forEach(function(p) { p.classList.remove('active'); });
      btn.classList.add('active');
      var panel = document.getElementById('rtab-' + btn.dataset.tab);
      if (panel) panel.classList.add('active');
    });
  });
})();
</script>
