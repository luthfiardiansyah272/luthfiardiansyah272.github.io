file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Cari baris penutup </div> dari hero-cta (setelah GitHub button)
# Cari baris yang berisi "GitHub" lalu cari </a> berikutnya
for i, line in enumerate(lines):
    if 'GitHub' in line and 'btn-secondary' not in line and 'svg' not in line:
        # Cari </a> setelah baris ini
        for j in range(i, i+5):
            if '</a>' in lines[j]:
                download_btn = '''        <div class="btn-download btn-secondary" tabindex="0" style="cursor:pointer;position:relative;display:inline-flex;align-items:center;gap:0.45rem;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 16l-5-5h3V4h4v7h3l-5 5zm-7 4h14v-2H5v2z"/></svg>
          Download CV
          <svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor"><path d="M7 10l5 5 5-5z"/></svg>
          <div class="btn-download-menu">
            <a href="CV_Luthfi_Ardiansyah_Lampung.pdf" download>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
              CV &ndash; Lampung
            </a>
            <a href="CV_Luthfi_Ardiansyah_Palembang.pdf" download>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
              CV &ndash; Palembang
            </a>
          </div>
        </div>\n'''
                lines.insert(j+1, download_btn)
                break
        break

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('done')
