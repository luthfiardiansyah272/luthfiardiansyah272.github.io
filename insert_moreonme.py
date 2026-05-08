file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Cari baris "CV &ndash; Palembang" lalu insert tombol setelah </div></div></div> penutup hero-cta
target = 'CV &ndash; Palembang'
for i, line in enumerate(lines):
    if target in line:
        # Cari </div> penutup hero-cta (sekitar 5 baris setelah ini)
        for j in range(i, i+10):
            if lines[j].strip() == '</div>' and '      </div>' in lines[j]:
                # ini penutup hero-cta
                lines.insert(j+1, '      <a href="#summary" class="btn-more-on-me">\n        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12l7 7 7-7"/></svg>\n        More on Me\n      </a>\n')
                break
        break

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('done')
