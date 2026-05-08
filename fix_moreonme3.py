file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Step 1: Hapus semua sisa btn-more-on-me yang ada
result = []
skip = False
for i, line in enumerate(lines):
    if '<a href="#summary" class="btn-more-on-me">' in line:
        skip = True
    if skip:
        if '</a>' in line:
            skip = False
        continue
    result.append(line)

lines = result

# Step 2: Cari penutup </div> hero-cta (setelah Download CV closing div)
# Tandai dengan mencari baris yang berisi </div> setelah "btn-download-menu"
# Lalu cari </div> penutup hero-cta, lalu insert More on Me setelahnya
found_download = False
inserted = False
for i, line in enumerate(lines):
    if 'btn-download-menu' in line:
        found_download = True
    if found_download and not inserted:
        # Cari </div> penutup hero-cta (indentasi 6 spasi)
        if line.strip() == '</div>' and '      </div>' in line:
            lines.insert(i + 1, '\n      <a href="#summary" class="btn-more-on-me">\n        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12l7 7 7-7"/></svg>\n        More on Me\n      </a>\n')
            inserted = True
            break

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('inserted:', inserted)
