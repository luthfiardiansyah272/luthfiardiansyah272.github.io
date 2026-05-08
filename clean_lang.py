import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. HAPUS semua script block yang berisi setLang / setLanguage ──
content = re.sub(r'\n<script>\s*(const translations|function setLang|function setLanguage|// Language switcher).*?</script>', '', content, flags=re.DOTALL)

# ── 2. HAPUS CSS lang-switch duplikat ──
content = re.sub(r'\n\s*/\* Language Switch \*/.*?\.lang-btn:hover:not\(\.active\) \{[^}]+\}\n', '', content, flags=re.DOTALL)

# ── 3. HAPUS tombol lang-switch di navbar jika ada ──
content = re.sub(r'\n\s*<div class="lang-switch">.*?</div>\n', '', content, flags=re.DOTALL)

# ── 4. HAPUS data-en/data-id yang nested/rusak ──
# Hapus semua atribut data-en dan data-id dulu
content = re.sub(r' data-en="[^"]*"', '', content)
content = re.sub(r' data-id="[^"]*"', '', content)

# ── 5. PERBAIKI tagline yang rusak ──
content = content.replace(
    '<p class="tagline">data-en="Electrical Engineering &middot; Sensor Systems &middot; TPM &middot; Operational Excellence" data-id="Teknik Elektro &middot; Sistem Sensor &middot; TPM &middot; Keunggulan Operasional"</p>',
    '<p class="tagline" data-en="Electrical Engineering &middot; Sensor Systems &middot; TPM &middot; Operational Excellence" data-id="Teknik Elektro &middot; Sistem Sensor &middot; TPM &middot; Keunggulan Operasional">Electrical Engineering &middot; Sensor Systems &middot; TPM &middot; Operational Excellence</p>'
)

# ── 6. PERBAIKI About Me paragraphs yang rusak ──
# Paragraph 1
old_p1 = '''<p >Electrical Engineering graduate with proven experience in production system digitalization, equipment reliability, and maintenance engineering within FMCG agribusiness operations. Demonstrated impact in cost reduction exceeding IDR 1.2B/year, multi-site system deployment, and TPM implementation across multiple business units." data-id="Lulusan Teknik Elektro dengan pengalaman terbukti dalam digitalisasi sistem produksi, keandalan peralatan, dan rekayasa pemeliharaan dalam operasi agribisnis FMCG. Dampak yang terbukti dalam pengurangan biaya melebihi IDR 1.2B/tahun, deployment sistem multi-situs, dan implementasi TPM di berbagai unit bisnis.">Electrical Engineering graduate with proven experience in production system digitalization, equipment reliability, and maintenance engineering within FMCG agribusiness operations. Demonstrated impact in cost reduction exceeding <strong>IDR 1.2B/year</strong>, multi-site system deployment, and TPM implementation across multiple business units.</p>'''
new_p1 = '''<p data-en="Electrical Engineering graduate with proven experience in production system digitalization, equipment reliability, and maintenance engineering within FMCG agribusiness operations. Demonstrated impact in cost reduction exceeding IDR 1.2B/year, multi-site system deployment, and TPM implementation across multiple business units." data-id="Lulusan Teknik Elektro dengan pengalaman terbukti dalam digitalisasi sistem produksi, keandalan peralatan, dan rekayasa pemeliharaan di operasi agribisnis FMCG. Dampak nyata dalam penghematan biaya melebihi IDR 1,2M/tahun, penerapan sistem multi-lokasi, dan implementasi TPM di berbagai unit bisnis.">Electrical Engineering graduate with proven experience in production system digitalization, equipment reliability, and maintenance engineering within FMCG agribusiness operations. Demonstrated impact in cost reduction exceeding <strong>IDR 1.2B/year</strong>, multi-site system deployment, and TPM implementation across multiple business units.</p>'''
content = content.replace(old_p1, new_p1)

