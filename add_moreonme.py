file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Tambah CSS btn-more-on-me sebelum closing </style>
css = '''    /* More on Me button */
    .btn-more-on-me {
      display: inline-flex; align-items: center; gap: 0.45rem;
      color: rgba(255,255,255,0.6); font-size: 0.82rem; font-weight: 500;
      text-decoration: none; margin-top: 1rem;
      transition: color .2s, transform .2s;
      animation: fadeInUp 0.8s ease 1.1s both;
    }
    .btn-more-on-me svg { animation: bounce 2s ease-in-out infinite; }
    @keyframes bounce {
      0%,100% { transform: translateY(0); }
      50%      { transform: translateY(5px); }
    }
    .btn-more-on-me:hover { color: rgba(255,255,255,0.95); transform: translateY(2px); }
'''
for i, line in enumerate(lines):
    if '</style>' in line:
        lines.insert(i, css)
        break

# 2. Tambah tombol setelah </div> penutup hero-cta
# Cari baris yang berisi hero-cta closing div lalu tambah tombol sebelum </div> hero-right
for i, line in enumerate(lines):
    if 'hero-cta' in line and 'animation' not in line and 'display' not in line and 'flex-direction' not in line:
        # Cari penutup </div> dari hero-cta
        for j in range(i, i+30):
            if lines[j].strip() == '</div>' and j > i+2:
                lines.insert(j+1, '      <a href="#summary" class="btn-more-on-me">\n        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12l7 7 7-7"/></svg>\n        More on Me\n      </a>\n')
                break
        break

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('done')
