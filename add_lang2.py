file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# --- 1. Inject CSS sebelum </style> ---
css = """    /* Language Switch */
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
for i, line in enumerate(lines):
    if '  </style>' in line:
        lines.insert(i, css)
        break

# --- 2. Inject tombol di navbar setelah </ul> ---
for i, line in enumerate(lines):
    if '  </ul>' in line and i < 530:
        lines.insert(i+1, '  <div class="lang-switch">\n    <button class="lang-btn active" id="btn-en" onclick="setLang(\'en\')">EN</button>\n    <button class="lang-btn" id="btn-id" onclick="setLang(\'id\')">ID</button>\n  </div>\n')
        break

# --- 3. Inject script sebelum </body> ---
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
  var savedLang = localStorage.getItem('lang') || 'en';
  if (savedLang === 'id') { window.addEventListener('DOMContentLoaded', function(){ setLang('id'); }); }
</script>
"""
for i, line in enumerate(lines):
    if '</body>' in line:
        lines.insert(i, script)
        break

# --- 4. Tambah data-en/data-id ke elemen kunci ---
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
    # Skills table headers
    ('>Technical</td>', ' data-en="Technical" data-id="Teknis">Technical</td>'),
    ('>Tools &amp; Software</td>', ' data-en="Tools &amp; Software" data-id="Alat &amp; Perangkat Lunak">Tools &amp; Software</td>'),
    ('>Soft Skills</td>', ' data-en="Soft Skills" data-id="Soft Skills">Soft Skills</td>'),
    ('>Languages</td>', ' data-en="Languages" data-id="Bahasa">Languages</td>'),
    # More on Me
    ('>More on Me\n      </a>', ' data-en="More on Me" data-id="Lebih Tentang Saya">More on Me\n      </a>'),
]

content = ''.join(lines)
for old, new in pairs:
    content = content.replace(old, new, 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
