import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# --- BERSIHKAN semua injeksi sebelumnya ---
# Hapus CSS lang-switch duplikat (semua instance)
content = re.sub(r'\s*/\* Language Switch \*/.*?\.lang-btn:hover:not\(\.active\) \{[^}]+\}\n', '', content, flags=re.DOTALL)

# Hapus tombol lang-switch di navbar
content = re.sub(r'\s*<div class="lang-switch">.*?</div>\n', '', content, flags=re.DOTALL)

# Hapus script setLang duplikat
content = re.sub(r'\n<script>\s*function setLang.*?</script>\n', '', content, flags=re.DOTALL)

# Hapus data-en/data-id yang sudah ada (bersihkan dulu)
content = re.sub(r' data-en="[^"]*" data-id="[^"]*"', '', content)

# --- INJECT BARU ---

# 1. CSS (satu kali)
css = """
    /* Language Switch */
    .lang-switch {
      display: flex; align-items: center;
      background: rgba(255,255,255,0.1); border-radius: 20px;
      overflow: hidden; border: 1px solid rgba(255,255,255,0.2);
      margin-left: 1.5rem; flex-shrink: 0;
    }
    .lang-btn {
      background: none; border: none; cursor: pointer;
      color: rgba(255,255,255,0.6); font-size: 0.78rem; font-weight: 700;
      padding: 0.28rem 0.75rem; transition: all .2s; letter-spacing: 0.5px;
    }
    .lang-btn.active { background: rgba(255,255,255,0.22); color: #fff; border-radius: 20px; }
    .lang-btn:hover:not(.active) { color: rgba(255,255,255,0.9); }
"""
content = content.replace('  </style>', css + '  </style>', 1)

# 2. Tombol navbar (satu kali)
content = content.replace(
    '  </ul>\n</nav>',
    '  </ul>\n  <div class="lang-switch">\n    <button class="lang-btn active" id="btn-en" onclick="setLang(\'en\')">EN</button>\n    <button class="lang-btn" id="btn-id" onclick="setLang(\'id\')">ID</button>\n  </div>\n</nav>',
    1
)

# 3. data-en/data-id ke elemen kunci
pairs = [
    ('>About</a>', ' data-en="About" data-id="Tentang">About</a>'),
    ('>Experience</a>', ' data-en="Experience" data-id="Pengalaman">Experience</a>'),
    ('>Projects</a>', ' data-en="Projects" data-id="Proyek">Projects</a>'),
    ('>Skills</a>', ' data-en="Skills" data-id="Keahlian">Skills</a>'),
    ('>Education</a>', ' data-en="Education" data-id="Pendidikan">Education</a>'),
    ('>Certs</a>', ' data-en="Certs" data-id="Sertifikat">Certs</a>'),
    ('>About Me</span>', ' data-en="About Me" data-id="Tentang Saya">About Me</span>'),
    ('>Work Experience</span>', ' data-en="Work Experience" data-id="Pengalaman Kerja">Work Experience</span>'),
    ('>Key Projects</span>', ' data-en="Key Projects" data-id="Proyek Utama">Key Projects</span>'),
    ('>Skills &amp; Tools</span>', ' data-en="Skills &amp; Tools" data-id="Keahlian &amp; Alat">Skills &amp; Tools</span>'),
    ('>Education</span>', ' data-en="Education" data-id="Pendidikan">Education</span>'),
    ('>Certifications &amp; Training</span>', ' data-en="Certifications &amp; Training" data-id="Sertifikasi &amp; Pelatihan">Certifications &amp; Training</span>'),
    ('>Organization &amp; Leadership</span>', ' data-en="Organization &amp; Leadership" data-id="Organisasi &amp; Kepemimpinan">Organization &amp; Leadership</span>'),
    ('>Years Exp.</span>', ' data-en="Years Exp." data-id="Thn Pengalaman">Years Exp.</span>'),
    ('>Sites Deployed</span>', ' data-en="Sites Deployed" data-id="Lokasi Deploy">Sites Deployed</span>'),
    ('>Technical</td>', ' data-en="Technical" data-id="Teknis">Technical</td>'),
    ('>Tools &amp; Software</td>', ' data-en="Tools &amp; Software" data-id="Alat &amp; Perangkat Lunak">Tools &amp; Software</td>'),
    ('>Soft Skills</td>', ' data-en="Soft Skills" data-id="Soft Skills">Soft Skills</td>'),
    ('>Languages</td>', ' data-en="Languages" data-id="Bahasa">Languages</td>'),
    ('>More on Me', ' data-en="More on Me" data-id="Lebih Tentang Saya">More on Me'),
    ('>Connect on LinkedIn<', ' data-en="Connect on LinkedIn" data-id="Hubungi di LinkedIn">Connect on LinkedIn<'),
]
for old, new in pairs:
    content = content.replace(old, new, 1)

# 4. Script (satu kali) sebelum </body>
script = """
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
  });
</script>
"""
content = content.replace('</body>', script + '</body>', 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