# Paragraph 2
old_p2 = '''<p >Strong in systems thinking, problem solving, and operational execution — with hands-on involvement from development and pilot through to full implementation. Highly driven to grow as a Production or Maintenance Engineer, with a focus on operational excellence and continuous improvement." data-id="Kuat dalam pemikiran sistem, pemecahan masalah, dan eksekusi operasional — dengan keterlibatan langsung dari pengembangan dan pilot hingga implementasi penuh. Sangat termotivasi untuk berkembang sebagai Production atau Maintenance Engineer, dengan fokus pada keunggulan operasional dan perbaikan berkelanjutan.">Strong in systems thinking, problem solving, and operational execution — with hands-on involvement from development and pilot through to full implementation. Highly driven to grow as a Production or Maintenance Engineer, with a focus on operational excellence and continuous improvement.</p>'''
new_p2 = '''<p data-en="Strong in systems thinking, problem solving, and operational execution — with hands-on involvement from development and pilot through to full implementation. Highly driven to grow as a Production or Maintenance Engineer, with a focus on operational excellence and continuous improvement." data-id="Kuat dalam pemikiran sistematis, pemecahan masalah, dan eksekusi operasional — dengan keterlibatan langsung dari pengembangan dan pilot hingga implementasi penuh. Sangat termotivasi untuk berkembang sebagai Production atau Maintenance Engineer, dengan fokus pada keunggulan operasional dan perbaikan berkelanjutan.">Strong in systems thinking, problem solving, and operational execution — with hands-on involvement from development and pilot through to full implementation. Highly driven to grow as a Production or Maintenance Engineer, with a focus on operational excellence and continuous improvement.</p>'''
content = content.replace(old_p2, new_p2)

# ── 7. PERBAIKI footer yang rusak ──
content = content.replace(
    '<p>data-en="© 2025 Luthfi Ardiansyah" data-id="© 2025 Luthfi Ardiansyah">© 2025 Luthfi Ardiansyah',
    '<p>© 2025 Luthfi Ardiansyah'
)

# ── 8. PERBAIKI skills table Languages td yang rusak ──
content = content.replace(
    '<td>data-en="Indonesian (Native) &nbsp;|&nbsp; English (Professional Working Proficiency)" data-id="Indonesia (Asli) &nbsp;|&nbsp; Inggris (Kemampuan Kerja Profesional)">Indonesian (Native) &nbsp;|&nbsp; English (Professional Working Proficiency)</td>',
    '<td data-en="Indonesian (Native) &nbsp;|&nbsp; English (Professional Working Proficiency)" data-id="Indonesia (Asli) &nbsp;|&nbsp; Inggris (Kemampuan Kerja Profesional)">Indonesian (Native) &nbsp;|&nbsp; English (Professional Working Proficiency)</td>'
)

