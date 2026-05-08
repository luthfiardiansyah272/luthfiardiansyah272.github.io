import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Tambah CSS tombol language switch di navbar
lang_css = """
    /* Language Switch */
    .lang-switch {
      display: flex; align-items: center; gap: 0;
      background: rgba(255,255,255,0.1); border-radius: 20px;
      overflow: hidden; border: 1px solid rgba(255,255,255,0.2);
      margin-left: 1.5rem;
    }
    .lang-btn {
      background: none; border: none; cursor: pointer;
      color: rgba(255,255,255,0.6); font-size: 0.78rem; font-weight: 600;
      padding: 0.3rem 0.7rem; transition: all .2s; letter-spacing: 0.5px;
    }
    .lang-btn.active {
      background: rgba(255,255,255,0.2); color: #fff;
      border-radius: 20px;
    }
    .lang-btn:hover:not(.active) { color: rgba(255,255,255,0.9); }
"""
content = content.replace('  </style>', lang_css + '  </style>')

# 2. Tambah tombol di navbar setelah </ul>
content = content.replace(
    '  </ul>\n</nav>',
    '''  </ul>
  <div class="lang-switch">
    <button class="lang-btn active" id="btn-en" onclick="setLang('en')">EN</button>
    <button class="lang-btn" id="btn-id" onclick="setLang('id')">ID</button>
  </div>
</nav>'''
)

# 3. Tambah data-en dan data-id ke semua teks konten utama
translations = [
    # Tagline
    ('Electrical Engineering &middot; Sensor Systems &middot; TPM &middot; Operational Excellence',
     'data-en="Electrical Engineering &middot; Sensor Systems &middot; TPM &middot; Operational Excellence" data-id="Teknik Elektro &middot; Sistem Sensor &middot; TPM &middot; Keunggulan Operasional"'),

    # Nav links
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

    # Hero badges
    ('>&#9881;&#65039; Production Engineer</span>', ' data-en="&#9881;&#65039; Production Engineer" data-id="&#9881;&#65039; Insinyur Produksi">&#9881;&#65039; Production Engineer</span>'),
    ('>&#128161; Digital Innovation</span>', ' data-en="&#128161; Digital Innovation" data-id="&#128161; Inovasi Digital">&#128161; Digital Innovation</span>'),

    # Stats
    ('>Years Exp.</span>', ' data-en="Years Exp." data-id="Thn Pengalaman">Years Exp.</span>'),
    ('>Sites Deployed</span>', ' data-en="Sites Deployed" data-id="Lokasi Deploy">Sites Deployed</span>'),

    # Contact
    ('>Lampung / Palembang, Indonesia</span>', ' data-en="Lampung / Palembang, Indonesia" data-id="Lampung / Palembang, Indonesia">Lampung / Palembang, Indonesia</span>'),

    # CTA buttons
    ('>LinkedIn\n        </a>', ' data-en="LinkedIn" data-id="LinkedIn">\n          LinkedIn\n        </a>'),
    ('>More on Me\n      </a>', ' data-en="More on Me" data-id="Lebih Tentang Saya">\n        More on Me\n      </a>'),
    ('>Download CV\n\n\n          <svg', ' data-en="Download CV" data-id="Unduh CV">\n          Download CV\n\n\n          <svg'),

    # About Me paragraphs
    ('Electrical Engineering graduate with proven experience in production system digitalization',
     'data-en="Electrical Engineering graduate with proven experience in production system digitalization, equipment reliability, and maintenance engineering within FMCG agribusiness operations. Demonstrated impact in cost reduction exceeding IDR 1.2B/year, multi-site system deployment, and TPM implementation across multiple business units." data-id="Lulusan Teknik Elektro dengan pengalaman terbukti dalam digitalisasi sistem produksi, keandalan peralatan, dan rekayasa pemeliharaan di operasi agribisnis FMCG. Dampak nyata dalam penghematan biaya melebihi IDR 1,2M/tahun, penerapan sistem multi-lokasi, dan implementasi TPM di berbagai unit bisnis."\n    >Electrical Engineering graduate with proven experience in production system digitalization'),

    # Summary p2
    ('Strong in systems thinking, problem solving',
     'data-en="Strong in systems thinking, problem solving, and operational execution — with hands-on involvement from development and pilot through to full implementation. Highly driven to grow as a Production or Maintenance Engineer, with a focus on operational excellence and continuous improvement." data-id="Kuat dalam pemikiran sistematis, pemecahan masalah, dan eksekusi operasional — dengan keterlibatan langsung dari pengembangan dan pilot hingga implementasi penuh. Sangat termotivasi untuk berkembang sebagai Production atau Maintenance Engineer, dengan fokus pada keunggulan operasional dan perbaikan berkelanjutan."\n    >Strong in systems thinking, problem solving'),

    # Work Projects label
    ('>&#128188; Work Projects</p>', ' data-en="&#128188; Work Projects" data-id="&#128188; Proyek Kerja">&#128188; Work Projects</p>'),
    ('>&#128025; Personal Projects (GitHub)</p>', ' data-en="&#128025; Personal Projects (GitHub)" data-id="&#128025; Proyek Pribadi (GitHub)">&#128025; Personal Projects (GitHub)</p>'),

    # Skills table
    ('>Technical</td>', ' data-en="Technical" data-id="Teknis">Technical</td>'),
    ('>Tools &amp; Software</td>', ' data-en="Tools &amp; Software" data-id="Alat &amp; Perangkat Lunak">Tools &amp; Software</td>'),
    ('>Soft Skills</td>', ' data-en="Soft Skills" data-id="Soft Skills">Soft Skills</td>'),
    ('>Languages</td>', ' data-en="Languages" data-id="Bahasa">Languages</td>'),
    ("Indonesian (Native) &nbsp;|&nbsp; English (Professional Working Proficiency)",
     'data-en="Indonesian (Native) &nbsp;|&nbsp; English (Professional Working Proficiency)" data-id="Indonesia (Asli) &nbsp;|&nbsp; Inggris (Kemampuan Kerja Profesional)">Indonesian (Native) &nbsp;|&nbsp; English (Professional Working Proficiency)'),

    # Education
    (">Bachelor's Degree in Electrical Engineering</p>",
     ' data-en="Bachelor\'s Degree in Electrical Engineering" data-id="Sarjana Teknik Elektro">Bachelor\'s Degree in Electrical Engineering</p>'),

    # Footer
    ('© 2025 Luthfi Ardiansyah', 'data-en="© 2025 Luthfi Ardiansyah" data-id="© 2025 Luthfi Ardiansyah">© 2025 Luthfi Ardiansyah'),
]

for old, new in translations:
    content = content.replace(old, new, 1)

# 4. Tambah script language switch sebelum </body>
lang_script = """
<script>
  const translations = {
    en: {}, id: {}
  };

  function setLang(lang) {
    document.querySelectorAll('[data-en]').forEach(el => {
      const val = el.getAttribute('data-' + lang);
      if (val !== null) el.innerHTML = val;
    });
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');
    document.getElementById('btn-id').classList.toggle('active', lang === 'id');
    document.documentElement.lang = lang === 'id' ? 'id' : 'en';
    localStorage.setItem('lang', lang);
  }

  // Load saved language
  const savedLang = localStorage.getItem('lang') || 'en';
  if (savedLang === 'id') setLang('id');
</script>
"""
content = content.replace('</body>', lang_script + '\n</body>')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