# ── 9. TAMBAH data-en/data-id yang bersih ke elemen kunci ──
pairs = [
    # Nav
    ('>About</a>', ' data-en="About" data-id="Tentang">About</a>'),
    ('>Experience</a>', ' data-en="Experience" data-id="Pengalaman">Experience</a>'),
    ('>Projects</a>', ' data-en="Projects" data-id="Proyek">Projects</a>'),
    ('>Skills</a>', ' data-en="Skills" data-id="Keahlian">Skills</a>'),
    ('>Education</a>', ' data-en="Education" data-id="Pendidikan">Education</a>'),
    ('>Certs</a>', ' data-en="Certs" data-id="Sertifikat">Certs</a>'),
    # Section titles
    ('>About Me</span>', ' data-en="About Me" data-id="Tentang Saya">About Me</span>'),
    ('>Work Experience</span>', ' data-en="Work Experience" data-id="Pengalaman Kerja">Work Experience</span>'),
    ('>Key Projects</span>', ' data-en="Key Projects" data-id="Proyek Utama">Key Projects</span>'),
    ('>Skills &amp; Tools</span>', ' data-en="Skills &amp; Tools" data-id="Keahlian &amp; Alat">Skills &amp; Tools</span>'),
    ('>Education</span>', ' data-en="Education" data-id="Pendidikan">Education</span>'),
    ('>Certifications &amp; Training</span>', ' data-en="Certifications &amp; Training" data-id="Sertifikasi &amp; Pelatihan">Certifications &amp; Training</span>'),
    ('>Organization &amp; Leadership</span>', ' data-en="Organization &amp; Leadership" data-id="Organisasi &amp; Kepemimpinan">Organization &amp; Leadership</span>'),
    # Stats
    ('>Years Exp.</span>', ' data-en="Years Exp." data-id="Thn Pengalaman">Years Exp.</span>'),
    ('>Sites Deployed</span>', ' data-en="Sites Deployed" data-id="Lokasi Deploy">Sites Deployed</span>'),
    # Skills table
    ('>Technical</td>', ' data-en="Technical" data-id="Teknis">Technical</td>'),
    ('>Soft Skills</td>', ' data-en="Soft Skills" data-id="Soft Skills">Soft Skills</td>'),
    ('>Languages</td>', ' data-en="Languages" data-id="Bahasa">Languages</td>'),
    # More on Me
    ('>More on Me</span>', ' data-en="More on Me" data-id="Lebih Tentang Saya">More on Me</span>'),
]
for old, new in pairs:
    content = content.replace(old, new, 1)

# ── 10. TAMBAH CSS lang-switch (satu kali) sebelum </style> ──
lang_css = """
    /* Language Switch */
    .lang-switch {
      display: flex; align-items: center;
      background: rgba(255,255,255,0.1); border-radius: 20px;
      overflow: hidden; border: 1px solid rgba(255,255,255,0.2);
      margin-left: 0.5rem; flex-shrink: 0;
    }
    .lang-btn {
      background: none; border: none; cursor: pointer;
      color: rgba(255,255,255,0.6); font-size: 0.78rem; font-weight: 700;
      padding: 0.28rem 0.75rem; transition: all .2s; letter-spacing: 0.5px;
    }
    .lang-btn.active { background: rgba(255,255,255,0.22); color: #fff; border-radius: 20px; }
    .lang-btn:hover:not(.active) { color: rgba(255,255,255,0.9); }
"""
content = content.replace('  </style>', lang_css + '  </style>', 1)

# ── 11. TAMBAH tombol EN/ID di navbar setelah </ul></nav> ──
content = content.replace(
    '  </ul></nav>',
    '  </ul>\n  <div class="lang-switch">\n    <button class="lang-btn active" id="btn-en" onclick="setLang(\'en\')">EN</button>\n    <button class="lang-btn" id="btn-id" onclick="setLang(\'id\')">ID</button>\n  </div>\n</nav>'
)

# ── 12. TAMBAH script setLang yang bersih sebelum </body> ──
lang_script = """
<script>
  function setLang(lang) {
    document.querySelectorAll('[data-en]').forEach(function(el) {
      var val = el.getAttribute('data-' + lang);
      if (val !== null) el.innerHTML = val;
    });
    var btnEn = document.getElementById('btn-en');
    var btnId = document.getElementById('btn-id');
    if (btnEn) btnEn.classList.toggle('active', lang === 'en');
    if (btnId) btnId.classList.toggle('active', lang === 'id');
    document.documentElement.lang = lang === 'id' ? 'id' : 'en';
    localStorage.setItem('lang', lang);
  }
  window.addEventListener('DOMContentLoaded', function() {
    var saved = localStorage.getItem('lang') || 'en';
    if (saved === 'id') setLang('id');
    // Sync with existing languageToggle if present
    var btnEn = document.getElementById('btn-en');
    var btnId = document.getElementById('btn-id');
    if (saved === 'id') {
      if (btnEn) btnEn.classList.remove('active');
      if (btnId) btnId.classList.add('active');
    }
  });
</script>
"""
content = content.replace('</body>', lang_script + '</body>', 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
